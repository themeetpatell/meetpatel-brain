"""Tool registry — single source of truth for what Maahi can do.

Each tool entry maps a stable name to (function, JSON schema, one-line desc).
The brain only sees what's here.
"""
from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from typing import Any

from . import (
    calendar_tool,
    control,
    mac,
    mail,
    notes,
    obsidian,
    reminders,
    system,
    vision,
    web,
)


@dataclass(frozen=True)
class Tool:
    name: str
    description: str
    func: Callable[..., dict[str, Any]]
    arg_schema: dict[str, str]   # arg_name -> "type: description"


TOOLS: tuple[Tool, ...] = (
    # ----- Obsidian -----
    Tool("obsidian_read", "Read a note from the Obsidian vault by name or path.",
         obsidian.read_note, {"name": "str: note name or relative path"}),
    Tool("obsidian_search", "Full-text search across the whole vault.",
         obsidian.search_vault, {"query": "str: words to search for",
                                 "limit": "int: max hits (default 8)"}),
    Tool("obsidian_list", "List notes in a vault folder.",
         obsidian.list_notes, {"folder": "str: folder relative to vault (empty = root)",
                               "limit": "int: max files (default 50)"}),
    Tool("obsidian_create", "Create a new note in the vault.",
         obsidian.create_note, {"name": "str: note name (no .md)",
                                "content": "str: markdown body",
                                "folder": "str: target folder (optional)"}),
    Tool("obsidian_append", "Append text to an existing note.",
         obsidian.append_to_note, {"name": "str: note name",
                                   "content": "str: text to append"}),
    Tool("obsidian_daily", "Append a timestamped block to today's daily note.",
         obsidian.append_to_daily, {"content": "str: text to log"}),

    # ----- Mac control -----
    Tool("open_app", "Open a macOS application.",
         mac.open_app, {"name": "str: app name e.g. 'Slack'"}),
    Tool("close_app", "Quit a macOS application.",
         mac.close_app, {"name": "str: app name"}),
    Tool("running_apps", "List currently visible apps.",
         mac.list_running_apps, {}),
    Tool("frontmost_app", "Get the name of the app currently in focus.",
         mac.frontmost_app, {}),
    Tool("set_volume", "Set system volume 0-100.",
         mac.set_volume, {"level": "int: 0-100"}),
    Tool("get_volume", "Get current system volume.",
         mac.get_volume, {}),
    Tool("mute", "Mute system audio.", mac.mute, {}),
    Tool("unmute", "Unmute system audio.", mac.unmute, {}),
    Tool("screenshot", "Take a screenshot of the full screen.",
         mac.screenshot, {"path": "str: optional save path"}),
    Tool("spotify", "Control Spotify: play/pause/next/previous/current.",
         mac.spotify, {"command": "str: play|pause|next|previous|current"}),
    Tool("send_imessage", "Send an iMessage to a contact.",
         mac.send_imessage, {"recipient": "str: phone or email",
                             "text": "str: message body"}),
    Tool("notify", "Show a native macOS notification.",
         mac.notify, {"title": "str", "body": "str: optional"}),

    # ----- Calendar -----
    Tool("calendar_today", "List today's calendar events.",
         calendar_tool.today_events, {}),
    Tool("calendar_week", "List this week's calendar events.",
         calendar_tool.this_week_events, {}),
    Tool("calendar_upcoming", "List events starting within the next N minutes.",
         calendar_tool.events_starting_within,
         {"minutes": "int: lookahead window (default 5)"}),
    Tool("calendar_create", "Create a calendar event.",
         calendar_tool.create_event,
         {"title": "str", "start_iso": "str: YYYY-MM-DD HH:MM",
          "end_iso": "str: optional end time", "calendar": "str: default 'Home'",
          "notes": "str: optional"}),

    # ----- Mail -----
    Tool("mail_unread", "Get summaries of recent unread emails.",
         mail.unread_summary, {"limit": "int: default 10"}),
    Tool("mail_draft", "Open a draft email in Mail.",
         mail.draft_email, {"to": "str", "subject": "str", "body": "str"}),
    Tool("mail_send", "Send an email immediately. Use with care.",
         mail.send_email, {"to": "str", "subject": "str", "body": "str"}),

    # ----- Reminders -----
    Tool("reminders_open", "List open reminders.",
         reminders.list_open, {"limit": "int: default 20"}),
    Tool("reminders_add", "Add a new reminder.",
         reminders.add, {"title": "str", "list_name": "str: default 'Reminders'",
                         "due_iso": "str: optional YYYY-MM-DD HH:MM"}),

    # ----- Apple Notes -----
    Tool("notes_list", "List recent Apple Notes by title.",
         notes.list_notes, {"limit": "int: max notes (default 20)"}),
    Tool("notes_read", "Read the body of an Apple Note by partial title match.",
         notes.read_note, {"name": "str: note title or partial match"}),
    Tool("notes_create", "Create a new Apple Note.",
         notes.create_note, {"name": "str: note title",
                              "body": "str: note text",
                              "folder": "str: target folder (default 'Notes')"}),
    Tool("notes_append", "Append text to an existing Apple Note.",
         notes.append_to_note, {"name": "str: note title or partial match",
                                "body": "str: text to append"}),

    # ----- Web -----
    Tool("web_search", "Search the web via DuckDuckGo.",
         web.web_search, {"query": "str", "max_results": "int: default 6"}),
    Tool("web_fetch", "Fetch a URL and return its text content.",
         web.web_fetch, {"url": "str: http(s) URL"}),

    # ----- System -----
    Tool("now", "Current local date and time.", system.now, {}),
    Tool("system_info", "Battery, uptime, disk free.", system.system_info, {}),
    Tool("shell", "Run a safelisted shell command.",
         system.shell, {"command": "str: command line"}),
    Tool("read_screen", "OCR the current screen.", system.read_screen, {}),
    Tool("front_window", "Title of the frontmost window.", system.front_window, {}),

    # ----- Vision (multimodal screen understanding) -----
    Tool("vision_screen",
         "Take a screenshot and describe / answer a question about what's on screen.",
         vision.vision_screen,
         {"question": "str: what to ask about the screen (empty = describe)"}),
    Tool("vision_region",
         "Vision over a screen region.",
         vision.vision_region,
         {"question": "str", "x": "int", "y": "int",
          "w": "int: width", "h": "int: height"}),

    # ----- Control (cursor / keyboard / Accessibility) -----
    Tool("cursor_move",
         "Move the mouse cursor to (x, y) screen coordinates.",
         control.cursor_move,
         {"x": "int", "y": "int",
          "duration_ms": "int: smoothing duration, default 120"}),
    Tool("cursor_click",
         "Click the mouse. Omit x/y to click at current position.",
         control.cursor_click,
         {"x": "int: optional", "y": "int: optional",
          "button": "str: left|right|middle (default left)",
          "clicks": "int: default 1"}),
    Tool("cursor_scroll",
         "Vertical scroll. Positive = up, negative = down.",
         control.cursor_scroll, {"dy": "int"}),
    Tool("keyboard_type",
         "Type text at the current focus.",
         control.keyboard_type,
         {"text": "str",
          "interval_ms": "int: per-char delay (default 15)"}),
    Tool("keyboard_key",
         "Press a key or combo. Examples: 'return', 'cmd+t', 'cmd+shift+4'.",
         control.keyboard_key, {"key": "str"}),
    Tool("ax_perform",
         "Semantic action via Accessibility. action: focus|click|press|menu.",
         control.ax_perform,
         {"app": "str: app name",
          "action": "str: focus|click|press|menu",
          "target": "str: element name or menu path 'File > New'"}),
)


# ============================================================
#  DISPATCH
# ============================================================


_BY_NAME: dict[str, Tool] = {t.name: t for t in TOOLS}


def call_tool(name: str, args: dict[str, Any]) -> dict[str, Any]:
    """Dispatch a tool by name. Returns a normalized result dict."""
    tool = _BY_NAME.get(name)
    if tool is None:
        return {"ok": False, "error": f"Unknown tool: {name}"}
    try:
        result = tool.func(**(args or {}))
        if not isinstance(result, dict):
            return {"ok": True, "value": result}
        return result
    except TypeError as e:
        return {"ok": False, "error": f"Bad arguments for {name}: {e}"}
    except Exception as e:  # noqa: BLE001
        return {"ok": False, "error": f"{name} failed: {e}"}


def render_tool_catalog() -> str:
    """Render tools as a compact list for the LLM system prompt."""
    lines: list[str] = []
    for t in TOOLS:
        args_str = (
            ", ".join(f"{k}: {v}" for k, v in t.arg_schema.items())
            if t.arg_schema else "(no args)"
        )
        lines.append(f"- {t.name}({args_str}) — {t.description}")
    return "\n".join(lines)
