#!/usr/bin/env bash
# System-wide capture: AppleScript dialog → write to 00 Inbox/ → git commit & push.
# Bound to a global hotkey via Automator Quick Action (see capture-setup-guide.md).
#
# Exits silently on cancel. Logs to /tmp/capture.log.

set -uo pipefail

VAULT="${VAULT_PATH:-/Users/themeetpatel/My brain}"
LOG="/tmp/capture.log"
exec >>"$LOG" 2>&1
echo "=== $(date) ==="

cd "$VAULT" || { echo "vault not found: $VAULT"; exit 1; }

# Prompt via AppleScript. Captures Cancel by exiting non-zero from osascript.
INPUT=$(osascript -e '
tell application "System Events"
    activate
    set theResponse to display dialog "Capture to Brain:" default answer "" with title "🧠 Capture" buttons {"Cancel", "Save"} default button "Save"
    return text returned of theResponse
end tell
' 2>/dev/null) || { echo "user cancelled"; exit 0; }

# Empty input → no-op
[[ -z "${INPUT// /}" ]] && { echo "empty input, skipping"; exit 0; }

# Title = first line, sanitized for filename. Body = full input.
FIRST_LINE=$(echo "$INPUT" | head -1)
TITLE=$(echo "$FIRST_LINE" | tr -cd '[:alnum:][:space:]-_.' | cut -c1-60 | sed 's/[[:space:]]*$//')
[[ -z "$TITLE" ]] && TITLE="capture"

DATE=$(date +%Y-%m-%d)
TIME=$(date +%H%M)
FILE="00 Inbox/${DATE}-${TIME} ${TITLE}.md"

# Avoid overwriting if same timestamp + title (rare)
counter=1
ORIG="$FILE"
while [[ -e "$FILE" ]]; do
    FILE="${ORIG%.md} (${counter}).md"
    counter=$((counter + 1))
done

# Write with frontmatter
cat > "$FILE" <<NOTE
---
type: inbox
created: ${DATE}
captured_via: mac-shortcut
tags: []
---

# ${TITLE}

${INPUT}
NOTE

echo "wrote: $FILE"

# Auto-commit and push (non-blocking on failure)
if git add "$FILE" 2>/dev/null && git commit -m "capture: ${TITLE}" --quiet 2>/dev/null; then
    echo "committed"
    if git push --quiet 2>/dev/null; then
        echo "pushed"
    else
        echo "push failed (will retry on next sync)"
    fi
else
    echo "commit failed or no changes"
fi

# Brief notification
osascript -e "display notification \"${TITLE}\" with title \"🧠 Captured\"" 2>/dev/null || true
