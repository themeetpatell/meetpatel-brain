# Vault Foundation — Design Spec

**Date:** 2026-05-15
**Owner:** Meet Patel
**Vault:** `/Users/themeetpatel/My brain`
**Status:** Approved for implementation
**Part of:** "Self-growing brain" program — Subsystem 1 of 5
  1. **Foundation** ← this spec
  2. Capture pipeline (next)
  3. Self-growing AI layer
  4. Operator dashboards (extended)
  5. Output engines

---

## 1. Goal

Transform the existing 306-note vault from a half-built, structurally-collided personal store into a **clean, queryable, version-controlled, dashboard-driven operator OS** that the later AI layer can read and write safely.

A successful Foundation means:
- One coherent folder structure with no collisions.
- Every note created from a template with consistent frontmatter.
- One dashboard surfaces the operator's state on open.
- Every change is a Git commit (rollback + audit trail).
- The vault is ready to be a target for autonomous agents in Subsystem 3.

## 2. Non-goals

- No AI/LLM integrations in this phase (those belong to Subsystem 3).
- No mobile/iOS workflow (Foundation assumes Mac desktop only; mobile addressed in Subsystem 2).
- No content/output generation (Subsystem 5).
- No external integrations (Calendar, Notion, etc.) — handled by Capture (Subsystem 2).

## 3. Current state (baseline)

- 306 markdown notes.
- ~30 top-level folders with **4 collisions**: `00 Inbox`/`01 Inbox`, `90 Archive`/`99 Archive`, `10 Personal Brand`/`10 Projects`, `20 Areas`/`20 Playbooks`.
- Vanilla Obsidian — no community plugins installed.
- 4 templates exist; only 1 dashboard.
- Daily Notes folder empty; Weekly Reviews has 1 entry.
- No version control. No sync.
- Strong skeleton: Founder Dossier, 30 Core Notes, multi-venture structure (Finanshels, Biggdate, StartupOS, ZeroHuman, MealVerse, Soulmap).

## 4. Design decisions (locked)

| Decision | Choice | Rationale |
|---|---|---|
| Architecture | Founder OS (8 zones) | Matches Meet's existing "Core Notes" mental model; clean targets for AI agents per venture/area. |
| Restructure scope | Full clean reboot | User explicitly opted in; surgical fix would leave permanent structural debt. |
| Sync | Git only (with optional GitHub remote) | Atomic, reviewable changes; required for Subsystem 3's safety. |
| Daily entry point | Operator dashboard | Action-first matches operator role over journaler role. |
| Plugin scope | All 9 recommended plugins | Each earns its place; gaps would block later subsystems. |
| Mobile | Out of scope for Foundation | Will be addressed in Capture (Subsystem 2). |

## 5. Architecture — the 8-zone Founder OS

```
00 Inbox/                  Single capture point. Triaged daily.
10 Daily/
   Daily/                  Daily notes (auto-created).
   Weekly/                 Weekly reviews.
   Monthly/                Monthly reviews (new in this design).
   Journal/                Long-form journaling.
20 Compass/                Identity + decision system.
   Identity/               About, story, voice, themes.
   Principles/             Decision principles, frameworks.
   Decisions/              Decision log.
   Vision/                 Life vision, ideal week, 90-day plans.
   Dossier/                Founder dossier (working doc).
30 Ventures/               One folder per company.
   Finanshels/  Biggdate/  StartupOS/  ZeroHuman/  MealVerse/  Soulmap/
     (each: README.md, Strategy.md, Decisions.md, Experiments.md, Notes/)
40 Areas/                  Life domains (no end state).
   Self/  Brand/  Money/  Relationships/  Health/
50 Atlas/                  Reference material.
   Competitive/  Signals/  Playbooks/  Experiments/  Resources/
60 Outputs/                Things shipped to the world.
   Content/                Drafts, ideas, published.
   Dossier/                Polished dossier exports.
70 Meta/                   Vault infrastructure.
   Templates/  Scripts/  Dashboards/  Bases/  MOCs/
99 Archive/                Single archive.
```

