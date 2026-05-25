---
name: ad-copy-generator
description: Use when a Finanshels marketer needs paid ad copy for Google Search, Meta (Instagram/Facebook), or LinkedIn promoting a Finanshels service. Triggers include: "write Google ads for VAT registration", "I need Meta ad copy for the CT deadline", "draft LinkedIn ads for outsourced CFO services", "generate ad variations for company formation". Produces per-platform ad sets — headlines, descriptions, primary text within character limits, and CTAs — built on the Pain → Solution → Proof → CTA formula.
---

# Ad Copy Generator

Generates platform-ready paid ad copy for Finanshels services using the master-brand Ad Copy Formula: Pain → Solution → Proof → CTA.

## When to use
- Producing Google Search ads for high-intent keywords (VAT registration, CT filing, bookkeeping UAE).
- Writing Meta (Instagram/Facebook) ad copy for awareness or lead-generation campaigns.
- Creating LinkedIn ads aimed at founders and finance leads.
- Generating multiple ad variations for A/B testing within a campaign.
- Refreshing fatigued creative for an ongoing campaign.

## Inputs needed
**Required**
- Service to promote (CT registration/filing, VAT, bookkeeping, outsourced CFO, audit support, payroll, company formation).
- Target segment (entity type, revenue band, role, compliance situation).
- Platform(s) — Google Search, Meta, LinkedIn, or all three.

**Optional**
- Promotion / offer (free assessment, deadline checklist, discovery call).
- Urgency hook (a real FTA deadline or filing window).
- Landing-page URL / destination.
- Keyword list (for Google Search) or audience definition (for Meta/LinkedIn).
- Number of variations required.

## Workflow
### Step 1 — Lock the formula inputs
For the chosen service and segment, write the four formula beats in plain English first, before formatting:
- **Pain** — the specific UAE compliance pain the segment feels (missed deadline, FTA penalty, messy books, registration confusion).
- **Solution** — what Finanshels does, framed as the relief to that pain.
- **Proof** — one approved proof point (7,000+ businesses served, 150+ qualified accountants, named client, AI-native delivery).
- **CTA** — the single next step (Book a free assessment, Get the checklist, Talk to a tax expert).

### Step 2 — Confirm platform specs
Open `templates/ad-formats-reference.md` and note the exact character limits and asset counts for each requested platform. Copy must fit the limits with no truncation — count characters including spaces.

### Step 3 — Write Google Search ads
Produce a responsive search ad set: 8-12 headlines (≤30 chars each) and 3-4 descriptions (≤90 chars each). Front-load keywords, include the urgency hook, and make at least three headlines benefit-led. Add the path fields. Keep one CTA headline.

### Step 4 — Write Meta ad copy
Produce 2-3 ad variations, each with primary text (lead with Pain in the first ~125 visible chars), a headline (≤40 chars), and a description (≤30 chars). Conversational, founder-first tone; emoji only sparingly and only if on-brand.

### Step 5 — Write LinkedIn ad copy
Produce 2-3 variations with intro text (≤150 chars before "see more"), a headline (≤70 chars), and a professional CTA. Tone is credible and peer-to-peer for finance leads — no hype.

### Step 6 — Add the compliance and brand pass
Check every ad: WHY → WHAT framing, no jargon, no corporate filler, no superlatives that imply guarantees ("never pay a penalty"), urgency tied only to real FTA deadlines, one proof point per ad, brand orange #F16610 noted for CTA buttons.

### Step 7 — Package with testing notes
Group output by platform. Add a short note on what each variation tests (different pain angle, different proof point, different CTA) so the team can run a clean A/B test.

## Output format
```
# Ad Copy — [Service] · [Segment]

Formula inputs:
- Pain: [...]
- Solution: [...]
- Proof: [approved proof point]
- CTA: [single next step]

## Google Search — Responsive Search Ad
Headlines (≤30 chars):
1. [...]  2. [...]  ... (8-12)
Descriptions (≤90 chars):
1. [...]  2. [...]  ... (3-4)
Paths: /[path1] /[path2]
Final URL: [landing page]

## Meta (Instagram/Facebook)
### Variation A — [angle]
- Primary text: [...]
- Headline (≤40): [...]
- Description (≤30): [...]
- CTA button: [Book Now / Learn More / Get Offer]
### Variation B ... (2-3 total)

## LinkedIn
### Variation A — [angle]
- Intro text (≤150 visible): [...]
- Headline (≤70): [...]
- CTA: [Request Demo / Learn More / Sign Up]
### Variation B ... (2-3 total)

## Testing notes
- A vs B tests: [what differs]
- CTA buttons use brand orange #F16610

## Next steps
- [ ] Finanshels team review
- [ ] Verify FTA deadline before launch
```

## Quality checklist
- [ ] Every ad follows Pain → Solution → Proof → CTA.
- [ ] All copy fits the exact character limits per `templates/ad-formats-reference.md`.
- [ ] One approved proof point per ad — no invented numbers or clients.
- [ ] Founder-first voice ("you/your"); plain English, no jargon or filler.
- [ ] Leads WHY → WHAT — never opens with "We are an accounting firm".
- [ ] Urgency hooks reference only real, verified FTA deadlines.
- [ ] No guarantees or superlatives that could mislead ("zero penalties, guaranteed").
- [ ] Each variation has a clear, distinct testing angle.
- [ ] One single, unambiguous CTA per ad.
- [ ] CTA buttons noted in brand orange #F16610.
- [ ] No pricing stated — offers described, AED figures left for account-manager sign-off.
- [ ] Output grouped cleanly by platform.

## Examples
**Example 1** "Write Google Search ads for VAT registration targeting mainland startups near the AED 375,000 threshold."
**Example 2** "I need three Meta ad variations for the Corporate Tax filing deadline aimed at free zone founders."
**Example 3** "Draft LinkedIn ad copy promoting outsourced CFO services to finance leads at AED 10–50M companies."

## Guardrails
- UAE jurisdiction only — never reference IRS, US states, UK/EU tax, or CPE.
- Ad copy is professional work product — a Finanshels team member must review and approve before any ad goes live.
- AI does not set or confirm pricing — describe offers, never state fees; leave AED figures for account-manager completion.
- Never invent Finanshels credentials, client names, case studies, testimonials, or numbers beyond the approved proof points.
- Treat all prospect/client data as confidential; never use real client identifiers in examples.
- Verify all tax rates, thresholds, and deadlines against current FTA guidance before relying on them.

## Reference
See `templates/ad-formats-reference.md` for character limits and format specs per platform.
See ../_shared/finanshels-context.md for UAE tax facts, rates, and deadlines.
See the `master-brand` skill for the Ad Copy Formula, voice, proof points, and brand colours.
