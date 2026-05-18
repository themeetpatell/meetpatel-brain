---
name: tax-data-validator
description: Use when you need to validate, standardize, or audit client financial and tax data before processing — including chart of accounts uploads, invoice batches, VAT line items, TRN numbers, AED amounts, and date formats. Triggers on phrases like "check this data", "validate the CSV", "is the TRN correct", "review the invoice data", "data quality check", or any import/upload of client financial records. Produces a structured data-quality report with per-field validation results, a list of errors and warnings, and transformation rules to fix bad records.
---

# Tax Data Validator

Validates and standardises client financial and tax data for UAE compliance work, producing a data-quality report with actionable transformation rules.

## When to use

- A client uploads a CSV, spreadsheet, or JSON extract of invoices, transactions, or chart-of-accounts entries.
- You need to verify TRN formats before submitting an EmaraTax return.
- You are preparing VAT or CT data and want to catch bad records before they cause a filing error.
- You receive a data dump from a third-party accounting system (Xero, QuickBooks, Zoho Books, SAP B1) and need to normalise it.
- A new client is onboarded and their historical data needs a quality sweep.
- You are debugging a mismatch between the VAT return and the underlying transaction detail.

## Inputs needed

**Required**
- Raw data — can be a file path, pasted CSV, Python dict/list, or structured text.
- Data type — one of: `invoices`, `chart_of_accounts`, `vat_lines`, `transactions`, or `mixed`.

**Optional**
- Client TRN (for cross-checking supplier/customer TRNs in the data).
- Tax period start and end dates (for date-range validation).
- Expected VAT rate(s) to enforce (default: 5% standard; 0% zero-rated; exempt = 0 with flag).
- Strictness level: `warn` (report issues only) or `strict` (mark records invalid on any error). Default: `warn`.

## Workflow

1. **Identify the data schema**
   - Inspect the first 5–10 rows to infer column names and types.
   - Map columns to canonical field names (see validation-rules.py for the canonical schema).
   - Flag any unrecognised columns as `UNKNOWN_FIELD` — do not discard them.

2. **Run structural validation**
   - Check all required fields are present per data type (see table below).
   - Detect completely blank rows and mark them `SKIP`.
   - Detect duplicate records: same invoice number + supplier/customer TRN + date + amount.

3. **Run field-level validation** (see `tools/validation-rules.py` for exact rules)
   - **TRN format:** Must be exactly 15 digits, starting with `1` for UAE-registered businesses. No spaces or hyphens accepted in the canonical form (strip them first).
   - **Dates:** Must be ISO-8601 (`YYYY-MM-DD`). Accept `DD/MM/YYYY` and `MM/DD/YYYY` as warnings — normalise to ISO-8601 in the transformation output.
   - **AED amounts:** Must be numeric, ≥ 0, with at most 2 decimal places. Negative amounts are allowed only on credit notes (type = `CN`).
   - **VAT rate sanity:** VAT amount / net amount = 5% ± 0.01 for standard-rated; 0% for zero-rated/exempt. Flag anything outside this as `VAT_RATE_MISMATCH`.
   - **VAT category codes:** Must be one of `S` (standard), `Z` (zero-rated), `E` (exempt), `OS` (out of scope). Any other code → `INVALID_VAT_CATEGORY`.
   - **Invoice numbers:** Must be non-empty strings. Numeric-only invoice numbers are accepted but flagged as `NUMERIC_INVOICE_ID` (warn).
   - **Currency:** Must be `AED`. Foreign-currency amounts flagged as `FOREIGN_CURRENCY` — include for review; do not auto-convert.

4. **Aggregate results**
   - Count: total records, valid, warnings, errors.
   - Produce a per-record status: `VALID`, `WARNING`, `ERROR`, `SKIP`.
   - Group errors by rule code (e.g. `TRN_FORMAT_ERROR`, `DATE_FORMAT_WARN`, `VAT_RATE_MISMATCH`).

5. **Generate transformation rules**
   - For each fixable warning, output a transformation instruction: field name, original value, corrected value, reason.
   - For errors that require human input (e.g. missing TRN), flag as `NEEDS_REVIEW` with a plain-English note.

6. **Produce the data-quality report** (see Output format below).

7. **Run the validation tool** (optional automated step)
   - If data is available as Python-readable input, run `python3 tools/validation-rules.py` and append the output to the report.

### Required fields by data type

| Data type | Required fields |
|-----------|----------------|
| `invoices` | `invoice_number`, `invoice_date`, `supplier_trn` or `customer_trn`, `net_amount`, `vat_amount`, `vat_category` |
| `vat_lines` | `invoice_number`, `invoice_date`, `net_amount`, `vat_amount`, `vat_category` |
| `chart_of_accounts` | `account_code`, `account_name`, `account_type` |
| `transactions` | `transaction_date`, `description`, `debit` or `credit`, `account_code` |

## Output format

```
## Data Quality Report
**Client:** [name/reference]
**Data type:** [type]
**Tax period:** [start] – [end]
**Generated:** [date]

### Summary
| Metric | Count |
|--------|-------|
| Total records | N |
| Valid | N |
| Warnings | N |
| Errors | N |
| Skipped (blank) | N |

### Error breakdown
| Rule code | Count | Description |
|-----------|-------|-------------|
| TRN_FORMAT_ERROR | N | TRN is not 15 digits |
| VAT_RATE_MISMATCH | N | VAT amount does not equal 5% of net |
| ... | | |

### Transformation rules
| # | Field | Original | Corrected | Reason |
|---|-------|----------|-----------|--------|
| 1 | invoice_date | 15/01/2024 | 2024-01-15 | Normalised to ISO-8601 |
| ... | | | | |

### Records requiring manual review
| Row | Field | Issue | Action needed |
|-----|-------|-------|--------------|
| 12 | supplier_trn | 9876543210 (10 digits) | Obtain correct TRN from supplier |
| ... | | | |

### Clean data
[Attach or reference the corrected dataset]
```

## Quality checklist

- [ ] All required fields present for the declared data type
- [ ] TRNs are 15 digits — no formatting artefacts
- [ ] All dates normalised to `YYYY-MM-DD`
- [ ] VAT amounts reconcile at 5% / 0% / exempt as declared
- [ ] No duplicate invoice numbers within the same supplier/customer and period
- [ ] AED amounts have ≤ 2 decimal places
- [ ] Foreign-currency records flagged and not silently included in AED totals
- [ ] Summary counts match (valid + warnings + errors + skipped = total)
- [ ] Transformation rules are specific and reversible
- [ ] Records needing manual review have a plain-English action note

## Examples

- "Validate this invoice CSV before we prepare the Q1 VAT return."
- "The client sent over a Xero export — check the TRN formats and VAT categories."
- "Run a data quality check on this chart of accounts upload. The account codes look inconsistent."

## Guardrails

- UAE jurisdiction only. Do not apply non-UAE VAT rules or tax codes.
- This report is a professional work product. A qualified Finanshels team member must review findings before contacting a client or amending a return.
- All client financial data is confidential. Do not log, share, or include real client data in examples or error messages.
- Tax rules change. Verify the 5% VAT rate and TRN format against current FTA guidance before processing a large batch.
- Do not auto-correct errors that require client confirmation (missing TRN, negative amounts on non-CN records). Flag them as `NEEDS_REVIEW`.

## Reference

See ../_shared/finanshels-context.md for UAE tax facts, rates, and deadlines.
