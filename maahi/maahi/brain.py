"""Maahi's brain — Ollama client + tool-calling loop.

Flow:
  user_text → system_prompt + history → Ollama → response
    if response is a tool JSON → execute → feed result back → loop
    else → speak it to Meet

We use the OpenAI-compatible /v1/chat/completions endpoint Ollama exposes,
which gives us a stable interface and easy streaming.
"""
from __future__ import annotations

import json
import logging
import re
from collections.abc import Iterator
from dataclasses import dataclass

import httpx

from .config import get_config
from .event_bus import emit_tool_end, emit_tool_start, emit_transcript
from .memory import recall_facts, recall_preferences
from .personality import build_system_prompt
from .tools.registry import call_tool, render_tool_catalog

log = logging.getLogger(__name__)


# ============================================================
#  MESSAGE TYPES (frozen — immutable)
# ============================================================


@dataclass(frozen=True)
class Message:
    role: str        # "system" | "user" | "assistant" | "tool"
    content: str

    def to_dict(self) -> dict[str, str]:
        return {"role": self.role, "content": self.content}


# ============================================================
#  TOOL CALL PARSER
# ============================================================
# Maahi prefers a compact call syntax:
#   @call tool_name(arg="value", count=3)           — preferred
# and still accepts JSON as a fallback:
#   {"tool": "...", "args": {...}}                  — tolerated
#   ```json {"tool": ...} ```                       — tolerated
#   any line that begins with {"tool":              — tolerated
#
# We do brace-counted extraction rather than regex because nested
# objects like "args": {} blow up naive non-greedy patterns.
# ============================================================


_AT_CALL_HEAD = re.compile(r"@call\s+([A-Za-z_]\w*)\s*\(")


def _coerce_value(raw: str) -> object:
    """Turn a raw @call argument token into a typed Python value."""
    raw = raw.strip()
    if not raw:
        return ""
    if len(raw) >= 2 and raw[0] == raw[-1] and raw[0] in ("'", '"'):
        inner = raw[1:-1]
        return (
            inner.replace('\\"', '"').replace("\\'", "'").replace("\\\\", "\\")
        )
    low = raw.lower()
    if low == "true":
        return True
    if low == "false":
        return False
    if low in ("none", "null"):
        return None
    try:
        return int(raw)
    except ValueError:
        pass
    try:
        return float(raw)
    except ValueError:
        pass
    return raw  # bare word — pass through as a string


def _split_call_args(args_str: str) -> list[str]:
    """Split an arg string on top-level commas, respecting quotes/brackets."""
    parts: list[str] = []
    buf: list[str] = []
    in_str = False
    quote = ""
    escape = False
    depth = 0
    for ch in args_str:
        if in_str:
            buf.append(ch)
            if escape:
                escape = False
            elif ch == "\\":
                escape = True
            elif ch == quote:
                in_str = False
            continue
        if ch in ("'", '"'):
            in_str = True
            quote = ch
            buf.append(ch)
        elif ch in "([{":
            depth += 1
            buf.append(ch)
        elif ch in ")]}":
            depth = max(0, depth - 1)
            buf.append(ch)
        elif ch == "," and depth == 0:
            parts.append("".join(buf))
            buf = []
        else:
            buf.append(ch)
    if buf:
        parts.append("".join(buf))
    return [p for p in parts if p.strip()]


def _parse_at_call(text: str) -> tuple[str, dict] | None:
    """Parse `@call name(arg=val, ...)`. Returns (name, args) or None."""
    head = _AT_CALL_HEAD.search(text)
    if head is None:
        return None
    name = head.group(1)
    open_idx = head.end() - 1  # index of the '('
    # Scan to the balanced ')', respecting string literals.
    depth = 0
    in_str = False
    quote = ""
    escape = False
    end_idx = -1
    for i in range(open_idx, len(text)):
        ch = text[i]
        if in_str:
            if escape:
                escape = False
            elif ch == "\\":
                escape = True
            elif ch == quote:
                in_str = False
            continue
        if ch in ("'", '"'):
            in_str = True
            quote = ch
        elif ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
            if depth == 0:
                end_idx = i
                break
    if end_idx == -1:
        return None
    args: dict[str, object] = {}
    for part in _split_call_args(text[open_idx + 1:end_idx]):
        key, sep, val = part.partition("=")
        if not sep:
            continue
        key = key.strip()
        if key:
            args[key] = _coerce_value(val)
    return name, args


