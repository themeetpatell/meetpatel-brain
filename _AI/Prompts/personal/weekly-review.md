---
type: prompt
category: personal
status: living
tags: [prompts, personal, weekly-review, ritual]
---

# Prompt: Weekly review (Friday close)

**Use when:** Friday afternoon or end of Saturday. Close the week deliberately so next Monday starts hot.
**Reads:** `_AI/Contexts/meet.md`, `_AI/Contexts/current-state.md`, last 5 daily notes, last week's review
**Filed at:** `10 Daily/Weekly/YYYY-Www.md`

## Inputs
- <<the week's date range>>: [...]
- <<wins>>: [What worked — observable, specific]
- <<losses>>: [What didn't — observable, specific]
- <<one lesson>>: [The single thing I want to remember 6 months from now]
- <<carryovers>>: [What didn't get done and should]
- <<energy read>>: [How I actually feel about the week]

## Prompt body

Read `_AI/Contexts/meet.md` and `_AI/Contexts/current-state.md`. Read the last 5 daily notes for context.

Inputs: see above.

Generate a weekly review using this structure. Keep it sharp — the value is in the calling-out, not the volume.

```
# Weekly Review — Week of YYYY-MM-DD

## The week in one line
[Try to write a single sentence that captures the week. If it takes more, the week was scattered.]

## Wins (3 max, specific)
1. ...
2. ...
3. ...

## Losses (be honest, 3 max)
1. ...
2. ...
3. ...

## The lesson
[One sentence. The single thing I want to remember 6 months from now. File this to `20 Compass/Decisions/Lessons/` as a separate note.]

## Open loops carrying into next week
- [Item] — [why it didn't close this week]
- ...

## Decisions made this week
- [Decision] (link to `20 Compass/Decisions/` if logged)

## Decisions still open (with review date)
- [Decision] — review by [date]

## Energy read
- Physical: [1–10 + 1 sentence]
- Mental: [1–10 + 1 sentence]
- Relational: [1–10 + 1 sentence]
- Founder: [1–10 + 1 sentence]

## What I wanted to do and didn't
[Be honest. If the same thing shows up 3 weeks in a row, it needs a different treatment.]

## Next week's top 3 priorities (drafted, will lock Monday)
1.
2.
3.

## What I'm NOT doing next week
- [Explicit de-prioritizations]

## Public moment from this week worth sharing?
[Anything worth a post? Pass to content engine if yes.]

## Person to reach out to next week
[One name from `40 Areas/Relationships/`. Cadence-overdue or important.]
```

When done, update `_AI/Contexts/current-state.md` Monday block.

## Output format
See above.

## Example
*(populate after first real weekly review)*
