#!/usr/bin/env bash
# ============================================================
#  Maahi — one-time setup script
# ============================================================
#  Installs Python deps, downloads the Whisper + Piper TTS models, and
#  pulls the Ollama model defined in config.yaml.
#
#  Run from this directory:
#      bash setup.sh
# ============================================================

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"

echo ""
echo "  Maahi — setup"
echo "  -------------"
echo ""

# --- 1. Python ---
if ! command -v python3 &>/dev/null; then
    echo "  [x] python3 not found. Install from https://www.python.org/downloads/"
    exit 1
fi
PY_VER="$(python3 -c 'import sys; print("%d.%d" % sys.version_info[:2])')"
echo "  [+] Python $PY_VER"

# --- 2. Virtualenv ---
if [ ! -d ".venv" ]; then
    echo "  [+] Creating .venv ..."
    python3 -m venv .venv
fi
# shellcheck disable=SC1091
source .venv/bin/activate
echo "  [+] Activated .venv"

# --- 3. System dependencies ---
echo "  [+] Checking system deps (portaudio for sounddevice) ..."
if ! command -v brew &>/dev/null; then
    echo "  [!] Homebrew not found. Install it from https://brew.sh"
    echo "      Then run: brew install portaudio"
else
    brew list portaudio &>/dev/null || brew install portaudio
fi

# --- 4. Python packages ---
echo "  [+] Installing Python packages ..."
pip install --upgrade pip
pip install -r requirements.txt

# --- 5. Ollama ---
echo ""
if ! command -v ollama &>/dev/null; then
    echo "  [!] Ollama not installed."
    echo "      Install it: https://ollama.com/download"
    echo "      Or:         brew install ollama"
else
    echo "  [+] Ollama found."
    # Pull the model defined in config.yaml
    MODEL="$(grep -E '^\s*model:' config.yaml | head -1 | awk -F'"' '{print $2}')"
    if [ -n "$MODEL" ]; then
        echo "  [+] Pulling model: $MODEL"
        ollama pull "$MODEL" || echo "  [!] Failed to pull $MODEL — pull manually later."
    fi
fi

# --- 6. Piper TTS voice ---
echo ""
echo "  [+] Downloading Piper TTS voice (en_US-lessac-medium) ..."
VOICE_DIR="$ROOT/voices"
mkdir -p "$VOICE_DIR"
PIPER_BASE="https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/lessac/medium"
for f in en_US-lessac-medium.onnx en_US-lessac-medium.onnx.json; do
    if [ -f "$VOICE_DIR/$f" ]; then
        echo "  [+] $f already present"
    elif curl -fSL "$PIPER_BASE/$f" -o "$VOICE_DIR/$f"; then
        echo "  [+] Downloaded $f"
    else
        echo "  [!] Failed to download $f — Maahi will fall back to macOS 'say'."
        rm -f "$VOICE_DIR/$f"
    fi
done

# --- 7. Whisper warmup ---
echo "  [+] Warming up Whisper model (first run downloads it) ..."
python3 -c "
from maahi.config import get_config
from maahi.listener import _get_model
cfg = get_config()
_get_model(cfg.stt.model)
_get_model('tiny.en')
print('OK')
" || echo "  [!] Whisper warmup failed — it will retry on first launch."

# --- 8. Permissions reminder ---
echo ""
echo "  ============================================================"
echo "   IMPORTANT: macOS permissions"
echo "  ============================================================"
echo "   Open System Settings → Privacy & Security and grant your"
echo "   Terminal (or whichever app runs Maahi) access to:"
echo ""
echo "     • Microphone         (required)"
echo "     • Accessibility      (required for AppleScript control)"
echo "     • Automation         (allow control of Calendar, Mail,"
echo "                           Reminders, Spotify, Messages, etc.)"
echo "     • Full Disk Access   (required to read Mail/Calendar DBs)"
echo ""
echo "  Done."
echo "  Launch with:  bash start.sh"
echo ""
