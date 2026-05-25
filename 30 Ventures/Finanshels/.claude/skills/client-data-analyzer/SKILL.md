---
name: client-data-analyzer
description: Use when a Finanshels accountant, analyst, or outsourced CFO team member needs to extract insights from a client's financial or accounting data. Triggers include requests to analyse revenue trends, expense ratios, VAT input/output patterns, Corporate Tax exposure, or to produce a visualization-ready financial summary. Produces a structured analysis report with computed metrics, trend tables, and CT/VAT-specific observations ready for client presentation or internal review.
---

# Client Data Analyzer

Extracts insights and trends from client financial and accounting data — revenue, expenses, VAT balances, and Corporate Tax exposure — and produces a structured, visualization-ready analysis.

## When to use

- Preparing a quarterly or annual management report for a client
- Onboarding a new client: first-look analysis of historical financials
- Identifying whether a client is approaching VAT registration thresholds (AED 375,000 / AED 187,500)
- Assessing a client's Corporate Tax exposure ahead of their first CT return
- Spotting unusual expense ratios, revenue swings, or VAT recovery anomalies for review
- Building charts or dashboard inputs from trial balance / general ledger exports
- Pre-audit financial trend review

## Inputs needed

**Required**
- Client identifier (anonymised ID or internal code)
- Financial data: at least one of —
  - Trial balance or P&L export (CSV or structured text) with period labels
  - VAT return history (output tax, input tax, net VAT per period)
  - General ledger summary by category
- Analysis period (e.g., Jan 2024 – Dec 2024; or last 4 quarters)

**Optional**
- Prior-year data for year-over-year (YoY) comparison
- Industry sector (used for ratio context — e.g., retail vs. professional services)
- Client's stated revenue figure (to cross-check against CT Small Business Relief threshold of AED 3M)
- Free zone / mainland flag (affects CT rate analysis)

## Workflow

1. **Validate and normalise input data**
   - Confirm all figures are in AED
   - Check for missing periods (gaps in monthly/quarterly data)
   - Identify any negative revenue or implausibly large single-period swings; flag for human review
   - Standardise category labels to: Revenue, Cost of Sales, Gross Profit, Operating Expenses, EBITDA, Finance Costs, Net Profit

2. **Revenue trend analysis**
   - Compute period-over-period revenue growth rate: `growth% = (current − prior) / prior × 100`
   - Compute trailing-12-month (T12M) total revenue
   - Identify best and worst performing periods
   - Flag if T12M revenue is within 20% of VAT mandatory registration threshold (AED 375,000) or voluntary threshold (AED 187,500) — relevant for unregistered clients
   - Flag if T12M revenue is within 20% of CT Small Business Relief ceiling (AED 3M) — relevant for registered CT clients approaching/leaving eligibility

3. **Expense ratio analysis**
   - Gross margin: `(Gross Profit / Revenue) × 100`
   - Operating expense ratio: `(Operating Expenses / Revenue) × 100`
   - Net profit margin: `(Net Profit / Revenue) × 100`
   - Compare ratios across periods — flag swings > 5 percentage points as "notable movement"
   - If sector is known, note whether ratios appear typical (qualitative flag only — not a benchmark score; use `benchmark-analyzer-tax` skill for full benchmark)

4. **VAT input/output pattern analysis**
   - For each period: output VAT (VAT charged on sales), input VAT (VAT recoverable on purchases), net VAT payable
   - Compute input recovery ratio: `Input VAT / Output VAT × 100` — a very high ratio (> 90%) may indicate a VAT-refund position; flag for review
   - Identify periods with nil or zero output VAT — check whether revenue was zero-rated, exempt, or whether a filing error is possible
   - Compute T12M taxable supplies — compare against VAT registration thresholds
   - Note any period where net VAT payable jumped > 50% QoQ without a corresponding revenue jump — flag as anomaly

5. **Corporate Tax exposure assessment**
   - Compute estimated taxable income: `Net Profit − Exempt Income Adjustments` (note: full CT adjustments require a qualified review; this is indicative only)
   - Apply CT rate tiers:
     - 0% on first AED 375,000 of taxable income
     - 9% on taxable income above AED 375,000
   - Check Small Business Relief eligibility: revenue ≤ AED 3M per tax period (available for periods ending on or before 31 Dec 2026)
   - If free zone flag is set: note that QFZP status and qualifying income determination require practitioner review before applying 0% rate
   - Produce indicative CT liability estimate with clear caveat that this is pre-adjustment and requires practitioner sign-off

