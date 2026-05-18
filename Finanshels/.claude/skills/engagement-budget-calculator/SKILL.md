---
name: engagement-budget-calculator
description: Use when a Finanshels team member needs to scope, price, or propose a new client engagement or renew an existing one. Accepts an engagement type (bookkeeping, VAT filing, CT return, audit support, or CFO retainer), client profile, and complexity inputs — then produces a structured proposal budget with estimated hours, AED fees, timeline, and staffing assumptions. Ideal for pre-sales scoping, renewals, or internal capacity checks before committing to a client.
---

# Engagement Budget Calculator

Produces a detailed proposal budget — hours, AED fees, timeline, staffing — for any Finanshels service engagement.

## When to use

- A prospect or existing client has asked for a quote or scope-of-work
- A team lead needs to check whether an engagement is commercially viable before accepting
- Renewing or restructuring an existing engagement (scope creep review)
- Management wants a portfolio view of estimated revenue vs. hours across pending proposals
- Internally verifying that a fixed-fee quote covers actual expected effort

## Inputs needed

**Required**
- `engagement_type`: One of — `bookkeeping`, `vat_filing`, `ct_return`, `audit_support`, `cfo_retainer`
- `client_name_or_code`: Internal reference (never a real public name in deliverables)
- `entity_type`: Mainland LLC / Free Zone entity / Branch / Sole Establishment
- `annual_revenue_aed`: Approximate annual revenue in AED

**Optional**
- `transaction_volume`: Average monthly bank/journal transactions (Low < 100 / Medium 100–500 / High > 500)
- `number_of_entities`: If the engagement spans multiple legal entities
- `vat_registered`: Yes / No / Pending
- `ct_registered`: Yes / No / Pending
- `complexity_flags`: Any of — `multi-currency`, `related-party transactions`, `free-zone QFZP`, `payroll >20 staff`, `audit-required`, `prior-year catch-up`
- `preferred_delivery_timeline`: e.g. "VAT return due 28 Jul 2026"
- `existing_accounting_system`: e.g. Xero, QuickBooks, Zoho Books, spreadsheets/none
- `notes`: Anything else relevant (e.g. "client has 3 years of unfiled returns")

## Workflow

1. **Classify engagement tier**
   Map `annual_revenue_aed` and `transaction_volume` to a size tier:
   - Tier 1 — Micro: Revenue ≤ AED 500K, Low volume
   - Tier 2 — Small: Revenue AED 500K–3M, Low–Medium volume
   - Tier 3 — Mid: Revenue AED 3M–15M, Medium volume
   - Tier 4 — Growth: Revenue AED 15M–50M, Medium–High volume
   - Tier 5 — Enterprise: Revenue > AED 50M (flag for senior review; audited financials mandatory above AED 50M)

2. **Apply base hour ranges by engagement type**
   Use the reference table in `workflows/budget-calculation.md` to pull the base hours for the tier and engagement type. These are starting estimates — step 3 adjusts them.

3. **Apply complexity multipliers**
   For each `complexity_flag` present, add the incremental hours:
   - Multi-currency ledger: +15% of base hours
   - Related-party / TP disclosure: +8 hours per entity (CT engagements)
   - QFZP qualification review: +10 hours (CT engagement)
   - Payroll > 20 staff (WPS + gratuity): +4 hours/month
   - Audit-required (revenue > AED 50M or QFZP): +20–40 hours setup
   - Prior-year catch-up (per year): +50% of base bookkeeping hours per year
   - No accounting system / spreadsheets: +20% bookkeeping hours (migration effort)

4. **Calculate AED fees**
   Multiply total hours by the applicable blended rate. Finanshels internal blended rate guidance is documented in `workflows/budget-calculation.md`. Present fees as:
   - Monthly retainer (if recurring)
   - One-off setup / onboarding fee (where applicable)
   - Per-filing fee (VAT return, CT return)
   Total fee = setup + (monthly retainer × contract months) + per-filing fees

5. **Build timeline**
   - Anchor to the UAE compliance calendar:
     - VAT returns: due 28th of month following the tax period
     - CT returns: within 9 months of financial year-end
     - CT registration: FTA deadlines based on licence-issuance month (verify on EmaraTax)
   - Identify the earliest hard deadline for the client
   - Work backward: assign kickoff date, data-gathering phase, first deliverable date, review cycle, submission date

6. **Assign staffing model**
   Recommend team composition based on tier:
   - Tier 1–2: 1 × Accountant, review by Senior Accountant
   - Tier 3: 1 × Senior Accountant + 1 × Accountant, Manager sign-off
   - Tier 4–5: Manager-led team, Director review
   Flag if total hours require >50% of one staff member's capacity (capacity risk).

