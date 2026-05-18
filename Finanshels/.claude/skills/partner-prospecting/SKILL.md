---
name: partner-prospecting
description: Use when a Finanshels business development or partnerships team member needs to identify and qualify a potential referral or channel partner. Triggers include: "is this a good partner for us", "evaluate this business-setup consultant as a referral partner", "which free zone authorities should we partner with", "score this VC fund as a channel partner", "build a partner shortlist", "should we approach this law firm". Produces a scored partner profile with client-overlap analysis, mutual-value assessment, conflict check, partner tier, recommended partnership model, and an outreach angle.
---

# Partner Prospecting

Identifies and qualifies UAE businesses whose client base overlaps with Finanshels' ICP, then scores them as referral or channel partners and recommends how to engage.

## When to use
- Evaluating a specific partner candidate raised by the team or an inbound partnership enquiry
- Building a shortlist of partners within a category (free zones, setup consultants, VC funds, banks)
- Deciding whether a partnership is worth pursuing before investing outreach time
- Re-scoring an existing partner relationship that has gone quiet or under-delivered
- Quarterly partner-pipeline review to prioritise the highest-overlap targets

## Inputs needed
**Required**
- Partner category, or a named partner candidate (use a reference code if anonymising)
- What the partner offers — their core service or product
- Their client base — entity types, revenue band, lifecycle stage, volume if known

**Optional**
- How the candidate was sourced (inbound, referral, event, team suggestion)
- Existing accounting/tax relationships the partner already has (incumbent or in-house)
- Geography focus (which emirates, which free zones, GCC reach)
- Any prior contact history with Finanshels
- Decision-maker name and title

## Workflow
### Step 1 — Classify the partner
Place the candidate into a UAE partner category using `references/partner-categories.md`. If they span categories, pick the primary one and note the secondary. Categories: free zone authorities, company-formation / business-setup consultants, law firms, banks & neobanks, VC funds & accelerators, fintech/SaaS platforms (POS, payroll, e-commerce), audit firms needing accounting overflow.

### Step 2 — Assess client overlap
Compare the partner's client base to Finanshels' ICP (UAE-incorporated startups & SMEs, AED 0–50M revenue, mainland and free zone). Score overlap: High (most clients are ICP), Medium (a meaningful segment), Low (little overlap). Note the lifecycle moment the partner touches — formation, banking, fundraising, scaling — since that signals when a referral is natural.

### Step 3 — Assess mutual value
State plainly what Finanshels gains and what the partner gains. A partnership only works if the partner can answer "what's in it for me and my clients". Identify the partner's incentive type (revenue share, better client outcomes, a gap they cannot serve, stickier clients) — but do not set rates.

### Step 4 — Estimate referral volume potential
Estimate annual referral volume as a band: Low (<10/yr), Medium (10–40/yr), High (>40/yr). Base it on the partner's client throughput and how often their clients need accounting/tax — never invent a precise number.

### Step 5 — Conflict check
Flag conflicts: does the partner offer competing accounting/tax services in-house, have an exclusive incumbent, or serve a segment that conflicts with an existing Finanshels partner? Mark as Clear, Caution, or Conflict and explain.

### Step 6 — Assign partner tier and model
Combine overlap, mutual value, volume, and conflict into a tier (Tier 1 strategic / Tier 2 active / Tier 3 opportunistic / Pass). Recommend a partnership model: referral, co-marketing, white-label / embedded, or reseller.

### Step 7 — Draft the outreach angle
Write a 2–3 sentence partner-first outreach angle leading with the partner's benefit, anchored to one proof point and the partner-facing tagline "7,000+ businesses. One finance infrastructure."

## Output format
```
PARTNER PROSPECT PROFILE — [partner name or ref code]
Date: [date]   Prepared by: [team member]   For: [partnerships review]

1. CLASSIFICATION
   Category: [category]   Secondary: [if any]
   What they offer: [one line]
   Client base: [entity types, revenue band, stage, volume]

2. SCORING
   Client overlap:        [High / Medium / Low] — [rationale]
   Mutual value:          [High / Medium / Low] — Finanshels gains: [...] Partner gains: [...]
   Referral volume:       [Low / Medium / High band] — [basis]
   Conflict check:        [Clear / Caution / Conflict] — [detail]

3. RECOMMENDATION
   Partner tier:          [Tier 1 / Tier 2 / Tier 3 / Pass]
   Recommended model:     [Referral / Co-marketing / White-label / Reseller]
   Partner incentive type: [revenue share / client outcomes / capability gap] — rate TBD by management

4. OUTREACH ANGLE
   [2-3 sentence partner-first opener]

5. NEXT STEP
   [concrete action — e.g. "warm intro via X", "send partner-pitch-builder output"]
```

## Quality checklist
- [ ] Partner placed in a category from `references/partner-categories.md`
- [ ] Client overlap assessed against the AED 0–50M UAE SME ICP, not assumed
- [ ] Mutual value states the partner's benefit explicitly, not just Finanshels'
- [ ] Referral volume given as a band with a stated basis, never an invented exact number
- [ ] Conflict check completed and labelled Clear / Caution / Conflict
- [ ] Partner tier and model are consistent with the scores above
- [ ] No commission or referral rate stated — left for management
- [ ] Outreach angle leads with the partner's benefit and uses one approved proof point
- [ ] No invented partner names, client names, or numbers used
- [ ] Output marked as draft for partnerships-team review
- [ ] UAE jurisdiction only — no foreign-tax references
- [ ] Next step is concrete and assignable

## Examples
**Example 1** "Evaluate a Dubai business-setup consultant who does ~300 free zone formations a year as a referral partner."
**Example 2** "Should we partner with a UAE neobank that onboards early-stage startups for SME current accounts?"
**Example 3** "Score a VC accelerator with 25 portfolio companies as a channel partner — most are pre-revenue UAE tech startups."

## Guardrails
- UAE jurisdiction only — never reference IRS, US states, UK/EU tax regimes, or CPE.
- Output is professional work product — a Finanshels partnerships team member must review it before any partner is approached.
- AI does not set or confirm commission, referral, or revenue-share rates — mark those fields for management completion.
- Never invent Finanshels credentials, partner names, client names, case studies, or numbers beyond the approved proof points.
- Treat all partner and client data as confidential — never use real identifiers in examples; use reference codes.
- Verify any tax rate, threshold, or deadline referenced against current FTA guidance before relying on it.

## Reference
See `references/partner-categories.md` for the UAE partner-category map.
See ../_shared/finanshels-context.md for UAE tax facts, rates, and deadlines.
See the `master-brand` skill for positioning, voice, proof points, and brand colours.
