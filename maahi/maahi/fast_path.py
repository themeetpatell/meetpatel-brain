"""Fast-path intent router — Siri-style bypass for the LLM.

Goal: anything that's *unambiguous* should never wait for `qwen2.5:7b`.
"What time is it?", "Open Chrome", "Mute", "Lock the screen" — Siri
answers these in <300ms because she pattern-matches the intent and
dispatches. So do we.

Contract: `try_fast_path(command)` returns the spoken response if it
handled the command (side effects already executed), else None. main.py
short-circuits the brain when it gets a string back.

Adding an intent = append a (regex, handler) row. Handlers return the
exact string Maahi will say. Keep them short — TTS is the bottleneck
once the brain is out of the loop.
"""
from __future__ import annotations

import datetime as _dt
import logging
import re
import subprocess
from collections.abc import Callable
from typing import NamedTuple

log = logging.getLogger(__name__)


# ============================================================
#  TYPES
# ============================================================


class _Intent(NamedTuple):
    name: str
    pattern: re.Pattern[str]
    handler: Callable[[re.Match[str]], str | None]


# ============================================================
#  PUBLIC ENTRY POINT
# ============================================================


def try_fast_path(command: str) -> str | None:
    """Return Maahi's spoken response if a fast-path intent handled the
    command, else None.

    Side effects (opening apps, changing volume, etc.) run *inside* the
    matched handler before this function returns. If a handler returns
    None (e.g. the underlying subprocess failed), we fall through to the
    LLM so Meet isn't left hanging.
    """
    if not command:
        return None
    norm = _normalize(command)
    for intent in _INTENTS:
        m = intent.pattern.match(norm)
        if m is None:
            continue
        try:
            log.info("Fast-path: %s", intent.name)
            result = intent.handler(m)
            if result:
                return result
        except Exception:  # noqa: BLE001
            log.exception("Fast-path handler %s crashed", intent.name)
        return None  # matched-but-failed → let LLM try
    return None


# ============================================================
#  NORMALIZATION
# ============================================================


_FILLER_PREFIX = re.compile(
    r"^(please\s+|can\s+you\s+|could\s+you\s+|would\s+you\s+|"
    r"hey\s+|now\s+|just\s+)+",
    re.I,
)
_TRAILING_PUNCT = re.compile(r"[.!?,\s]+$")


def _normalize(text: str) -> str:
    s = text.strip().lower()
    s = _FILLER_PREFIX.sub("", s)
    s = _TRAILING_PUNCT.sub("", s)
    s = re.sub(r"\s+", " ", s)
    return s


# ============================================================
#  HANDLERS
# ============================================================


def _say_time(_m: re.Match[str]) -> str:
    now = _dt.datetime.now()
    return now.strftime("It's %-I:%M %p.")


def _say_date(_m: re.Match[str]) -> str:
    today = _dt.date.today()
    return today.strftime("It's %A, %B %-d.")


def _say_day(_m: re.Match[str]) -> str:
    return _dt.date.today().strftime("It's %A.")


# Common apps Whisper transcribes phonetically — map to real app names.
_APP_ALIASES: dict[str, str] = {
    "chrome": "Google Chrome",
    "google chrome": "Google Chrome",
    "safari": "Safari",
    "vs code": "Visual Studio Code",
    "vscode": "Visual Studio Code",
    "code": "Visual Studio Code",
    "cursor": "Cursor",
    "claude": "Claude",
    "claude code": "Claude",
    "terminal": "Terminal",
    "iterm": "iTerm",
    "iterm2": "iTerm",
    "warp": "Warp",
    "slack": "Slack",
    "discord": "Discord",
    "telegram": "Telegram",
    "whatsapp": "WhatsApp",
    "notion": "Notion",
    "obsidian": "Obsidian",
    "spotify": "Spotify",
    "music": "Music",
    "mail": "Mail",
    "calendar": "Calendar",
    "messages": "Messages",
    "finder": "Finder",
    "preview": "Preview",
    "system settings": "System Settings",
    "system preferences": "System Settings",
    "settings": "System Settings",
    "zoom": "zoom.us",
    "figma": "Figma",
    "linear": "Linear",
}


def _resolve_app(name: str) -> str:
    n = name.strip().lower()
    return _APP_ALIASES.get(n, name.strip().title())


def _open_app(m: re.Match[str]) -> str | None:
    raw = m.group("app").strip()
    app = _resolve_app(raw)
    proc = subprocess.run(
        ["open", "-a", app],
        capture_output=True,
        text=True,
        timeout=5,
    )
    if proc.returncode != 0:
        return None
    return f"Opening {app}."


def _close_app(m: re.Match[str]) -> str | None:
    raw = m.group("app").strip()
    app = _resolve_app(raw)
    script = f'tell application "{app}" to quit'
    proc = subprocess.run(
        ["osascript", "-e", script],
        capture_output=True,
        text=True,
        timeout=5,
    )
    if proc.returncode != 0:
        return None
    return f"Closing {app}."


def _set_volume(m: re.Match[str]) -> str:
    pct = max(0, min(100, int(m.group("pct"))))
    subprocess.run(
        ["osascript", "-e", f"set volume output volume {pct}"],
        capture_output=True, timeout=5,
    )
    return f"Volume {pct}."


def _mute(_m: re.Match[str]) -> str:
    subprocess.run(
        ["osascript", "-e", "set volume with output muted"],
        capture_output=True, timeout=5,
    )
    return "Muted."


