#!/usr/bin/env bash
# Verify the Capture pipeline (Subsystem 2) Definition of Done.
cd "$(dirname "$0")/../.."
set -u
PASS=0
FAIL=0
check() {
  local name="$1" cmd="$2"
  if eval "$cmd" >/dev/null 2>&1; then
    echo "  PASS  $name"; PASS=$((PASS+1))
  else
    echo "  FAIL  $name"; FAIL=$((FAIL+1))
  fi
}

echo "== Capture pipeline verification =="

# In-vault prerequisites
check "QuickAdd macro 'Quick Capture to Inbox' configured" \
  "python3 -c \"import json; d=json.load(open('.obsidian/plugins/quickadd/data.json')); assert any(c['name']=='Quick Capture to Inbox' for c in d['choices'])\""
check "Hotkey ⌘⇧I bound to QuickAdd macro" \
  "python3 -c \"import json; d=json.load(open('.obsidian/hotkeys.json')); assert any('quickadd:choice:' in k and any(b['key']=='I' for b in v) for k,v in d.items())\""
check "Inbox template has captured_via field" \
  "grep -q 'captured_via' '70 Meta/Templates/Inbox Quick Capture.md'"
check "Daily Note template has Inbox triage section" \
  "grep -q 'Inbox to triage' '70 Meta/Templates/Daily Note.md'"
check "capture.sh exists and is executable" \
  "[[ -x '70 Meta/Scripts/capture.sh' ]]"
check "Inbox folder exists" "[[ -d '00 Inbox' ]]"

# End-to-end capture.sh test (skipped by default — requires GUI dialog)
echo "  SKIP  end-to-end capture.sh (interactive; run manually with: bash '70 Meta/Scripts/capture.sh')"

# Mobile setup is user-side; we only check the setup guide exists
check "Capture setup guide exists for user" "[[ -f '70 Meta/Scripts/capture-setup-guide.md' ]]"

echo
echo "== $PASS passed, $FAIL failed =="
exit $((FAIL > 0 ? 1 : 0))
