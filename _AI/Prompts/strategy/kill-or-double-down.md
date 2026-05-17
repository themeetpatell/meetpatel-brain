---
type: prompt
category: strategy
status: living
tags: [prompts, strategy, portfolio, decision]
---

# Prompt: Quarterly kill-or-double-down call

**Use when:** End-of-quarter portfolio review. Every P1+ venture gets evaluated. No third option allowed.
**Reads:** `_AI/Contexts/meet.md`, `ventures-overview.md`, each venture's `CLAUDE.md`, last quarter's metrics
**Filed at:** `20 Compass/Decisions/YYYY-QX-portfolio-call.md`

## Inputs
- <<venture>>: [One venture, run separately for each]
- <<quarter-over-quarter metrics>>: [Revenue, engagement, user count, whatever proxy applies]
- <<time invested this quarter>>: [Rough % of deep work hours]
- <<wins>>: [What worked]
- <<losses>>: [What didn't]
- <<external signals>>: [Market movement, competitor moves, regulatory, capital environment]

## Prompt body

Read `_AI/Contexts/meet.md`, `30 Ventures/<<venture>>/CLAUDE.md`, and the last quarterly review for this venture (if any).

Apply the kill-or-double-down frame. No "stay the course" option allowed. Force the binary.

Score across:
1. **Trajectory** — slope of the primary metric over the last 2 quarters
2. **Founder energy** — am I energized or extracting it on willpower?
3. **Market signal** — are customers / users / category insiders giving stronger or weaker signals?
4. **Opportunity cost** — what better thing could the time go to?
5. **Optionality value** — does keeping this alive preserve a real future option?

Return:

```
# Portfolio Call — [Venture] — YYYY-QX

## Trajectory
[Last quarter vs this quarter, with the actual numbers]

## Founder energy read
[Honest, 1–2 sentences]

## Market signal read
[What's getting stronger / weaker]

## Opportunity cost
[Where would this time go if we killed it]

## Optionality value
[Is the optionality real or are we just hoarding]

## Recommendation
**[KILL] or [DOUBLE DOWN]**

## Plan if KILL
- Wind-down timeline: [...]
- Asset preservation: [what IP/learnings get saved to vault]
- Communication plan: [if team/users/investors involved]
- Closing note for the founder: [one line — what this venture taught us]

## Plan if DOUBLE DOWN
- New 90-day target: [specific]
- New resource commitment: [time, money, hires]
- New kill criteria for next quarter: [specific]

## What would change my mind
[Two conditions for each direction]
```

Be opinionated. The whole point is to force the call.

## Output format
See above.

## Example
*(populate after first real run)*
