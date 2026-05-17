---
type: prompt
category: sales
status: living
tags: [prompts, sales, qualification, meddic]
---

# Prompt: Lead qualification (MEDDIC-style)

**Use when:** A new lead lands (WhatsApp, form, intro). Want a 5-minute structured qualification before sinking sales time.
**Reads:** `_AI/Contexts/meet.md`, venture `CLAUDE.md`, ICP definition, skill `finanshels-coe` for Finanshels leads
**Filed at:** Wherever the venture stores lead notes (CRM ideally; here for prep)

## Inputs
- <<lead source>>: [WhatsApp / form / intro / event / outbound reply]
- <<what we know>>: [Company, contact, raw message / form data, prior context]
- <<venture>>: [Which venture they're a lead for]

## Prompt body

Read `_AI/Contexts/meet.md` and `30 Ventures/<<venture>>/CLAUDE.md`. Apply MEDDIC + a UAE/GCC sanity layer.

Lead source: <<lead source>>
What we know: <<what we know>>

Return:

```
# Lead Qualification — [Company / Contact] — YYYY-MM-DD

## ICP fit (gate 1)
- [Yes / No / Maybe — and why in one line]
- If No: politely decline / refer. Stop here.

## MEDDIC fill
- **Metrics** — what measurable outcome do they want?
- **Economic buyer** — do we know who actually signs the cheque?
- **Decision criteria** — what will they compare us against?
- **Decision process** — how decisions get made (committee, single, board)?
- **Identify pain** — what's broken today, concretely?
- **Champion** — is there a person inside who'll push for us?

## UAE/GCC sanity layer
- **Legal form** — mainland / free zone / offshore (Finanshels lead only)
- **License status** — do they have an active trade license?
- **Decision urgency** — is there a regulatory / fiscal calendar driver?
- **Cultural fit** — Khaleeji / NRI / Western expat / sub-continent SME? Adjust register.

## Tier (output)
- **Tier A** — full ICP + champion + urgency. Sales priority.
- **Tier B** — partial fit. Nurture, schedule discovery in 2 weeks.
- **Tier C** — wrong fit. Polite decline + referral if possible.

## Next action (one specific move)
- [Schedule discovery / Send specific resource / Refer to partner / Decline]

## Suggested first message (in voice for this venture)
[Drafted in venture's register — Finanshels = calm + trust; Biggdate = warm + sharp; etc.]

## Where to log this in CRM
- [Pipeline / Stage / Tags]
```

Default to action. If the lead is Tier A, ship the next message inside the same response.

## Output format
See above.

## Example
*(populate after first 10 real leads)*
