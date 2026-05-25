---
name: case-study-writer
description: Use when a Finanshels marketer needs to turn a client engagement into a publishable case study or success story, anonymised by default. Triggers include: "write a case study from this client engagement", "turn this onboarding win into a success story", "draft a case study about the CT-registration rescue we did", "we need a customer story for the website". Produces a full case study — headline, at-a-glance stats box, Challenge → Solution → Result narrative, a pull quote, and a CTA.
---

# Case Study Writer

Turns a real Finanshels client engagement into a publishable, brand-aligned case study using the Challenge → Solution → Result structure — anonymised unless the client has approved attribution.

## When to use
- Converting a successful engagement into a marketing asset for the website or sales deck.
- Producing proof content for a campaign (see the `campaign-planner` skill).
- Creating a segment-specific success story (free zone QFZP, AED 0–3M startup, scaling SME).
- Refreshing the case-study library with a recent win.
- Building a sales-enablement story reps can send to similar prospects.

## Inputs needed
**Required**
- Client type, anonymised (e.g. "a Dubai free zone e-commerce startup", "an AED 12M mainland services firm").
- Starting situation / the challenge (the problem, pain, or risk the client faced).
- What Finanshels did (services delivered, approach, what changed).
- Measurable outcomes (time saved, penalties avoided, compliance achieved, hours freed).

**Optional**
- An approved client quote and the name/title cleared for attribution.
- Whether the client has approved being named (default: keep anonymous).
- The target reader segment for the finished story.
- The CTA to feature and where the case study will be published.

## Workflow
### Step 1 — Confirm consent and anonymisation level
Default to fully anonymised — describe the client by type, not name. Only name the client, an individual, or include a quote if explicit approval is recorded. Never use real client identifiers without it. Note the chosen level at the top of the draft.

### Step 2 — Frame the challenge
Write the Challenge section: the situation before Finanshels, in the client's terms. Make the stakes concrete and relatable to similar founders (a looming FTA deadline, messy books before a fundraise, penalty exposure). Lead with WHY this mattered — do not open with what Finanshels does.

### Step 3 — Tell the solution
Write the Solution section: what Finanshels did, the services involved, and the approach. Show the how, not a feature list. Reference the AI-native delivery model where relevant. Keep it founder-readable — translate any tax term.

### Step 4 — Quantify the result
Write the Result section around the measurable outcomes. Use only real numbers the client supplied — never invent or round up. Frame results as the client's win. Where a figure is sensitive, describe the outcome qualitatively rather than fabricating a number.

### Step 5 — Build the at-a-glance stats box and headline
Using `templates/case-study-template.md`, write a benefit-led headline (names the outcome, not the service) and a 3-4 metric stats box (client profile + 2-3 result metrics). Pull the strongest result into the headline.

### Step 6 — Place the pull quote and CTA
Insert the approved client quote as a pull quote — or, if none is approved, a one-line summary of the outcome with no fabricated attribution. Anchor one approved Finanshels proof point. End with one clear CTA inviting similar businesses to take the next step.

### Step 7 — Brand and compliance pass
Check: anonymisation honoured, no invented numbers/quotes/clients, voice founder-first and WHY → WHAT, one proof point, nothing reading as a guarantee, brand colours noted. Add the review checkbox.

## Output format
```
# Case Study — [Headline: outcome-led]
Anonymisation: fully anonymous / named with approval
Segment: [target reader]

## At-a-glance
| | |
|---|---|
| Client | [type — anonymised] |
| Challenge | [one line] |
| Services | [Finanshels services used] |
| Result | [headline metric] |

## The Challenge
[2-4 short paragraphs — the situation before, WHY it mattered]

## The Solution
[2-4 short paragraphs — what Finanshels did and how]

## The Result
[2-3 short paragraphs — measurable outcomes, client's win]
- [Result metric 1]
- [Result metric 2]
- [Result metric 3]

> "[Approved client quote]" — [Name, Title — only if attribution approved]

## Why it matters
[1-2 sentences + one approved Finanshels proof point]

## CTA
[One clear next step for similar businesses]
→ [Button label] (#F16610)

## Next steps
- [ ] Finanshels team review
- [ ] Client consent confirmed for anonymisation level / quote
- [ ] Tax facts verified against current FTA guidance
```

## Quality checklist
- [ ] Anonymisation level confirmed; client not named without recorded consent.
- [ ] No quote used unless explicitly approved — no fabricated attribution.
- [ ] Challenge → Solution → Result structure followed.
- [ ] Challenge leads WHY → WHAT and is relatable to similar founders.
- [ ] Solution shows the how, not a feature list; tax terms translated.
- [ ] Every result metric is a real number the client supplied — none invented or inflated.
- [ ] Headline is outcome-led, not service-led.
- [ ] At-a-glance box has client profile + 2-3 result metrics.
- [ ] One approved Finanshels proof point anchored.
- [ ] No language implying a guarantee of outcomes.
- [ ] One clear CTA for similar businesses; button in brand orange #F16610.
- [ ] Ends with a review / consent / next-steps block.

## Examples
**Example 1** "Write a case study from the engagement where we rescued a free zone startup's Corporate Tax registration before its deadline."
**Example 2** "Turn the bookkeeping cleanup we did for an AED 15M mainland firm before its fundraise into a success story."
**Example 3** "Draft an anonymised case study about taking VAT filing fully off a founder's plate for a scaling e-commerce business."

## Guardrails
- UAE jurisdiction only — never reference IRS, US states, UK/EU tax, or CPE.
- The case study is professional work product — a Finanshels team member must review before publication.
- Client consent is mandatory — anonymise by default; never name a client or use a quote without recorded approval.
- AI does not set or confirm pricing — describe value, never state fees; leave AED figures for account-manager completion.
- Never invent Finanshels credentials, client names, case studies, testimonials, or numbers beyond the approved proof points.
- Treat all prospect/client data as confidential; never use real client identifiers in examples.
- Verify all tax rates, thresholds, and deadlines against current FTA guidance before relying on them.

## Reference
See `templates/case-study-template.md` for the fillable case-study layout and stats box.
See ../_shared/finanshels-context.md for UAE tax facts, rates, and deadlines.
See the `master-brand` skill for positioning, voice, proof points, and brand colours.
See the `campaign-planner` skill when a case study is being produced as proof content for a campaign.
