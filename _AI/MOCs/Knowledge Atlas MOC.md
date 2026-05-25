---
type: moc
tags: [moc, atlas, knowledge, navigation]
status: living
updated: 2026-05-17
owner: Meet Patel
---

# Knowledge Atlas — Map of Content

> The world's relevant knowledge, structured for retrieval and application. This MOC is the navigation surface for `50 Atlas/`. Most of it is *intentionally empty* right now — Phase 2 of the godmode rollout fills it.

## What lives here

Anything that's not me, not my ventures, not my personal life — but is *knowledge I can apply*. Books, frameworks, market intel, playbooks, competitive dossiers, signals.

## Sub-MOCs

- [[_Framework Atlas MOC]] — **LIVE** — 25 strategic frameworks distilled and made Meet-applicable (Phase 2 / Wave 1 ✓)
- [[_Founder Library MOC]] — **LIVE (Wave 2A)** — 20 founder books distilled (more to come in Wave 2B) (Phase 2 / Wave 2 ✓)
- [[UAE GCC Playbook MOC]] *(coming Phase 2 / Wave 3)* — 30 region-specific plays
- [[Competitive Atlas MOC]] *(coming Phase 2 / Wave 4)* — competitor dossiers across all ventures
- [[Market Signals MOC]] *(coming Phase 2)* — weekly captured signals
- [[Experiments Log MOC]] *(coming Phase 2)* — hypothesis + result log
- [[AI-Native Building MOC]] *(coming Phase 2)* — agent design patterns, model + tool canon
- [[Dating + Relationships Research MOC]] *(coming Phase 2)* — Esther Perel, Sue Johnson, Helen Fisher, attachment, compatibility

## Folder map

```
50 Atlas/
├── Competitive/    [Phase 2: per-venture competitor dossiers]
├── Experiments/    [Phase 2: hypothesis → test → result logs]
├── Playbooks/      [Phase 2: reusable plays — GTM, hiring, fundraise, ops]
├── Resources/
│   └── Books/      [Phase 2: founder library — replaces creative-writing books]
└── Signals/        [Phase 2: weekly market scans, auto-ingested]
```

## Capture rules

- **Books:** one note per book using the standard schema (Why it matters → Frameworks → Quotes → How to apply → Related)
- **Frameworks:** one note per framework. Includes template + trigger conditions.
- **Competitors:** one note per competitor per venture. Weekly delta entries.
- **Signals:** weekly digest (per scheduled task), individual signals only if Tier-A important
- **Experiments:** every meaningful test gets logged (hypothesis → test → result → lesson)
- **Playbooks:** distilled from real execution, not theory — only ship what's been used

## Retrieval rules

- Every note has frontmatter `tags` — at minimum [book|framework|competitor|signal|experiment|playbook]
- Use Obsidian search + Dataview queries to retrieve
- High-value notes get explicit wikilinks from this MOC

## Standing search queries (Dataview, when populated)

```dataview
TABLE WITHOUT ID 
  file.link as Note, 
  tags, 
  file.mtime as Updated
FROM "50 Atlas"
WHERE contains(tags, "framework")
SORT file.mtime DESC
LIMIT 20
```

## Ingestion pipeline (Phase 2)

- **Books:** Meet picks 20 → Claude distills → review → ship
- **Frameworks:** Top 50 from canonical list (in `_GODMODE_PROPOSAL.md` Section 5)
- **Competitors:** scout agent runs weekly per venture
- **Signals:** scheduled task pulls top 5 sources weekly, summarises, files
- **Playbooks:** captured post-hoc as Meet ships real plays — *not* prospectively

## Related MOCs

- [[Ventures MOC]]
- [[Life OS MOC]] *(coming)*
- [[Brand & Content MOC]] *(coming)*
- [[People & Relationships MOC]] *(coming)*

---

*Phase 2 turns this MOC from skeleton into the most-used surface in the vault.*
