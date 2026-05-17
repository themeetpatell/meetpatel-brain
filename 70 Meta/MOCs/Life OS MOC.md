---
type: moc
tags: [moc, life-os, areas, personal, navigation]
status: living
updated: 2026-05-17
owner: Meet Patel
---

# Life OS — Map of Content

> Everything outside of ventures and knowledge: health, money, relationships, brand, self. The personal operating system. This MOC is the navigation surface for `40 Areas/`.

## Why a Life OS matters

Founders who lose the personal OS lose the ventures eventually. The personal stack is the *substrate* under all the operating work. Treat it with the same rigor.

## Current zone status

| Zone | Status | Files | Priority |
|---|---|---|---|
| [[#Brand]] | Half-built | 15 | active |
| [[#Health]] | **Empty** | 0 | seed Phase 1 |
| [[#Money]] | **Empty** | 0 | seed Phase 1 |
| [[#Relationships]] | Half-built | 22 | active |
| [[#Self]] | Half-built | 5 | active |

## Zone breakdowns

### Brand

`40 Areas/Brand/`

Personal brand strategy, content pillars, social presence, founder-brand assets.

Notable files:
- Target Audience, Planning, Content Pillars, Social Media Content Planning System (in legacy notion)
- Cross-link to [[Brand & Content MOC]]

Cadence: monthly review of voice + pillars; weekly review of posting cadence.

### Health

`40 Areas/Health/` — **needs seeding (Phase 1)**

Plan:
- Health/Energy log (sleep, training, nutrition, energy levels)
- Health/Protocols (training plan, supplements, sleep hygiene)
- Health/Medical (annual labs, doctor visits, prescriptions)
- Health/Mental (meditation, stress monitoring, therapy if relevant)

Cadence: monthly energy audit (use `_AI/Prompts/personal/energy-audit.md`).

### Money

`40 Areas/Money/` — **needs seeding (Phase 1)**

Plan:
- Money/Personal (net worth, cash, runway, savings rate, allocations)
- Money/Ventures (per-venture cash, burn, runway, equity, investor obligations)
- Money/Tax (UAE corporate tax, India residency status, advisor notes)
- Money/Allocations (investments, real estate, crypto, family commitments)
- Money/Decisions (major financial decisions logged with rationale)

Cadence: monthly close + quarterly portfolio review.

### Relationships

`40 Areas/Relationships/`

Family OS, People CRM, key relationships with cadence.

Notable existing files:
- `27 People I Want Closer.md`
- `Relationships/FamilyOS/` (FamilyOS plan, strategy, features)
- `Relationships/People/` (12+ person notes already imported)

Cadence: weekly relationship-nudge run (use `_AI/Prompts/personal/relationship-nudge.md`).

### Self

`40 Areas/Self/`

Career, identity-adjacent, self-development that doesn't fit elsewhere.

Notable files:
- `Self/CareerOS/` (career frame from Notion import)

Cross-link to `20 Compass/Identity/` for the deeper identity layer.

## Maintenance cadence (Life OS)

- **Daily:** daily note touches health (energy), relationships (calls/messages), self (mood)
- **Weekly:** weekly review touches all 5 zones (energy read in review template)
- **Monthly:** energy audit, money close, relationship nudge sweep, brand pillar check
- **Quarterly:** zone-by-zone audit — is the zone serving its purpose?

## Standing dashboard queries (when populated)

```dataview
TABLE WITHOUT ID 
  file.link as Note, 
  tags, 
  file.mtime as Updated
FROM "40 Areas"
WHERE !contains(file.path, "legacy")
SORT file.mtime DESC
LIMIT 30
```

## Related MOCs

- [[Ventures MOC]]
- [[Knowledge Atlas MOC]]
- [[Brand & Content MOC]]
- [[People & Relationships MOC]]

---

*The Life OS is what makes the venture OS sustainable. Don't skip it.*
