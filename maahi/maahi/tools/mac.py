"""Mac control via AppleScript / osascript.

Everything here is a thin pure function that returns a dict.
Side effects are real — these change the system state.
"""
from __future__ import annotations

import logging
import subprocess
from pathlib import Path

log = logging.getLogger(__name__)


def _osascript(script: str) -> dict[str, object]:
    """Run an AppleScript and return its result."""
    try:
        proc = subprocess.run(
            ["osascript", "-e", script],
            capture_output=True,
            text=True,
            timeout=20,
        )
    except subprocess.TimeoutExpired:
        return {"ok": False, "error": "AppleScript timed out."}
    except FileNotFoundError:
        return {"ok": False, "error": "osascript not available."}
    if proc.returncode != 0:
        return {"ok": False, "error": proc.stderr.strip() or "AppleScript failed."}
    return {"ok": True, "output": proc.stdout.strip()}


# ============================================================
#  APP CONTROL
# ============================================================


def open_app(name: str) -> dict[str, object]:
    """Open a macOS app by name."""
    try:
        subprocess.run(["open", "-a", name], check=True, timeout=10)
        return {"ok": True, "opened": name}
    except subprocess.CalledProcessError as e:
        return {"ok": False, "error": f"Could not open {name}: {e}"}
    except subprocess.TimeoutExpired:
        return {"ok": False, "error": f"Timed out opening {name}."}


def close_app(name: str) -> dict[str, object]:
    """Quit a macOS app gracefully."""
    return _osascript(f'tell application "{name}" to quit')


def list_running_apps() -> dict[str, object]:
    """List currently visible apps."""
    result = _osascript(
        'tell application "System Events" to '
        'get name of (every process whose visible is true)'
    )
    if not result["ok"]:
        return result
    apps = [a.strip() for a in str(result["output"]).split(",") if a.strip()]
    return {"ok": True, "apps": apps}


def frontmost_app() -> dict[str, object]:
    """Get the app currently in focus."""
    return _osascript(
        'tell application "System Events" to '
        'get name of first process whose frontmost is true'
    )


# ============================================================
#  VOLUME + DISPLAY
# ============================================================


def set_volume(level: int) -> dict[str, object]:
    """Set output volume 0-100."""
    level = max(0, min(100, int(level)))
    return _osascript(f"set volume output volume {level}")


def get_volume() -> dict[str, object]:
    return _osascript("output volume of (get volume settings)")


def mute() -> dict[str, object]:
    return _osascript("set volume with output muted")


def unmute() -> dict[str, object]:
    return _osascript("set volume without output muted")


# ============================================================
#  SCREENSHOT
# ============================================================


def screenshot(path: str = "") -> dict[str, object]:
    """Take a screenshot of the entire screen. Returns the saved path."""
    from datetime import datetime
    out = Path(path) if path else Path.home() / "Desktop" / f"maahi-screenshot-{datetime.now():%Y%m%d-%H%M%S}.png"
    out.parent.mkdir(parents=True, exist_ok=True)
    try:
        subprocess.run(["screencapture", "-x", str(out)], check=True, timeout=10)
    except subprocess.CalledProcessError as e:
        return {"ok": False, "error": str(e)}
    return {"ok": True, "path": str(out)}


# ============================================================
#  SPOTIFY
# ============================================================


def spotify(command: str) -> dict[str, object]:
    """Control Spotify. command in: play, pause, next, previous, current."""
    cmd = command.strip().lower()
    actions = {
        "play": 'tell application "Spotify" to play',
        "pause": 'tell application "Spotify" to pause',
        "next": 'tell application "Spotify" to next track',
        "previous": 'tell application "Spotify" to previous track',
        "prev": 'tell application "Spotify" to previous track',
    }
    if cmd in actions:
        return _osascript(actions[cmd])
    if cmd == "current":
        return _osascript(
            'tell application "Spotify" to '
            'return (name of current track) & " by " & (artist of current track)'
        )
    return {"ok": False, "error": f"Unknown spotify command: {command}"}


# ============================================================
#  MESSAGES
# ============================================================


def send_imessage(recipient: str, text: str) -> dict[str, object]:
    """Send an iMessage. recipient = phone number or email."""
    text_escaped = text.replace('"', '\\"')
    script = (
        f'tell application "Messages"\n'
        f'  set targetService to 1st account whose service type = iMessage\n'
        f'  set targetBuddy to participant "{recipient}" of targetService\n'
        f'  send "{text_escaped}" to targetBuddy\n'
        f'end tell'
    )
    return _osascript(script)


# ============================================================
#  NOTIFICATION
# ============================================================


def notify(title: str, body: str = "") -> dict[str, object]:
    """Show a native macOS notification."""
    t = title.replace('"', '\\"')
    b = body.replace('"', '\\"')
    return _osascript(f'display notification "{b}" with title "{t}"')
