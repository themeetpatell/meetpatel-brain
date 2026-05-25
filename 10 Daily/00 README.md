---
type: readme
status: living
updated: 2026-05-25
tags: [readme, system, cadence]
---

# 10 Daily — operating cadence

> The heartbeat of the system. Daily / Weekly / Monthly / Journal.

## Subfolders
- `Daily/` — one note per day, `YYYY-MM-DD.md`
- `Weekly/` — Friday review, `YYYY-Www.md`
- `Monthly/` — first-of-month review, `YYYY-MM.md`
- `Journal/` — long-form reflection, unstructured

## Template (Daily)
Frontmatter: `type: daily`, `date`, `focus`, `energy: 1-10`, `tags`.

Sections: Today's focus → Top 3 → Decisions made → Open decisions → Wins → Misses → Captured signals → Open loops → People to reach out to → Content from today → End-of-day reflection.

## Rules
- Write daily on working days, even if 3 lines
- Friday: run `_AI/Prompts/personal/weekly-review.md`
- Monthly: run `_AI/Workflows/monthly-strategy.md`

## How agents use this folder
- `_AI/Contexts/current-state.md` should be regenerated weekly from the last 7 daily notes
- Decision Log: pull `## Decisions made` lines across daily notes weekly
- Content engine: pull `## Content from today worth posting?` lines
