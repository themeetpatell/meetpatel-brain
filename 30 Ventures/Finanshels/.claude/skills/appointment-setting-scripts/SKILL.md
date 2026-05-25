---
name: appointment-setting-scripts
description: Use when a Finanshels SDR or appointment setter needs a call script or talk-track to book a discovery call. Triggers include: preparing for a cold call, an inbound callback, a follow-up call to a prospect who got outreach, calling an event lead, building objection handling for the phone, or training a new appointment setter. Produces a structured call script (opening, qualify, hook, ask, objection branches, close) plus a quick-reference cheat sheet.
---

# Appointment-Setting Scripts

Produces phone scripts and talk-tracks for a Finanshels SDR whose only goal on the call is to book a short discovery call — not to sell, advise, or quote.

## When to use

- Preparing for a batch of cold calls to a defined segment
- An inbound enquiry needs a callback and you want a script
- Following up by phone after a cold email or LinkedIn sequence
- Calling leads collected at an event or webinar
- Building objection-handling for a new appointment setter
- Refreshing a script that is getting too many "send me an email" deflections

## Inputs needed

**Required**
- Call type: cold call / inbound callback / follow-up to outreach / event lead
- Prospect segment (e.g. "Sharjah mainland trading LLC, AED 1–5M revenue, founder-led")
- The hook (e.g. CT first-return deadline, VAT penalty exposure, new free zone licence, fundraise, year-end)

**Optional**
- SDR name and Finanshels role
- What the prospect already knows (got an email, met at event, downloaded a guide)
- Decision-maker name and title
- Discovery call length to offer (default 15 minutes) and who runs it
- Known objection patterns for this segment

## Workflow

### Step 1 — Set the call's single goal
The goal is one booked discovery call with a specific time. Not a sale, not advice, not a price. Write this at the top of the script so the SDR stays on track.

### Step 2 — Write the opening (pattern interrupt + reason)
Open with a brief pattern interrupt (not "how are you today"), the SDR's name and Finanshels, and a one-line honest reason for the call tied to the hook. For callbacks and follow-ups, reference the prior touch. Keep the opening under 20 seconds of speaking.

### Step 3 — Ask permission
Ask for a short slice of time explicitly ("Have you got 30 seconds for me to explain why I called, then you decide?"). This earns attention and lowers resistance. Respect a "no" — offer to call back at a stated time.

### Step 4 — Ask one or two qualifying questions
Short, open questions that confirm fit and surface the pain — e.g. "Have you registered for Corporate Tax yet?" or "Who looks after your books today?" Two questions maximum. Listen; do not interrogate.

### Step 5 — Deliver the value hook
Connect their answer to the hook in one or two sentences. Give a genuinely useful UAE-tax point, not a pitch. Anchor lightly to a proof point if natural (7,000+ businesses, 150+ accountants). Never advise in depth — that is what the discovery call is for.

### Step 6 — Make the booking ask with a specific time
Offer two concrete time slots ("Does Tuesday 11am or Wednesday 3pm work better?") — never "when are you free?". The ask is for a short discovery call with a named Finanshels person. Confirm channel (call / video) and contact details.

### Step 7 — Handle objections, then confirm and close
Use the objection branches below and the responses in `references/call-objection-responses.md`. After agreement: repeat the date, time, timezone (GST), and channel; confirm email/WhatsApp for the invite; tell them what the call will cover; thank them. Send the calendar invite immediately after.

## Output format

```
APPOINTMENT-SETTING SCRIPT
Call type: [Cold / Callback / Follow-up / Event lead]
Segment: [X] | Hook: [X] | Goal: book a [15]-min discovery call
Prepared by: [Name] — REVIEW BEFORE USE

1. OPENING (pattern interrupt + reason)
"[Script line]"

2. PERMISSION
"[Script line]"

3. QUALIFYING QUESTIONS
Q1: "[Question]"
Q2: "[Question]"

4. VALUE HOOK
"[Script line connecting their answer to the hook]"

5. BOOKING ASK (specific times)
"[Script line offering two concrete slots]"

6. OBJECTION BRANCHES
- "Send me an email instead" -> "[Response]"
- "Not interested" -> "[Response]"
- "We already have an accountant" -> "[Response]"
- "Call me later / I'm busy" -> "[Response]"
- "How much does it cost?" -> "[Response — no number, redirect to call]"
- "How did you get my number?" -> "[Honest response]"

7. CONFIRM & CLOSE
"[Script line: repeat date/time/GST/channel, confirm contact, what to expect]"

POST-CALL ACTIONS
- [ ] Send calendar invite immediately
- [ ] Log outcome in CRM
- [ ] [Any follow-up]

----- CHEAT SHEET (one screen) -----
GOAL: one booked call, specific time.
DO: pattern interrupt, ask permission, two questions, two time slots.
DON'T: pitch, advise in depth, say a price, ask "when are you free?".
TOP 3 OBJECTION ONE-LINERS:
- Email instead: "[short line]"
- Have an accountant: "[short line]"
- How much: "[short line]"
ALWAYS CLOSE: date + time + GST + channel + what to expect.
```

## Quality checklist

- [ ] The single goal (one booked call) is stated at the top
- [ ] Opening has a pattern interrupt and an honest, hook-tied reason
- [ ] A permission step is present and respects a "no"
- [ ] No more than two qualifying questions
- [ ] The value hook is genuinely useful, not a sales pitch
- [ ] The booking ask offers two specific time slots, not "when are you free?"
- [ ] All six objection branches are scripted
- [ ] No fee, price, or pricing hint anywhere — "how much" redirects to the call
- [ ] The close repeats date, time, GST timezone, and channel
- [ ] Only approved proof points and client names are used
- [ ] Voice is founder-first, plain English, confident, never alarmist
- [ ] A one-screen cheat sheet is included

## Examples

**Example 1** "Write a cold-call script for calling founders of Dubai mainland trading LLCs whose first Corporate Tax return is due in four months — goal is a 15-minute discovery call."

**Example 2** "Build an inbound callback script — the prospect downloaded our VAT guide and a finance manager left their number. Hook is VAT registration threshold."

**Example 3** "We have event leads from a free zone business expo. Write a follow-up call script — hook is QFZP decisions for newly licensed companies."

## Guardrails

- UAE jurisdiction only — never reference IRS, US states, UK/EU tax, or CPE.
- Outputs are professional work product — a Finanshels team member must review the script before it is used.
- AI does not set or confirm pricing — no fee or pricing hint in any script; "how much does it cost?" redirects to the discovery call.
- The SDR's job is to book a call, not to give tax advice — scripts must not contain detailed advisory answers.
- Never invent Finanshels credentials, client names, case studies, testimonials, or numbers beyond the approved proof points.
- Never fabricate a prospect detail to fake rapport — use only genuinely known facts.
- Respect anti-spam and consent norms — be honest about who is calling and why; if asked, answer plainly how the number was sourced; honour do-not-call requests.
- Treat all prospect data as confidential; never use real client identifiers in examples.
- Verify every tax rate, threshold, and deadline against current FTA guidance before relying on it.

## Reference

See ../_shared/finanshels-context.md for UAE tax facts, rates, and deadlines.
See `references/call-objection-responses.md` for objection responses tuned to the appointment-setting call context.
See the `master-brand` skill for positioning, voice, proof points, and brand colours.
See the sibling `discovery-call-guide` skill for what happens once the call is booked.
