---
name: meeting-booking-followup
description: Use when a Finanshels SDR needs the messages that protect and convert a booked discovery call. Triggers include: writing a booking confirmation, a pre-call value primer, 24h or 1h reminders, a no-show recovery sequence, or a reschedule message. Produces the full message set for a booked meeting, each message labelled with its send-timing.
---

# Meeting Booking Follow-up

Writes every message between a booked discovery call and the moment it actually happens — confirmation, value primer, reminders, no-show recovery, and reschedule — so booked calls convert into attended calls.

## When to use

- A discovery call was just booked and you need confirmation + reminder messages
- You want a pre-call value primer that makes the prospect show up engaged
- A 24-hour or 1-hour reminder is due
- A prospect no-showed and you need a recovery sequence that re-books them
- A prospect asked to reschedule and you need a clean, no-friction message
- You are setting up a reusable cadence for all booked discovery calls

## Inputs needed

**Required**
- Meeting type (discovery call / follow-up consultation / proposal review)
- Channel for the messages (email / WhatsApp / both)
- Prospect details (name, company, segment — only genuinely known facts)
- Time booked (date, time, GST timezone)
- Status: newly booked / confirmed / no-showed / reschedule requested

**Optional**
- The hook that got the meeting booked (CT deadline, VAT risk, fundraise, etc.)
- Meeting channel and link (video call / phone / in person)
- Name and role of the Finanshels person running the call
- Call length (default 15–20 minutes)
- Anything the prospect should bring or think about beforehand

## Workflow

### Step 1 — Confirm what message set is needed
From the status input, decide which messages to produce: a newly booked meeting needs the full set (confirmation -> primer -> 24h -> 1h); a no-show needs the recovery sequence; a reschedule needs the reschedule message plus a refreshed reminder set.

### Step 2 — Write the booking confirmation (send immediately)
Confirm date, time, GST timezone, channel, link, and who they will meet. Set expectations: what the call will and will not cover, how long it is, that it is no-obligation. Tell them what to bring or have ready (e.g. "rough idea of revenue and whether you've registered for CT" — nothing onerous). Warm, brief, founder-first.

### Step 3 — Write the pre-call value primer (send ~24–48h before)
Give one genuinely useful, relevant UAE-tax point tied to the hook so they arrive engaged and see value before the call. No selling. End with light reinforcement of the time and a one-line "reply if anything changes".

### Step 4 — Write the reminder cadence
- **24-hour reminder:** short, friendly, restate date/time/GST/channel/link, one line on what they'll get out of it.
- **1-hour reminder:** very short, the link, "see you shortly" — WhatsApp tone if that channel is used.
Skip a reminder if it would land outside reasonable hours or on a UAE holiday.

### Step 5 — Write the no-show recovery sequence
Three touches over ~5 working days, no guilt-tripping:
- **Touch 1 (same day):** assume good faith ("looks like the timing slipped — happens to every founder"), offer to re-book with two specific slots.
- **Touch 2 (+2 days):** restate the value/hook, one-line re-book ask.
- **Touch 3 (+5 days):** soft close, leave the door open, easy opt-out.

### Step 6 — Write the reschedule message
Make rescheduling effortless and blame-free. Offer two new specific slots, confirm the new details, keep the relationship warm. Then regenerate the reminder cadence for the new time.

### Step 7 — Date and label every message, hand off for review
Lay each message on the calendar relative to the meeting time, label every one with its send-timing, and flag that a Finanshels team member reviews before sending.

## Output format

```
MEETING FOLLOW-UP MESSAGE SET
Prospect: [Name, Company] | Meeting: [Type]
Booked for: [Date, Time GST] | Channel: [X] | With: [Finanshels person]
Status: [Newly booked / Confirmed / No-showed / Reschedule]
Prepared by: [Name] — REVIEW BEFORE SENDING

--- BOOKING CONFIRMATION --- Send: immediately --- Channel: [X]
[Subject if email]
[Body: date/time/GST, link, who they meet, what to expect, what to bring]

--- PRE-CALL VALUE PRIMER --- Send: [24-48h before] --- Channel: [X]
[Subject if email]
[Body: one useful UAE-tax insight tied to the hook + light time reinforcement]

--- 24-HOUR REMINDER --- Send: [Date, Time] --- Channel: [X]
[Body: restate details + one-line value]

--- 1-HOUR REMINDER --- Send: [Date, Time] --- Channel: [X]
[Body: link + see-you-shortly]

--- NO-SHOW RECOVERY (only if no-showed) ---
Touch 1 — Send: same day — [Body: good-faith re-book, two slots]
Touch 2 — Send: +2 days — [Body: value restated, re-book ask]
Touch 3 — Send: +5 days — [Body: soft close + opt-out]

--- RESCHEDULE MESSAGE (only if reschedule requested) ---
Send: on request — [Body: blame-free, two new slots, confirm details]

SEND SCHEDULE
- [Each message with its exact send date/time]

NOTES FOR SENDER
- [Personalisation slots, holiday/timezone caveats, what to verify]
```

## Quality checklist

- [ ] Booking confirmation states date, time, GST timezone, channel, and link
- [ ] Confirmation sets expectations and lists anything the prospect should bring
- [ ] The pre-call primer delivers one genuinely useful UAE-tax insight, no pitch
- [ ] 24h and 1h reminders are present and short
- [ ] No-show recovery has three touches and contains zero guilt-tripping
- [ ] Reschedule message is blame-free and offers two specific new slots
- [ ] Every message is labelled with its exact send-timing
- [ ] No fee, price, or pricing hint appears in any message
- [ ] Only approved proof points and client names are used
- [ ] Personalisation is bracketed — no invented prospect facts
- [ ] Every email message offers an easy opt-out / "reply to change or cancel"
- [ ] Voice is warm, founder-first, plain English, never alarmist

## Examples

**Example 1** "A founder of an Abu Dhabi mainland LLC just booked a 20-minute discovery call for next Tuesday 2pm GST. Write the full confirmation, primer, and reminder set — hook was the Corporate Tax return deadline."

**Example 2** "A prospect no-showed their VAT discovery call this morning. Write a 3-touch no-show recovery sequence that re-books them without making them feel bad."

**Example 3** "A DMCC free zone founder asked to move their Thursday call to next week. Write the reschedule message plus a refreshed reminder cadence for the new slot."

## Guardrails

- UAE jurisdiction only — never reference IRS, US states, UK/EU tax, or CPE.
- Outputs are professional work product — a Finanshels team member must review before anything is sent to a prospect.
- AI does not set or confirm pricing — no fee or pricing hint in confirmations, primers, reminders, or recovery messages; the discovery call decides scope and proposal.
- Never invent Finanshels credentials, client names, case studies, testimonials, or numbers beyond the approved proof points.
- Never fabricate a prospect detail to fake personalisation — use only genuinely known facts and bracket the rest.
- No-show recovery must never guilt-trip, shame, or pressure — assume good faith and make re-booking easy.
- Respect anti-spam and consent norms — every message is relevant, honest, and easy to opt out of; stop messaging on request.
- Treat all prospect data as confidential; never use real client identifiers in examples.
- Verify every tax rate, threshold, and deadline against current FTA guidance before relying on it.

## Reference

See ../_shared/finanshels-context.md for UAE tax facts, rates, and deadlines.
See `templates/meeting-message-set.md` for the fill-in message templates this skill assembles.
See the `master-brand` skill for positioning, voice, proof points, and brand colours.
See the sibling `discovery-call-guide` skill for running the call once the prospect attends.
