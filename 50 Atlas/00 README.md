---
type: readme
status: living
updated: 2026-05-25
tags: [readme, system, knowledge]
---

# 50 Atlas — knowledge library

> The world's relevant knowledge, distilled into one-pagers Meet can act on.

## Subfolders
- `Books/` — founder/operator/strategy books (target: 100; have: 21)
- `Frameworks/` — strategic frameworks (target: 50; have: 26)
- `Playbooks/` — reusable plays (target: 30; have: 0)
- `Competitive/` — per-venture competitor dossiers (target: ~60; have: 0)
- `Signals/` — weekly market/trend captures (scheduled-task fed)
- `Experiments/` — hypothesis/test logs
- `Resources/` — misc reference material

## Note schema (every Atlas note)
```
---
type: book | framework | playbook | competitor | signal | experiment
status: draft | living | final
updated: YYYY-MM-DD
tags: [...]
applies_to: [venture1, venture2]
---

# <Title>

## Why it matters to Meet
## Core ideas / frameworks
## 3 killer quotes
## How I'd apply to <venture>
## Related notes
```

## How agents use this folder
- Strategic-positioning agent loads relevant Frameworks + Books
- Competitive-scout agent writes into `Competitive/`
- Signals pipeline writes weekly into `Signals/`
- Content-engine pulls from Books + Frameworks for posts