def _unmute(_m: re.Match[str]) -> str:
    subprocess.run(
        ["osascript", "-e", "set volume without output muted"],
        capture_output=True, timeout=5,
    )
    return "Unmuted."


def _volume_step(direction: int) -> Callable[[re.Match[str]], str]:
    def handler(_m: re.Match[str]) -> str:
        proc = subprocess.run(
            ["osascript", "-e", "output volume of (get volume settings)"],
            capture_output=True, text=True, timeout=5,
        )
        try:
            cur = int(proc.stdout.strip())
        except ValueError:
            cur = 50
        new = max(0, min(100, cur + direction * 10))
        subprocess.run(
            ["osascript", "-e", f"set volume output volume {new}"],
            capture_output=True, timeout=5,
        )
        return f"Volume {new}."
    return handler


def _lock_screen(_m: re.Match[str]) -> str:
    # macOS lock shortcut.
    subprocess.run(
        ["osascript", "-e",
         'tell application "System Events" to keystroke "q" using {command down, control down}'],
        capture_output=True, timeout=5,
    )
    return "Locking."


def _sleep_mac(_m: re.Match[str]) -> str:
    subprocess.run(["pmset", "sleepnow"], capture_output=True, timeout=5)
    return "Going to sleep."


def _screenshot(_m: re.Match[str]) -> str:
    stamp = _dt.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    path = f"/tmp/maahi-screenshot-{stamp}.png"
    subprocess.run(["screencapture", "-x", path], capture_output=True, timeout=10)
    return "Screenshot saved."


def _media_play_pause(_m: re.Match[str]) -> str:
    subprocess.run(
        ["osascript", "-e",
         'tell application "System Events" to key code 100'],  # F8
        capture_output=True, timeout=5,
    )
    return "Toggled playback."


def _media_next(_m: re.Match[str]) -> str:
    subprocess.run(
        ["osascript", "-e",
         'tell application "System Events" to key code 101'],  # F9
        capture_output=True, timeout=5,
    )
    return "Next track."


def _media_prev(_m: re.Match[str]) -> str:
    subprocess.run(
        ["osascript", "-e",
         'tell application "System Events" to key code 98'],  # F7
        capture_output=True, timeout=5,
    )
    return "Previous track."


# ============================================================
#  INTENT TABLE — order matters: most specific first.
# ============================================================


_INTENTS: tuple[_Intent, ...] = (
    # ---- clock ----
    _Intent("time",
            re.compile(r"^(what(?:'s|s| is)?\s+the\s+time|what\s+time\s+is\s+it|time)$"),
            _say_time),
    _Intent("date",
            re.compile(r"^(what(?:'s|s| is)?\s+the\s+date|what\s+(?:is\s+)?today(?:'s)?\s+date|today(?:'s)?\s+date)$"),
            _say_date),
    _Intent("day",
            re.compile(r"^(what\s+day\s+is\s+(?:it|today)|day\s+of\s+the\s+week)$"),
            _say_day),

    # ---- apps ----
    _Intent("open_app",
            re.compile(r"^(?:open|launch|start)\s+(?:the\s+|app\s+)?(?P<app>[a-z0-9 .]+?)(?:\s+app)?$"),
            _open_app),
    _Intent("close_app",
            re.compile(r"^(?:close|quit|kill|exit)\s+(?:the\s+|app\s+)?(?P<app>[a-z0-9 .]+?)(?:\s+app)?$"),
            _close_app),

    # ---- volume ----
    _Intent("set_volume",
            re.compile(r"^set\s+(?:the\s+)?volume\s+(?:to\s+)?(?P<pct>\d{1,3})\s*%?$"),
            _set_volume),
    _Intent("volume_up",
            re.compile(r"^(?:volume\s+up|louder|turn\s+(?:it\s+)?up)$"),
            _volume_step(+1)),
    _Intent("volume_down",
            re.compile(r"^(?:volume\s+down|quieter|softer|turn\s+(?:it\s+)?down)$"),
            _volume_step(-1)),
    _Intent("mute",
            re.compile(r"^(?:mute|silence|be\s+quiet)$"),
            _mute),
    _Intent("unmute",
            re.compile(r"^unmute$"),
            _unmute),

    # ---- system ----
    _Intent("lock",
            re.compile(r"^(?:lock(?:\s+(?:the\s+)?(?:screen|mac|computer))?)$"),
            _lock_screen),
    _Intent("sleep",
            re.compile(r"^(?:go\s+to\s+sleep|sleep(?:\s+(?:the\s+)?(?:mac|computer))?)$"),
            _sleep_mac),
    _Intent("screenshot",
            re.compile(r"^(?:take\s+(?:a\s+)?screenshot|screenshot|screen\s+shot|capture\s+(?:the\s+)?screen)$"),
            _screenshot),

    # ---- media ----
    _Intent("play_pause",
            re.compile(r"^(?:play|pause|play/pause|toggle\s+(?:play|music))$"),
            _media_play_pause),
    _Intent("next_track",
            re.compile(r"^(?:next(?:\s+track|\s+song)?|skip(?:\s+track)?)$"),
            _media_next),
    _Intent("prev_track",
            re.compile(r"^(?:previous(?:\s+track|\s+song)?|prev(?:ious)?|back\s+(?:a\s+)?track)$"),
            _media_prev),
)
