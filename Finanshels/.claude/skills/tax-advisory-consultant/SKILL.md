---
name: tax-advisory-consultant
description: Use when a Finanshels team member needs to analyze a prospect or existing client's UAE tax situation and produce a sales-ready tax optimization plan. Triggers include: onboarding a new client, pre-sales discovery, client asking about CT or VAT exposure, reviewing entity structure (mainland vs free zone), or preparing a strategy meeting agenda. Produces a structured tax analysis covering CT registration status, VAT position, QFZP eligibility, Small Business Relief applicability, and concrete optimization recommendations.
---

# Tax Advisory Consultant

Analyzes a UAE client or prospect's tax situation and produces a sales-ready, advisor-reviewed tax optimization plan covering Corporate Tax, VAT, and structural considerations.

## When to use

- A prospect asks: "How much CT will we owe?" or "Are we better off as a free zone entity?"
- Pre-sales discovery: you have basic financials and want a structured analysis before a strategy call
- Existing client review: annual tax health-check or triggered by a revenue milestone
- Entity restructuring enquiry (mainland → free zone or adding a subsidiary)
- Client mentions they have not yet registered for CT or VAT and you need to assess urgency
- Preparing talking points or a written strategy memo for a client meeting

## Inputs needed

**Required**
- Entity name (or working title) and licence type (mainland DED / free zone — which free zone)
- Estimated annual revenue (AED) for the current or most recent financial year
- Nature of business / industry (trading, services, tech, manufacturing, etc.)
- Financial year-end date (e.g., 31 Dec, 30 June)
- CT registration status: registered / not yet registered / unsure
- VAT registration status: registered / not yet registered / not required

**Optional**
- Breakdown of revenue by activity type (qualifying vs non-qualifying if free zone)
- Existence of related-party / intercompany transactions
- Number of employees and payroll AED (substance indicators)
- Current accounting standards in use (IFRS / IFRS for SMEs / cash basis)
- Whether audited financials are prepared
- Prior-year CT or VAT issues / FTA correspondence

## Workflow

### Step 1 — Establish the entity profile
1. Confirm jurisdiction: mainland (DED) or free zone (identify the specific free zone authority — DIFC, ADGM, JAFZA, DMCC, etc.).
2. Confirm financial year-end. Determine which CT tax period the client is currently in and when the first CT return is due (9 months after financial year-end).
3. Flag if the entity has not registered for CT — note that registration is mandatory via EmaraTax; late registration attracts administrative penalties.

### Step 2 — Corporate Tax exposure assessment
1. Apply the tiered rate:
   - Taxable income ≤ AED 375,000 → 0%
   - Taxable income > AED 375,000 → 9% on the excess
2. Check Small Business Relief eligibility: revenue ≤ AED 3M for tax periods ending on or before 31 Dec 2026 → client can elect to be treated as having no taxable income. Flag the sunset date — this relief does not continue indefinitely.
3. For free zone entities: assess QFZP eligibility using the four conditions:
   - (a) Qualifying activities generating qualifying income
   - (b) Adequate substance in the free zone (employees, premises, decision-making)
   - (c) De minimis non-qualifying revenue threshold met (≤ 5% of total revenue or AED 5M, whichever is lower — confirm current FTA guidance)
   - (d) Audited financial statements prepared
   If all four are met: 0% on qualifying income, 9% on non-qualifying income.
   If conditions are borderline: flag risk and recommend a formal QFZP eligibility review.
4. Check for natural-person businesses: if the client is a sole trader / individual, CT applies if business turnover > AED 1M per calendar year.
5. Transfer pricing flag: if the entity has related-party transactions (group companies, loans, management fees, IP licenses), note that the arm's-length principle applies and a disclosure form is required with the CT return. Above prescribed thresholds, a master file / local file is needed.

### Step 3 — VAT position assessment
1. Check mandatory registration threshold: taxable supplies > AED 375,000 in any trailing 12-month period or expected in the next 30 days.
2. Check voluntary registration threshold: taxable supplies or deductible expenses > AED 187,500.
3. Determine supply classification: standard-rated (5%), zero-rated (exports, certain education/healthcare), or exempt (certain financial services, bare land, local passenger transport). Mixed-supply businesses have partial-recovery complexity.
4. Review filing frequency: quarterly or monthly — confirm via EmaraTax registration status.
5. Due date reminder: VAT returns and payments are due by the 28th of the month following the tax period.

### Step 4 — Compliance gap analysis
Run through this checklist against the client's known status:

