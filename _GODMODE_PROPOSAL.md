---
type: proposal
tags: [godmode, audit, architecture, system-upgrade]
status: awaiting-approval
created: 2026-05-17
owner: Meet Patel
---

# Godmode Proposal — Vault Upgrade Plan

> Audit of the current vault, gap analysis, and a 3-phase plan to evolve `My brain` into a supernatural founder OS — knowledge-rich, AI-native, and execution-ready.

---

## 1. Current State (audit)

**Scale.** 3,389 markdown files, ~40MB content, 1,695 imported from Notion on 2026-05-15.

**Shell — strong.** PARA-like architecture with numbered prefixes (00 Inbox → 99 Archive), Obsidian Dataview dashboards live, templates exist, `.claude/` worktree present, capture scripts in `70 Meta/Scripts`.

**Identity & personal OS — rich.** `20 Compass` has 24 dossier files + 18 identity files (Founder Profile, Writing Voice, Operating System, 90-Day Plan, Content Pillars, Strategic Themes, Companies, Public Proof, Relationship Map, Open Loops).

**Ventures — placeholders over legacy.** Each venture has a 1-paragraph snapshot pointing to deep legacy folders:

| Venture | Active notes | Legacy notes | State |
|---|---|---|---|
| StartupOS | 0 | 805 | massive legacy, no working layer |
| QKard | 0 | 282 | legacy only |
| ZeroHuman | 0 | 99 | legacy only |
| MealVerse | 0 | 41 | legacy only |
| Biggdate | 0 | 22 | legacy only |
| Biggmate | 0 | 14 | legacy only |
| Finanshels | 0 | 5 | thin (despite being revenue venture) |
| Soulmap | 0 | 4 | concept-stage |

**Knowledge Atlas — empty.** `50 Atlas` is the knowledge ingestion zone and it's nearly hollow:

| Zone | Files | Should hold |
|---|---|---|
| Competitive | 0 | competitor dossiers per venture |
| Playbooks | 0 | reusable plays (GTM, hiring, fundraise, ops) |
| Resources | 49 (creative writing books from old Notion) | founder books, frameworks, market reports |
| Experiments | 1 | hypothesis/test logs |
| Signals | 1 | weekly market/trend captures |

**Daily cadence — not yet activated.** Daily/Weekly/Monthly folders all = 0 files. Templates exist, the dashboard is wired, but no notes have been created.

**Life OS — half-built.** Brand✓ (15), Relationships✓ (22), Self✓ (5). **Health=0. Money=0.**

**AI-native layer — missing.** No agent context files (`CLAUDE.md` per venture), no prompt library, no skill manifests inside the vault, no semantic anchors for retrieval. All AI context lives in `.claude/skills/` outside the vault.

---

## 2. Gap Diagnosis

The vault has world-class **bones** but very little **muscle**. Three diagnoses:

**A. Legacy drag.** 1,695 raw Notion exports sit untouched in `legacy/` folders. They are noise to search and to humans, but they contain real IP. They need to be *distilled* into ~150 working notes — not migrated as-is.

**B. Knowledge starvation.** A founder operating at your scope (8 ventures, UAE/GCC GTM, AI-native thesis, personal brand) needs a *living atlas* of frameworks, books, competitors, signals, and plays. Today there's almost none of that captured.

**C. No AI surface.** Claude/Cursor/agents have no way to *read* your vault as context. There are no per-venture context files, no prompt library, no MOCs that act as agent instructions, no "ask Claude" blocks embedded in dashboards. The vault is for humans only.

---

## 3. Proposed Architecture (3 phases, 90 days)

### Phase 1 — Foundation (weeks 1–3): "Make it usable"

**Goal:** Activate the system so daily ops, AI agents, and knowledge ingestion all have a place to land.

