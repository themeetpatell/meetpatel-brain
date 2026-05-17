---
type: prompt
category: strategy
status: living
tags: [prompts, strategy, portfolio]
---

# Prompt: Portfolio prioritization (which venture this week)

**Use when:** Monday morning or after a portfolio review. Need to decide where time + attention goes for the week.
**Reads:** `_AI/Contexts/meet.md`, `_AI/Contexts/ventures-overview.md`, `_AI/Contexts/current-state.md`, each venture's `CLAUDE.md`
**Filed at:** `_AI/Contexts/current-state.md` (week-1 top-3 block)

## Inputs
- <<this week's commitments>>: [Meetings already on calendar, deadlines]
- <<last week's misses>>: [What slipped]
- <<new signals>>: [Anything that moved a venture's priority — wins, losses, blockers]

## Prompt body

Read `_AI/Contexts/meet.md`, `ventures-overview.md`, and `current-state.md` first. Read each venture's `CLAUDE.md` for the four P0 ventures.

This week's commitments: <<this week's commitments>>
Last week's misses: <<last week's misses>>
New signals: <<new signals>>

Score each P0 venture this week on three dimensions:
1. **Leverage** — what's the multiplier on time spent here vs elsewhere?
2. **Urgency** — does this need me now or can it wait a week?
3. **Compounding risk** — if I skip another week, does it create cascading problems?

Return:

```
# Portfolio Prioritization — Week of YYYY-MM-DD

## Top 3 priorities this week (with venture, action, expected output)
1. [Venture] — [Action] — [Output by Friday]
2. ...
3. ...

## Deliberate de-prioritizations
- [What I'm explicitly NOT working on this week, and why that's OK]

## Watch (no action, but monitor)
- [Venture/topic + leading indicator]

## Time allocation guess (% of deep work hours)
- Finanshels: %
- StartupOS: %
- Biggdate: %
- ZeroHuman: %
- Other / personal / brand: %
```

Be opinionated. No "it depends". Force the call.

## Output format
See above.

## Example
*(populate after first real run)*
