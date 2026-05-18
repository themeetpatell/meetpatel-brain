---
name: documentation-auditor
description: Use when a Finanshels team member needs to verify that a client's records, invoices, contracts, and supporting evidence meet UAE record-keeping and engagement documentation standards. Triggers include: new client onboarding document review, pre-FTA-audit document readiness check, CT or VAT record-keeping compliance review, verifying 7-year retention compliance, or checking that engagement documentation (signed letter, KYC, UBO register) is complete. Produces a structured gap report and a prioritised remediation checklist.
---

# Documentation Auditor

Verifies that client documentation meets UAE record-keeping, FTA compliance, and Finanshels engagement standards; produces a gap report and remediation checklist.

## When to use

- New client onboarding: confirming all required engagement documents are in place (KYC, UBO, signed engagement letter)
- Pre-FTA-audit readiness: verifying that records can withstand an FTA document request
- Annual compliance review: checking that records for the period are complete and correctly retained
- CT or VAT filing preparation: confirming supporting evidence exists for each material line item
- AML/CFT compliance check: verifying CDD documents and sanctions screening records
- UBO / shareholder register filing: checking the register is current and filed with the correct registrar
- Record-retention audit: confirming that records more than 7 years old have been correctly disposed of or archived

## Inputs needed

**Required**
- Entity name (internal ID only) and entity type (mainland LLC / free zone / branch / natural person)
- Type of documentation review requested (select one or more):
  - `engagement` — Finanshels engagement and onboarding documents
  - `ct-records` — CT supporting documentation
  - `vat-records` — VAT supporting documentation
  - `aml-kyc` — AML/CFT / KYC / CDD documents
  - `ubo` — UBO and shareholder register
  - `financial-records` — General accounting records and retention
- Brief description of what documents are available (or a list/inventory)

**Optional**
- Prior documentation audit or gap report (to check if prior gaps were remediated)
- Engagement letter reference (to confirm scope of Finanshels service)
- Financial year(s) in scope

## Workflow

1. **Scope the review**
   Confirm which documentation categories are in scope (from the inputs above). If the request is open-ended ("check everything"), default to all five categories.

2. **Run the engagement documentation check (always run for new clients)**
   Verify the following are on file:
   - Signed engagement letter (Finanshels standard template, dated, covering the service scope)
   - Terms of business / fee schedule accepted
   - KYC documents: passport / Emirates ID for all beneficial owners and authorised signatories
   - Trade licence (valid, not expired)
   - Certificate of incorporation / Memorandum and Articles of Association
   - Confirmation of business address
   - Sanctions screening completed and documented (mandatory for Finanshels as a DNFBP)
   - Risk rating assigned in the client intake form (low / medium / high AML risk)
   - UBO details captured (see UBO section below)

3. **Run the CT record-keeping check (if `ct-records` in scope)**
   UAE CT Law requires records to be retained for **7 years** from the end of the tax period.
   Verify the following exist and are accessible:
   - Audited or management financial statements for each CT period
   - Trial balance and general ledger
   - Supporting schedules for each CT return line item (income, deductions, adjustments)
   - CT return as filed (EmaraTax confirmation)
   - EmaraTax registration certificate
   - Related-party transaction documentation / TP file (if applicable)
   - Supporting evidence for exempt income claims (participation exemption — ownership certificates, holding period evidence)
   - Small Business Relief election (if applicable): revenue calculation, election form
   - QFZP supporting documents (if applicable): substance evidence, qualifying-income analysis, audited financials

4. **Run the VAT record-keeping check (if `vat-records` in scope)**
   UAE VAT requires records for **5 years** (15 years for real-estate transactions — verify with FTA).
   Verify:
   - All tax invoices issued (sales): sequentially numbered, contain required FTA fields (supplier TRN, date, description, tax amount separately stated, VAT rate)
   - All tax invoices received (purchases): originals or scanned copies on file
   - Import documentation (customs entries, import declarations) for all imported goods/services
   - Export documentation for all zero-rated exports (customs export declaration, proof of departure)
   - VAT returns as filed (EmaraTax confirmations for all periods)
   - VAT payment receipts or refund records
   - Input tax claim listings with invoice references
   - Partial exemption calculation (if entity makes exempt supplies)
   - Reverse charge records for cross-border services

5. **Run the AML/CFT / KYC check (if `aml-kyc` in scope)**
   Finanshels is a DNFBP. Required records:
   - goAML portal registration confirmed (Finanshels firm-level, not client-level — but note in file)
   - Customer Due Diligence (CDD) form completed for this client
   - Risk assessment documented: business type, transaction volumes, geographic exposure, PEP status
   - Politically Exposed Person (PEP) screening result documented
   - Sanctions list screening: screened against UAE Cabinet Decision No. 74 of 2020 (Consolidated Sanctions List) — result documented
   - Source of funds / source of wealth documented for high-risk clients
   - Ongoing monitoring: CDD refreshed at risk-based intervals (annually for high-risk, every 3 years for medium)
   - Suspicious Activity Report (SAR/STR) log: note if any STR was filed or the assessment was "no STR required"

6. **Run the UBO check (if `ubo` in scope)**
   UAE entities must maintain and file UBO registers.
   Verify:
   - UBO register on file: full name, nationality, date of birth, passport/ID number, nature and extent of beneficial interest, date of becoming/ceasing to be a UBO
   - Shareholder register on file and current
   - Nominee director register (if applicable)
   - Register filed with the relevant registrar (DED for mainland; free zone authority for free zone entities)
   - Last update date: registers must be kept current — flag if not updated in > 12 months or following an ownership change