| Obligation | Status | Priority |
|---|---|---|
| CT registration on EmaraTax | ✓ / ✗ / Unknown | High if not done |
| First CT return filed or scheduled | ✓ / ✗ / Upcoming | High |
| VAT registration (if threshold met) | ✓ / ✗ | High |
| VAT returns current (no overdue) | ✓ / ✗ | High |
| Audited financials (if QFZP or revenue > AED 50M) | ✓ / ✗ | Medium/High |
| UBO register filed with registrar | ✓ / ✗ | Medium |
| Record retention (7 years) policy in place | ✓ / ✗ | Medium |
| Transfer pricing disclosure (if applicable) | ✓ / ✗ | High if RP txns exist |

### Step 5 — Optimization recommendations
Generate 3–6 concrete, prioritized recommendations. Each recommendation must include:
- What to do
- Why it matters (tax/compliance benefit)
- Estimated effort (low / medium / high)
- Finanshels service that delivers it

Examples of recommendation types (choose relevant ones):
- Elect Small Business Relief before the 31 Dec 2026 sunset if eligible
- Register for CT immediately to avoid penalties
- Conduct a formal QFZP eligibility review before filing
- Implement arm's-length documentation for intercompany transactions
- Switch to audited financials to protect QFZP status
- Restructure revenue streams so qualifying income proportion stays above de minimis
- Register for VAT voluntarily to reclaim input tax on start-up costs
- Align financial year-end to optimize CT filing timing

### Step 6 — Package as a sales-ready strategy memo
Use the template at `templates/tax-strategy-template.md`. The memo should be:
- 1–2 pages max
- Written to the client (second person)
- Lead with the headline finding (e.g., "Your current structure leaves AED X of tax savings on the table" or "You are not yet registered for CT — here is what to do this week")
- End with a clear call to action and list of Finanshels services recommended

## Output format

```
TAX STRATEGY MEMO — [Client / Entity Name]
Prepared by: Finanshels | Date: [Date]

HEADLINE FINDING
[1-2 sentences: the single most important thing the client needs to know]

ENTITY SNAPSHOT
- Licence type & free zone / mainland
- Financial year-end
- Revenue (AED, estimated)
- CT registration status
- VAT registration status

CORPORATE TAX ANALYSIS
- Applicable rate / relief
- QFZP status (if free zone)
- Transfer pricing flag (if applicable)
- First return due date

VAT ANALYSIS
- Registration status vs threshold
- Supply classification summary
- Next return due date

COMPLIANCE GAP SUMMARY
[Table: Obligation | Status | Priority]

RECOMMENDATIONS (prioritized)
1. [Action] — [Why] — [Finanshels service]
2. ...

NEXT STEPS
- [Immediate action, this week]
- [Short-term, this quarter]
- [Book a strategy call: contact@finanshels.com]

IMPORTANT: This memo is a professional work product prepared by Finanshels for internal review. It is not final tax advice. All figures and deadlines should be confirmed against current FTA guidance before client delivery.
```

## Quality checklist

- [ ] CT rate applied correctly (0% / 9% tiers, AED 375,000 threshold)
- [ ] Small Business Relief sunset date (31 Dec 2026) mentioned where eligible
- [ ] QFZP analysis covers all four eligibility conditions if entity is in a free zone
- [ ] VAT thresholds stated in AED (375,000 mandatory, 187,500 voluntary)
- [ ] VAT return due date (28th of following month) included
- [ ] Transfer pricing flagged if related-party transactions exist
- [ ] CT return deadline stated as 9 months after financial year-end
- [ ] Record retention (7 years) noted
- [ ] No IRS / US state / CPE references anywhere
- [ ] Recommendations tied to named Finanshels services
- [ ] Memo ends with disclaimer that this is work product, not final advice
- [ ] Rates confirmed against current FTA guidance (instruction to verify included)

## Examples

**Example 1**
"We have a Dubai mainland trading LLC, AED 4M revenue, financial year ending 31 December. We're registered for VAT but haven't done CT yet. What should we know?"

**Example 2**
"Our DMCC free zone entity runs a SaaS platform. Revenue is AED 2.8M, all from outside the UAE. Are we a QFZP? What do we need to have in place?"

**Example 3**
"A client is a professional services firm in Abu Dhabi mainland, AED 600K revenue, sole-practitioner setup. They've asked whether they even need to register for CT or VAT."

## Guardrails

- UAE jurisdiction only. No US, UK, EU tax references.
- All output is a professional work product to be reviewed by a qualified Finanshels team member before being shared with any client.
- Rates and deadlines must be verified against current FTA guidance — cite the figure and flag the need to verify.
- Never include real client names, TRNs, or financial data in examples or templates.
- Do not guarantee tax outcomes — use language like "may be eligible", "subject to meeting the conditions", "confirm with the FTA".

## Reference

See ../_shared/finanshels-context.md for UAE tax facts, rates, and deadlines.
