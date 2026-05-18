---
name: risk-assessment-tax
description: Use when a Finanshels team member needs to evaluate a client's UAE Corporate Tax and VAT position for FTA audit risk, penalty exposure, or compliance gaps. Triggers include: pre-filing review, client onboarding risk profiling, a client flagging an unusual transaction, suspected VAT under-declaration, related-party transactions requiring transfer pricing documentation, or a free zone entity's QFZP status being uncertain. Produces a structured risk score (Red / Amber / Green) with a prioritised mitigation plan.
---

# Risk Assessment — UAE Tax (CT & VAT)

Analyses a client's UAE CT and VAT position for FTA audit and penalty risk; delivers a scored risk register and a concrete mitigation plan.

## When to use

- Client onboarding: baseline risk profile before taking on engagement
- Pre-CT-return review: flag issues before filing with the FTA
- Pre-VAT-return review: identify under-declared output tax or over-claimed input tax
- Free zone entity: assess whether QFZP conditions are being met
- Related-party / connected-person transactions that may require TP documentation
- A client mentions a significant one-off transaction (asset sale, restructuring, large import)
- Following an FTA query, audit notice, or VAT refund review
- Annual compliance health-check as part of the Finanshels service

## Inputs needed

**Required**
- Client name (internal use only) and entity type (mainland LLC / free zone / branch / natural person)
- Financial year end date and relevant tax period(s) under review
- Approximate annual revenue (AED) — determines rate tier, SBR eligibility, audit-report requirement
- Brief description of business activities and main revenue streams

**Optional (but materially improves accuracy)**
- Draft or filed CT return (or trial balance / management accounts)
- Draft or filed VAT returns for the period
- List of related-party and connected-person transactions with amounts
- Free zone licence details and activity list (for QFZP assessment)
- Any prior FTA correspondence or audit history
- Details of any cross-border transactions, imports, or exports

## Workflow

1. **Gather and organise inputs**
   Confirm you have entity type, revenue, tax period, and activity description. If any are missing, ask before proceeding — a risk assessment with gaps produces misleading scores.

2. **Check structural compliance (foundation layer)**
   Verify the following basics against the shared context file:
   - Is the entity registered for CT on EmaraTax? (Mandatory for all taxable persons)
   - Is the CT return due date known? (9 months after tax period end)
   - If revenue > AED 375,000 taxable supplies in any 12-month period: is the entity VAT-registered?
   - If revenue ≤ AED 3M and tax period ends on/before 31 Dec 2026: is Small Business Relief being claimed correctly?
   - If revenue > AED 50M or entity is a QFZP: are audited financial statements in place?
   - Record-keeping: are records being retained for 7 years?

