---
name: audit-workpaper-reviewer
description: Use when a Finanshels team member needs to review accounting or tax workpapers for quality, completeness, and UAE compliance standards before they are used to prepare a return, shared with an auditor, or filed with the FTA. Triggers include: CT return workpaper review, VAT reconciliation review, year-end close quality check, junior staff workpaper sign-off, or preparing audit-ready financials for a QFZP or revenue > AED 50M entity. Produces a structured gap list and a required-changes register.
---

# Audit Workpaper Reviewer

Reviews accounting and tax workpapers against Finanshels quality standards and UAE compliance requirements; produces a gap list and a prioritised required-changes register.

## When to use

- Reviewing a junior team member's CT or VAT workpaper before manager sign-off
- Pre-filing quality control: CT return workpaper, VAT reconciliation, or transfer pricing disclosure
- Preparing audit-ready financials for a QFZP (audited financials are a QFZP condition) or an entity with revenue > AED 50M
- Year-end close review: ledger reconciliations, trial balance, journal entries
- Client deliverable review before the work is shared externally
- Responding to an FTA audit notice: checking whether existing workpapers will withstand scrutiny

## Inputs needed

**Required**
- Workpaper set (paste content, upload, or describe the structure in detail)
- Entity type (mainland LLC / free zone / branch) and financial year end
- Purpose of the workpaper (CT return support / VAT reconciliation / financial statements / other)

**Optional**
- Prior-year workpaper (for year-over-year consistency check)
- CT or VAT return draft (to cross-check figures)
- Engagement letter or scope of work (to verify what was agreed to be produced)
- Name of preparer and reviewer (for sign-off section assessment)

## Workflow

1. **Identify workpaper type and scope**
   Determine which category applies (one or more may apply):
   - A: CT return support workpapers
   - B: VAT reconciliation workpapers
   - C: Financial statement / trial balance workpapers
   - D: Transfer pricing documentation
   Use the checklist at `./checklists/workpaper-checklist.md` for the relevant category.

