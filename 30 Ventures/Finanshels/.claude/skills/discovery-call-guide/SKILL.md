---
name: discovery-call-guide
description: Use when a Finanshels sales or business development team member is preparing for, running, or debriefing a discovery call with a UAE SME prospect. Triggers include: "prep me for a discovery call", "I have a call with a prospect", "what should I ask on this call", "debrief my discovery call", "turn my call notes into a structured summary". Produces a pre-call prep brief, a tailored call agenda with a UAE-tax-specific question bank, buying-signal cues, and a structured post-call debrief note ready to hand to the prospect-qualification skill.
---

# Discovery Call Guide

Gives the Finanshels sales team a structured discovery-call framework — prep, agenda, question bank, buying-signal radar, and a clean post-call debrief — so every prospect conversation produces qualified, scoreable notes.

## When to use

- Preparing for a first discovery call with an inbound or referred UAE SME prospect
- Running the call live and needing a question script that keeps it on track
- A prospect's enquiry is vague and you need to uncover the real compliance need
- Debriefing immediately after a call to capture clean notes before detail fades
- Coaching a new BD hire on how Finanshels runs discovery
- Re-qualifying a stalled prospect on a re-engagement call

## Inputs needed

**Required**
- Prospect profile: company name (or reference code), UAE entity type (mainland / free zone / not yet incorporated), industry, estimated revenue band
- Enquiry source and stated reason for enquiry (website form, referral, event, ad, cold outreach)
- Call stage: first discovery call / follow-up call / re-engagement call

**Optional**
- Decision-maker name and title
- Any known compliance gaps or deadlines (CT registration, VAT penalty, audit due)
- Current accountant / bookkeeper, if any
- Prior touchpoints or notes from the CRM
- Time allotted for the call

## Workflow

### Step 1 — Pre-call prep
Build a one-paragraph prep brief: who they are, why they enquired, the most likely compliance trigger (e.g. first CT return, VAT registration threshold, bookkeeping behind), and two hypotheses to test on the call. Note the CT/VAT deadline math from `../_shared/finanshels-context.md` so you can speak to their actual timeline. Decide the single outcome you want from the call (book a proposal, scope a catch-up, qualify out).

### Step 2 — Open the call
Spend the first 2-3 minutes setting the frame: confirm time available, state the agenda ("I'll ask about your business and where finance sits today, then we'll see if and how we can help — no pitch unless it's a fit"), and lead WHY before WHAT. Founder-first language ("you/your"), warm and confident, never alarmist.

### Step 3 — Run the question framework
Work through the six question categories in `references/discovery-question-bank.md` — Situation, Pain, Compliance Status, Timeline, Decision Process, Budget Signals. Ask open questions, then go one level deeper on anything compliance-relevant. Do not interrogate: aim for a conversation that naturally covers all six. Capture answers verbatim where the wording matters (especially objections and timeline language).

### Step 4 — Listen for buying signals
Tag what you hear against the buying-signal cues: urgency language ("deadline", "penalty", "auditor asked"), dissatisfaction with the incumbent, founder personally involved, explicit ask for pricing or a proposal, multiple service lines surfacing. Note red flags too: price-shopping only, no UAE compliance need, structure beyond Finanshels' scope.

### Step 5 — Close with a clear next step
Never end on "we'll be in touch". Summarise what you heard, name the gap, and propose one concrete next step with a date: send a proposal, book a scoping call, share a compliance checklist, or — if not a fit — say so kindly and refer out. Confirm the next step and who owns it before hanging up.

### Step 6 — Debrief while it is fresh
Within 30 minutes, complete the debrief note using the output format. Convert raw notes into the structured fields the `prospect-qualification` skill needs: entity type, revenue band, compliance status, pain point, decision-maker access, urgency. Flag anything uncertain rather than guessing.

### Step 7 — Hand off
State the recommended next action and route: score with `prospect-qualification`, scope with `engagement-budget-calculator`, or draft with `proposal-generator`. Assign an owner and a follow-up date.

## Output format