def _extract_first_json_object(text: str) -> str | None:
    """Return the first balanced top-level JSON object in text, or None.

    Walks character by character, tracks brace depth, and respects string
    literals (including escaped quotes) so braces inside strings don't count.
    """
    start = text.find("{")
    if start == -1:
        return None
    depth = 0
    in_str = False
    escape = False
    for i in range(start, len(text)):
        ch = text[i]
        if in_str:
            if escape:
                escape = False
            elif ch == "\\":
                escape = True
            elif ch == '"':
                in_str = False
            continue
        if ch == '"':
            in_str = True
        elif ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return text[start:i + 1]
    return None


def _parse_tool_call(text: str) -> tuple[str, dict] | None:
    """Return (tool_name, args) if text is a tool call, else None.

    Tries the preferred `@call name(...)` syntax first, then falls back
    to JSON-object extraction.
    """
    at_call = _parse_at_call(text)
    if at_call is not None:
        return at_call

    # JSON fallback. Strip code fences first.
    cleaned = re.sub(r"```(?:json)?\s*", "", text)
    cleaned = cleaned.replace("```", "")

    # Walk the string and try each candidate object until one parses + has "tool"
    cursor = 0
    while cursor < len(cleaned):
        candidate = _extract_first_json_object(cleaned[cursor:])
        if candidate is None:
            return None
        try:
            obj = json.loads(candidate)
        except json.JSONDecodeError:
            obj = None
        if isinstance(obj, dict) and "tool" in obj:
            args = obj.get("args") or {}
            if not isinstance(args, dict):
                args = {}
            return str(obj["tool"]), args
        # Advance past this candidate and keep looking
        next_brace = cleaned.find("{", cursor + cleaned[cursor:].find("{") + 1)
        if next_brace == -1:
            return None
        cursor = next_brace
    return None


# ============================================================
#  OLLAMA CLIENT
# ============================================================


