# Capture Pipeline — Setup Guide

What you (Meet) need to do to finish wiring Subsystem 2. Three blocks, ~10 minutes total.

## A. Mac in-app capture (Obsidian open) — DONE

The QuickAdd macro `Quick Capture to Inbox` and hotkey `⌘⇧I` were written directly to the vault config. **Restart Obsidian** to load.

**Test:** open Obsidian → press `⌘⇧I` → input prompt should appear → type "test capture" → press Enter → check that `00 Inbox/2026-MM-DD-HHmm test capture.md` exists.

## B. Mac system-wide capture (any app) — 3 minutes

Goal: bind a global hotkey (suggested: `⌃⌥⌘Space`) that runs `70 Meta/Scripts/capture.sh` from anywhere on macOS.

### Easiest path: Automator Quick Action

1. Open **Automator** (Spotlight → "Automator").
2. New Document → **Quick Action**.
3. At the top: "Workflow receives" → **no input** in **any application**.
4. Drag in **Run Shell Script** action.
5. Pasted shell script:
   ```bash
   /bin/bash "/Users/themeetpatel/My brain/70 Meta/Scripts/capture.sh"
   ```
6. Save as: **Capture to Brain**.
7. Open **System Settings → Keyboard → Keyboard Shortcuts → Services → General**.
8. Find "Capture to Brain", click the keyboard column, press `⌃⌥⌘Space` (or your preferred chord).

**Test:** with any app focused (e.g., browser), press your chord → dialog appears → type → Enter. Check `00 Inbox/`. Should also auto-commit visible in `git log`.

### Alternative: Raycast / Alfred / Karabiner
Any of these can run the same `capture.sh` from a hotkey. Use whichever you already use.

## C. iPhone capture — 5 minutes

Goal: `Capture to Brain` works from Lockscreen widget, Siri, and Share sheet.

### One-time setup

1. **Install Working Copy** from the App Store (free; pro features not required).
2. In Working Copy: **+ → Clone repository** → `https://github.com/themeetpatell/meetpatel-brain.git`. Authenticate via GitHub (use a Personal Access Token if HTTPS).
3. **Install Shortcuts.app** if not already (it's preinstalled on most iPhones).
4. Create a new Shortcut named **Capture to Brain** with these actions in order:

   - **Ask for Input** — Prompt: "Capture:", Input Type: Text, Allow Multiple Lines: ON
   - **Get Current Date** — Format: Custom → `yyyy-MM-dd-HHmm`
   - **Text** (variable: `frontmatter`):
     ```
     ---
     type: inbox
     created: [Current Date formatted yyyy-MM-dd]
     captured_via: ios-shortcut
     tags: []
     ---
     
     # [Provided Input — first line, max 60 chars]
     
     [Provided Input — full]
     ```
   - **Save File** — Service: **Working Copy**, Destination: `meetpatel-brain/00 Inbox/`, File Name: `[Date]-[title].md`, Overwrite If Exists: OFF.
   - **Open URL**: `working-copy://x-callback-url/commit/?repo=meetpatel-brain&message=capture%20[title]&push=1`
   - **Show Notification** — "Captured ✓"

5. Save. Long-press the shortcut → **Add to Home Screen** (or add to Lockscreen widget via Wallpaper customization).
6. Test: tap the shortcut → enter text → wait 5–10s. Check GitHub repo's `00 Inbox/` for the new file. Within 10 min, your Mac vault will pull it via Obsidian Git.

### Use it from Siri
Once the Shortcut exists, say "Hey Siri, Capture to Brain" → Siri prompts → done.

### Use from Share sheet
Long-press the Shortcut → Details → toggle "Show in Share Sheet" ON. Now from Safari/Mail, share → Capture to Brain.

## D. Daily triage — already wired

Open today's daily note (`⌘⇧D`). The "Inbox to triage" section auto-lists all Inbox files. For each:
- **Move:** `⌘P` → "Move file to another folder" → pick destination.
- **Promote to typed note:** `⌘P` → "Templater: Replace templates in active file" → pick Decision Log / Person / etc.
- **Trash:** `⌘⌫`.

Goal: Inbox empty by end of the daily ritual.

## Verification

After completing A, B, C above:
```bash
bash "/Users/themeetpatel/My brain/70 Meta/Scripts/verify-capture.sh"
```
Should print all PASS. The script does NOT test the GUI parts (Automator binding, iOS Shortcut existence) — verify those manually with the smoke test above.
