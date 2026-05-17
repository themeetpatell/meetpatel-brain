---
type: prompt
category: sales
status: living
tags: [prompts, sales, diagnosis, stuck-deal]
---

# Prompt: Deal stuck — what's actually blocking

**Use when:** A deal has gone quiet for 10+ days or stalled at a stage for 2+ weeks. Need to diagnose the real block (vs. the stated one).
**Reads:** `_AI/Contexts/meet.md`, venture `CLAUDE.md`, lead notes, last 3 communications
**Filed at:** CRM note + (optionally) `30 Ventures/[Venture]/Sales/Postmortems/YYYY-MM-DD-[prospect].md`

## Inputs
- <<prospect>>: [Name + last known stage]
- <<last communication date + channel>>: [...]
- <<stated reason for delay>>: [If any]
- <<my last 3 messages to them>>: [Summarize]
- <<their last 3 messages to me>>: [Summarize]
- <<original pain we agreed on>>: [Recap]

## Prompt body

Read `_AI/Contexts/meet.md` and `30 Ventures/<<venture>>/CLAUDE.md`.

Run a stuck-deal diagnostic. The job is to separate the stated reason ("we're busy right now") from the real reason.

Inputs: see above.

Apply the diagnostic frame:

```
# Stuck Deal Diagnostic — [Prospect] — [Date]

## Stated reason
[Their words]

## Likely real reason (rank-ordered)
1. **[Hypothesis]** — evidence: [...]
2. **[Hypothesis]** — evidence: [...]
3. **[Hypothesis]** — evidence: [...]

## The 4 classic stuck-deal patterns — which one is this?
- **Champion lost internal influence** — signal: champion went quiet, new names appeared, requests for more "info"
- **Pain isn't urgent enough** — signal: they're still "exploring", no calendar pressure
- **Budget didn't materialize** — signal: pricing questions intensified then evaporated
- **We're a feature in someone else's evaluation** — signal: comparison Qs vs. specific competitor

## What to do (concrete next move)
- [One specific message / action — not "follow up"]

## How to write the message
[Draft the actual message — in voice for this venture, designed to either un-stick or kill]

## Kill criteria
- If [no response in X days OR no movement on Y by Z], close as lost with reason: [...]

## Lesson to capture (vault note path)
- If this dies, what does it teach our ICP / pain hypothesis / qualification process?
- File at: 30 Ventures/[Venture]/Sales/Lessons/[lesson].md
```

Be honest. The job is not to revive every deal. Some should die so the pipeline tells the truth.

## Output format
See above.

## Example
*(populate after first 5 real stuck deals)*