### Migration map (every current folder → destination)

| Current | New |
|---|---|
| `00 Inbox/`, `01 Inbox/` | `00 Inbox/` (merge + dedupe) |
| `01 Daily Notes/` | `10 Daily/Daily/` |
| `02 Weekly Reviews/` | `10 Daily/Weekly/` |
| `02 Journal/` | `10 Daily/Journal/` |
| `28 First 30 Core Notes/` | Split: identity files → `20 Compass/Identity/`; principles → `20 Compass/Principles/`; vision → `20 Compass/Vision/`; venture snapshots → `30 Ventures/<name>/README.md`. **Original folder snapshotted to `99 Archive/2026-05-15-pre-migration-snapshot/` before split.** |
| `30 Decisions/` | `20 Compass/Decisions/` |
| `51 About Me/` | `20 Compass/Identity/` |
| `17 Founder Dossier/` (with sub-structure) | `20 Compass/Dossier/` (preserve sub-structure) |
| `10 Projects/` | Split per venture into `30 Ventures/<name>/` (manual triage required for ambiguous notes) |
| `11 Biggdate/` | `30 Ventures/Biggdate/` |
| `10 Personal Brand/`, `14 Content Ideas/` | `60 Outputs/Content/` |
| `12 Competitive Intelligence/` | `50 Atlas/Competitive/` |
| `13 Market Signals/` | `50 Atlas/Signals/` |
| `15 Growth Experiments/` | `50 Atlas/Experiments/` |
| `20 Areas/` (with sub-structure) | `40 Areas/` (preserve sub-structure) |
| `20 Playbooks/` | `50 Atlas/Playbooks/` |
| `30 Resources/` | `50 Atlas/Resources/` |
| `40 Templates/` | `70 Meta/Templates/` |
| `90 Dashboards/` | `70 Meta/Dashboards/` |
| `00 Home/` | Merge into `70 Meta/Dashboards/` (Home.md → `70 Meta/Dashboards/Home.md`; Today.md preserved) |
| `90 Archive/`, `99 Archive/` | `99 Archive/` (merge) |
| `Untitled.base` | `70 Meta/Bases/` (rename to a descriptive name) |

### Migration mechanics

1. `git init` + initial commit of current state — rollback point.
2. Pre-flight: `find . -name "*.md" | xargs -n1 basename | sort | uniq -d` to detect any duplicate filenames; rename losers to `<name> (dup).md` so wikilinks remain unique.
3. **Snapshot `28 First 30 Core Notes/` to `99 Archive/2026-05-15-pre-migration-snapshot/`** before any destructive split.
4. Single bash migration script using `git mv` so file history follows each note.
5. Manual triage pass: review the ~15 notes from `10 Projects/` and assign each to a venture. Script presents one at a time; human chooses.
6. Wikilinks (`[[Note Name]]`) survive automatically because Obsidian uses filename-based links, not paths — confirmed safe by the dedupe step above.
7. Final commit: `feat: migrate to Founder OS structure`.

### Risks & mitigations

| Risk | Mitigation |
|---|---|
| Filename collision after move breaks wikilinks | Pre-flight uniqueness check; rename before move. |
| `28 First 30 Core Notes/` split is destructive | Pre-snapshot to archive; `git mv` keeps history. |
| User regrets restructure | `git reset --hard <pre-migration-commit>` returns to baseline in one command. |
| Plugin config drift across machines | Version `.obsidian/plugins/` and `.obsidian/snippets/` in Git. |
| Auto-commit floods Git history | 10-min interval is the floor; can be raised. |

## 6. Plugin install — order, settings, dependencies

Install order matters because plugins depend on each other.

