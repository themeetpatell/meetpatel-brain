---
name: deal-review-coach
description: Use when a Finanshels sales team member or manager wants to review an open deal or a whole pipeline and decide the next best action. Triggers include: "review my pipeline", "is this deal healthy", "what should I do next on this deal", "which deals are at risk", "help me prioritise my open opportunities", "this deal feels stalled". Produces a deal-health scorecard, a flagged list of stalled or at-risk deals, a ranked next-action list, and a pipeline summary with where to spend time.
---

# Deal Review Coach

Reviews a single open deal or an entire pipeline against a structured health rubric and tells the Finanshels sales team exactly where to spend time and what to do next.

## When to use

- A weekly or monthly pipeline review needs a structured, honest assessment
- A specific deal feels stuck and you need to diagnose why and what to do
- A manager is coaching a rep on prioritisation across many open deals
- Forecasting: deciding which deals are real and which are wishful
- A deal has had no movement and you need to decide push, pause, or close-lost
- Onboarding a new rep on how Finanshels reads deal health

## Inputs needed

**Required**
- For a single deal: stage, estimated value band, days since last contact, prospect signals (engagement, fit, urgency, decision-maker access)
- For a pipeline: a list of deals each with stage, value band, last-contact date, and any notes

**Optional**
- Prospect profile per deal: entity type, revenue band, industry, compliance status
- Objections raised, competitor presence
- The next step currently planned (if any)
- The rep's available selling capacity this period
- Target close dates or quota context

## Workflow

### Step 1 — Confirm the deal data
Capture stage, value band, last-contact date, and signals for each deal. Mark unknowns explicitly — a missing decision-maker is a risk, not a neutral. Do not invent value figures; use bands.

### Step 2 — Score deal health
Score each deal on the four dimensions in `references/deal-health-rubric.md` — Engagement, Fit, Urgency, Decision Access — 1-5 each. Sum to a /20 health score and convert to a band: Healthy, Watch, At Risk, Stalled.

### Step 3 — Check stage fit
Compare the health score and the most recent activity against the deal's stated stage. Flag deals that are parked in a stage they have outgrown (e.g. "proposal sent" 25 days ago, no reply — that is not a live proposal stage, it is At Risk) and deals advanced on the board without evidence.

### Step 4 — Flag risks and stalled deals
List every deal that is At Risk or Stalled with the specific reason: gone quiet, no decision-maker access, no real urgency, objection unresolved, competitor winning, or scope drift. Be honest — a clean pipeline is more useful than an optimistic one.

### Step 5 — Prioritise where to spend time
Rank deals by a simple lens: expected value (value band x health) and effort-to-advance. Identify the few deals worth real focus, the deals that need one decisive action, and the deals to close-lost so they stop consuming attention.

### Step 6 — Recommend a concrete next action per deal
For each live deal, give one specific next action with an owner and a date — not "follow up". Examples: "book a 15-min call with the founder to confirm decision timeline", "run the objection-handling-playbook on the price pushback", "send the deadline-driven follow-up sequence", "build a competitive-battlecard — a setup consultant is in the mix". Route to sibling skills where relevant.

### Step 7 — Summarise the pipeline
Produce the pipeline summary: total deals, value by health band, count of at-risk and stalled, and the top three actions for the period.

## Output format

```
DEAL REVIEW — [Single deal / Pipeline] — [Rep / Team]
Date: [Date] | Reviewed by: [Name]

--- DEAL-HEALTH SCORECARD ---

| Deal (ref) | Stage | Value band | Last contact | Eng | Fit | Urg | DM | Health /20 | Band |
|---|---|---|---|---|---|---|---|---|---|
| [ref] | [stage] | AED [band] | [days ago] | /5 | /5 | /5 | /5 | /20 | [Healthy/Watch/At Risk/Stalled] |
| ... |

HEALTH BANDS: Healthy 16-20 | Watch 11-15 | At Risk 6-10 | Stalled <=5

--- RISK & STALLED FLAGS ---
- [Deal ref]: [Band] — [specific reason] — [recommended call: push / decisive action / close-lost]
- ...

--- RANKED NEXT-ACTION LIST ---
1. [Deal ref] — Priority: High — Next action: [concrete action] — Owner: [Name] — By: [Date]
2. [Deal ref] — Priority: [High/Med/Low] — Next action: [...] — Owner — By
... (route to sibling skills where useful: objection-handling-playbook,
    sales-followup-sequencer, competitive-battlecard, discovery-call-guide,
    proposal-generator)

--- PIPELINE SUMMARY ---
- Total open deals: [X]
- Value by band: Healthy AED [X] | Watch AED [X] | At Risk AED [X] | Stalled AED [X]
- At Risk / Stalled count: [X] — recommend close-lost: [X]
- Top 3 focus actions this period:
  1. [...]
  2. [...]
  3. [...]
- Coaching note for the rep: [one honest observation]

NOTES
- Pricing: all value figures are bands for internal forecasting — account manager owns actual fees.
```

## Quality checklist

- [ ] Every deal scored on all four dimensions — no blanks
- [ ] Health score totalled and banded correctly
- [ ] Stage fit checked — deals parked in an outgrown stage are flagged
- [ ] Every At Risk / Stalled deal has a specific named reason, not "gone quiet" alone
- [ ] Each live deal has one concrete next action with owner and date
- [ ] Next actions route to sibling skills where relevant
- [ ] Deals worth closing-lost are explicitly recommended, not left to linger
- [ ] Pipeline summary includes value by health band and top three actions
- [ ] Assessment is honest — no optimistic inflation of stalled deals
- [ ] A coaching note for the rep is included
- [ ] Value figures are bands for internal forecasting only
- [ ] No real client identifiers used in examples

## Examples

**Example 1** "Review this deal: proposal sent to a free zone consultancy 22 days ago, value around AED 60K/year, one reply early on then silence, founder never joined the calls. What should I do?"

**Example 2** "Here's my pipeline of 9 open deals with stages, value bands and last-contact dates. Score them, flag what's at risk, and tell me where to spend my week."

**Example 3** "This mainland trading-company deal feels stuck — they were keen after discovery, then a competitor setup consultant got involved. Assess deal health and recommend next steps."

## Guardrails

- UAE jurisdiction only — never reference IRS, US states, UK/EU tax, or CPE.
- The review is an internal sales document — health scores, bands, and value figures stay internal and must never be shared with the prospect.
- Outputs are professional work product — a Finanshels team member or manager must review and own them before they drive forecasting or commercial decisions.
- AI does not set or confirm pricing — all deal values are bands for internal forecasting; the account manager owns actual fees.
- Never invent Finanshels credentials, client names, case studies, testimonials, or numbers beyond the approved proof points (7,000+ businesses, 150+ qualified accountants).
- Be honest, not optimistic — do not inflate stalled deals to flatter the pipeline.
- Treat all prospect data as confidential — never use real client identifiers in examples.
- Verify any CT/VAT deadline used as an urgency signal against current FTA guidance.

## Reference

See ../_shared/finanshels-context.md for UAE tax facts, rates, and deadlines.
See `references/deal-health-rubric.md` for the deal-health scoring rubric and stage-fit guide.
See the `prospect-qualification` skill for initial ICP-fit scoring of new leads.
See the `objection-handling-playbook`, `sales-followup-sequencer`, and `competitive-battlecard` skills for the next actions this skill routes to.
See the `master-brand` skill for positioning, voice, proof points, and brand colours.
