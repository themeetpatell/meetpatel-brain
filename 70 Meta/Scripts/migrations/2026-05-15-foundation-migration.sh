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