7. **Run the general financial records check (if `financial-records` in scope)**
   - Books of account (general ledger, cash book, purchase/sales journals): in place and up to date
   - Bank statements: all accounts, all periods
   - Bank reconciliations: completed and signed off
   - Fixed-asset register: current, with acquisition/disposal records and depreciation schedules
   - Payroll records: salary slips, WPS transfer confirmations, GPSSA contribution records for nationals
   - Contracts and agreements: key commercial contracts on file (supplier, customer, lease, loan)
   - Board resolutions or management approvals for material transactions
   - Retention compliance: 7-year rule for CT; 5-year rule for VAT; 10-year for AML/CFT (verify each with FTA/applicable authority)

8. **Build the gap report**
   For every missing or deficient item:
   - Name the specific document
   - State why it is required (legal basis / FTA requirement / Finanshels standard)
   - Classify: CRITICAL (regulatory non-compliance, FTA penalty risk, AML obligation) | MATERIAL (significant gap, affects return filing or audit readiness) | MINOR (best practice, internal standard)
   - State who is responsible for obtaining it: client / Finanshels bookkeeping team / Finanshels compliance officer

9. **Produce the remediation checklist**
   Group gaps by responsible party and priority. Each item: specific action, responsible party, target date.

10. **Write the executive summary**
    3–5 sentences: overall documentation status (Ready / Needs attention / Critical gaps), top 3 risks, recommended next steps.

## Output format

```
# Documentation Audit Report
**Client:** [Internal ID]
**Entity type:** [Mainland LLC / Free Zone / etc.]
**Review scope:** [engagement | ct-records | vat-records | aml-kyc | ubo | financial-records]
**Period covered:** [FY / calendar year]
**Reviewed by:** [Name]
**Date:** YYYY-MM-DD
**Overall status:** READY / NEEDS ATTENTION / CRITICAL GAPS

---

## Executive Summary
[3–5 sentences]

---

## Document Inventory

| Category | Documents Available | Documents Missing | Critical Gaps |
|----------|---------------------|-------------------|---------------|
| Engagement | X of Y | Z | [list] |
| CT Records | X of Y | Z | [list] |
| VAT Records | X of Y | Z | [list] |
| AML / KYC | X of Y | Z | [list] |
| UBO Register | X of Y | Z | [list] |
| Financial Records | X of Y | Z | [list] |

---

## Detailed Gap Report

| # | Category | Document / Item | Why Required | Classification | Gap Detail |
|---|----------|-----------------|-------------|---------------|------------|
| 1 | | | | CRITICAL / MATERIAL / MINOR | |
| 2 | | | | | |

---

## Remediation Checklist

### Client Actions Required

| # | Action | Document to Obtain / Provide | Deadline | Priority |
|---|--------|------------------------------|----------|----------|
| 1 | | | | HIGH / MEDIUM / LOW |

### Finanshels Team Actions Required

| # | Action | Responsible | Deadline | Priority |
|---|--------|-------------|----------|----------|
| 1 | | | | HIGH / MEDIUM / LOW |

---

## Retention Compliance Note

[Are records being retained for the correct periods? Note any records approaching or past their required retention window.
CT: 7 years from end of tax period. VAT: 5 years (15 years for real estate — verify with FTA). AML/CFT: 10 years (verify with applicable authority).]

---
*Internal Finanshels work product. Verify all retention and compliance requirements against current FTA guidance and applicable UAE regulations before advising clients.*
```

## Quality checklist

- [ ] All in-scope categories reviewed (engagement, CT, VAT, AML, UBO, financial records)
- [ ] Every gap has a legal/regulatory basis stated (not just "best practice")
- [ ] Every CRITICAL gap has a remediation action and deadline
- [ ] AML sanctions screening and CDD documented for all clients (DNFBP obligation)
- [ ] UBO register currency checked (not just existence)
- [ ] Record-retention periods stated for each category and verified against current FTA/authority guidance
- [ ] Overall status (READY / NEEDS ATTENTION / CRITICAL GAPS) stated
- [ ] No real client names or identifiers in output

## Examples

**Example 1 — New client onboarding**
> "We've just signed a new client — a Dubai mainland restaurant chain, AED 7M revenue, 3 shareholders. Run a documentation audit to confirm our engagement files are complete and they're set up for VAT and CT record-keeping."

**Example 2 — Pre-FTA-audit readiness**
> "A free zone trading company, DAFZA, AED 18M revenue, has received an FTA document request for their VAT period Q1–Q4 2023. Check whether their documentation is FTA-audit-ready and identify critical gaps."

**Example 3 — Annual AML/CDD refresh**
> "We're doing annual AML refreshes. Client is a Sharjah mainland professional services firm, medium AML risk rating, last CDD done 18 months ago. Check what needs to be updated."

## Guardrails

- Output is an internal Finanshels work product. A qualified team member must review before communicating gaps to the client.
- AML/CFT obligations (including SAR/STR filing) are legal requirements, not optional. Flag critical AML gaps immediately to the Finanshels Compliance Officer — do not hold them in a queue.
- UAE jurisdiction only. Do not reference non-UAE documentation requirements.
- All client data used in this review is confidential and must not be included in any external communication.
- Do not confirm that documentation is "FTA-proof" — state that it meets the requirements as assessed, subject to current FTA guidance.

## Reference

See `../_shared/finanshels-context.md` for UAE tax facts, rates, and deadlines.