| # | Plugin | Settings (load-bearing) |
|---|---|---|
| 1 | Obsidian Git | Auto-backup interval: **10 min** · Auto-pull on start: **ON** · Commit msg: `vault: {{date}} {{hostname}}` |
| 2 | Templater | Template folder: `70 Meta/Templates` · Trigger Templater on file creation: **ON** · Folder template mappings (Section 7) |
| 3 | Periodic Notes | Daily → `10 Daily/Daily/`, format `YYYY-MM-DD` · Weekly → `10 Daily/Weekly/`, format `YYYY-[W]ww` · Monthly → `10 Daily/Monthly/`, format `YYYY-MM` |
| 4 | Dataview | Enable JS queries: **ON** · Inline queries: **ON** |
| 5 | Tasks | Global query filter: `path does not include 99 Archive` |
| 6 | QuickAdd | 6 macros (Section 7) |
| 7 | Homepage | Open: `70 Meta/Dashboards/Home.md` · On startup + new tab |
| 8 | Iconize | Pack: Lucide. Icons assigned to the 8 top-level zones. |
| 9 | Bases (core) | Enable in Core Plugins. |

## 7. Templates, frontmatter schema, hotkeys

### Folder → template auto-assignment (Templater)

| Folder | Auto-template |
|---|---|
| `00 Inbox/` | Inbox Quick Capture |
| `10 Daily/Daily/` | Daily Note |
| `10 Daily/Weekly/` | Weekly Review |
| `10 Daily/Monthly/` | Monthly Review |
| `20 Compass/Decisions/` | Decision Log |
| `30 Ventures/*/Notes/` | Venture Note |
| `40 Areas/Relationships/` | Person Note |
| `50 Atlas/Competitive/` | Competitor Entry |
| `50 Atlas/Experiments/` | Experiment Log |
| `60 Outputs/Content/` | Content Idea |

### The 10 templates (in `70 Meta/Templates/`)

1. **Inbox Quick Capture** — title prompt, single tag, blank body. ~5 lines.
2. **Daily Note** — date header, top-3 priorities, calendar pull (manual paste OK at this stage), today's open loops (Dataview), evening reflection, links to active venture.
3. **Weekly Review** — wins, lessons, decisions made, open loops carried over, next week's focus, per-venture status block.
4. **Monthly Review** — themes, key decisions, content shipped, relationships nurtured, north-star metrics per venture.
5. **Decision Log** — context, options considered, decision, reasoning, expected outcome, review date, linked ventures.
6. **Venture Note** — venture link, type (strategy/exec/learning), summary, action, links.
7. **Person Note** — name, role, last contact, relationship goal, recent context, follow-up, related ventures.
8. **Competitor Entry** — name, market, ICP, pricing, strengths, weaknesses, signals, last reviewed.
9. **Experiment Log** — hypothesis, ICE score, setup, result, learning, next step.
10. **Content Idea** — hook, audience, angle, format, status, distribution.

### Frontmatter schema (load-bearing — Subsystem 3 reads this)

Every template emits consistent frontmatter so Dataview can query across the vault.

Common keys (all notes):
```yaml
type: <inbox|daily|weekly|monthly|decision|venture|person|competitor|experiment|content>
created: YYYY-MM-DD
tags: []
```

Conditional keys by type:
- `decision`: `status` (open|made|reviewed), `review_date`, `ventures` (list), `outcome` (free text after review)
- `venture` notes: `venture` (single), `subtype` (strategy|exec|learning)
- `person`: `last_contact` (date), `follow_up` (bool), `cadence_days` (int)
- `competitor`: `market`, `last_reviewed` (date)
- `experiment`: `hypothesis`, `ice_score` (int), `status` (planned|running|done)
- `content`: `status` (idea|drafting|scheduled|published), `format`, `audience`

### Hotkeys (via QuickAdd)

| Shortcut | Action |
|---|---|
| `⌘⇧I` | Quick capture to Inbox |
| `⌘⇧D` | Open today's daily note |
| `⌘⇧L` | New decision log |
| `⌘⇧M` | New meeting/person note |
| `⌘⇧V` | New venture note (prompts: which venture?) |
| `⌘⇧C` | New content idea |
| `⌘⇧H` | Jump to Home dashboard |

## 8. Operator dashboard — `70 Meta/Dashboards/Home.md`

One file, eight live blocks via Dataview. Opens automatically on Obsidian launch (Homepage plugin).

