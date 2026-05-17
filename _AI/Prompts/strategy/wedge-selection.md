---
type: prompt
category: strategy
status: living
tags: [prompts, strategy, wedge, gtm]
---

# Prompt: Wedge selection for a venture

**Use when:** A venture has multiple plausible first products / first ICPs / first geographies and I need to pick the wedge.
**Reads:** `_AI/Contexts/meet.md`, target venture's `CLAUDE.md`, `50 Atlas/Playbooks/wedge-selection-frameworks.md` (when populated)
**Filed at:** `30 Ventures/[Venture]/Notes/Wedge Selection.md`

## Inputs
- <<venture>>: [Venture name]
- <<candidate wedges>>: [List of 2–4 possible wedges — product/ICP/geo combinations]
- <<constraints>>: [Bandwidth, capital, regulatory, timing]

## Prompt body

Read `_AI/Contexts/meet.md` and `30 Ventures/<<venture>>/CLAUDE.md` first.

Candidate wedges: <<candidate wedges>>
Constraints: <<constraints>>

Apply a wedge-selection frame using these criteria (weighted):

1. **Time to first paying customer** (heavy weight — speed beats theory)
2. **Cost to acquire that customer** (CAC inside our reach?)
3. **Quality of feedback loop** (will the wedge teach us about the bigger market?)
4. **Defensibility once we win** (can we build moat here, or does it commodify?)
5. **Founder-market fit** (does Meet have native advantage in this segment?)
6. **UAE/GCC native advantage** (cite specifics where relevant)
7. **Adjacent expansion path** (after we win this wedge, where do we go next?)

For each candidate, score 1–5 on each criterion. Sum with weights. Recommend.

Return:

```
# Wedge Selection — [Venture]

## Candidates evaluated
[List]

## Scoring table
| Criterion | Weight | Wedge A | Wedge B | Wedge C |
|---|---|---|---|---|
| ... | ... | 1-5 | 1-5 | 1-5 |
| **Weighted total** | — | X | Y | Z |

## Recommendation
**Wedge [X], because [one-sentence why].**

## Why not the others
- [Wedge B] — [specific reason it loses]
- [Wedge C] — [specific reason it loses]

## What we accept by choosing [X]
- [Trade-off named]

## First 90 days if we go with [X]
- Week 1–2: [...]
- Week 3–6: [...]
- Week 7–12: [...]

## Kill criteria
- If by [date], [metric] hasn't hit [threshold], we revisit the wedge.
```

## Output format
See above.

## Example
*(populate after first real run)*
