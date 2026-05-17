"""HUD server — FastAPI + WebSocket bridge to the dashboard.

Serves the static HUD on http://127.0.0.1:<port>/ and a WebSocket at
/ws that streams `event_bus` events as JSON to the HUD.

Loopback only. No auth — relies on the bind address.

Lifecycle:
  start_in_thread(cfg) → returns the running uvicorn.Server. The server
  runs on a daemon thread with its own asyncio loop. main.py shuts it
  down by setting .should_exit = True.
"""
from __future__ import annotations

import asyncio
import json
import logging
import threading
from pathlib import Path
from typing import Any

import uvicorn
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from .config import HudCfg
from .event_bus import bus

log = logging.getLogger(__name__)

HUD_DIR = Path(__file__).resolve().parent / "hud"


def _build_app() -> FastAPI:
    app = FastAPI(title="Maahi HUD", version="1.0")

    if HUD_DIR.exists():
        app.mount("/static", StaticFiles(directory=str(HUD_DIR)), name="static")

    @app.get("/")
    async def root() -> Any:
        index = HUD_DIR / "index.html"
        if not index.exists():
            return {"error": "HUD assets missing", "expected": str(index)}
        return FileResponse(str(index))

    @app.get("/health")
    async def health() -> dict[str, Any]:
        return {"ok": True}

    @app.websocket("/ws")
    async def ws(ws: WebSocket) -> None:
        await ws.accept()
        log.info("HUD WS connected")
        sub = bus().subscribe()

        for ev in bus().recent(limit=32):
            try:
                await ws.send_text(json.dumps({"replay": True, **ev.to_dict()}))
            except Exception:
                pass

        async def pump_outbound() -> None:
            try:
                while True:
                    ev = await sub.get()
                    await ws.send_text(json.dumps(ev.to_dict()))
            except WebSocketDisconnect:
                pass
            except Exception as e:  # noqa: BLE001
                log.warning("HUD outbound pump stopped: %s", e)

        async def pump_inbound() -> None:
            try:
                while True:
                    raw = await ws.receive_text()
                    try:
                        msg = json.loads(raw)
                    except json.JSONDecodeError:
                        continue
                    kind = msg.get("type")
                    if not kind:
                        continue
                    bus().publish(f"hud:{kind}", msg.get("payload") or {})
            except WebSocketDisconnect:
                pass
            except Exception as e:  # noqa: BLE001
                log.warning("HUD inbound pump stopped: %s", e)

        try:
            await asyncio.gather(pump_outbound(), pump_inbound())
        finally:
            bus().unsubscribe(sub)
            log.info("HUD WS disconnected")

    return app


def start_in_thread(cfg: HudCfg) -> uvicorn.Server | None:
    """Spin uvicorn on a daemon thread. Returns Server (None if disabled)."""
    if not cfg.enabled:
        log.info("HUD disabled in config")
        return None

    app = _build_app()
    uvi_cfg = uvicorn.Config(
        app,
        host="127.0.0.1",
        port=cfg.port,
        log_level="warning",
        loop="asyncio",
        access_log=False,
    )
    server = uvicorn.Server(uvi_cfg)

    def _run() -> None:
        try:
            asyncio.run(server.serve())
        except Exception as e:  # noqa: BLE001
            log.exception("HUD server crashed: %s", e)

    th = threading.Thread(target=_run, name="hud-server", daemon=True)
    th.start()
    log.info("HUD server listening on http://127.0.0.1:%d", cfg.port)
    return server
