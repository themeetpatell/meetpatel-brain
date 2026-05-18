---
name: email-newsletter-writer
description: Use when a Finanshels marketer needs to write an edition of the recurring nurture newsletter — "the Finanshels Brief" — for the prospect and client list. Triggers include: "write this month's newsletter", "draft the Finanshels Brief on the new CT update", "turn this FTA announcement into a newsletter", "write the VAT-quarter email to our list". Produces a full newsletter — subject-line and preview-text options, intro, 2-3 short segments, one CTA, and a sign-off.
---

# Email Newsletter Writer

Writes a complete edition of "the Finanshels Brief" — a recurring UAE tax and finance nurture newsletter that keeps prospects and clients informed and warm.

## When to use
- Producing a regular (monthly or fortnightly) newsletter edition for the list.
- Turning a recent FTA or Ministry of Finance update into a digestible email.
- Sending a deadline-reminder edition ahead of a CT or VAT filing window.
- Nurturing leads captured by a lead magnet (handoff from the `lead-magnet-builder` skill).
- Re-engaging a quiet segment with a useful, no-pressure update.

## Inputs needed
**Required**
- Edition theme OR the recent regulatory update / topic to cover.
- Audience segment (prospects, active clients, a specific ICP slice, or the whole list).

**Optional**
- A specific CTA to feature (book an assessment, register before a deadline, read a new article).
- Recent Finanshels content to link (blog posts, case studies, lead magnets).
- The edition number / cadence and the send date.
- Tone steer (educational, deadline-urgent, celebratory).

## Workflow
### Step 1 — Set the edition angle
Decide the single spine of the edition: one regulatory update or theme that earns the open. Everything else supports it. Confirm the topic is timely and relevant to the chosen segment. Note the desired reader action.

### Step 2 — Write subject-line and preview-text options
Draft 3 subject lines (≤50 characters, specific and curiosity-driven, no clickbait or fake urgency) and 2 preview-text options (≤90 characters) that extend — not repeat — the subject. At least one subject should name the concrete benefit or deadline.

### Step 3 — Write the intro
Open with WHY — why this edition matters to the reader right now — in 2-3 short sentences. Founder-first ("you/your"). No "Dear valued client" filler. Set up what the edition covers.

### Step 4 — Write the 2-3 content segments
Use `templates/newsletter-template.md`. Each segment: a clear sub-heading, 2-4 short sentences or a tight bullet list, plain English with any tax term translated, and UAE figures cited from the shared context with a "verify with the Finanshels team" line where a reader might act. Keep the whole email scannable in under two minutes.

### Step 5 — Place one CTA
One primary CTA only — a single button or link to the desired action. Make it specific ("Book your free CT-readiness assessment", not "Learn more"). Anchor one approved proof point near the CTA for credibility.

### Step 6 — Write the sign-off
Close warmly and briefly, signed from the Finanshels team. Include the recall line "Think Finance. Think Finanshels." where it fits naturally. Add a plain unsubscribe note.

### Step 7 — Brand and compliance pass
Check: WHY → WHAT framing, one proof point, no invented numbers or clients, urgency tied only to real FTA deadlines, nothing reading as definitive personal tax advice, brand orange #F16610 noted for the CTA button. Add the review checkbox.

## Output format
```
# The Finanshels Brief — [Edition theme] (Edition #[n], [date])
Segment: [audience]

## Subject lines (≤50 chars)
1. [...]  2. [...]  3. [...]

## Preview text (≤90 chars)
1. [...]  2. [...]

## Body
**Intro**
[2-3 sentences — WHY this matters now]

**[Segment 1 sub-heading]**
[2-4 sentences / bullets]

**[Segment 2 sub-heading]**
[2-4 sentences / bullets]

**[Segment 3 sub-heading — optional]**
[2-4 sentences / bullets]

**[CTA heading]**
[1-2 sentences + proof point]
→ [Button label] (#F16610) — [link]

**Sign-off**
[Warm close] — The Finanshels team
Think Finance. Think Finanshels.
[Unsubscribe note]

## Next steps
- [ ] Finanshels team review
- [ ] Verify tax facts against current FTA guidance
```

## Quality checklist
- [ ] One clear edition angle that earns the open.
- [ ] 3 subject lines ≤50 chars; 2 preview texts ≤90 chars; no fake urgency.
- [ ] Intro leads WHY → WHAT and is founder-first.
- [ ] 2-3 segments, each scannable; whole email reads in under 2 minutes.
- [ ] Tax terms translated; UAE figures cited with a verify-with-team note.
- [ ] Exactly one primary CTA, specific and action-led.
- [ ] One approved proof point anchored near the CTA.
- [ ] No invented numbers, clients, or testimonials.
- [ ] Urgency references only real, verified FTA deadlines.
- [ ] Sign-off is warm; recall line used naturally; unsubscribe note included.
- [ ] CTA button noted in brand orange #F16610.
- [ ] Nothing reads as definitive personal tax advice.

## Examples
**Example 1** "Write this month's Finanshels Brief on the upcoming Corporate Tax return deadline for the prospect list."
**Example 2** "Turn the latest FTA VAT public clarification into a newsletter edition for our active clients."
**Example 3** "Draft a re-engagement edition for quiet free zone leads explaining what QFZP status means for them."

## Guardrails
- UAE jurisdiction only — never reference IRS, US states, UK/EU tax, or CPE.
- The newsletter is professional work product — a Finanshels team member must review before it is sent.
- AI does not set or confirm pricing — describe offers, never state fees; leave AED figures for account-manager completion.
- Never invent Finanshels credentials, client names, case studies, testimonials, or numbers beyond the approved proof points.
- Treat all prospect/client data as confidential; never use real client identifiers in examples.
- Verify all tax rates, thresholds, and deadlines against current FTA guidance before relying on them.

## Reference
See `templates/newsletter-template.md` for the fillable edition layout.
See ../_shared/finanshels-context.md for UAE tax facts, rates, and deadlines.
See the `master-brand` skill for positioning, voice, proof points, and brand colours.
See the `thought-leadership-writer` skill when a topic deserves a full article the newsletter can link to.
