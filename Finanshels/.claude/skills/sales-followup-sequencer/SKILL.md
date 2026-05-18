---
name: sales-followup-sequencer
description: Use when a Finanshels sales team member needs a multi-touch follow-up sequence after a proposal has been sent or a deal has gone quiet. Triggers include: "the prospect went quiet after our proposal", "build me a follow-up sequence", "we sent a quote two weeks ago and heard nothing", "design a nurture cadence for this deal", "what should I send next to this prospect". Produces a dated, touch-by-touch follow-up sequence across email, WhatsApp, LinkedIn, and call, with distinct copy and a value-add per touch, plus clear exit and breakup criteria.
---

# Sales Follow-up Sequencer

Designs a disciplined multi-touch follow-up sequence so a Finanshels deal stays warm after a proposal or a quiet patch — with every touch carrying a distinct angle and a value-add, never "just checking in".

## When to use

- A proposal has been sent and the prospect has gone silent
- A discovery call went well but the prospect stopped replying
- A deal is stalled and you need a structured re-engagement plan
- You need follow-up copy that does not sound repetitive or needy
- Building a default cadence for a deal stage so reps stop improvising
- Deciding when to gracefully break up with an unresponsive prospect

## Inputs needed

**Required**
- Deal stage: proposal sent / post-discovery-call / verbal interest then quiet / long-stalled
- What was last sent or discussed (proposal, quote, call summary, resource)
- How long since the last contact

**Optional**
- Prospect's stated timeline or deadline (CT filing, VAT return, audit, fundraise)
- Any objection raised earlier
- Prospect profile: entity type, revenue band, industry, compliance status
- Channels available (email, WhatsApp, LinkedIn, phone) and prospect's preferred channel
- Decision-maker vs gatekeeper contact

## Workflow

### Step 1 — Set the cadence
Choose the rhythm using `templates/followup-sequence-template.md`. Default: 5-6 touches over ~3 weeks. Tighten the cadence if a real deadline is near (e.g. CT return due in weeks); stretch it if the prospect signalled a longer timeline. Front-load value; never bunch touches.

### Step 2 — Assign a distinct angle per touch
Every touch must have its own reason to exist. Rotate angles: (1) recap & make it easy to act, (2) value-add resource, (3) deadline / compliance reminder, (4) address the likely objection, (5) social proof / peer outcome, (6) graceful breakup. No touch may be "just checking in".

### Step 3 — Build in a value-add per touch
Each touch gives the prospect something useful even if they do not reply: a relevant compliance reminder (CT registration deadline, VAT filing window, 7-year record-keeping rule, Small Business Relief eligibility), a short resource, a deadline calculation specific to their financial year, or a clarifying answer. Value-adds keep Finanshels welcome in the inbox.

### Step 4 — Match channel to touch
Vary channels so the prospect does not feel chased on one. Email for substance and resources; WhatsApp for short, warm nudges (UAE-appropriate and common); LinkedIn for a soft professional touch; a call for the mid-sequence human moment. Respect the prospect's preferred channel if known.

### Step 5 — Write the copy
Draft each touch in Finanshels voice: founder-first, plain English, WHY before WHAT, short. Anchor at least one touch to a proof point (7,000+ businesses, 150+ qualified accountants). Every touch ends with one clear, low-friction CTA. Leave any fee or price detail to the account manager — never restate or discount a quoted figure.

### Step 6 — Define exit and breakup criteria
State when to stop: prospect replies and re-engages (exit to next stage), prospect explicitly declines (exit, mark closed-lost with reason), or sequence completes with no response (send the breakup touch, then move to long-term nurture). The breakup touch should be gracious and leave the door open.

### Step 7 — Assemble the dated sequence
Produce the touch-by-touch plan with concrete send dates, channel, angle, value-add, copy, and CTA, plus the exit rules.

## Output format

```
FOLLOW-UP SEQUENCE — [Prospect / Reference]
Deal stage: [...] | Last contact: [date / what] | Rep: [Name] | Start date: [Date]

CADENCE SUMMARY
- Number of touches: [X] over [X] days
- Pacing rationale: [deadline-driven / standard / extended]

TOUCH-BY-TOUCH

Touch 1 — [Date] — [Channel] — Angle: [Recap & make it easy]
Value-add: [...]
Copy:
"[message]"
CTA: [one clear ask]

Touch 2 — [Date] — [Channel] — Angle: [Value-add resource]
Value-add: [...]
Copy:
"[message]"
CTA: [...]

Touch 3 — [Date] — [Channel] — Angle: [Deadline / compliance reminder]
... (continue for all touches)

Touch [N] — [Date] — [Channel] — Angle: [Graceful breakup]
Copy:
"[message]"
CTA: [door-open ask]

EXIT & BREAKUP CRITERIA
- Re-engages: [action -> next stage]
- Declines: [mark closed-lost, reason, route]
- No response after final touch: [move to long-term nurture]

NOTES FOR THE REP
- Pricing: [do not restate or discount — route to account manager]
- Objection to pre-empt: [if any] -> see objection-handling-playbook
```

## Quality checklist

- [ ] Cadence pacing matches the prospect's real timeline / deadline
- [ ] Every touch has a distinct angle — none is "just checking in"
- [ ] Every touch carries a genuine value-add
- [ ] Channels are varied across the sequence, respecting prospect preference
- [ ] Each touch ends with one clear, low-friction CTA
- [ ] At least one touch anchors to an approved proof point
- [ ] All copy is in Finanshels voice — founder-first, plain English, WHY before WHAT
- [ ] A graceful breakup touch is included
- [ ] Exit criteria cover re-engage, decline, and no-response
- [ ] No fee restated, discounted, or invented
- [ ] All CT/VAT deadlines and rules verified against current FTA guidance
- [ ] No real client identifiers used in examples

## Examples

**Example 1** "We sent a bookkeeping + CT proposal to a Dubai mainland trading company 12 days ago and heard nothing. Their financial year ends in three months. Build me a follow-up sequence."

**Example 2** "A free zone consultancy had a great discovery call, said they were keen, then went quiet for two weeks. Design a re-engagement cadence."

**Example 3** "A prospect raised a price objection, we addressed it, sent a revised scope, and now silence for 10 days. Give me a follow-up sequence that does not feel pushy."

## Guardrails

- UAE jurisdiction only — never reference IRS, US states, UK/EU tax, or CPE.
- The sequence is professional work product — a Finanshels team member must review and own every touch before it is sent.
- AI does not set or confirm pricing — never restate, discount, or invent a fee; route price questions to the account manager.
- Never invent Finanshels credentials, client names, case studies, testimonials, or numbers beyond the approved proof points (7,000+ businesses, 150+ qualified accountants).
- Never use fear or false urgency — deadline reminders must be factual and reassuring, not alarmist.
- Treat all prospect data as confidential — never use real client identifiers in examples.
- Verify every CT/VAT deadline, rate, and threshold against current FTA guidance before putting it in a touch.
- Respect channel etiquette — WhatsApp and LinkedIn touches stay brief and professional; do not over-contact.

## Reference

See ../_shared/finanshels-context.md for UAE tax facts, rates, and deadlines.
See `templates/followup-sequence-template.md` for the reusable cadence and touch template.
See the `objection-handling-playbook` skill if an objection needs to be addressed in a touch.
See the `master-brand` skill for positioning, voice, proof points, and brand colours.
