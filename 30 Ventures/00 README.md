---
type: readme
status: living
updated: 2026-05-25
tags: [readme, system, ventures]
---

# 30 Ventures — 8 active ventures, consistent shape

> One folder per venture. Same shape. Agents can navigate any venture without retraining.

## Active ventures
Biggdate · Biggmate · Finanshels · MealVerse · QKard · Soulmap · StartupOS · ZeroHuman

See `00 Ventures Index.md` for the human-facing list, `_AI/MOCs/Ventures MOC.md` for the navigation map.

## Per-venture shape (CANONICAL — see `_Template/`)
```
<Venture>/
├── CLAUDE.md            # agent context — read first
├── README.md            # human snapshot (or <Venture>.md, being migrated)
├── Notes/
│   └── _MOC.md          # working notes index
├── Decisions/
│   └── _README.md       # decision log
└── legacy/              # pre-restructure raw (distill, don't quote)
```

## Rules
- Every venture MUST have `CLAUDE.md` and `Notes/`
- New venture? Copy `_Template/` to `<NewVenture>/`
- Never write into another venture's `legacy/` — distill into `Notes/` instead
- `_Shared/` holds cross-venture assets (portfolio thesis, shared decks)

## How agents use this folder
1. Open `30 Ventures/<name>/CLAUDE.md` first — full context
2. Read `Notes/_MOC.md` for the working set
3. Check `Decisions/` for open decisions
4. Treat `legacy/` as archive — quote sparingly
