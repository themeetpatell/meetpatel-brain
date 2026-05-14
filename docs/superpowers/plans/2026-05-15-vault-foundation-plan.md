# Vault Foundation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Migrate the existing 306-note Obsidian vault to the 8-zone Founder OS structure, install and configure 9 plugins, create 10 templates, and ship the operator dashboard — all under Git with full rollback.

**Architecture:** Six sequential phases (Pre-flight → Migration → Plugins → Templates → Dashboard → Verification). Every phase ends in a Git commit. The full implementation is reversible at any point via `git reset --hard <pre-migration-tag>`.

**Tech Stack:** Obsidian 1.7+ (with core Bases plugin), Bash, Git, plus 8 Obsidian community plugins (Obsidian Git, Templater, Periodic Notes, Dataview, Tasks, QuickAdd, Homepage, Iconize).

**Spec:** [`docs/superpowers/specs/2026-05-15-vault-foundation-design.md`](../specs/2026-05-15-vault-foundation-design.md)

**Working directory:** `/Users/themeetpatel/My brain` for all commands.

---

## Phase A — Pre-flight (no destructive changes)

### Task 1: Verify Git state and dedupe filenames

**Files:**
- Read-only: entire vault
- Modify: any duplicate filenames (rename losers to `<name> (dup).md`)

- [ ] **Step 1: Confirm Git is initialized and the spec commit exists**

Run:
```bash
cd "/Users/themeetpatel/My brain"
git log --oneline
```
Expected: at least one commit, the most recent being `docs: vault foundation design spec (subsystem 1 of 5)`.

If no Git: STOP. Re-run the brainstorming-skill commit step. The spec commit must exist as the rollback anchor.

- [ ] **Step 2: Tag the pre-migration anchor**

Run:
```bash
git tag pre-migration-2026-05-15
git tag --list
```
Expected output includes `pre-migration-2026-05-15`. This is the rollback target if anything goes wrong.

- [ ] **Step 3: Detect duplicate filenames**

Run:
```bash
find . -path ./.git -prune -o -name "*.md" -print | xargs -n1 basename 2>/dev/null | sort | uniq -d
```
Expected: empty output. If any duplicates appear, list them in the next step.

- [ ] **Step 4: Rename any duplicates (only if Step 3 returned anything)**

For each duplicate name `X.md` returned by Step 3:
1. Find both copies: `find . -name "X.md" -not -path "./.git/*"`
2. Decide which is the "primary" by checking modification dates and content.
3. Rename the secondary: `git mv "<path>/X.md" "<path>/X (dup).md"`
4. Re-run Step 3 — output must now be empty before continuing.

- [ ] **Step 5: Commit if any renames happened**

If Step 4 made changes:
```bash
git status
git commit -am "chore: rename duplicate filenames before migration"
```
If no changes: skip the commit.

---

### Task 2: Snapshot the destructive-split source folder

**Files:**
- Create: `99 Archive/2026-05-15-pre-migration-snapshot/28 First 30 Core Notes/` (copy)

- [ ] **Step 1: Create the snapshot directory**

Run:
```bash
mkdir -p "99 Archive/2026-05-15-pre-migration-snapshot"
```

