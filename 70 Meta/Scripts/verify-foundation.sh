#!/usr/bin/env bash
# Verify the Foundation phase Definition of Done.
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

echo "== Foundation verification =="
check "git initialized" "git rev-parse --git-dir"
check "pre-migration tag exists" "git rev-parse pre-migration-2026-05-15"
check "post-migration tag exists" "git rev-parse post-migration-2026-05-15"

for z in "00 Inbox" "10 Daily" "20 Compass" "30 Ventures" "40 Areas" "50 Atlas" "60 Outputs" "70 Meta" "99 Archive"; do
  check "zone exists: $z" "[[ -d \"$z\" ]]"
done

check "no '01 Inbox'" "[[ ! -d '01 Inbox' ]]"
check "no '90 Archive'" "[[ ! -d '90 Archive' ]]"
check "no '10 Personal Brand'" "[[ ! -d '10 Personal Brand' ]]"
check "no '20 Playbooks'" "[[ ! -d '20 Playbooks' ]]"

DUPES=$(find . -path ./.git -prune -o -name "*.md" -print0 2>/dev/null | xargs -0 -n1 basename | sort | uniq -d)
if [[ -z "$DUPES" ]]; then
  echo "  PASS  no duplicate filenames"; PASS=$((PASS+1))
else
  echo "  FAIL  duplicate filenames: $DUPES"; FAIL=$((FAIL+1))
fi

for p in obsidian-git templater-obsidian periodic-notes dataview obsidian-tasks-plugin quickadd homepage obsidian-icon-folder; do
  check "plugin installed: $p" "[[ -d '.obsidian/plugins/$p' ]]"
done

for t in "Inbox Quick Capture" "Daily Note" "Weekly Review" "Monthly Review" "Decision Log" "Venture Note" "Person Note" "Competitor Entry" "Experiment Log" "Content Idea"; do
  check "template: $t" "[[ -f '70 Meta/Templates/$t.md' ]]"
done

check "Home dashboard exists" "[[ -f '70 Meta/Dashboards/Home.md' ]]"

for v in Finanshels Biggdate StartupOS ZeroHuman MealVerse Soulmap; do
  check "venture overview: $v" "[[ -f '30 Ventures/$v/$v.md' ]]"
done

echo
echo "== $PASS passed, $FAIL failed =="
exit $((FAIL > 0 ? 1 : 0))
