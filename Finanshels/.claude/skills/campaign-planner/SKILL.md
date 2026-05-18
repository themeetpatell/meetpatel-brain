---
name: campaign-planner
description: Use when a Finanshels marketer needs to plan a multi-channel marketing campaign — a Corporate Tax deadline awareness push, a free-zone VAT campaign, a new-service launch, or a seasonal lead-generation drive. Triggers include: "plan a campaign for the CT filing deadline", "we need a VAT campaign for free zone clients", "build a launch plan for outsourced CFO services", "map the channels for a Small Business Relief push". Produces a structured campaign brief with objective, audience, core message, a channel-mix table, a week-by-week calendar, KPIs, and budget allocation.
---

# Campaign Planner

Turns a marketing goal into a structured, multi-channel campaign brief that the Finanshels team can execute and measure.

## When to use
- Planning a seasonal compliance push (CT return season, VAT quarter-end, registration deadlines).
- Launching a new or repositioned service (outsourced CFO, audit support, company formation).
- Running a segment-specific drive (free zone QFZP entities, AED 0–3M Small Business Relief firms).
- Building an always-on lead-generation campaign tied to a lead magnet or webinar.
- Coordinating content, paid ads, email, and events around a single trigger or deadline.

## Inputs needed
**Required**
- Campaign goal (awareness, lead generation, registration, retention, reactivation).
- Target segment (ICP slice — entity type, revenue band, compliance status).
- Trigger / timing (a deadline, a regulatory change, a fiscal-year event, an evergreen window).
- Channels available (organic social, paid search, paid social, email, webinar, partnerships, PR).

**Optional**
- Budget band (low / medium / high — actual AED figures left for account-manager sign-off).
- Existing assets (lead magnets, case studies, blog content) that can be reused.
- Sales-team capacity to follow up leads.
- Past campaign benchmarks for the same segment.

## Workflow
### Step 1 — Define objective and KPI
State one primary objective in a single sentence and attach one measurable KPI (e.g. "Generate 120 CT-registration enquiries from free zone SMEs before the 30 Sep deadline"). Add 1-2 secondary metrics. Avoid vanity metrics — tie everything to pipeline or compliance outcomes.

### Step 2 — Sharpen the audience
Narrow the segment to a single, recognisable persona: their entity type (mainland DED / free zone), revenue band, role (founder vs finance lead), and the specific compliance pain or deadline they face. Note what they currently believe and what they need to believe to act.

### Step 3 — Build the core message and offer
Write the campaign's one-line WHY → WHAT message (lead with why the deadline or change matters to them, then what Finanshels does). Define the offer / hook (free assessment, deadline checklist, discovery call) and the urgency device (a real FTA deadline — never a fabricated one). Anchor one approved proof point.

### Step 4 — Plan the channel mix and sequencing
Use `templates/campaign-brief-template.md` and the channel matrix inside it to assign each channel a role (reach / nurture / convert), an asset, a cadence, and an owner. Sequence channels into phases: tease → educate → convert → last-call. For ad copy delegate to the `ad-copy-generator` skill; for organic content map to `content-planner-tax` and `thought-leadership-writer`.

### Step 5 — Build the week-by-week calendar
Lay out a calendar from kickoff to the trigger date (and a short post-deadline tail). Each row = a week with channel activity, asset due, and owner. Front-load education, back-load conversion and last-call urgency.

### Step 6 — Set the measurement plan
Define how each KPI is tracked (UTM tags, form source, CRM stage), the review cadence (weekly check-in, end-of-campaign retro), and a mid-campaign decision point to reallocate budget toward the best-performing channel.

### Step 7 — Allocate budget
Split the budget band across channels as percentages and rationale. Leave actual AED amounts as `[AED — account manager to confirm]`. Flag the largest bet and the cheapest test.

## Output format
```
# Campaign Brief — [Campaign Name]

## 1. Objective & KPIs
- Primary objective: [one sentence]
- Primary KPI: [metric + target + deadline]
- Secondary metrics: [1-2]

## 2. Audience
- Persona: [entity type, revenue band, role]
- Current belief → desired belief: [from] → [to]
- Core pain / trigger: [deadline or regulatory change]

## 3. Core Message & Offer
- Campaign message (WHY → WHAT): [one line]
- Offer / hook: [...]
- Urgency device: [real FTA deadline]
- Proof point anchored: [7,000+ businesses / 150+ accountants / named client]

## 4. Channel Plan
| Channel | Role | Asset | Cadence | Owner |
|---------|------|-------|---------|-------|
| ... | reach/nurture/convert | ... | ... | ... |

## 5. Week-by-Week Calendar
| Week | Dates | Channel activity | Asset due | Owner |
|------|-------|------------------|-----------|-------|
| ... | ... | ... | ... | ... |

## 6. Measurement Plan
- Tracking: [UTMs, form sources, CRM stages]
- Review cadence: [...]
- Mid-campaign decision point: [date + trigger to reallocate]

## 7. Budget Allocation
| Channel | % of budget | Rationale | AED |
|---------|-------------|-----------|-----|
| ... | ...% | ... | [AED — account manager to confirm] |

## Next steps
- [ ] Finanshels team review and sign-off
- [ ] Account manager confirms budget figures
```

## Quality checklist
- [ ] One clear primary objective with a measurable, time-bound KPI.
- [ ] Audience narrowed to a single recognisable UAE persona.
- [ ] Core message leads WHY → WHAT and is founder-first ("you/your").
- [ ] At least one approved proof point anchored.
- [ ] Urgency device uses a real FTA deadline, verified against current guidance.
- [ ] Every channel has a role, asset, cadence, and named owner.
- [ ] Calendar runs from kickoff through the trigger date with a post-deadline tail.
- [ ] Measurement plan specifies tracking and a mid-campaign review point.
- [ ] Budget split as percentages; AED figures left for account-manager sign-off.
- [ ] No invented clients, numbers, or testimonials.
- [ ] Plain English, no corporate filler ("synergies", "leverage", "holistic").
- [ ] Ends with a clear next-steps / review block.

## Examples
**Example 1** "Plan a campaign to drive Corporate Tax return filings from free zone SMEs before the September deadline."
**Example 2** "We're launching outsourced CFO services for AED 5–50M companies — build the launch campaign plan."
**Example 3** "Build a Q1 awareness campaign about Small Business Relief for firms under AED 3M revenue."

## Guardrails
- UAE jurisdiction only — never reference IRS, US states, UK/EU tax, or CPE.
- This brief is professional work product — a Finanshels team member must review it before execution or external use.
- AI does not set or confirm pricing — leave all AED budget and fee fields marked for account-manager completion.
- Never invent Finanshels credentials, client names, case studies, testimonials, or numbers beyond the approved proof points.
- Treat all prospect/client data as confidential; never use real client identifiers in examples.
- Verify all tax rates, thresholds, and deadlines against current FTA guidance before relying on them.

## Reference
See `templates/campaign-brief-template.md` for the fillable brief and channel matrix.
See ../_shared/finanshels-context.md for UAE tax facts, rates, and deadlines.
See the `master-brand` skill for positioning, voice, proof points, and brand colours.