7. **Draft engagement summary table**
   Produce the output described in the Output Format section.

8. **Validation check**
   Before finalising, verify:
   - Fee / hour ratio is within acceptable range (not below AED 150/hr blended)
   - All applicable UAE compliance deadlines have been captured
   - QFZP flag triggers note about audited financials requirement
   - Small Business Relief eligibility noted where revenue ≤ AED 3M

## Output format

```
ENGAGEMENT BUDGET PROPOSAL
Client code: [code]          Date: [YYYY-MM-DD]
Engagement type: [type]      Entity: [mainland/FZ/branch]
Revenue band: [AED range]    Tier: [1–5]

─────────────────────────────────────────
SCOPE SUMMARY
[2–3 sentence plain-English description of what is included]

─────────────────────────────────────────
EFFORT ESTIMATE

Phase                  Hours   Notes
──────────────────────────────────────
Onboarding / setup     XX      [e.g. system access, data migration]
Monthly bookkeeping    XX/mo   [transactions, reconciliation, reports]
VAT return prep        XX/rtn  [if applicable]
CT return              XX      [if applicable, once per year]
Management reporting   XX/mo   [if CFO retainer]
Audit support          XX      [if applicable]
──────────────────────────────────────
TOTAL HOURS            XX      [first year estimate]

─────────────────────────────────────────
FEE SCHEDULE (AED, excl. VAT)

One-off onboarding fee:         AED XX,XXX
Monthly retainer:               AED XX,XXX / month
VAT return fee (per filing):    AED X,XXX
CT return fee (annual):         AED XX,XXX
──────────────────────────────────────
Estimated Year 1 total:         AED XXX,XXX

─────────────────────────────────────────
TIMELINE

Milestone              Target date     Owner
Kickoff call           [date]          Account Manager
Data gathering done    [date]          Client
First deliverable      [date]          Finanshels
VAT filing deadline    [date]          Finanshels
CT registration by     [date]          Finanshels
Annual CT return due   [date]          Finanshels

─────────────────────────────────────────
STAFFING

Recommended team: [roles]
Capacity flag: [None / "Review — engagement consumes >50% of [name]'s bandwidth"]

─────────────────────────────────────────
ASSUMPTIONS & NOTES
- [List all assumptions made: transaction volume, filing frequency, system used]
- [Flag any complexity items that could expand scope]
- All fees quoted exclude 5% VAT.
- Rates and deadlines should be verified against current FTA guidance on EmaraTax.
```

## Quality checklist

- [ ] Engagement type and tier are correctly identified
- [ ] All `complexity_flags` provided have been reflected in the hours
- [ ] UAE compliance deadlines (VAT 28th rule, CT 9-month rule) are present where applicable
- [ ] QFZP flag triggers audited-financials note if relevant
- [ ] Small Business Relief eligibility called out where revenue ≤ AED 3M
- [ ] Fees are stated excl. VAT and the 5% VAT line is mentioned
- [ ] Staffing recommendation matches the tier
- [ ] Capacity risk flag raised if applicable
- [ ] All assumptions listed so reviewers can challenge them

## Examples

**Example 1**
> "Scope a bookkeeping and VAT filing engagement for a Dubai mainland trading LLC, AED 4M revenue, 200 transactions/month, using Xero, VAT registered."

Expected: Tier 3, Medium volume, bookkeeping retainer + quarterly VAT filing fee, 12-month timeline anchored to next VAT due date.

**Example 2**
> "Quote a Corporate Tax return engagement for a JAFZA free zone entity, AED 22M revenue, related-party transactions with a sister company in India, no current accounting system."

Expected: Tier 4, QFZP assessment hours added, TP disclosure hours added, migration-effort uplift, audited-financials note, Manager-led staffing.

**Example 3**
> "Give me a CFO retainer proposal for a SaaS startup in DIFC, AED 1.2M ARR, 3 entities (UAE + 2 offshore), multi-currency, payroll for 15 staff."

Expected: Tier 2 (per-entity revenue), multi-entity and multi-currency uplifts, monthly retainer structure, staffing recommendation includes Senior Accountant minimum.

## Guardrails

- UAE jurisdiction only. Never reference IRS, US states, or CPE.
- This output is a professional work product for internal use and proposal drafting — it must be reviewed by a qualified Finanshels team member before being shared with a client.
- Fee figures are internal estimates based on team inputs; final pricing must be approved by a manager.
- Always verify VAT and CT deadlines against current FTA guidance on EmaraTax before committing dates to a client.
- Client financial data is confidential. Never include real client names or financial figures in training examples or shared outputs.

## Reference

See `../_shared/finanshels-context.md` for UAE tax facts, rates, and deadlines.
