---
name: code-reviewer-tax-software
description: Use when reviewing code written for Finanshels' internal tax and accounting tools — including VAT calculation logic, Corporate Tax threshold checks, EmaraTax data preparation scripts, accounting API integrations (Xero, QuickBooks, Zoho Books), rounding functions, or any code that touches AED amounts, UAE tax rates, or FTA filing formats. Triggers on phrases like "review this code", "check my VAT logic", "is this CT calculation right", "code review for the EmaraTax script", or when a developer shares a diff, PR, or function touching financial computation. Produces a structured review with a risk-rated checklist, specific line-level findings, and a pass/warn/block recommendation.
---

# Code Reviewer — Tax Software

Reviews code for Finanshels' internal tax and accounting tools for correctness, UAE tax-rule compliance, rounding safety, and integration risk. Produces a review checklist and risk assessment.

## When to use

- A developer writes or modifies VAT calculation logic (rate application, rounding, category mapping).
- Code prepares data for EmaraTax submissions (return XMLs, CSV uploads, API payloads).
- A new accounting API integration is built or updated (Xero, QuickBooks, Zoho Books, SAP B1, Odoo).
- Corporate Tax threshold logic is implemented (0% / 9% tiers, Small Business Relief eligibility, QFZP qualifying income split).
- A script processes AED amounts, applies exchange-rate conversions, or handles multi-currency transactions.
- Any financial rounding function, tax period date logic, or TRN validation routine is touched.
- Before merging a PR that affects compliance outputs (return figures, audit trail, record-keeping).

## Inputs needed

**Required**
- Code to review — file path(s), pasted snippet, or PR diff.
- Context — what does this code do? (e.g. "VAT return aggregator", "CT taxable income calculator", "Xero webhook handler")

**Optional**
- Tax period / filing context (e.g. "Q1 2024 VAT return", "FY2024 CT return").
- Known edge cases or assumptions the developer made.
- Language and framework (Python, TypeScript, Node, etc.) — infer from code if not provided.
- Prior review findings to check were resolved.

## Workflow

1. **Understand the intent**
   - Read the code and the context. Identify: what tax rule does this implement? What data does it consume and produce?
   - Map the code to a specific UAE tax obligation: VAT computation, CT threshold, TRN validation, EmaraTax payload, etc.

2. **Run the checklist** (see `checklists/code-review-checklist.md` for the full list)
   - Work through every section: rounding, VAT logic, CT logic, EmaraTax integration, data handling, error handling, test coverage.
   - Mark each item: PASS / WARN / FAIL / N/A.

3. **Identify findings**
   - For each WARN or FAIL, write a finding with: severity, location (file + line), description, UAE tax impact, and recommended fix.
   - Severity levels:
     - **CRITICAL** — produces wrong tax figures, causes a filing error, or risks an FTA penalty. Block merge.
     - **HIGH** — likely incorrect in edge cases (e.g. rounding on large amounts, incorrect threshold boundary). Should fix before merge.
     - **MEDIUM** — code works today but is fragile or will break on a foreseeable input. Consider fixing.
     - **LOW** — style, naming, or minor improvement. Optional.

4. **Assess overall risk**
   - **BLOCK** if any CRITICAL finding exists.
   - **WARN** if only HIGH/MEDIUM findings exist.
   - **PASS** if only LOW findings or none.

5. **Produce the review report** (see Output format below).

6. **Suggest test cases** — for each CRITICAL or HIGH finding, name at least one test case that would have caught it.

## Output format

```
## Code Review — Tax Software
**Component:** [what the code does]
**Reviewer:** Finanshels AI Review
**Date:** [date]
**Overall verdict:** PASS | WARN | BLOCK

---

### Checklist summary
| Section | Status | Notes |
|---------|--------|-------|
| Rounding & precision | PASS / WARN / FAIL | |
| VAT rate application | | |
| VAT category logic | | |
| CT threshold logic | | |
| EmaraTax data format | | |
| API integration safety | | |
| Error handling | | |
| Test coverage | | |

---

### Findings

#### [CRITICAL / HIGH / MEDIUM / LOW] — Short title
**Location:** `filename.py:42`
**Description:** What is wrong and why.
**UAE tax impact:** What filing error or penalty this could cause.
**Fix:** Specific recommended change, with a code snippet if helpful.
**Test case:** `test_vat_rounding_on_large_invoice` — assert VAT on AED 999,999 rounds correctly.

---

### Suggested test cases (new)
- [ ] `test_ct_threshold_boundary` — income exactly at AED 375,000 must produce 0% tax.
- [ ] `test_small_business_relief_cutoff` — revenue at AED 3,000,001 must not qualify.
- [ ] ...

---

### Summary
[2–4 sentences. What the code does well. What must be fixed. Next steps.]
```

## Quality checklist

- [ ] Every VAT calculation checked against 5% rate with correct rounding (fils = 2 d.p.)
- [ ] CT threshold boundaries tested at exactly AED 375,000 and AED 3,000,000
- [ ] No hardcoded tax rates — rates sourced from a config or constant, not magic numbers
- [ ] Rounding uses banker's rounding or consistent half-up — not truncation
- [ ] TRN format validation present wherever TRNs are accepted as input
- [ ] EmaraTax field names and formats match current FTA schema
- [ ] API calls have error handling — network failure does not silently produce zero tax
- [ ] Multi-currency amounts flagged, not silently converted
- [ ] Date arithmetic uses proper date libraries — no string manipulation of tax period dates
- [ ] All findings rated by severity with a UAE tax impact statement
- [ ] At least one suggested test case per CRITICAL/HIGH finding

## Examples

- "Review this Python function that calculates the VAT payable for a quarterly return."
- "Check this TypeScript class that maps Xero invoice data to EmaraTax XML format — is the rounding correct?"
- "PR review: this service computes CT taxable income and applies Small Business Relief. Does the threshold logic hold up?"

## Guardrails

- UAE jurisdiction only. Do not apply HMRC, GAAP (US), or any non-UAE VAT rules.
- This review is professional work product. A qualified Finanshels team member must sign off before any filing logic goes to production.
- If a CRITICAL finding is found, state clearly: **do not merge until resolved**. Do not soften this.
- Tax rates and FTA schema versions change. Flag any hardcoded values that will break on a rate or format change.
- Do not share code snippets containing real client data in the review output.

## Reference

See ../_shared/finanshels-context.md for UAE tax facts, rates, and deadlines.