```
Today — <weekday>, <date>
Focus: <pulled from today's daily note "focus" field>

▸ TOP 3 TODAY                  pulled from today's daily note
▸ INBOX — N items waiting       count of files in 00 Inbox/
▸ OPEN LOOPS — N due this week  Tasks query, sorted by due date
▸ DECISIONS DUE FOR REVIEW — N  decision notes where review_date <= today
▸ VENTURE PULSE                 per-venture row: open count, last update, last decision, ⚠ if stale > 7d
▸ CONTENT PIPELINE — N in flight content notes where status != published
▸ PEOPLE TO NURTURE — N         person notes where last_contact > cadence_days
▸ THIS WEEK                     link to current weekly review
```

Stale heuristics:
- Venture stale: `last update > 7 days ago` AND at least one open task exists.
- Person to nurture: `today - last_contact > cadence_days` (default 14 if unset).

The dashboard self-updates as notes are written — no manual maintenance. The "stale" warnings are the first pre-AI nudges; Subsystem 3 will replace them with richer suggestions.

## 9. Git setup

```bash
cd "/Users/themeetpatel/My brain"
git init
git branch -m main
```

`.gitignore` (committed at repo root):
```
.DS_Store
.obsidian/workspace*
.obsidian/cache
.obsidian/cache.json
.trash/
```

We **do** version `.obsidian/plugins/` and `.obsidian/snippets/` so plugin configs and CSS travel with the vault.

Commits:
1. `chore: snapshot pre-migration vault state` — rollback point before any change.
2. `feat: migrate to Founder OS structure` — after the migration script runs and is reviewed.
3. `feat: install plugin stack and templates` — after plugin install + template files committed.
4. `feat: add operator dashboard` — after Home.md is in place and queries verified.

Obsidian Git plugin then takes over for ongoing auto-commits every 10 min.

**Optional GitHub remote (recommended):** private repo `meetpatel-brain`. Off-site backup + history. `git remote add origin git@github.com:<user>/meetpatel-brain.git` and toggle Obsidian Git's auto-push ON.

## 10. Verification (Definition of Done)

10-point checklist run after migration:

1. `git log` shows ≥ 2 commits (snapshot + migration).
2. Top-level folders match the 8-zone canonical layout exactly. No collisions remain.
3. `find . -name "*.md" | xargs -n1 basename | sort | uniq -d` returns empty.
4. All 9 plugins enabled and configured per Section 6.
5. Open Obsidian cold → Home dashboard renders (Homepage works).
6. All 7 hotkeys fire and create notes in the right folders with the right templates.
7. Today's daily note auto-creates with the Daily Note template applied.
8. Dataview blocks on Home.md return real data — not "0 results" everywhere. Specifically: ≥ 1 open loop, ≥ 1 venture row, ≥ 1 person.
9. Make a trivial edit → wait 10 min → confirm Obsidian Git committed it.
10. (If remote configured) `git push` succeeds; the repo is visible on GitHub.

**7-day smoke test:** use the vault daily for one week, exercising each hotkey at least once. If no plugin crashes, no template misfires, and the dashboard stays useful — Foundation ships and we move to Subsystem 2 (Capture).

## 11. What Foundation explicitly enables for later subsystems

| Subsystem | What Foundation gives it |
|---|---|
| 2. Capture | Single inbox folder, QuickAdd hotkey, frontmatter schema for triage. |
| 3. AI layer | Clean folder targets per venture/area, consistent frontmatter to query, Git for safe writes + audit. |
| 4. Dashboards (extended) | Dataview installed, Home.md as the model to extend. |
| 5. Output engines | `60 Outputs/` zone exists, content frontmatter schema in place. |

## 12. Open questions for implementation phase

These are not unresolved design choices — they are details that surface during implementation and need a human-in-the-loop call:

- The ~15 notes in `10 Projects/` that need per-venture assignment (decided one at a time during migration).
- Exact Iconize icon per zone (cosmetic; pick during install).
- Whether to seed the initial Daily Note for today as part of Foundation, or wait for the first real morning use.
- Whether to create the GitHub remote during this phase or defer.