class Brain:
    """Stateful conversation with Ollama. Owns history + tool loop."""

    # Same call within _CACHE_TTL_S returns the cached tool result without
    # re-executing — important for noisy reads like `now` or `get_volume`
    # that the LLM may invoke repeatedly in a single conversation turn.
    _CACHE_TTL_S = 30.0
    _CACHE_MAX = 64

    def __init__(self) -> None:
        self.cfg = get_config()
        self.history: list[Message] = []
        self._http = httpx.Client(
            base_url=self.cfg.brain.host,
            timeout=httpx.Timeout(120.0, connect=10.0),
        )
        self._system_message = self._build_system_message()
        self._tool_cache: dict[tuple, tuple[dict, float]] = {}

    def prewarm(self) -> bool:
        """Send a 1-token dummy completion so Ollama loads the model.

        Best-effort: failures are logged and swallowed. Never blocks boot.
        """
        try:
            self._http.post(
                "/v1/chat/completions",
                json={
                    "model": self.cfg.brain.model,
                    "messages": [{"role": "user", "content": "."}],
                    "stream": False,
                    "options": {"num_predict": 1},
                },
                timeout=httpx.Timeout(180.0, connect=10.0),
            ).raise_for_status()
            log.info("Brain prewarm complete: %s loaded", self.cfg.brain.model)
            return True
        except httpx.HTTPError as e:
            log.warning("Brain prewarm failed: %s", e)
            return False

    @staticmethod
    def _cache_key(name: str, args: dict) -> tuple:
        return (name, tuple(sorted((k, repr(v)) for k, v in (args or {}).items())))

    def _cached_or_call(self, name: str, args: dict) -> dict:
        import time as _t
        key = self._cache_key(name, args)
        hit = self._tool_cache.get(key)
        now = _t.time()
        if hit is not None and (now - hit[1]) < self._CACHE_TTL_S:
            log.debug("Tool cache hit: %s", name)
            return dict(hit[0])
        result = call_tool(name, args)
        if (
            isinstance(result, dict)
            and result.get("ok", True)
            and _is_cacheable(name)
        ):
            if len(self._tool_cache) >= self._CACHE_MAX:
                oldest = min(self._tool_cache.items(), key=lambda kv: kv[1][1])[0]
                self._tool_cache.pop(oldest, None)
            self._tool_cache[key] = (dict(result), now)
        return result

    # ----- public API -----

    def respond(self, user_text: str) -> str:
        """Take a user utterance, run the tool loop, return final spoken text."""
        self.history.append(Message("user", user_text))

        for iteration in range(self.cfg.brain.max_iterations):
            reply = self._chat_once()
            tool_call = _parse_tool_call(reply)
            if tool_call is None:
                # Plain text reply → final answer
                self.history.append(Message("assistant", reply))
                emit_transcript("maahi", reply)
                return reply
            name, args = tool_call
            log.info("Tool call: %s args=%s", name, args)
            emit_tool_start(name, args)
            result = self._cached_or_call(name, args)
            emit_tool_end(name, result)
            # Push both the call and the result so the model sees what happened.
            self.history.append(Message("assistant", reply))
            self.history.append(Message(
                "tool",
                f"[tool:{name}] {json.dumps(result, ensure_ascii=False)}",
            ))
        # Loop bailed — return a graceful fallback.
        log.warning("Tool loop hit max_iterations (%d)", self.cfg.brain.max_iterations)
        fallback = "I'm caught in a loop on this one. Try rephrasing."
        self.history.append(Message("assistant", fallback))
        emit_transcript("maahi", fallback)
        return fallback

    def reset(self) -> None:
        """Clear history but keep the system prompt."""
        self.history = []
        self._system_message = self._build_system_message()

    # ----- internals -----

    def _build_system_message(self) -> Message:
        catalog = render_tool_catalog()
        prompt = build_system_prompt(catalog)
        facts = recall_facts()
        prefs = recall_preferences()
        if facts:
            prompt += f"\n\nLONG-TERM FACTS YOU'VE LEARNED:\n{facts}"
        if prefs:
            prompt += f"\n\nMEET'S PREFERENCES:\n{prefs}"
        return Message("system", prompt)

    def _chat_once(self) -> str:
        """One round-trip to Ollama. Returns assistant text."""
        messages = [self._system_message.to_dict()] + [m.to_dict() for m in self.history]
        payload = {
            "model": self.cfg.brain.model,
            "messages": messages,
            "temperature": self.cfg.brain.temperature,
            "stream": False,
            "options": {"num_predict": self.cfg.brain.max_tokens},
        }
        try:
            r = self._http.post("/v1/chat/completions", json=payload)
            r.raise_for_status()
        except httpx.HTTPError as e:
            log.error("Ollama call failed: %s", e)
            return "I lost connection to the brain. Check Ollama."
        data = r.json()
        choices = data.get("choices") or []
        if not choices:
            return "Empty response from the model."
        return (choices[0].get("message") or {}).get("content", "").strip()

    def stream_respond(self, user_text: str) -> Iterator[str]:
        """Streaming variant. Yields tokens for the FINAL (non-tool) reply only.

        We can't truly stream tool calls — we need the full JSON before dispatching.
        So this falls back to non-streaming for tool turns and only streams the
        last text turn. That's what the speaker wants anyway.
        """
        self.history.append(Message("user", user_text))

        for _ in range(self.cfg.brain.max_iterations - 1):
            reply = self._chat_once()
            tool_call = _parse_tool_call(reply)
            if tool_call is None:
                self.history.append(Message("assistant", reply))
                emit_transcript("maahi", reply)
                # Yield in pseudo-tokens so the speaker can flush sentences.
                for chunk in _pseudo_tokens(reply):
                    yield chunk
                return
            name, args = tool_call
            log.info("Tool call: %s args=%s", name, args)
            emit_tool_start(name, args)
            result = self._cached_or_call(name, args)
            emit_tool_end(name, result)
            self.history.append(Message("assistant", reply))
            self.history.append(Message(
                "tool",
                f"[tool:{name}] {json.dumps(result, ensure_ascii=False)}",
            ))
        # Final attempt
        final = self._chat_once()
        self.history.append(Message("assistant", final))
        emit_transcript("maahi", final)
        for chunk in _pseudo_tokens(final):
            yield chunk


def _pseudo_tokens(text: str, size: int = 8) -> Iterator[str]:
    for i in range(0, len(text), size):
        yield text[i:i + size]


# Tools that are safe to cache for a short TTL. Anything that writes,
# sends, or has time-sensitive side effects is excluded.
_CACHEABLE_TOOLS: frozenset[str] = frozenset({
    "now", "system_info", "get_volume", "frontmost_app", "front_window",
    "running_apps", "obsidian_list", "obsidian_read", "obsidian_search",
    "obsidian_semantic_search", "reminders_open", "calendar_today",
    "calendar_week", "calendar_upcoming", "notes_list", "notes_read",
    "web_search", "web_fetch",
})


def _is_cacheable(tool_name: str) -> bool:
    return tool_name in _CACHEABLE_TOOLS
