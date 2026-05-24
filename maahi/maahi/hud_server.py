"""HUD server — FastAPI + WebSocket bridge to the dashboard.

Serves the static HUD on http://127.0.0.1:<port>/ and a WebSocket at
/ws that streams `event_bus` events as JSON to the HUD.

Also exposes a REST surface for the Settings panel, privacy view, and
first-run permission wizard:

  GET  /api/config              → editable config subset
  POST /api/config              → atomic write + reload
  GET  /api/voices              → macOS `say -v ?` parsed
  POST /api/audition            → speak a sample in a voice
  GET  /api/brain/probe         → Ollama health + latency
  GET  /api/permissions         → probe Mic / Accessibility / Screen / Automation
  POST /api/permissions/open    → deep-link to a Settings pane
  GET  /api/transcript/today    → today's conversation turns
  POST /api/transcript/clear    → drop today's transcript
  POST /api/listening           → pause/resume the mic loop
  GET  /api/skills              → list installed skill packs

Loopback only. No auth — relies on the bind address.
"""
from __future__ import annotations

import asyncio
import json
import logging
import threading
from pathlib import Path
from typing import Any

import uvicorn
from fastapi import FastAPI, HTTPException, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Dict, Optional

from .config import HudCfg
from .event_bus import bus, emit_state


# Pydantic request models. Module-level so type resolution works under 3.9.

class ConfigPatch(BaseModel):
    patch: Dict[str, Any]


class AuditionBody(BaseModel):
    voice: str
    text: Optional[str] = None


class OpenPaneBody(BaseModel):
    pane: str


class ListeningBody(BaseModel):
    paused: bool

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

    # ----------------------------------------------------------
    # Settings panel
    # ----------------------------------------------------------

    @app.get("/api/config")
    async def get_config_view() -> dict[str, Any]:
        from . import settings_api
        return {"ok": True, "config": settings_api.public_view()}

    @app.post("/api/config")
    async def post_config(body: ConfigPatch) -> dict[str, Any]:
        from . import settings_api
        res = settings_api.write(body.patch)
        if not res.ok:
            raise HTTPException(status_code=500, detail=res.error or "write failed")
        return {
            "ok": True,
            "written": res.written,
            "backup": res.backup_path,
        }

    @app.get("/api/voices")
    async def voices() -> dict[str, Any]:
        from . import settings_api
        return {"ok": True, "voices": settings_api.list_macos_voices()}

    @app.post("/api/audition")
    async def audition(body: AuditionBody) -> dict[str, Any]:
        from . import settings_api
        return settings_api.audition_voice(body.voice, body.text)

    @app.get("/api/brain/probe")
    async def brain_probe() -> dict[str, Any]:
        from . import settings_api
        return settings_api.probe_brain()

    # ----------------------------------------------------------
    # Permissions wizard
    # ----------------------------------------------------------

    @app.get("/api/permissions")
    async def permissions() -> dict[str, Any]:
        from . import permissions as perms
        return {"ok": True, "status": perms.probe_all()}

    @app.post("/api/permissions/open")
    async def open_pane(body: OpenPaneBody) -> dict[str, Any]:
        from . import permissions as perms
        return perms.open_settings(body.pane)

    # ----------------------------------------------------------
    # Privacy view — transcript + listening control
    # ----------------------------------------------------------

    @app.get("/api/transcript/today")
    async def transcript_today() -> dict[str, Any]:
        from . import privacy
        return privacy.todays_turns()

    @app.post("/api/transcript/clear")
    async def transcript_clear() -> dict[str, Any]:
        from . import privacy
        return privacy.clear_today()

    @app.post("/api/listening")
    async def listening(body: ListeningBody) -> dict[str, Any]:
        bus().publish("listening_set", {"paused": body.paused})
        emit_state("paused" if body.paused else "idle")
        return {"ok": True, "paused": body.paused}

    # ----------------------------------------------------------
    # Skills catalog (read-only)
    # ----------------------------------------------------------

    @app.get("/api/skills")
    async def skills() -> dict[str, Any]:
        from .tools.registry import TOOLS
        return {
            "ok": True,
            "count": len(TOOLS),
            "tools": [
                {"name": t.name, "description": t.description,
                 "args": dict(t.arg_schema)}
                for t in TOOLS
            ],
        }

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