6. **Summary statistics**
   - Mean, median, min, max for: revenue, gross margin, net profit margin, VAT net payable
   - Compound Annual Growth Rate (CAGR) if ≥ 2 years of data: `CAGR = (End / Start)^(1/years) − 1`
   - Volatility score (coefficient of variation on revenue): low < 15%, medium 15–30%, high > 30%

7. **Produce output**
   - Narrative summary section (3–5 sentences)
   - Structured tables (trend data, ratios, VAT pattern, CT estimate)
   - Visualization-ready arrays: period labels + values for revenue, margins, VAT net
   - Action flags list: items requiring practitioner attention before client delivery
   - Run `tools/analysis-functions.py` to reproduce all computed metrics

## Output format

```
FINANSHELS — CLIENT FINANCIAL ANALYSIS
Client ID    : [ID]
Period       : [start] – [end]
Generated    : [date]
Prepared by  : [practitioner name or "Draft — review required"]

═══════════════════════════════════════════════════════════════
NARRATIVE SUMMARY
═══════════════════════════════════════════════════════════════
[3–5 sentence plain-English summary of key findings]

═══════════════════════════════════════════════════════════════
REVENUE TREND
═══════════════════════════════════════════════════════════════
Period    | Revenue (AED) | QoQ Growth% | YoY Growth%
──────────|───────────────|─────────────|────────────
...
T12M Total: AED [X]
CAGR (if applicable): [X]%

═══════════════════════════════════════════════════════════════
PROFITABILITY RATIOS
═══════════════════════════════════════════════════════════════
Period    | Gross Margin% | OpEx Ratio% | Net Margin%
...

═══════════════════════════════════════════════════════════════
VAT INPUT / OUTPUT PATTERN
═══════════════════════════════════════════════════════════════
Period    | Output VAT (AED) | Input VAT (AED) | Net Payable | Recovery%
...
T12M Taxable Supplies: AED [X] — [above/below/near] mandatory threshold

═══════════════════════════════════════════════════════════════
CORPORATE TAX INDICATIVE ESTIMATE
═══════════════════════════════════════════════════════════════
Estimated Taxable Income (pre-adjustment): AED [X]
Small Business Relief eligible?          : [Yes / No / Check]
Indicative CT Liability                  : AED [X]
  — 0% tier (first AED 375,000)          : AED 0
  — 9% tier (above AED 375,000)          : AED [X]
⚠ Pre-adjustment estimate only. Requires practitioner review.

═══════════════════════════════════════════════════════════════
ACTION FLAGS
═══════════════════════════════════════════════════════════════
[Bulleted list of items requiring review before client delivery]

═══════════════════════════════════════════════════════════════
VISUALIZATION DATA (JSON-ready)
═══════════════════════════════════════════════════════════════
{
  "periods": [...],
  "revenue": [...],
  "gross_margin_pct": [...],
  "net_margin_pct": [...],
  "vat_net_payable": [...]
}
```

## Quality checklist

- [ ] All figures in AED; no foreign currency mixed in without explicit note
- [ ] VAT thresholds checked against T12M taxable supplies
- [ ] CT Small Business Relief eligibility assessed and documented
- [ ] Free zone clients flagged for QFZP review before CT rate applied
- [ ] Any VAT anomaly (nil output, recovery ratio > 90%, QoQ jump > 50%) flagged
- [ ] CT estimate clearly marked as indicative / pre-adjustment
- [ ] Action flags list populated for every item requiring practitioner attention
- [ ] Visualization JSON arrays match the period labels and are correctly ordered
- [ ] No real client names — client ID only throughout
- [ ] Output reviewed by a qualified Finanshels team member before client delivery

## Examples

- "Here's a trial balance export for client C042 covering Jan–Dec 2024. Give me the full financial analysis with VAT patterns and CT exposure."
- "I need a management report input for a free zone client — revenue data attached. Flag anything relevant for their CT and check if they're near the VAT threshold."
- "Client hasn't registered for VAT yet. Analyse these 12 months of revenue and tell me if they're approaching the registration threshold."

## Guardrails

- CT liability figures produced by this skill are indicative only — pre-adjustment estimates based on net profit. Full CT adjustments (disallowable expenses, exempt income, related-party rules, transfer pricing) require practitioner review.
- QFZP 0% qualifying income determination must be performed by a qualified practitioner; this skill flags the issue but does not make the determination.
- All client financial data is strictly confidential. Do not include real client names, trade licence numbers, or EmaraTax TRNs in any output.
- UAE jurisdiction only. If a client has cross-border income or foreign subsidiaries, flag for specialist review — do not attempt to compute foreign tax obligations.
- Outputs are professional internal work products. Must be reviewed and signed off by a qualified Finanshels team member before being shared with clients.

## Reference

See ../_shared/finanshels-context.md for UAE tax facts, rates, and deadlines.