1. **Build MOC backbone.** One MOC (Map of Content) per top zone — Ventures, Atlas, Life OS, Brand — linking everything that exists. MOCs become the navigation layer and the agent-readable index.
2. **Create `_AI/` operating folder.** This is the new AI-native layer (see Section 4 for full spec).
3. **Per-venture `CLAUDE.md` context files** in each `30 Ventures/<X>/` — so any agent that opens a venture folder gets full context (thesis, ICP, GTM, current state, open questions, voice).
4. **Activate Daily/Weekly cadence.** Bootstrap today's daily note, run for 14 days to prove the loop.
5. **Distill 10 legacy mega-notes** into the active `Notes/` layer per venture. The 805 StartupOS files probably collapse to ~25 working notes.
6. **Plug Health + Money OS** — even sparse stubs better than missing zones.

**Output:** Vault is navigable, agents have context, daily ops works.

---

### Phase 2 — Ingestion (weeks 4–8): "Make it powerful"

**Goal:** Pull the world's relevant knowledge into structured, queryable notes.

1. **Founder Library.** 100 founder/operator/strategy books distilled into a standard schema (Why it matters → Core frameworks → Killer quotes → How I'd apply → Related notes). Priorities: *Crossing the Chasm, Play Bigger, Hard Thing About Hard Things, Working Backwards, High Output Management, Amp It Up, Founders at Work, Zero to One, The Mom Test, Lean B2B, Lean Analytics, The Alchemy of Growth, Reforge essays, First Round Review canon, YC Startup School library*.
2. **Framework Atlas.** 50 strategic frameworks (Jobs-to-be-Done, ICE/RICE, AARRR, MEDDIC, Challenger Sale, Lenny Rachitsky's growth loops, Wardley Maps, Cynefin, 4DX, EOS V/TO, BCG matrix, Porter, Blue Ocean, Working Backwards, North Star Framework, Hooked, Octalysis, Pirate Metrics, etc.) — each as a one-pager with template and trigger.
3. **UAE/GCC Playbook.** 30 region-specific plays (DET/Dubai Free Zones, NRI distribution, WhatsApp-first SMB sales, Ramadan/EID cycles, GCC investor map, VARA, mainland vs free zone, PRO services, Khaleeji buyer psychology, Indian-diaspora SMEs).
4. **Competitive Atlas.** Per venture, 5–10 competitor dossiers (positioning, pricing, growth signals, ICP overlap, our moat).
5. **Market Signals pipeline.** Scheduled task (using `mcp__scheduled-tasks`) that runs weekly: pulls top AI/dating/SME/UAE news, summarises, drops into `50 Atlas/Signals/`.
6. **AI Agent Prompt Library.** ~40 reusable prompts (deal qualification, content draft, investor memo, founder reply, competitive scan, hiring scorecard, OKR setter, decision frame, premortem, etc.).
7. **Personal Life OS.** Health (sleep, energy, body, mind), Money (net worth, cash, runway, allocations, tax) — pulled into living dashboards.
8. **People CRM enrichment.** Top 50 relationships → full Person Notes with cadence, last contact, why they matter, how to help them.

**Output:** Vault becomes a *thinking partner*. You can ask "what would Hamilton Helmer say about Biggdate's moat?" or "give me the UAE SMB GTM play for a $99/mo accounting product" and get a real answer because the knowledge is there.

---

### Phase 3 — Superpowers (weeks 9–12+): "Make it supernatural"

**Goal:** Vault stops being a place you read; it becomes a place that *thinks with you*.

1. **AI-native query layer.** Every MOC embeds an "Ask Claude" prompt block — open the MOC, hit hotkey, get a synthesized answer from across the vault.
2. **Auto-research agents.** Scheduled tasks (weekly/daily) that:
   - Scan competitors for any product/pricing/funding/leadership change
   - Pull top AI-builder essays and add 1-paragraph TL;DRs to `50 Atlas/Signals/`
   - Watch UAE regulatory feeds (VARA, MOEC, DIFC) for changes
   - Generate a Monday morning brief across all ventures
3. **Personal Brand Engine.** Content pipeline (Pillars → Idea → Draft → Polish → Schedule) feeds LinkedIn / X / newsletter. Voice guardrails from your `Writing Voice` file.
4. **Decision Architecture.** Decision logs auto-feed quarterly reviews; each open decision gets a forced "review by" date; Bayesian update column when reality lands.
5. **Investor-Ready Dossiers.** Per venture: an auto-assembled one-pager pulling Snapshot + Thesis + Market + Traction + Ask. Always shippable.
6. **Memory Consolidation skill.** Monthly pass that merges duplicate notes, kills dead links, archives stale stuff, and surfaces patterns (your `anthropic-skills:consolidate-memory` skill is already installed).
7. **Cross-venture pattern detection.** Quarterly agent run that compares ventures and surfaces shared lessons, overlapping ICP, reusable assets.
8. **Founder God Dashboard.** Single Obsidian page: today's focus, all 8 ventures' last update + open loops, this week's content, decision review queue, life OS pulse (health, money, family), next 3 actions.

**Output:** You think faster. You decide better. You compound publicly.

---

## 4. The `_AI/` Folder Spec (new addition)

This becomes the AI-native layer sitting alongside `70 Meta/`:

```
_AI/
├── 00 README.md                  # how the AI layer works
├── Agents/
│   ├── chief-of-staff.md         # daily ops agent prompt
│   ├── content-engine.md         # writes in Meet's voice
│   ├── competitive-scout.md      # weekly competitor scan
│   ├── investor-translator.md    # converts updates → investor-ready
│   ├── decision-frame.md         # structured decision support
│   ├── hiring-scorecard.md
│   └── premortem.md
├── Prompts/
│   ├── _index.md                 # taxonomy by job-to-be-done
│   ├── content/                  # 12 content prompts
│   ├── strategy/                 # 8 strategy prompts
│   ├── ops/                      # 8 ops prompts
│   ├── sales/                    # 6 sales prompts
│   └── personal/                 # 6 personal/life prompts
├── Contexts/
│   ├── meet.md                   # who I am, how I think, what I'm building
│   ├── voice.md                  # voice rules + examples + anti-patterns
│   ├── ventures-overview.md      # 8 ventures, 1 paragraph each
│   └── current-state.md          # auto-updated weekly: live priorities
├── Workflows/
│   ├── weekly-review.md          # multi-step claude workflow
│   ├── monthly-strategy.md
│   ├── new-venture-brief.md
│   └── investor-update.md
└── Skills/
    └── _registry.md              # links to /var/.../claude-hostloop-plugins/skills (your installed skills)
```

**Per venture**, additionally:

```
30 Ventures/<Venture>/
├── CLAUDE.md                     # agent context (read first)
├── <Venture>.md                  # human-facing snapshot
├── Notes/
│   ├── _MOC.md                   # human + agent navigation
│   ├── Thesis.md
│   ├── ICP.md
│   ├── GTM.md
│   ├── Competitive.md
│   ├── Open Questions.md
│   └── Decisions/
└── legacy/                       # kept, but distilled-from
```

---

## 5. Knowledge Ingestion — what gets pulled in

A non-exhaustive list of what Phase 2 ingests, scoped to your world:

**Strategy & venture building** — Helmer's *7 Powers*, Christensen's *Innovator's Dilemma*, Kim & Mauborgne's *Blue Ocean*, Geoffrey Moore's chasm + tornado, Roger Martin on strategy, Hamilton on monopoly, Reid Hoffman's blitzscaling, Frank Slootman's *Amp It Up*, Bill Walsh's *Score Takes Care of Itself*, Andy Grove's HOM, Ben Horowitz, Keith Rabois lectures, First Round Review.

**Product & growth** — *Hooked*, *The Mom Test*, *Lean Analytics*, Sean Ellis on PMF, Reforge essays, Lenny Rachitsky canon, Brian Balfour growth loops, Elena Verna PLG, Casey Winters, ARR/CAC/LTV models.

**AI-native building** — Anthropic + OpenAI design guides, prompt engineering canon, agent design patterns (ReAct, reflection, tool use), AI-native company patterns (Sierra, Decagon, Cursor case studies), Andrej Karpathy on agentic systems, Latent Space pod canon.

**UAE/GCC intelligence** — MAGNiTT reports, Wamda, Forbes ME, MOEC + DET updates, Dubai SME profile, VARA + DIFC + ADGM frameworks, NRI buyer behavior, Khaleeji business culture, Ramadan/EID commerce cycles.

**Dating/relationships (Biggdate + Soulmap)** — Helen Fisher, Esther Perel, Sue Johnson EFT, attachment theory, compatibility research, Hinge/Bumble/Match Group filings + investor decks, OkCupid data essays.

**Personal performance** — Huberman protocols, Tim Ferriss interviews, Naval canon, Morgan Housel on money, Ramit Sethi on systems, Atomic Habits, Deep Work, Range, *Working Backwards* on writing.

**Operating systems** — EOS (V/TO, Rocks, L10), Scaling Up (Verne Harnish), 4DX, OKRs (Doerr + WorkBoard patterns), Amp It Up cadence.

Each entry distilled into a one-page note with: **Why it matters to Meet → Core frameworks → 3 killer quotes → How to apply to <venture> → Related notes**.

---

## 6. 90-Day Rollout (calendar view)

| Week | Theme | Deliverable |
|---|---|---|
| 1 | Foundation | `_AI/` folder, MOC backbone, daily cadence live, 1 `CLAUDE.md` per venture |
| 2 | Foundation | Health + Money OS stubs, distill StartupOS legacy → 25 working notes |
| 3 | Foundation | Distill Biggdate + Finanshels legacy, Decision Log starter, Prompt Library v1 (20 prompts) |
| 4 | Ingestion | Founder Library Wave 1 (20 books) |
| 5 | Ingestion | Framework Atlas v1 (25 frameworks) |
| 6 | Ingestion | UAE/GCC Playbook (30 plays) |
| 7 | Ingestion | Competitive Atlas (all 8 ventures) |
| 8 | Ingestion | Founder Library Wave 2 (40 more books), People CRM enrichment top 50 |
| 9 | Superpowers | Auto-research agents (3 scheduled tasks live) |
| 10 | Superpowers | Personal Brand Engine wired (Pillars → Draft → Schedule) |
| 11 | Superpowers | Investor-Ready Dossier auto-assembly per venture |
| 12 | Superpowers | Founder God Dashboard + Memory Consolidation monthly pass |

---

## 7. What I built today (sample artifacts to show direction)

I've dropped two sample files to make this concrete:

1. **`_AI/Contexts/meet.md`** — the kind of context file Claude/Cursor read first, written in a format optimised for agents.
2. **`70 Meta/MOCs/Ventures MOC.md`** — the kind of MOC that becomes the navigation + agent-readable index for all 8 ventures.

Open them, look at the format, and tell me if this is the direction.

---

## 8. What I need from you to proceed

Three decisions before I start Phase 1 in earnest:

1. **Sample artifact approval** — do the two sample files match your taste? (If not: what should change — tone, depth, structure, frontmatter?)
2. **Sequencing override** — the rollout above prioritizes Ventures MOC + AI layer first. Want me to flip a phase? E.g., do Personal Life OS before venture deep dives?
3. **Cadence** — do you want this built in long sprints (I produce 20+ files per work session and you review), or short sprints (5 files per session, faster feedback loop)?

When you say go, I start with **Phase 1 / Week 1**: building the full `_AI/` folder, 8 `CLAUDE.md` venture context files, the MOC backbone, and bootstrapping today's daily note. That's a ~40-file output and roughly one focused work session.

---

## 9. Stretch ideas (post-90-day)

- **Voice clone API** — fine-tune a Claude prompt against your published writing so the content engine drafts indistinguishably from you
- **Live investor data room** — vault auto-syncs investor-ready dossiers to a private web page (Vercel)
- **Knowledge graph visualization** — Obsidian Graph view becomes a real navigation surface
- **Multi-venture financial model** — XLSX that pulls cash/runway/spend across the portfolio
- **Public second brain** — selective subset of the vault published as a Quartz/Obsidian Publish site (founder-brand multiplier)
- **Daily AI standup** — scheduled 6am brief: yesterday's wins/losses, today's 3 priorities, blockers, this week's decisions due
- **MCP server for your vault** — so Claude can read it natively from anywhere, not just inside Cowork

---

*Awaiting your approval to proceed.*