```
DISCOVERY CALL PACK — [Company / Reference]
Call stage: [First / Follow-up / Re-engagement] | Date: [Date] | Rep: [Name]

PRE-CALL PREP BRIEF
- Who they are: [1-2 sentences]
- Why they enquired: [stated reason]
- Likely compliance trigger: [CT / VAT / bookkeeping / audit / formation]
- Deadline math: [e.g. FY ends 31 Dec 2025 -> CT return due 30 Sep 2026]
- Hypotheses to test: [1] [2]
- Desired call outcome: [one sentence]

CALL AGENDA
1. Open & frame (3 min)
2. Situation & business model
3. Pain & current finance setup
4. Compliance status & gaps
5. Timeline & triggers
6. Decision process & budget signals
7. Summary & next step

QUESTION BANK (tailored — see references/discovery-question-bank.md)
- Situation: [2-3 picked questions]
- Pain: [2-3]
- Compliance status: [2-3]
- Timeline: [1-2]
- Decision process: [1-2]
- Budget signals: [1-2]

--- POST-CALL DEBRIEF ---

WHAT WE LEARNED
- Entity type: [Mainland / Free zone (name) / Not incorporated]
- Revenue band: AED [band]
- Industry / activity: [X]
- Current finance setup: [in-house / freelancer / firm / nothing]
- Compliance status: [CT reg, VAT reg, bookkeeping, audit — what's done / missing]
- Primary pain point (verbatim if useful): "[X]"
- Timeline / triggers: [deadlines, events driving urgency]
- Decision-maker: [Name, title — engaged / not engaged]
- Decision process: [who else decides, expected timeframe]

BUYING SIGNALS HEARD
- [signal] [signal]

RED FLAGS / RISKS
- [flag or "none identified"]

OBJECTIONS RAISED (verbatim)
- "[objection]" -> route to objection-handling-playbook

NEXT STEP AGREED ON THE CALL
- [Concrete action + date]

HANDOFF
- Score with: prospect-qualification [Yes/No]
- Recommended bundle hypothesis: [Starter / Growth / Advisory / Catch-up]
- Pricing: [TBD — account manager to set, do not quote]
- Owner: [Name] | Follow-up date: [Date]
```

## Quality checklist

- [ ] Pre-call brief states a single desired outcome, not a vague goal
- [ ] Deadline math uses the prospect's actual financial-year-end
- [ ] All six question categories are represented in the tailored question bank
- [ ] Questions are specific to the prospect's likely gap, not generic
- [ ] Debrief fills every field the prospect-qualification skill needs (or marks it unknown)
- [ ] Objections captured verbatim and routed to the objection-handling-playbook
- [ ] A concrete, dated next step was agreed — not "we'll be in touch"
- [ ] No fee or price was quoted on the call or written into the pack
- [ ] Buying signals and red flags both filled (never both blank)
- [ ] Owner and follow-up date assigned
- [ ] No real client identifiers used in any example
- [ ] Tone is founder-first, confident, never alarmist

## Examples

**Example 1** "I've got a discovery call in an hour with a Dubai mainland trading LLC, around AED 6M revenue. They filled in the website form saying their auditor flagged messy books. Prep me and give me a question script."

**Example 2** "Just finished a call with a DMCC free zone consultancy that hasn't registered for Corporate Tax. The founder was on the call and asked what it would cost. Turn my notes into a debrief I can score."

**Example 3** "Re-engagement call coming up with a prospect who went quiet two months ago after we sent a bookkeeping proposal. What should I ask to find out if this deal is still alive?"

## Guardrails

- UAE jurisdiction only — never reference IRS, US states, UK/EU tax rules, or CPE.
- The call pack and debrief are professional work product — a Finanshels team member must review and own them before any commercial decision.
- AI does not set or confirm pricing — leave all fee fields marked "TBD — account manager".
- Never invent Finanshels credentials, client names, case studies, testimonials, or numbers beyond the approved proof points (7,000+ businesses, 150+ qualified accountants).
- Treat all prospect data as confidential — never use real client names or financial data in examples.
- Verify every CT/VAT rate, threshold, and deadline against current FTA guidance before stating it on a call.
- Never promise an outcome (e.g. "we'll waive your penalty") — describe the process, not a guaranteed result.

## Reference

See ../_shared/finanshels-context.md for UAE tax facts, rates, and deadlines.
See `references/discovery-question-bank.md` for the categorised question bank with UAE-tax-specific probes.
See the `master-brand` skill for positioning, voice, proof points, and brand colours.