3. **CT risk factors — assess each**

   | Risk Factor | What to Check |
   |-------------|---------------|
   | **Taxable income calculation** | Deductions disallowed under CT Law (e.g. fines, non-arm's-length interest, entertainment > 50%), depreciation method, provisions |
   | **Related-party transactions** | Are related-party transactions at arm's length? Is the TP disclosure form prepared? Do volumes trigger master/local file requirements? |
   | **Free zone QFZP conditions** | Adequate substance in free zone, qualifying activities only, de minimis non-qualifying income test, audited financials, election made |
   | **Small Business Relief** | Revenue correctly calculated (all sources), election filed, no disqualifying structures |
   | **Loss relief** | Tax losses carried forward correctly, no restrictions missed |
   | **Exempt income** | Dividends/capital gains from qualifying participations — conditions met? |
   | **Registration timing** | Was CT registration completed by the FTA deadline based on licence-issuance month? Late registration = AED 10,000 penalty |
   | **Return deadline** | 9-month rule tracked correctly; penalties for late filing are significant |

4. **VAT risk factors — assess each**

   | Risk Factor | What to Check |
   |-------------|---------------|
   | **Output tax completeness** | All taxable supplies identified and rated correctly (5%, 0%, or exempt); no missed invoices |
   | **Input tax recovery** | Blocked input tax (entertainment, motor vehicles for personal use) correctly excluded; partial exemption calculation if applicable |
   | **Place of supply** | Cross-border services / imports treated correctly; reverse charge applied where required |
   | **Invoice compliance** | Tax invoices meet FTA format requirements (TRN, date, description, tax amount) |
   | **Registration threshold** | Was registration triggered on time? Retrospective registration penalties are steep |
   | **Return filing and payment** | Filed by 28th of the month following the tax period; penalties for late filing and late payment |
   | **Designated zones** | Correct treatment for supplies within and out of designated (free) zones |

5. **Score each risk factor**
   Use the scoring rubric in `./workflows/risk-scoring.md`:
   - **Green (1–3):** Low risk; current position appears compliant
   - **Amber (4–6):** Moderate risk; potential issue requiring attention
   - **Red (7–10):** High risk; likely FTA scrutiny or penalty exposure

6. **Calculate an overall risk rating**
   - Count Red, Amber, and Green scores
   - Overall: Red if any factor is Red 7+; Amber if two or more Amber; Green if all Green or one Amber

7. **Build the mitigation plan**
   For every Amber or Red finding:
   - State the specific issue
   - Recommended corrective action
   - Owner (Finanshels team member role)
   - Deadline (before next return / within 30 days / before year-end)
   - Estimated penalty exposure if not addressed (reference FTA penalty schedule; state "confirm with FTA" for exact amounts)

8. **Draft the executive summary**
   2–3 paragraph plain-English summary suitable for a partner review or client-facing discussion. State overall rating, top 3 risks, and top 3 actions.

## Output format

```
# UAE Tax Risk Assessment
**Client:** [Internal ID / initials only]
**Entity type:** [Mainland LLC / Free Zone / Branch / Natural Person]
**Tax period:** [FY end date]
**Prepared by:** [Name]
**Date:** YYYY-MM-DD
**Overall Rating:** RED / AMBER / GREEN

---

## Executive Summary
[2–3 paragraphs: overall rating rationale, top risks, top actions]

---

## Structural Compliance Check

| Item | Status | Notes |
|------|--------|-------|
| CT registration | ✓ Done / ✗ Missing / ? Unknown | |
| VAT registration | ✓ / ✗ / ? | |
| CT return deadline known | ✓ / ✗ / ? | |
| Audited financials (if required) | ✓ / ✗ / N/A | |
| Record-keeping (7 years) | ✓ / ✗ / ? | |

---

## CT Risk Register

| # | Risk Factor | Score (1–10) | RAG | Finding | Recommended Action |
|---|-------------|-------------|-----|---------|-------------------|
| 1 | Taxable income calc | | | | |
| 2 | Related-party / TP | | | | |
| 3 | Free zone QFZP | | | | |
| 4 | Small Business Relief | | | | |
| 5 | Loss relief | | | | |
| 6 | Exempt income | | | | |
| 7 | Registration timing | | | | |
| 8 | Return deadline | | | | |

---

## VAT Risk Register

| # | Risk Factor | Score (1–10) | RAG | Finding | Recommended Action |
|---|-------------|-------------|-----|---------|-------------------|
| 1 | Output tax completeness | | | | |
| 2 | Input tax recovery | | | | |
| 3 | Place of supply | | | | |
| 4 | Invoice compliance | | | | |
| 5 | Registration threshold | | | | |
| 6 | Return filing / payment | | | | |
| 7 | Designated zones | | | | |

---

## Mitigation Plan

| Priority | Finding | Action | Owner | Deadline | Est. Penalty if Unresolved |
|----------|---------|--------|-------|----------|---------------------------|
| 1 — RED | | | | | |
| 2 — RED | | | | | |
| 3 — AMBER | | | | | |

---

## Penalty Exposure Summary
**Estimated total exposure (AED):** [range or "see FTA penalty schedule — confirm amounts"]

---
*Internal work product. Verify all figures with FTA guidance before advising clients.*
```

## Quality checklist

- [ ] All 8 CT risk factors scored
- [ ] All 7 VAT risk factors scored
- [ ] Overall RAG rating derived from individual scores (not guessed)
- [ ] Every Red and Amber finding has a mitigation action, owner, and deadline
- [ ] No penalty amounts invented — FTA schedule cited or "confirm with FTA"
- [ ] QFZP section completed if entity is a free zone person
- [ ] SBR eligibility explicitly confirmed or denied
- [ ] Executive summary is free of jargon

## Examples

**Example 1 — New client onboarding**
> "We're onboarding a Dubai mainland trading LLC, AED 4M revenue, FY ending 31 Dec 2024. They have no prior FTA correspondence and we haven't seen their books yet. Run a baseline risk profile using what we know."

**Example 2 — Free zone tech startup**
> "Client is a JAFZA-registered tech company, AED 12M revenue, claiming QFZP status. Their income includes AED 2M from UAE mainland clients. Run a CT risk assessment focusing on QFZP qualification and the de minimis test."

**Example 3 — Pre-filing VAT review**
> "We're filing Q4 2024 VAT for a Dubai media agency, AED 8M annual revenue. They have AED 300K of entertainment expenses and buy services from a UK vendor. Flag any VAT risks before we submit."

## Guardrails

- Output is an internal Finanshels work product. A qualified team member must review findings before advising the client.
- Never state a penalty amount as definitive — always say "confirm current amount with FTA penalty schedule."
- Do not provide a clean-bill-of-health opinion; the assessment covers known risk factors from inputs provided only.
- UAE jurisdiction only. No reference to non-UAE tax regimes.
- Client data used in this assessment is confidential.

## Reference

See `../_shared/finanshels-context.md` for UAE tax facts, rates, and deadlines.
