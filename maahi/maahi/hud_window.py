"""HUD window — pywebview wrapper.

Opens a frameless, transparent, always-on-top WKWebView pointed at the
local HUD server. Must run on the macOS main thread (pywebview hard
requirement), so main.py hands the main thread to this module after
backgrounding the wake loop.
"""
from __future__ import annotations

import logging
from typing import Any

from .config import HudCfg

log = logging.getLogger(__name__)


def _resolve_position(cfg: HudCfg) -> tuple[int, int]:
    """Translate negative offsets to absolute screen coords."""
    x, y = cfg.x, cfg.y
    if x >= 0 and y >= 0:
        return x, y
    try:
        import pyautogui
        sw, sh = pyautogui.size()
    except Exception:  # noqa: BLE001
        sw, sh = 1440, 900
    if x < 0:
        x = max(0, sw + x - cfg.width)
    if y < 0:
        y = max(0, sh + y - cfg.height)
    return int(x), int(y)


def run(cfg: HudCfg) -> None:
    """Block on the main thread running the HUD window."""
    if not cfg.enabled:
        log.info("HUD window disabled in config")
        return
    try:
        import webview  # pywebview
    except ImportError:
        log.error("pywebview not installed — HUD window cannot launch")
        return

    x, y = _resolve_position(cfg)
    url = f"http://127.0.0.1:{cfg.port}/"

    create_kwargs: dict[str, Any] = dict(
        title="Maahi",
        url=url,
        width=cfg.width,
        height=cfg.height,
        x=x,
        y=y,
        resizable=False,
        frameless=True,
        easy_drag=True,
        on_top=cfg.always_on_top,
        transparent=cfg.transparent,
    )
    # pywebview only accepts 6-digit hex. With transparent=True we omit
    # background_color entirely; the framework handles the clear backdrop.
    if not cfg.transparent:
        create_kwargs["background_color"] = "#0A0E18"

    try:
        webview.create_window(**create_kwargs)
    except TypeError as e:
        log.warning("pywebview rejected kwargs (%s); retrying with minimum set", e)
        webview.create_window(
            title="Maahi",
            url=url,
            width=cfg.width,
            height=cfg.height,
            x=x, y=y,
            resizable=False,
            frameless=True,
            on_top=cfg.always_on_top,
        )

    webview.start()