2. **Check structural completeness**
   Every Finanshels workpaper must have:
   - [ ] Client name (internal use only — anonymise before sharing externally)
   - [ ] Tax period / financial year clearly stated
   - [ ] Preparer name and date
   - [ ] Reviewer name and date (or "Pending review" if that's the current stage)
   - [ ] Version number or date stamp
   - [ ] Source of each figure clearly referenced (ledger, EmaraTax, invoice listing)
   - [ ] Cross-references to related workpapers or schedules (e.g. WP-1 ties to WP-3)

3. **Check mathematical accuracy**
   - Agree opening balances to prior-year closing balances or prior filing
   - Foot and cross-foot all totals
   - Agree summary figures to source (trial balance, EmaraTax return totals, bank statements)
   - Flag any unexplained differences, even small ones — FTA auditors do the same

4. **Check UAE-specific compliance content**

   **For CT workpapers:**
   - Taxable income starting point: net profit per financial statements, then CT adjustments applied
   - Disallowed deductions identified and added back (fines, penalties, non-arm's-length interest, entertainment > 50%)
   - Related-party transactions listed with arm's-length analysis or reference to TP file
   - Exempt income identified separately (qualifying participation dividends/gains)
   - Small Business Relief election documented if applicable (revenue ≤ AED 3M, period ending on/before 31 Dec 2026)
   - Free zone QFZP income split: qualifying income at 0% vs. non-qualifying at 9%
   - Tax loss carry-forward correctly applied (75% cap per tax period — verify cap with FTA)
   - CT registration number and return due date stated

   **For VAT workpapers:**
   - Output tax: all supply categories listed (5%, 0%, exempt) with supporting invoices or listing
   - Input tax: blocked categories excluded; partial exemption applied if mixed-supply entity
   - Reverse charge: cross-border services identified; reverse charge entries included
   - Net VAT position agrees to EmaraTax return figures
   - Bank reconciliation to VAT payment/refund
   - Late-filing or underpayment penalties noted if applicable

   **For financial statement workpapers:**
   - IFRS or IFRS for SMEs basis stated (IFRS for SMEs permitted where revenue ≤ AED 50M)
   - Significant accounting policies noted
   - Bank reconciliations completed and signed off
   - Accounts receivable ageing with provision analysis
   - Fixed-asset register with depreciation schedule
   - Payroll reconciliation agrees to WPS records

5. **Identify gaps**
   For each gap found:
   - Describe the specific issue (not just "missing" — what is missing and why it matters)
   - Classify: CRITICAL (return cannot be filed / audit risk) | MATERIAL (significant quality issue) | MINOR (style or best-practice)
   - Assign to the responsible preparer

6. **Produce the required-changes register**
   List every gap with a required action, responsible person, and deadline.

7. **Write the reviewer sign-off block**
   State overall status: APPROVED / APPROVED WITH COMMENTS / REQUIRES REWORK.
   Include a brief narrative (2–3 sentences).

## Output format

```
# Workpaper Review — [Client Internal ID]
**Tax period / FY end:** [date]
**Workpaper type:** [CT / VAT / Financial Statements / TP]
**Reviewed by:** [Name]
**Review date:** YYYY-MM-DD
**Overall status:** APPROVED / APPROVED WITH COMMENTS / REQUIRES REWORK

---

## Review Summary
[2–3 sentences: what was reviewed, overall impression, top issues]

---

## Structural Completeness

| Item | Status | Notes |
|------|--------|-------|
| Client name / ID present | ✓ / ✗ | |
| Tax period stated | ✓ / ✗ | |
| Preparer name + date | ✓ / ✗ | |
| Reviewer sign-off | ✓ / Pending | |
| Version / date stamp | ✓ / ✗ | |
| Source references | ✓ / ✗ / Partial | |
| Cross-references | ✓ / ✗ / Partial | |

---

## Mathematical Accuracy

| Check | Result | Detail |
|-------|--------|--------|
| Opening balances agreed | Pass / Fail | |
| Totals footed | Pass / Fail | |
| Figures agreed to source | Pass / Fail | |
| Unexplained differences | None / [detail] | |

---

## UAE Compliance Content

| # | Check | Status | Finding |
|---|-------|--------|---------|
| 1 | [CT / VAT / FS specific check] | ✓ / ✗ / N/A | |
| ... | | | |

---

## Gap Register

| # | Section | Issue | Classification | Required Action | Responsible | Deadline |
|---|---------|-------|---------------|-----------------|-------------|---------|
| 1 | | | CRITICAL / MATERIAL / MINOR | | | |

---

## Reviewer Sign-Off

**Status:** APPROVED / APPROVED WITH COMMENTS / REQUIRES REWORK
**Notes:** [2–3 sentences]
**Reviewer:** [Name] — [Date]

---
*Internal Finanshels workpaper review. Not for external distribution.*
```

## Quality checklist

- [ ] All applicable checklist categories completed (CT, VAT, FS, TP)
- [ ] Every gap has a classification, action, owner, and deadline
- [ ] Mathematical accuracy checks completed (not just assumed)
- [ ] UAE-specific compliance checks completed for the workpaper type
- [ ] QFZP income split checked if entity is free zone
- [ ] SBR eligibility checked if revenue ≤ AED 3M
- [ ] Overall status (APPROVED / REWORK) stated with rationale
- [ ] No client-identifiable information in any sharable output

## Examples

**Example 1 — CT return workpaper sign-off**
> "Junior has prepared the CT workpaper for a Dubai mainland IT services company, AED 6M revenue, FY ending 31 Dec 2024. Review for quality and compliance before I sign it off and file."

**Example 2 — QFZP audit-ready financials**
> "Free zone logistics company, AED 22M revenue, JAFZA licence. We need to confirm their workpapers are audit-ready because audited financials are required for QFZP. What's missing?"

**Example 3 — VAT reconciliation review**
> "The Q1 2025 VAT workpaper for an Abu Dhabi retail client, AED 9M annual VAT-able sales. They have some zero-rated export sales and buy marketing services from a UK agency. Review the workpaper and flag any gaps before we submit."

## Guardrails

- Workpaper reviews are internal quality-control activities. Output must be reviewed by a qualified Finanshels team member before acting on any finding.
- Do not approve a workpaper as final — state "APPROVED WITH COMMENTS" or "REQUIRES REWORK" whenever any gap is identified.
- UAE jurisdiction only. Do not apply non-UAE accounting standards or tax rules.
- Workpaper content is highly confidential. Do not include real client data in examples.

## Reference

See `../_shared/finanshels-context.md` for UAE tax facts, rates, and deadlines.