- [ ] **Step 2: Copy (don't move) the source folder**

`28 First 30 Core Notes/` will be split into multiple destinations during Phase B. The snapshot preserves the original layout for archeology.

Run:
```bash
cp -R "28 First 30 Core Notes" "99 Archive/2026-05-15-pre-migration-snapshot/"
ls "99 Archive/2026-05-15-pre-migration-snapshot/28 First 30 Core Notes/" | wc -l
```
Expected: 31 (30 numbered notes + 1 index).

- [ ] **Step 3: Commit the snapshot**

```bash
git add "99 Archive/2026-05-15-pre-migration-snapshot"
git commit -m "chore: snapshot 28 First 30 Core Notes before migration split"
```

---

## Phase B — Structural migration

### Task 3: Create the empty 8-zone scaffold

**Files:**
- Create: 30+ empty directories (zone roots and sub-folders).

- [ ] **Step 1: Create all new zone directories**

Run:
```bash
cd "/Users/themeetpatel/My brain"
mkdir -p \
  "10 Daily/Daily" \
  "10 Daily/Weekly" \
  "10 Daily/Monthly" \
  "10 Daily/Journal" \
  "20 Compass/Identity" \
  "20 Compass/Principles" \
  "20 Compass/Decisions" \
  "20 Compass/Vision" \
  "20 Compass/Dossier" \
  "30 Ventures/Finanshels/Notes" \
  "30 Ventures/Biggdate/Notes" \
  "30 Ventures/StartupOS/Notes" \
  "30 Ventures/ZeroHuman/Notes" \
  "30 Ventures/MealVerse/Notes" \
  "30 Ventures/Soulmap/Notes" \
  "40 Areas/Self" \
  "40 Areas/Brand" \
  "40 Areas/Money" \
  "40 Areas/Relationships" \
  "40 Areas/Health" \
  "50 Atlas/Competitive" \
  "50 Atlas/Signals" \
  "50 Atlas/Playbooks" \
  "50 Atlas/Experiments" \
  "50 Atlas/Resources" \
  "60 Outputs/Content" \
  "60 Outputs/Dossier" \
  "70 Meta/Templates" \
  "70 Meta/Scripts/migrations" \
  "70 Meta/Dashboards" \
  "70 Meta/Bases" \
  "70 Meta/MOCs"
```

- [ ] **Step 2: Verify scaffold**

Run:
```bash
find . -maxdepth 2 -type d -name "[0-9][0-9]*" | sort
```
Expected: lists all 8 numbered zone roots (`./00 Inbox`, `./10 Daily`, `./20 Compass`, `./30 Ventures`, `./40 Areas`, `./50 Atlas`, `./60 Outputs`, `./70 Meta`, `./99 Archive`) plus their immediate sub-folders.

- [ ] **Step 3: Commit the scaffold**

Empty directories aren't tracked by Git. Add a `.gitkeep` to each:
```bash
find "10 Daily" "20 Compass" "30 Ventures" "40 Areas" "50 Atlas" "60 Outputs" "70 Meta" -type d -empty -exec touch {}/.gitkeep \;
git add -A
git commit -m "feat: create Founder OS zone scaffold"
```

---

### Task 4: Write the migration script

**Files:**
- Create: `70 Meta/Scripts/migrations/2026-05-15-foundation-migration.sh`

- [ ] **Step 1: Create the script file**

Write this exact content to `70 Meta/Scripts/migrations/2026-05-15-foundation-migration.sh`:

```bash
#!/usr/bin/env bash
# 2026-05-15 Foundation migration: old structure -> 8-zone Founder OS.
# Each `git mv` of a missing source is silently skipped via mv_if_exists.
set -u  # do NOT use -e — we want to continue past individual mv failures
cd "$(dirname "$0")/../../.."

mv_if_exists() {
  local src="$1" dst="$2"
  if [[ -e "$src" ]]; then
    mkdir -p "$(dirname "$dst")"
    git mv "$src" "$dst" && echo "moved: $src -> $dst"
  else
    echo "skip (not found): $src"
  fi
}

mv_folder_contents() {
  # Move every file/dir inside $1 into $2 (preserving filenames).
  local src="$1" dst="$2"
  if [[ -d "$src" ]]; then
    shopt -s nullglob dotglob
    for f in "$src"/*; do
      [[ "$(basename "$f")" == ".gitkeep" ]] && continue
      local name="$(basename "$f")"
      if [[ -e "$dst/$name" ]]; then
        git mv "$f" "$dst/${name%.*} (from $(basename "$src")).${name##*.}" \
          && echo "moved (renamed): $f -> $dst"
      else
        git mv "$f" "$dst/$name" && echo "moved: $f -> $dst/$name"
      fi
    done
    shopt -u nullglob dotglob
    rmdir "$src" 2>/dev/null && echo "removed empty: $src"
  fi
}

# --- Inbox merge ---
mv_folder_contents "01 Inbox" "00 Inbox"

# --- Daily/Journal/Weekly ---
mv_folder_contents "01 Daily Notes" "10 Daily/Daily"
mv_folder_contents "02 Weekly Reviews" "10 Daily/Weekly"
mv_folder_contents "02 Journal" "10 Daily/Journal"

# --- Compass ---
mv_folder_contents "30 Decisions" "20 Compass/Decisions"
mv_folder_contents "51 About Me" "20 Compass/Identity"
mv_folder_contents "17 Founder Dossier" "20 Compass/Dossier"

# --- Ventures (legacy 11 Biggdate folder, if exists) ---
if [[ -d "11 Biggdate" ]]; then
  git mv "11 Biggdate" "30 Ventures/Biggdate/legacy" && echo "moved: 11 Biggdate"
fi

# --- Outputs ---
mv_folder_contents "10 Personal Brand" "60 Outputs/Content"
mv_folder_contents "14 Content Ideas" "60 Outputs/Content"

# --- Atlas ---
mv_folder_contents "12 Competitive Intelligence" "50 Atlas/Competitive"
mv_folder_contents "13 Market Signals" "50 Atlas/Signals"
mv_folder_contents "15 Growth Experiments" "50 Atlas/Experiments"
mv_folder_contents "20 Playbooks" "50 Atlas/Playbooks"
mv_folder_contents "30 Resources" "50 Atlas/Resources"

# --- Areas (sub-folders mapped explicitly) ---
if [[ -d "20 Areas" ]]; then
  shopt -s nullglob dotglob
  for f in "20 Areas"/*; do
    name="$(basename "$f")"
    [[ "$name" == ".gitkeep" ]] && continue
    case "$name" in
      "21 Self") git mv "$f" "40 Areas/Self/legacy" ;;
      "22 Ventures")
        # Ventures live under 30 Ventures now. Move contents one-by-one
        # to inbox for human triage rather than blindly archive.
        mv_folder_contents "$f" "00 Inbox"
        ;;
      "24 Brand & Content") git mv "$f" "40 Areas/Brand/legacy" ;;
      "25 Relationships") git mv "$f" "40 Areas/Relationships/legacy" ;;
      "26 Money & Wealth") git mv "$f" "40 Areas/Money/legacy" ;;
      "27 Health & Life") git mv "$f" "40 Areas/Health/legacy" ;;
      *) git mv "$f" "40 Areas/$name" ;;
    esac
  done
  shopt -u nullglob dotglob
  rmdir "20 Areas" 2>/dev/null
fi

# --- Meta ---
if [[ -d "40 Templates" ]]; then
  shopt -s nullglob
  for f in "40 Templates"/*.md; do
    base="$(basename "$f" .md)"
    git mv "$f" "70 Meta/Templates/${base} (legacy).md"
  done
  shopt -u nullglob
  rmdir "40 Templates" 2>/dev/null
fi
mv_folder_contents "90 Dashboards" "70 Meta/Dashboards"
mv_folder_contents "00 Home" "70 Meta/Dashboards"

if [[ -f "Untitled.base" ]]; then
  git mv "Untitled.base" "70 Meta/Bases/inbox.base" && echo "moved: Untitled.base"
fi

# --- Archive merge ---
mv_folder_contents "90 Archive" "99 Archive"

# --- 10 Projects (mostly _Sunset) ---
if [[ -d "10 Projects" ]]; then
  if [[ -d "10 Projects/_Sunset" ]]; then
    git mv "10 Projects/_Sunset" "99 Archive/sunset-projects" && echo "moved: 10 Projects/_Sunset"
  fi
  shopt -s nullglob
  for f in "10 Projects"/*; do
    [[ "$(basename "$f")" == ".gitkeep" ]] && continue
    echo "MANUAL TRIAGE NEEDED: $f (assign to 30 Ventures/<name>/ or 99 Archive/)"
  done
  shopt -u nullglob
  rmdir "10 Projects" 2>/dev/null
fi

echo
echo "DONE. Review 'MANUAL TRIAGE NEEDED' lines above (Task 6)."
echo "Then run Task 7 to split '28 First 30 Core Notes/'."
```

- [ ] **Step 2: Make it executable**

```bash
chmod +x "70 Meta/Scripts/migrations/2026-05-15-foundation-migration.sh"
```

- [ ] **Step 3: Commit the script (don't run yet)**

```bash
git add "70 Meta/Scripts/migrations/2026-05-15-foundation-migration.sh"
git commit -m "feat: add foundation migration script"
```

---

### Task 5: Run the migration script

**Files:** entire vault (script does the moves)

- [ ] **Step 1: Pre-run snapshot of top-level folders**

```bash
git status        # must be clean
ls -d [0-9]* | sort
```
Note the current top-level numbered folders. After Step 2 only `00 Inbox`, `10 Daily`, `20 Compass`, `28 First 30 Core Notes`, `30 Ventures`, `40 Areas`, `50 Atlas`, `60 Outputs`, `70 Meta`, `99 Archive` should remain (modulo `10 Projects` if any unmapped notes remain).

- [ ] **Step 2: Run the migration**

```bash
bash "70 Meta/Scripts/migrations/2026-05-15-foundation-migration.sh" 2>&1 | tee /tmp/migration.log
```
Expected: many `moved:` and `removed empty:` lines. Watch for `MANUAL TRIAGE NEEDED:` lines — those need Task 6.

- [ ] **Step 3: Inspect leftover top-level folders**

```bash
ls -d [0-9]* | sort
```
Expected (in some order): `00 Inbox`, `10 Daily`, `20 Compass`, `28 First 30 Core Notes`, `30 Ventures`, `40 Areas`, `50 Atlas`, `60 Outputs`, `70 Meta`, `99 Archive`. The `28 First 30 Core Notes` folder is intentional — it gets split in Task 7.

If any other old numbered folder remains (e.g., `15 Growth Experiments`), the script's check missed it. Investigate before continuing.

- [ ] **Step 4: Verify wikilinks not broken (sample)**

```bash
find . -name "*.md" -not -path "./.git/*" -not -path "./99 Archive/*" -exec grep -l "\[\[" {} \; | head -5
```
Open one of these files in Obsidian after migration commit (Task 8) and confirm wikilinks resolve.

---

### Task 6: Triage any unmapped `10 Projects/` notes

**Files:** Any leftover files in `10 Projects/` (interactive)

- [ ] **Step 1: List leftover files**

```bash
find "10 Projects" -type f 2>/dev/null
```
If empty: the directory was removed by the script in Task 5; skip the rest of this task and move to Task 7.

- [ ] **Step 2: For each remaining file, choose a destination**

For each file, decide:
- Belongs to a venture → `git mv "<file>" "30 Ventures/<VentureName>/Notes/<file>"`
- Generic learning → `git mv "<file>" "50 Atlas/Resources/<file>"`
- Archive → `git mv "<file>" "99 Archive/<file>"`

Then `rmdir "10 Projects" 2>/dev/null` once empty.

---

### Task 7: Split `28 First 30 Core Notes/` per the design mapping

**Files:** 31 files moved out of `28 First 30 Core Notes/`

- [ ] **Step 1: Move identity-themed notes to Compass/Identity**

```bash
cd "/Users/themeetpatel/My brain"
for f in \
  "01 Who I Am.md" \
  "02 What I Stand For.md" \
  "04 My Founder Story.md" \
  "05 My Writing Voice.md" \
  "06 My Strategic Themes.md" \
  "22 Brand Positioning.md"; do
  [[ -f "28 First 30 Core Notes/$f" ]] && git mv "28 First 30 Core Notes/$f" "20 Compass/Identity/$f"
done
```

- [ ] **Step 2: Move operating-system notes to Compass/Principles**

```bash
for f in \
  "13 My Operating System.md" \
  "14 My Content System.md" \
  "15 My Research System.md" \
  "16 My Relationship System.md" \
  "17 My Wealth System.md" \
  "18 My Health System.md" \
  "24 Signature Frameworks.md"; do
  [[ -f "28 First 30 Core Notes/$f" ]] && git mv "28 First 30 Core Notes/$f" "20 Compass/Principles/$f"
done
```

- [ ] **Step 3: Move vision-themed notes to Compass/Vision**

```bash
for f in \
  "03 What I Am Building.md" \
  "25 Ideal Week.md" \
  "26 Life Vision.md" \
  "28 Things I Need to Cut.md" \
  "30 Next 90 Days.md"; do
  [[ -f "28 First 30 Core Notes/$f" ]] && git mv "28 First 30 Core Notes/$f" "20 Compass/Vision/$f"
done
```

- [ ] **Step 4: Move venture snapshots to per-venture READMEs**

```bash
declare -A snapshots=(
  ["07 Finanshels Snapshot.md"]="Finanshels"
  ["08 StartupOS Snapshot.md"]="StartupOS"
  ["09 Biggdate Snapshot.md"]="Biggdate"
  ["10 ZeroHuman Snapshot.md"]="ZeroHuman"
  ["11 MealVerse Snapshot.md"]="MealVerse"
  ["12 Soulmap Snapshot.md"]="Soulmap"
)
for src in "${!snapshots[@]}"; do
  v="${snapshots[$src]}"
  if [[ -f "28 First 30 Core Notes/$src" ]]; then
    git mv "28 First 30 Core Notes/$src" "30 Ventures/$v/README.md"
  fi
done
```

- [ ] **Step 5: Move dashboards-as-notes to Meta/Dashboards**

```bash
for f in \
  "19 Current Priorities.md" \
  "20 Key Decisions.md" \
  "21 Open Loops.md"; do
  [[ -f "28 First 30 Core Notes/$f" ]] && git mv "28 First 30 Core Notes/$f" "70 Meta/Dashboards/$f"
done
```

Note: `20 Key Decisions.md` could also live in `20 Compass/Decisions/`. We put it in Dashboards because it's a curated list of *the* most important decisions, distinct from the per-decision logs in `20 Compass/Decisions/`.

- [ ] **Step 6: Move remainders to their right homes**

```bash
[[ -f "28 First 30 Core Notes/23 AI Systems Stack.md" ]] && git mv "28 First 30 Core Notes/23 AI Systems Stack.md" "50 Atlas/Resources/23 AI Systems Stack.md"
[[ -f "28 First 30 Core Notes/27 People I Want Closer.md" ]] && git mv "28 First 30 Core Notes/27 People I Want Closer.md" "40 Areas/Relationships/27 People I Want Closer.md"
[[ -f "28 First 30 Core Notes/29 Proof Archive.md" ]] && git mv "28 First 30 Core Notes/29 Proof Archive.md" "60 Outputs/29 Proof Archive.md"
[[ -f "28 First 30 Core Notes/00 Core Notes Index.md" ]] && git mv "28 First 30 Core Notes/00 Core Notes Index.md" "70 Meta/MOCs/Core Notes Index (legacy).md"
```

- [ ] **Step 7: Verify and remove the empty source folder**

```bash
ls "28 First 30 Core Notes/" 2>/dev/null
```
Expected: empty. If anything remains, place it manually (likely a typo in earlier steps), then:
```bash
rmdir "28 First 30 Core Notes"
```

---

### Task 8: Verify migration completeness and commit

**Files:** Verification only

- [ ] **Step 1: Confirm only canonical zones remain at root**

```bash
ls -d [0-9]* | sort
```
Expected exactly: `00 Inbox`, `10 Daily`, `20 Compass`, `30 Ventures`, `40 Areas`, `50 Atlas`, `60 Outputs`, `70 Meta`, `99 Archive`. Nothing else.

- [ ] **Step 2: Re-confirm no duplicate filenames**

```bash
find . -path ./.git -prune -o -name "*.md" -print | xargs -n1 basename | sort | uniq -d
```
Expected: empty.

- [ ] **Step 3: Confirm note count preserved**

```bash
find . -name "*.md" -not -path "./.git/*" | wc -l
```
Expected: ≥ 306 (slightly more if any READMEs or migrated copies were added; the snapshot copy in Step 2 of Task 2 added 31 files). If significantly less, files were lost — DO NOT COMMIT, investigate `git status -uno`.

- [ ] **Step 4: Commit the migration**

```bash
git status   # review what's about to land
git add -A
git commit -m "feat: migrate vault to Founder OS 8-zone structure"
git tag post-migration-2026-05-15
```

**Phase B rollback:** if anything is wrong: `git reset --hard pre-migration-2026-05-15`.

---

## Phase C — Plugin install & configuration

### Task 9: Install all 9 plugins via Obsidian Community Browser

**Files:** Obsidian writes `.obsidian/plugins/<id>/` directories

This phase requires the Obsidian desktop app to be open.

- [ ] **Step 1: Open Obsidian → Settings → Community Plugins → Turn on community plugins**

Click the toggle to enable community plugins. Acknowledge the safety dialog.

- [ ] **Step 2: Install each plugin**

Click **Browse**. For each plugin below: search → click result → **Install** → **Enable**. Then return to Browse for the next.

- [ ] Obsidian Git
- [ ] Templater
- [ ] Periodic Notes
- [ ] Dataview
- [ ] Tasks
- [ ] QuickAdd
- [ ] Homepage
- [ ] Iconize

- [ ] **Step 3: Enable Bases (core plugin)**

Settings → Core Plugins → toggle **Bases** ON.

- [ ] **Step 4: Verify all 9 are present**

In a terminal:
```bash
ls .obsidian/plugins/
```
Expected: 8 directories — `obsidian-git`, `templater-obsidian`, `periodic-notes`, `dataview`, `obsidian-tasks-plugin`, `quickadd`, `homepage`, `obsidian-icon-folder` (Iconize). Bases is core so won't appear here. Folder names are plugin IDs and may differ slightly; presence of 8 directories is what matters.

- [ ] **Step 5: Snapshot commit**

```bash
git add .obsidian/plugins/ .obsidian/community-plugins.json 2>/dev/null
git commit -m "feat: install foundation plugin stack"
```

---

### Task 10: Configure Obsidian Git

**Files:** `.obsidian/plugins/obsidian-git/data.json` (managed via Obsidian UI)

- [ ] **Step 1: Open Settings → Community Plugins → Obsidian Git → Options**

- [ ] **Step 2: Set the following (leave others at defaults)**

| Setting | Value |
|---|---|
| Vault backup interval (minutes) | `10` |
| Auto pull interval (minutes) | `0` (off — single user, single machine for now) |
| Pull updates on startup | ON |
| Commit message on auto backup/commit | `vault: {{date}} {{hostname}}` |
| Commit author name | `Meet Patel` |
| Commit author email | `meet@finanshels.com` |

- [ ] **Step 3: Verify config wrote to disk**

```bash
cat .obsidian/plugins/obsidian-git/data.json
```
Expected: a JSON object containing your settings. If file doesn't exist yet, force-save by toggling any option then back.

- [ ] **Step 4: Commit**

```bash
git add .obsidian/plugins/obsidian-git/data.json
git commit -m "feat: configure obsidian-git auto-commit (10 min interval)"
```

---

### Task 11: Configure Templater

**Files:** `.obsidian/plugins/templater-obsidian/data.json` (managed via UI)

- [ ] **Step 1: Open Settings → Templater**

- [ ] **Step 2: Set general options**

| Setting | Value |
|---|---|
| Template folder location | `70 Meta/Templates` |
| Trigger Templater on new file creation | ON |
| Show Templater command palette in editor | ON |

- [ ] **Step 3: Add folder template mappings**

In "Folder Templates" section, click **Add new** for each row:

| Folder | Template |
|---|---|
| `00 Inbox` | `Inbox Quick Capture` |
| `10 Daily/Daily` | `Daily Note` |
| `10 Daily/Weekly` | `Weekly Review` |
| `10 Daily/Monthly` | `Monthly Review` |
| `20 Compass/Decisions` | `Decision Log` |
| `40 Areas/Relationships` | `Person Note` |
| `50 Atlas/Competitive` | `Competitor Entry` |
| `50 Atlas/Experiments` | `Experiment Log` |
| `60 Outputs/Content` | `Content Idea` |

Note: `30 Ventures/*/Notes/` is also supposed to auto-apply `Venture Note`. Templater's folder mapping doesn't natively support globs — add the 6 explicit rows:
- `30 Ventures/Finanshels/Notes` → `Venture Note`
- `30 Ventures/Biggdate/Notes` → `Venture Note`
- `30 Ventures/StartupOS/Notes` → `Venture Note`
- `30 Ventures/ZeroHuman/Notes` → `Venture Note`
- `30 Ventures/MealVerse/Notes` → `Venture Note`
- `30 Ventures/Soulmap/Notes` → `Venture Note`

The template files themselves don't exist yet (Task 16 creates them) — Templater will warn. That's fine; the mappings are saved and will activate as soon as the templates exist.

- [ ] **Step 4: Commit**

```bash
git add .obsidian/plugins/templater-obsidian/data.json
git commit -m "feat: configure templater folder mappings"
```

---

### Task 12: Configure Periodic Notes

- [ ] **Step 1: Open Settings → Periodic Notes**

- [ ] **Step 2: Daily Notes**

| Setting | Value |
|---|---|
| Enable Daily Notes | ON |
| Date format | `YYYY-MM-DD` |
| New file location | `10 Daily/Daily` |
| Template file location | `70 Meta/Templates/Daily Note` |

- [ ] **Step 3: Weekly Notes**

| Setting | Value |
|---|---|
| Enable Weekly Notes | ON |
| Date format | `YYYY-[W]ww` |
| New file location | `10 Daily/Weekly` |
| Template file location | `70 Meta/Templates/Weekly Review` |
| Start week on | Monday |

- [ ] **Step 4: Monthly Notes**

| Setting | Value |
|---|---|
| Enable Monthly Notes | ON |
| Date format | `YYYY-MM` |
| New file location | `10 Daily/Monthly` |
| Template file location | `70 Meta/Templates/Monthly Review` |

- [ ] **Step 5: Commit**

```bash
git add .obsidian/plugins/periodic-notes/data.json
git commit -m "feat: configure periodic notes (daily/weekly/monthly)"
```

---

### Task 13: Configure Dataview, Tasks, Homepage, Iconize, Bases

These are smaller configs — bundled into one task.

- [ ] **Step 1: Dataview**

Settings → Dataview:
- Enable JavaScript Queries: ON
- Enable Inline JavaScript Queries: ON
- Enable Inline Queries: ON
- Default date format: `MMMM dd, yyyy`

- [ ] **Step 2: Tasks**

Settings → Tasks:
- Global query filter: `path does not include 99 Archive`
- Set done date on every completed task: ON
- Use modal for new tasks: ON

- [ ] **Step 3: Homepage**

Settings → Homepage:
- Homepage: `70 Meta/Dashboards/Home` (Home.md is created in Task 17; this setting can be saved before the file exists)
- Open on startup: ON
- Open in new tab: OFF

- [ ] **Step 4: Iconize**

Settings → Iconize:
- Install icon pack: search "Lucide" → install
- For each top-level zone folder, right-click in file explorer → Change icon, pick:
  - `00 Inbox` → `inbox`
  - `10 Daily` → `calendar-days`
  - `20 Compass` → `compass`
  - `30 Ventures` → `rocket`
  - `40 Areas` → `layers`
  - `50 Atlas` → `library`
  - `60 Outputs` → `send`
  - `70 Meta` → `settings-2`
  - `99 Archive` → `archive`

- [ ] **Step 5: Bases**

Settings → Core Plugins → Bases — confirm enabled (set in Task 9 Step 3). No further config needed.

- [ ] **Step 6: Commit all configs**

```bash
git add .obsidian/plugins/dataview/data.json .obsidian/plugins/obsidian-tasks-plugin/data.json .obsidian/plugins/homepage/data.json .obsidian/plugins/obsidian-icon-folder/data.json .obsidian/core-plugins.json 2>/dev/null
git commit -m "feat: configure dataview, tasks, homepage, iconize, bases"
```

---

### Task 14: Configure QuickAdd — 6 capture macros

**Files:** `.obsidian/plugins/quickadd/data.json`

- [ ] **Step 1: Open Settings → QuickAdd**

- [ ] **Step 2: Create 6 choices, one at a time**

For each row below: click **Add Choice** → choose Type → fill the fields.

| Name | Type | Settings |
|---|---|---|
| Quick Capture to Inbox | Capture | Capture To: `00 Inbox/{{DATE:YYYY-MM-DD-HHmm}} {{VALUE}}.md` · Insert after: ON · Format: Templater (use `Inbox Quick Capture` template) |
| Open Today | Template | Template path: `70 Meta/Templates/Daily Note.md` · Folder: `10 Daily/Daily` · File name: `{{DATE:YYYY-MM-DD}}` · Open file: ON · Append link: OFF |
| New Decision | Template | Template path: `70 Meta/Templates/Decision Log.md` · Folder: `20 Compass/Decisions` · File name: `{{DATE:YYYY-MM-DD}} {{VALUE}}` · Prompt for filename: ON |
| New Person | Template | Template: `70 Meta/Templates/Person Note.md` · Folder: `40 Areas/Relationships` · File name: `{{VALUE}}` · Prompt: ON |
| New Venture Note | Macro | Macro steps: (1) UserScript prompt for venture from list `Finanshels,Biggdate,StartupOS,ZeroHuman,MealVerse,Soulmap` → variable `venture`; (2) Template `Venture Note` into folder `30 Ventures/{{VALUE:venture}}/Notes/` with filename `{{DATE:YYYY-MM-DD}} {{VALUE}}` |
| New Content Idea | Template | Template: `70 Meta/Templates/Content Idea.md` · Folder: `60 Outputs/Content` · File name: `{{VALUE}}` · Prompt: ON |

- [ ] **Step 3: Commit**

```bash
git add .obsidian/plugins/quickadd/data.json
git commit -m "feat: add quickadd macros for 6 capture flows"
```

---

### Task 15: Bind the 7 hotkeys

**Files:** `.obsidian/hotkeys.json` (managed via UI)

- [ ] **Step 1: Open Settings → Hotkeys**

- [ ] **Step 2: Search and bind each**

Search the hotkey list, click the keyboard icon, press the chord. If a conflict appears, accept overriding the default.

| Search for | Bind to |
|---|---|
| `QuickAdd: Quick Capture to Inbox` | `Cmd+Shift+I` |
| `QuickAdd: Open Today` | `Cmd+Shift+D` |
| `QuickAdd: New Decision` | `Cmd+Shift+L` |
| `QuickAdd: New Person` | `Cmd+Shift+M` |
| `QuickAdd: New Venture Note` | `Cmd+Shift+V` |
| `QuickAdd: New Content Idea` | `Cmd+Shift+C` |
| `Bookmarks: Open bookmark Home` (after bookmarking Home.md) | `Cmd+Shift+H` |

For the Home hotkey: enable the **Bookmarks** core plugin if not already; right-click `70 Meta/Dashboards/Home.md` → **Bookmark** → name it `Home`. Then bind that bookmark to the chord.

- [ ] **Step 3: Commit**

```bash
git add .obsidian/hotkeys.json .obsidian/bookmarks.json 2>/dev/null
git commit -m "feat: bind 7 capture/navigation hotkeys"
```

---

## Phase D — Templates

### Task 16: Write the 10 templates

**Files:** Create 10 files under `70 Meta/Templates/`.

- [ ] **Step 1: Create `70 Meta/Templates/Inbox Quick Capture.md`**

```markdown
---
type: inbox
created: <% tp.date.now("YYYY-MM-DD") %>
tags: []
---

# <% tp.file.title %>


```

- [ ] **Step 2: Create `70 Meta/Templates/Daily Note.md`**

````markdown
---
type: daily
created: <% tp.date.now("YYYY-MM-DD") %>
focus: 
tags: [daily]
---

# <% tp.date.now("dddd, MMMM Do, YYYY") %>

## Top 3 Today
1. 
2. 
3. 

## Calendar


## Open Loops (next 7 days)
```dataview
TASK
FROM ""
WHERE !completed AND due AND due <= date(today) + dur(7 days)
SORT due ASC
```

## Notes


## Evening Reflection
- What worked: 
- What didn't: 
- Tomorrow's #1: 
````

- [ ] **Step 3: Create `70 Meta/Templates/Weekly Review.md`**

````markdown
---
type: weekly
created: <% tp.date.now("YYYY-MM-DD") %>
week: <% tp.date.now("YYYY-[W]ww") %>
tags: [weekly]
---

# Week of <% tp.date.now("MMMM Do, YYYY") %>

## Wins


## Lessons


## Decisions Made This Week
```dataview
LIST
FROM "20 Compass/Decisions"
WHERE created >= date(today) - dur(7 days)
SORT created DESC
```

## Open Loops Carried Over


## Per-Venture Status
- **Finanshels** — 
- **Biggdate** — 
- **StartupOS** — 
- **ZeroHuman** — 
- **MealVerse** — 
- **Soulmap** — 

## Next Week's Focus
1. 
2. 
3. 
````

- [ ] **Step 4: Create `70 Meta/Templates/Monthly Review.md`**

````markdown
---
type: monthly
created: <% tp.date.now("YYYY-MM-DD") %>
month: <% tp.date.now("YYYY-MM") %>
tags: [monthly]
---

# <% tp.date.now("MMMM YYYY") %>

## Theme of the Month


## Key Decisions
```dataview
LIST
FROM "20 Compass/Decisions"
WHERE created >= date(today) - dur(30 days)
SORT created DESC
```

## Content Shipped
```dataview
LIST
FROM "60 Outputs/Content"
WHERE status = "published" AND created >= date(today) - dur(30 days)
```

## Relationships Nurtured


## Per-Venture North-Star Metrics
- **Finanshels** — 
- **Biggdate** — 
- **StartupOS** — 
- **ZeroHuman** — 
- **MealVerse** — 
- **Soulmap** — 

## What I'm Carrying Into Next Month
````

- [ ] **Step 5: Create `70 Meta/Templates/Decision Log.md`**

```markdown
---
type: decision
created: <% tp.date.now("YYYY-MM-DD") %>
status: open
review_date: <% tp.date.now("YYYY-MM-DD", 30) %>
ventures: []
tags: [decision]
---

# <% tp.file.title %>

## Context


## Options Considered
1. 
2. 
3. 

## Decision


## Reasoning


## Expected Outcome


## Review (filled on review_date)
- Outcome: 
- Lesson: 
```

- [ ] **Step 6: Create `70 Meta/Templates/Venture Note.md`**

```markdown
---
type: venture
created: <% tp.date.now("YYYY-MM-DD") %>
venture: 
subtype: exec
tags: [venture]
---

# <% tp.file.title %>

## Summary


## Action


## Links
- 
```

- [ ] **Step 7: Create `70 Meta/Templates/Person Note.md`**

```markdown
---
type: person
created: <% tp.date.now("YYYY-MM-DD") %>
last_contact: <% tp.date.now("YYYY-MM-DD") %>
follow_up: false
cadence_days: 14
ventures: []
tags: [person]
---

# <% tp.file.title %>

**Role:** 
**Relationship goal:** 

## Recent Context


## Follow-up
- 
```

- [ ] **Step 8: Create `70 Meta/Templates/Competitor Entry.md`**

```markdown
---
type: competitor
created: <% tp.date.now("YYYY-MM-DD") %>
market: 
last_reviewed: <% tp.date.now("YYYY-MM-DD") %>
tags: [competitor]
---

# <% tp.file.title %>

**ICP:** 
**Pricing:** 

## Strengths


## Weaknesses


## Signals (changes worth watching)


## Last Review Notes
```

- [ ] **Step 9: Create `70 Meta/Templates/Experiment Log.md`**

```markdown
---
type: experiment
created: <% tp.date.now("YYYY-MM-DD") %>
hypothesis: 
ice_score: 0
status: planned
ventures: []
tags: [experiment]
---

# <% tp.file.title %>

## Hypothesis


## ICE
- Impact (1-10): 
- Confidence (1-10): 
- Ease (1-10): 

## Setup


## Result


## Learning


## Next Step
```

- [ ] **Step 10: Create `70 Meta/Templates/Content Idea.md`**

```markdown
---
type: content
created: <% tp.date.now("YYYY-MM-DD") %>
status: idea
format: post
audience: 
tags: [content]
---

# <% tp.file.title %>

## Hook


## Audience


## Angle


## Distribution
- 
```

- [ ] **Step 11: Verify all 10 templates exist and contain frontmatter**

```bash
ls "70 Meta/Templates/" | grep -v legacy | sort
for f in "70 Meta/Templates"/*.md; do
  head -3 "$f" | grep -q "^type:" && echo "OK: $f" || echo "MISSING type: $f"
done
```
Expected: 10 entries listed (excluding any `*legacy*` files); all show `OK: ...`.

- [ ] **Step 12: Commit**

```bash
git add "70 Meta/Templates/"
git commit -m "feat: add 10 foundation templates with consistent frontmatter"
```

---

## Phase E — Operator Dashboard

### Task 17: Create the Home dashboard

**Files:** Create `70 Meta/Dashboards/Home.md`

- [ ] **Step 1: Write `70 Meta/Dashboards/Home.md` with all 8 blocks**

````markdown
---
type: dashboard
tags: [dashboard, home]
---

# Operator Dashboard

> **Today** — `=dateformat(date(today), "EEEE, MMMM d, yyyy")`

## Today's Focus

```dataviewjs
const today = window.moment().format("YYYY-MM-DD");
const page = dv.page(`10 Daily/Daily/${today}`);
if (page) {
    dv.paragraph(`**Focus:** ${page.focus || "(not set)"}`);
    dv.paragraph(`[Open today's note →](${page.file.path})`);
} else {
    dv.paragraph(`*No daily note yet for today.* Press \`Cmd+Shift+D\` to create one.`);
}
```

## Inbox

```dataviewjs
const items = dv.pages('"00 Inbox"').where(p => p.file.name !== "Home");
dv.paragraph(`**${items.length}** item${items.length === 1 ? "" : "s"} waiting`);
if (items.length > 0) {
    dv.list(items.sort(p => -p.file.ctime).limit(10).file.link);
}
```

## Open Loops (next 7 days)

```dataview
TASK
FROM ""
WHERE !completed AND due AND due <= date(today) + dur(7 days)
SORT due ASC
```

## Decisions Due for Review

```dataview
LIST "review on " + review_date
FROM "20 Compass/Decisions"
WHERE status = "open" AND review_date AND review_date <= date(today)
SORT review_date ASC
```

## Venture Pulse

```dataviewjs
const ventures = ["Finanshels", "Biggdate", "StartupOS", "ZeroHuman", "MealVerse", "Soulmap"];
const today = dv.date("today");
const rows = ventures.map(v => {
    const notes = dv.pages(`"30 Ventures/${v}"`);
    if (!notes.length) return [v, "—", "—", "no notes yet"];
    const lastUpdate = notes.file.mtime.values.reduce((a, b) => a > b ? a : b);
    const openTasks = notes.file.tasks.where(t => !t.completed).length;
    const daysSince = Math.floor((today - lastUpdate).as("days"));
    const stale = daysSince > 7 && openTasks > 0 ? " ⚠ stale" : "";
    return [
        `[[30 Ventures/${v}/README|${v}]]`,
        openTasks,
        `${daysSince}d ago`,
        stale || "ok"
    ];
});
dv.table(["Venture", "Open", "Last update", "Status"], rows);
```

## Content Pipeline

```dataview
TABLE status, format, audience
FROM "60 Outputs/Content"
WHERE status != "published"
SORT created DESC
LIMIT 20
```

## People to Nurture

```dataviewjs
const today = dv.date("today");
const people = dv.pages('"40 Areas/Relationships"').where(p => p.type === "person");
const overdue = people.where(p => {
    const cadence = p.cadence_days || 14;
    if (!p.last_contact) return true;
    return (today - dv.date(p.last_contact)).as("days") > cadence;
});
dv.paragraph(`**${overdue.length}** overdue (vs cadence)`);
if (overdue.length > 0) {
    const rows = overdue.sort(p => p.last_contact, "asc").limit(10).map(p => [
        p.file.link,
        p.last_contact ? `${Math.floor((today - dv.date(p.last_contact)).as("days"))}d ago` : "never",
        p.cadence_days || 14
    ]);
    dv.table(["Person", "Last contact", "Cadence"], rows);
}
```

## This Week

```dataviewjs
const week = window.moment().format("YYYY-[W]ww");
const wr = dv.page(`10 Daily/Weekly/${week}`);
if (wr) {
    dv.paragraph(`[Open this week's review →](${wr.file.path})`);
} else {
    dv.paragraph(`*No weekly review yet for ${week}.*`);
}
```
````

- [ ] **Step 2: Open Home.md in Obsidian**

Click on the file in the explorer. Switch to Reading view.

Expected: each section renders. Some queries may show "0 results" because templates aren't filled yet — that's fine. What matters is *no JS/DQL errors* and the structure renders.

If a Dataview block shows an error message instead of results, copy the error and fix the query before moving on.

- [ ] **Step 3: Commit**

```bash
git add "70 Meta/Dashboards/Home.md"
git commit -m "feat: add operator dashboard with 8 live blocks"
```

---

## Phase F — Verification

### Task 18: Write the verification script

**Files:** Create `70 Meta/Scripts/verify-foundation.sh`

- [ ] **Step 1: Create the script**

Write to `70 Meta/Scripts/verify-foundation.sh`:

```bash
#!/usr/bin/env bash
# Verify the Foundation phase Definition of Done.
# Exits 0 if all checks pass, 1 otherwise.
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

# No legacy collisions
check "no '01 Inbox'" "[[ ! -d '01 Inbox' ]]"
check "no '90 Archive'" "[[ ! -d '90 Archive' ]]"
check "no '10 Personal Brand'" "[[ ! -d '10 Personal Brand' ]]"
check "no '20 Playbooks'" "[[ ! -d '20 Playbooks' ]]"

# Filename uniqueness
DUPES=$(find . -path ./.git -prune -o -name "*.md" -print | xargs -n1 basename 2>/dev/null | sort | uniq -d)
if [[ -z "$DUPES" ]]; then
  echo "  PASS  no duplicate filenames"; PASS=$((PASS+1))
else
  echo "  FAIL  duplicate filenames: $DUPES"; FAIL=$((FAIL+1))
fi

# Plugins installed
for p in obsidian-git templater-obsidian periodic-notes dataview obsidian-tasks-plugin quickadd homepage obsidian-icon-folder; do
  check "plugin installed: $p" "[[ -d '.obsidian/plugins/$p' ]]"
done

# Templates exist
for t in "Inbox Quick Capture" "Daily Note" "Weekly Review" "Monthly Review" "Decision Log" "Venture Note" "Person Note" "Competitor Entry" "Experiment Log" "Content Idea"; do
  check "template: $t" "[[ -f '70 Meta/Templates/$t.md' ]]"
done

# Dashboard
check "Home dashboard exists" "[[ -f '70 Meta/Dashboards/Home.md' ]]"

# Per-venture READMEs
for v in Finanshels Biggdate StartupOS ZeroHuman MealVerse Soulmap; do
  check "venture README: $v" "[[ -f '30 Ventures/$v/README.md' ]]"
done

echo
echo "== $PASS passed, $FAIL failed =="
exit $((FAIL > 0 ? 1 : 0))
```

- [ ] **Step 2: Make executable**

```bash
chmod +x "70 Meta/Scripts/verify-foundation.sh"
```

- [ ] **Step 3: Commit**

```bash
git add "70 Meta/Scripts/verify-foundation.sh"
git commit -m "feat: add foundation verification script"
```

---

### Task 19: Run verification and remediate

- [ ] **Step 1: Run the script**

```bash
bash "70 Meta/Scripts/verify-foundation.sh"
```
Expected: every check prints `PASS`. If any `FAIL`, fix it and re-run.

- [ ] **Step 2: Manual checks not covered by the script**

Open Obsidian and verify:

- [ ] On launch, Home.md opens automatically (Homepage works).
- [ ] Press `Cmd+Shift+I` → inbox capture prompt appears.
- [ ] Press `Cmd+Shift+D` → today's daily note opens (or creates), template applied with frontmatter.
- [ ] Press `Cmd+Shift+L` → decision log creation prompt.
- [ ] Press `Cmd+Shift+V` → venture picker appears.
- [ ] Press `Cmd+Shift+C` → content idea creation.
- [ ] Press `Cmd+Shift+H` → jumps to Home.md.
- [ ] Make a trivial edit to any note, wait 10 minutes, run `git log --oneline -1` → expect a new auto-commit.
- [ ] Folder icons visible in the file explorer (Iconize).

If any item fails, return to the relevant Phase C/D/E task and fix before proceeding.

---

### Task 20: (Optional) Set up GitHub remote

- [ ] **Step 1: Create the private GitHub repo**

In a browser, create a new private repo named `meetpatel-brain` on GitHub. Do NOT initialize with README/license — the local repo already has history.

- [ ] **Step 2: Add remote and push**

```bash
git remote add origin git@github.com:<your-github-username>/meetpatel-brain.git
git push -u origin main
git push --tags
```

- [ ] **Step 3: Toggle Obsidian Git auto-push ON**

Settings → Obsidian Git → toggle **Push** ON. Set "Auto push interval" to `60` minutes (less aggressive than commit interval).

- [ ] **Step 4: Verify**

```bash
git remote -v
git ls-remote origin --heads
```
Expected: origin URL printed, and `refs/heads/main` listed.

---

### Task 21: Tag the foundation milestone

- [ ] **Step 1: Tag and push**

```bash
git tag foundation-shipped-2026-05-15
git push origin foundation-shipped-2026-05-15  # only if remote configured
git log --oneline | head -10
```

This is the entry point for Subsystem 2 (Capture). Future plans reference this tag.

---

## Done

When all 21 tasks pass:
- Vault is on the 8-zone Founder OS structure.
- 9 plugins installed and configured.
- 10 templates ship consistent frontmatter.
- Home dashboard renders 8 live blocks.
- Every change in Git, with named tags for rollback and milestones.
- The 7-day smoke test (per Section 10 of the spec) begins now.

Report back any of:
- Verification script failures that couldn't be remediated.
- Plugin features that didn't behave as the spec described (Obsidian versions move).
- Manual triage decisions made during Tasks 6 & 7 worth recording.

After the 7-day smoke test, return for Subsystem 2 brainstorming (Capture pipeline).
