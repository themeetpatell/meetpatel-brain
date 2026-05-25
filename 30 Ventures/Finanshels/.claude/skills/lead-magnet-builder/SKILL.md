---
name: lead-magnet-builder
description: Use when a Finanshels marketer needs to design and draft a gated lead magnet — a checklist, guide, template, or calculator concept — on a UAE tax or accounting topic to capture leads. Triggers include: "build a lead magnet on Corporate Tax registration", "we need a free downloadable for VAT", "create a gated checklist for free zone companies", "design an opt-in asset for the CT deadline". Produces the full lead-magnet content, the opt-in / landing-page copy, and a 3-email nurture outline.
---

# Lead Magnet Builder

Designs and drafts a gated lead magnet on a UAE tax or accounting topic, plus the opt-in page and nurture sequence needed to convert downloads into qualified leads.

## When to use
- Building a top-of-funnel asset to capture email addresses from a defined ICP segment.
- Supporting a campaign that needs a hook (see the `campaign-planner` skill).
- Converting a high-traffic blog topic into a gated, more valuable resource.
- Creating a sales-enablement asset reps can share to qualify prospects.
- Refreshing an outdated downloadable after an FTA rule change.

## Inputs needed
**Required**
- Topic (a specific UAE tax/accounting subject — CT registration, VAT for free zones, year-end close).
- Target segment (entity type, revenue band, role, compliance situation).
- Funnel stage (top — awareness, middle — consideration, bottom — decision).
- Format preference (checklist, guide, template, calculator concept) — or "recommend best fit".

**Optional**
- Campaign it supports and the desired CTA after download.
- Existing content that can be repurposed.
- Distribution channels (ads, organic social, email, partnerships).
- Deadline or trigger driving urgency.

## Workflow
### Step 1 — Pick the highest-pull topic and format
If the format is open, choose using the pull table in `templates/lead-magnet-outline.md`: checklists win for deadline/awareness, guides for consideration, templates and calculator concepts for decision-stage. Confirm the topic is narrow, urgent, and solves one real problem for the segment. State the promise in one sentence ("Everything you need to register for Corporate Tax before your FTA deadline").

### Step 2 — Outline the asset
Build the structure using `templates/lead-magnet-outline.md`: title, subtitle, the promise, 4-8 sections or steps, and where a proof point and CTA appear. Keep it skimmable — a busy founder should get value in five minutes.

### Step 3 — Draft the asset content
Write the full content section by section. Lead WHY → WHAT. Plain English; translate any tax term on first use. Cite UAE figures from the shared context and add a "verify against current FTA guidance" line. End with a soft CTA to the next step (assessment, discovery call).

### Step 4 — Write the opt-in / landing-page copy
Draft the gate: a benefit-led headline, 3-5 bullet points of what's inside, a one-line credibility anchor (proof point), the form fields (keep minimal — name, email, optionally entity type), and the submit-button label in brand orange #F16610.

### Step 5 — Plan the 3-email nurture sequence
Outline three follow-up emails: (1) deliver the asset + set expectations, (2) add value / address the next objection, (3) make the offer with a clear CTA. Note timing for each. For full newsletter-style copy, hand off to the `email-newsletter-writer` skill.

### Step 6 — Brand and compliance pass
Check voice, proof point, no invented numbers, urgency tied to real FTA deadlines, and that nothing reads as definitive tax advice. Add the review checkbox.

### Step 7 — Package and note distribution
Assemble the asset, opt-in copy, and nurture outline. Add a short note on which channels should promote it and how it ties into the campaign.

## Output format
```
# Lead Magnet — [Title]

## Concept
- Format: [checklist / guide / template / calculator concept]
- Topic & promise: [one sentence]
- Segment: [...] · Funnel stage: [...]

## The Asset
[Title]
[Subtitle]
### Section 1 — [name]
[content]
### Section 2 ... (4-8 sections)
Proof point: [where anchored]
CTA: [next step]

## Opt-In / Landing Page Copy
- Headline: [...]
- Subhead: [...]
- What's inside: [3-5 bullets]
- Credibility line: [proof point]
- Form fields: [name, email, ...]
- Button: [label] (#F16610)

## 3-Email Nurture Outline
- Email 1 (Day 0) — Deliver: [subject + summary]
- Email 2 (Day [n]) — Add value: [subject + summary]
- Email 3 (Day [n]) — Offer: [subject + summary + CTA]

## Distribution notes
[channels + campaign tie-in]

## Next steps
- [ ] Finanshels team review
- [ ] Verify tax facts against current FTA guidance
```

## Quality checklist
- [ ] Topic is narrow, urgent, and solves one real UAE compliance problem.
- [ ] Format matches the funnel stage per the pull table.
- [ ] Promise is stated in a single, benefit-led sentence.
- [ ] Asset is skimmable — value delivered within ~5 minutes of reading.
- [ ] Leads WHY → WHAT; founder-first voice; jargon translated on first use.
- [ ] One approved proof point anchored — no invented numbers or clients.
- [ ] UAE tax figures cited with a "verify against current FTA guidance" note.
- [ ] Opt-in form kept minimal; button in brand orange #F16610.
- [ ] 3-email sequence: deliver → add value → offer, with timing noted.
- [ ] CTA is a single, clear next step.
- [ ] Nothing reads as definitive personal tax advice.
- [ ] Ends with a review / next-steps block.

## Examples
**Example 1** "Build a lead magnet to capture leads ahead of the Corporate Tax registration deadline for mainland SMEs."
**Example 2** "We need a gated checklist for free zone companies wondering if they qualify as a QFZP."
**Example 3** "Design a year-end close template as a downloadable for finance leads at AED 5–50M companies."

## Guardrails
- UAE jurisdiction only — never reference IRS, US states, UK/EU tax, or CPE.
- The asset and its copy are professional work product — a Finanshels team member must review before publication.
- AI does not set or confirm pricing — describe offers, never state fees; leave AED figures for account-manager completion.
- Never invent Finanshels credentials, client names, case studies, testimonials, or numbers beyond the approved proof points.
- Treat all prospect/client data as confidential; never use real client identifiers in examples.
- Verify all tax rates, thresholds, and deadlines against current FTA guidance before relying on them.

## Reference
See `templates/lead-magnet-outline.md` for the format pull table and asset outline structure.
See ../_shared/finanshels-context.md for UAE tax facts, rates, and deadlines.
See the `master-brand` skill for positioning, voice, proof points, and brand colours.
