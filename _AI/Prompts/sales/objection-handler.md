---
type: prompt
category: sales
status: living
tags: [prompts, sales, objection]
---

# Prompt: Objection handler — written response

**Use when:** A prospect has raised an objection in writing (email, WhatsApp) and you want to respond in a way that resolves it rather than triggers a back-and-forth.
**Reads:** `_AI/Contexts/meet.md`, venture `CLAUDE.md`, common-objections library (when populated)
**Filed at:** CRM note + add to `30 Ventures/[Venture]/Sales/Objections/[type].md`

## Inputs
- <<objection (exact words)>>: [Paste exactly]
- <<channel>>: [WhatsApp / email / form]
- <<prospect tier>>: [A/B/C]
- <<venture>>: [Which venture]
- <<our standard rebuttal if we have one>>: [Optional]

## Prompt body

Read `_AI/Contexts/meet.md` and `30 Ventures/<<venture>>/CLAUDE.md`.

Objection: <<objection (exact words)>>
Channel: <<channel>>
Tier: <<prospect tier>>

Don't fight the objection. Map it first.

```
# Objection Response — [Prospect] — [Date]

## What objection type is this? (classify)
- **Price** — they think it costs too much
- **Authority** — they can't decide alone
- **Need** — they don't see the urgency
- **Trust** — they don't believe we'll deliver
- **Timing** — wrong moment
- **Comparison** — they're shortlisting us against someone

## The real objection underneath (often different from stated)
[Your read — in one sentence]

## Decision: respond, redirect, or let go
- **Respond** — if the objection is real but addressable
- **Redirect** — if the stated objection isn't the real one (gently reframe)
- **Let go** — if the objection signals wrong fit; lose with grace + referral

## Drafted response (in voice, channel-appropriate)
[The actual message they will receive]

## Why this response works
- [Acknowledges the concern without conceding]
- [Reframes the value if needed]
- [Ends with a small, specific next step — not "let me know your thoughts"]

## What I will NOT do in this response
- Defend with price comparison (race-to-the-bottom)
- Drop price unilaterally
- "Just to follow up" energy
- Soft language that signals weakness

## Add to objection library
- Type: [...]
- Pattern this fits: [...]
- Recommended canonical response for this type: [link to library entry, or "first instance, create entry"]
```

WhatsApp responses: max 3 short messages. Email responses: max 5 sentences. Never call to "explain further" unless the objection is genuinely too nuanced for text.

## Output format
See above.

## Example
*(populate after first 5 real objections)*
