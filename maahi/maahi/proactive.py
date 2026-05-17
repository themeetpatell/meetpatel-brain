"""Proactive monitor — Maahi speaks up unprompted.

A background thread that watches the calendar and warns Meet before a
meeting starts. She's an operator, not a vending machine: she should
interject when something is load-bearing.

To add a new trigger, write a `_check_*` method and call it from `_loop`.
"""
from __future__ import annotations

import logging
import threading

from .config import get_config
from .speaker import Speaker
from .tools import calendar_tool

log = logging.getLogger(__name__)


class ProactiveMonitor:
    """Background thread that interjects with timely, unprompted updates."""

    def __init__(self, speaker: Speaker) -> None:
        cfg = get_config()
        self._speaker = speaker
        self._cfg = cfg.proactive
        self._announced: set[str] = set()
        self._stop = threading.Event()
        self._thread: threading.Thread | None = None

    def start(self) -> None:
        """Spin up the monitor thread (no-op if disabled in config)."""
        if not self._cfg.enabled:
            log.info("Proactive monitor disabled in config.")
            return
        self._thread = threading.Thread(
            target=self._loop, name="proactive", daemon=True
        )
        self._thread.start()
        log.info("Proactive monitor on (poll=%ds, lead=%dm).",
                 self._cfg.poll_seconds, self._cfg.lead_minutes)

    def stop(self) -> None:
        """Signal the monitor thread to exit."""
        self._stop.set()

    # ----- internals -----

    def _loop(self) -> None:
        # Event.wait returns True when stopped, False on timeout — so this
        # both paces the polling and exits promptly on shutdown.
        while not self._stop.wait(self._cfg.poll_seconds):
            try:
                self._check_calendar()
            except Exception as e:  # noqa: BLE001
                log.warning("Proactive calendar check failed: %s", e)

    def _check_calendar(self) -> None:
        """Warn about any meeting starting inside the lead window."""
        res = calendar_tool.events_starting_within(self._cfg.lead_minutes)
        if not res.get("ok"):
            return
        for ev in res.get("events", []):
            key = f"{ev.get('title', '')}|{ev.get('start', '')}"
            if key in self._announced:
                continue
            self._announced.add(key)
            log.info("Proactive nudge: %s", key)
            self._speaker.say(_nudge_text(ev))


def _nudge_text(ev: dict) -> str:
    """Phrase a short spoken heads-up for an upcoming event."""
    title = ev.get("title") or "an event"
    mins = int(ev.get("minutes_until", 0))
    if mins <= 1:
        return f"Heads up. {title} is starting now."
    return f"Heads up. {title} starts in {mins} minutes."
