---
type: prompt
category: ops
status: living
tags: [prompts, ops, okr]
---

# Prompt: Quarterly OKR setter

**Use when:** Start of a quarter. Need to convert strategic themes into measurable objectives + key results per venture.
**Reads:** `_AI/Contexts/meet.md`, target venture `CLAUDE.md`, last quarter's review
**Filed at:** `30 Ventures/[Venture]/OKRs/YYYY-QX.md`

## Inputs
- <<venture>>: [Venture name]
- <<strategic themes for the quarter>>: [2–4 themes from portfolio review]
- <<last quarter's OKR results>>: [Hit / missed / dropped]
- <<team capacity>>: [Realistic deep-work hours available]

## Prompt body

Read `_AI/Contexts/meet.md`, `30 Ventures/<<venture>>/CLAUDE.md`, and last quarter's OKR file.

Themes: <<strategic themes for the quarter>>
Last quarter results: <<last quarter's OKR results>>
Capacity: <<team capacity>>

Apply John Doerr OKR discipline + Christina Wodtke pacing. Rules:

1. **3 Objectives max per venture per quarter.** More = no priority.
2. **Each Objective gets 3–5 Key Results.** KRs must be quantitative + outcome-based, not activity-based.
3. **At least one KR per Objective must be uncomfortable.** If we'd default to hitting it, the bar is too low.
4. **No "launch" or "complete" KRs unless they're irreversible milestones.** "Launch X" is activity. "Acquire 50 customers from X" is outcome.
5. **Tie every Objective to a strategic theme.** No orphans.

Return:

```
# OKRs — [Venture] — YYYY-QX

## Theme alignment
- Theme A → Objective 1
- Theme B → Objective 2
- ...

## Objective 1: [Punchy verb-led statement]
*Why this matters now:* [1 sentence]
**Key results:**
- KR1: [from X to Y by [date]]
- KR2: ...
- KR3: ...
*Stretch (uncomfortable) KR:* [the one that scares us]

## Objective 2: ...

## Objective 3: ...

## What we're NOT doing this quarter (de-priorities)
- [Things we're explicitly saying no to]

## Weekly cadence
- Monday: pull KR progress, surface at-risk
- Friday: log delta, write 1-line learning

## End-of-quarter review trigger
- Date: [last business day of quarter]
- Format: kill-or-double-down call per Objective
```

Don't pad to fill 3 Objectives if 2 is the honest answer.

## Output format
See above.

## Example
*(populate after first real quarter)*
