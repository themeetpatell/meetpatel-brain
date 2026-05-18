# Code Review Checklist — Tax Software (Finanshels)

Use this checklist for every review of code that touches UAE tax calculations,
EmaraTax integrations, accounting API data flows, or AED financial amounts.

Mark each item: **PASS** | **WARN** | **FAIL** | **N/A**

---

## 1. Rounding & Numerical Precision

| # | Check | Status | Notes |
|---|-------|--------|-------|
| R1 | All AED amounts stored and computed with at most 2 decimal places (fils precision). | | |
| R2 | Rounding strategy is explicit and consistent — half-up or banker's rounding; never truncation. | | |
| R3 | Floating-point types (`float`, `double`) are NOT used for final tax or monetary storage — use `Decimal` (Python), `BigDecimal` (Java/Kotlin), or integer fils. | | |
| R4 | VAT amounts computed as `round(net * 0.05, 2)` — not `net / 20` or other equivalent that may accumulate rounding error. | | |
| R5 | Aggregated totals computed by summing rounded line items, not by rounding a single aggregated float. | | |
| R6 | No implicit currency conversions — foreign-currency amounts are flagged, not silently converted. | | |

---

## 2. VAT Rate Application

| # | Check | Status | Notes |
|---|-------|--------|-------|
| V1 | Standard rate is sourced from a named constant (`VAT_RATE_STANDARD = Decimal("0.05")`), not a magic number. | | |
| V2 | VAT category codes used are exactly: `S` (standard 5%), `Z` (zero-rated), `E` (exempt), `OS` (out of scope). No other codes accepted without explicit mapping. | | |
| V3 | Zero-rated and exempt supplies produce VAT amount = 0.00, not 0.05 × net. | | |
| V4 | Out-of-scope supplies are excluded from the VAT return Box 1 (standard-rated) total. | | |
| V5 | Input tax (purchases) credit is only claimed on standard-rated purchases — not zero-rated or exempt. | | |
| V6 | Partial exemption / apportionment logic (if present) is documented and reviewed against FTA guidance. | | |

---

## 3. Corporate Tax Threshold Logic

| # | Check | Status | Notes |
|---|-------|--------|-------|
| C1 | 0% rate applies to taxable income ≤ AED 375,000 (inclusive boundary). | | |
| C2 | 9% rate applies only to the portion of taxable income **above** AED 375,000 — not the full amount. | | |
| C3 | Small Business Relief: revenue ≤ AED 3,000,000 check uses `<=`, not `<`. Relief period end date (31 Dec 2026) is enforced. | | |
| C4 | QFZP qualifying income vs non-qualifying income split is implemented, not treated as a single pool. | | |
| C5 | Natural-person threshold (AED 1,000,000 business turnover) is distinct from the corporate AED 375,000 taxable income threshold — not conflated. | | |
| C6 | Tax period dates are correct — CT applies to financial years starting **on or after 1 June 2023**. | | |
| C7 | Transfer pricing / related-party adjustments do not silently pass through unadjusted — flagged for disclosure form. | | |

---

## 4. EmaraTax Data Format & Integration

| # | Check | Status | Notes |
|---|-------|--------|-------|
| E1 | All field names and data types match the current FTA EmaraTax schema (version-pinned if possible). | | |
| E2 | TRN fields are validated as exactly 15 digits before submission — no hyphens, spaces, or other characters. | | |
| E3 | Tax period start/end dates are in the format expected by EmaraTax (confirm against FTA portal docs). | | |
| E4 | Return box totals (e.g. Box 1 standard-rated supplies, Box 9 input tax) are computed from the correct source lines. | | |
| E5 | HTTP errors from the EmaraTax API are caught and surfaced — not swallowed or logged silently. | | |
| E6 | API credentials (client ID, secret, token) are loaded from environment variables or a secrets manager — never hardcoded. | | |
| E7 | Idempotency: re-submitting the same return does not create a duplicate filing. | | |

---

## 5. Accounting API Integrations (Xero / QuickBooks / Zoho / SAP B1)

| # | Check | Status | Notes |
|---|-------|--------|-------|
| A1 | Tax code mappings from the third-party system to UAE VAT categories are explicit, documented, and cover all codes in use. | | |
| A2 | Webhook/event handlers are idempotent — duplicate delivery of the same event does not produce duplicate postings. | | |
| A3 | Pagination is handled — fetching invoices does not silently stop at page 1 of N. | | |
| A4 | Rate-limit errors (HTTP 429) are retried with back-off, not silently dropped. | | |
| A5 | Currency field from the third-party API is checked — AED assumed only after an explicit check. | | |
| A6 | Deleted/voided records in the source system are handled — not carried forward as valid transactions. | | |

---

## 6. Error Handling & Resilience

| # | Check | Status | Notes |
|---|-------|--------|-------|
| H1 | No bare `except` / `catch (e)` that swallows all errors silently. | | |
| H2 | Network failures produce a clear error — they do not return a default of zero tax. | | |
| H3 | Invalid input (missing TRN, null amount, bad date) raises a typed exception or returns a structured error — not a silent default. | | |
| H4 | Errors logged with sufficient context (tax period, invoice ID, field name) to diagnose without re-running. | | |
| H5 | Partial failure in a batch (one bad record) does not silently corrupt the rest of the batch — fail-fast or collect-all-errors pattern used. | | |

---

## 7. Test Coverage

| # | Check | Status | Notes |
|---|-------|--------|-------|
| T1 | Unit tests exist for VAT calculation on standard, zero-rated, exempt, and out-of-scope lines. | | |
| T2 | Unit tests cover CT threshold boundary: exactly AED 375,000 (0%) and AED 375,001 (9% on AED 1 only). | | |
| T3 | Small Business Relief boundary tested: AED 3,000,000 (qualifies) vs AED 3,000,001 (does not). | | |
| T4 | Rounding edge case tested: VAT on an amount that produces a recurring decimal (e.g. AED 1.00 → VAT 0.05). | | |
| T5 | Tests for invalid inputs: blank TRN, null amount, unsupported VAT category. | | |
| T6 | Integration tests mock the EmaraTax / accounting API — no real API calls in unit tests. | | |
| T7 | Overall coverage ≥ 80% on financial calculation modules. | | |

---

## 8. Code Quality & Security

| # | Check | Status | Notes |
|---|-------|--------|-------|
| Q1 | No hardcoded secrets (API keys, tokens, passwords) anywhere in the diff. | | |
| Q2 | No `console.log` / `print()` statements that could leak financial figures to logs in production. | | |
| Q3 | Tax rates and thresholds sourced from config/constants — a future rate change requires one edit, not a grep. | | |
| Q4 | Functions are focused (< 50 lines) — complex tax logic is not buried in a 200-line function. | | |
| Q5 | No mutation of shared state during a calculation — each tax computation is a pure function where possible. | | |
| Q6 | Record-keeping: computed return figures are persisted with their inputs so the calculation can be audited later (7-year retention requirement). | | |

---

## Severity Key

| Level | Meaning | Merge decision |
|-------|---------|----------------|
| CRITICAL | Wrong tax figures, filing error, FTA penalty risk | **BLOCK** — do not merge |
| HIGH | Incorrect in foreseeable edge cases | **WARN** — should fix before merge |
| MEDIUM | Fragile; will break on realistic future inputs | **INFO** — consider fixing |
| LOW | Style / minor suggestion | **NOTE** — optional |

---

## Reference

See `../../_shared/finanshels-context.md` for UAE tax facts, rates, and deadlines.
