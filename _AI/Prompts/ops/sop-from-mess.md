---
type: prompt
category: ops
status: living
tags: [prompts, ops, sop]
---

# Prompt: Turn messy process into clean SOP

**Use when:** A process is being done inconsistently, or being done well only by one person, or about to scale.
**Reads:** `_AI/Contexts/meet.md`, relevant venture `CLAUDE.md`, skill: `finanshels-coe` for Finanshels SOPs
**Filed at:** `30 Ventures/[Venture]/SOPs/[Process].md` OR `40 Areas/[Area]/SOPs/[Process].md`

## Inputs
- <<process name>>: [What the process is]
- <<who does it today>>: [Person or team]
- <<current state description>>: [How it's done now — even if messy]
- <<failure modes>>: [Where it breaks today]
- <<who needs to do it after the SOP>>: [Future operator profile — junior, ops team, BPO, etc.]

## Prompt body

Read `_AI/Contexts/meet.md`. If venture is Finanshels, also load skill `finanshels-coe`.

Process: <<process name>>
Current state: <<current state description>>
Failure modes: <<failure modes>>
Future operator: <<who needs to do it after the SOP>>

Build an SOP that a competent-but-new person could execute. Use this structure:

```
# SOP: [Process Name]

**Owner:** [Role, not person]
**Reviewed:** YYYY-MM-DD
**Reviewed by:** [Person]
**Frequency:** [Daily / per-event / weekly / monthly]
**Time to complete:** [Average minutes/hours]

## Purpose (1 line)
[Why this process exists. Without this, what breaks.]

## Trigger
[The signal that says "run this SOP now"]

## Pre-requisites
- [Access / tool / data needed before starting]

## Step-by-step
1. **[Step name]** — [Exact action]
   - Tool: [where this happens — CRM, WhatsApp, sheet, etc.]
   - Input: [what you start with]
   - Output: [what this step produces]
   - Time: [~minutes]
   - If [edge case], then [alternate path]

2. ...

## Quality check (run before marking done)
- [Specific check 1]
- [Specific check 2]

## What good looks like
[Concrete example of a well-executed instance]

## What bad looks like
[Concrete example of a failed instance — and the cost of the failure]

## Escalation
- If [condition], escalate to [role] within [timeframe].

## Metrics this process feeds
- [Scorecard metric that depends on this SOP being run well]

## Common mistakes (and the fix)
- [Mistake] → [Fix]

## Related SOPs
- [Upstream SOP that hands off to this one]
- [Downstream SOP that takes the output of this one]
```

Keep language simple. Operator-level English. No jargon unless the operator already speaks it.

## Output format
See above.

## Example
*(populate after first real SOP — Finanshels WhatsApp lead triage would be a great first one)*
