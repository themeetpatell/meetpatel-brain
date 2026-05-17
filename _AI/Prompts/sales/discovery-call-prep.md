---
type: prompt
category: sales
status: living
tags: [prompts, sales, discovery]
---

# Prompt: Discovery call prep brief

**Use when:** A discovery call is on the calendar. Want a one-page brief with the prospect's context, hypothesis of their pain, questions to ask, and the trap to avoid.
**Reads:** `_AI/Contexts/meet.md`, venture `CLAUDE.md`, lead qualification note, any public info on prospect
**Filed at:** Lead's CRM note + `30 Ventures/[Venture]/Sales/Calls/YYYY-MM-DD-[prospect].md`

## Inputs
- <<prospect company>>: [Name + 1-line description]
- <<contact attending>>: [Name, role, decision-power]
- <<lead source + prior context>>: [Recap]
- <<my hypothesis of their pain>>: [Best guess at why they're talking to us]
- <<venture>>: [Which venture]

## Prompt body

Read `_AI/Contexts/meet.md` and `30 Ventures/<<venture>>/CLAUDE.md`.

Prospect: <<prospect company>>
Contact: <<contact attending>>
Prior context: <<lead source + prior context>>
My hypothesis: <<my hypothesis of their pain>>

Generate a discovery call brief that fits on one screen.

```
# Discovery — [Prospect] — [Date]

## In 30 seconds
- Who: [company, size, geo]
- Why they're here: [hypothesis]
- Decision-power on call: [yes/no/partial]
- My read on urgency: [hot / warm / cold]

## Call objectives (max 3)
1. [Validate / disqualify pain hypothesis]
2. [Map decision process + economic buyer]
3. [Earn a next step — second meeting, proposal request, pilot scope]

## Opening (60 seconds — what I say first)
[Specific opener that respects their time]

## Questions to ask (rank-ordered)
1. **[Pain validator]** — "Walk me through how you handle [X] today."
2. **[Cost-of-status-quo]** — "What does [pain] cost you in time/money/risk?"
3. **[Decision process]** — "If you decided this was the right fit, what would the next 30 days look like internally?"
4. **[Champion test]** — "Who else inside the org should I be talking to?"
5. **[Trigger]** — "Why are you looking at this now and not 6 months ago?"

## What to listen for (signal)
- ✓ Specific numbers when describing pain (signal: real pain)
- ✓ Mention of other vendors they're evaluating (signal: real process)
- ✓ Asks about pricing in first 15 min (signal: budget exists)
- ✗ "Maybe in Q4" / "we're just exploring" (signal: kill the deal early)
- ✗ Only one person in the org cares (signal: champion-less)

## Traps to avoid
- Don't pitch in the first 10 minutes.
- Don't demo unless they ask specifically.
- Don't quote price without understanding scope.
- Don't "follow up" — schedule the next step on this call or it dies.

## Three next-step options to offer (in order of preference)
1. [Best]
2. [Acceptable]
3. [Worst-case "still in process"]

## After the call — capture in CRM
- Pain confirmed: yes/no
- Champion identified: yes/no/maybe
- Next step scheduled: yes/no (if no — root cause)
- Tier update: A/B/C
- One-line: what's the real decision criterion now
```

## Output format
See above.

## Example
*(populate after first 10 real calls)*
