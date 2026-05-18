---
name: benchmark-analyzer-tax
description: Use when a Finanshels practitioner, analyst, or outsourced CFO team member needs to compare a client's or the firm's financial and compliance performance against industry benchmarks. Triggers include requests for a gap analysis, a benchmark report, "how does this client compare to peers", or a health check against UAE tax-compliance and profitability norms. Produces a structured benchmark report with scored metrics, gap analysis table, and prioritised improvement actions.
---

# Benchmark Analyzer — Tax & Finance

Compares a client's financial ratios and tax-compliance metrics against UAE industry benchmarks, identifies performance gaps, and produces a scored benchmark report with prioritised recommendations.

## When to use

- A client asks: "How do our margins compare to similar UAE businesses?"
- Pre-CT-return advisory: assess whether a client's effective tax rate looks reasonable vs. peers
- Outsourced CFO engagement: produce a benchmark health check as part of a quarterly board pack
- Onboarding a new client: establish a baseline and identify quick wins
- Internal firm review: assess Finanshels' own compliance KPIs against professional-services norms
- Investor or lender asks for a peer-comparison view of the client's financials
- Identifying whether a client's VAT recovery ratio or tax burden is an outlier warranting investigation

## Inputs needed

**Required**
- Subject type: `client` or `firm` (determines which benchmark set to use)
- For `client`: client ID, industry sector, set of financial metrics for the period (gross margin, net margin, OpEx ratio, VAT recovery ratio, and/or CT effective rate)
- For `firm`: Finanshels internal KPI values (OTFR, RCR, RAR, DMR, PCR — from the `tax-metrics-dashboard` skill)
- Analysis period

**Optional**
- Client entity type (mainland / free zone) — affects CT benchmark interpretation
- Revenue tier (≤ AED 3M / AED 3M–50M / > AED 50M) — used to select the right peer group
- Prior-period actuals for trend-adjusted gap analysis
- Custom benchmark targets if the client or firm has set their own

## Workflow

1. **Select benchmark set**

   For `client` subjects, use the sector benchmarks defined in `tools/benchmark-queries.py`. Sectors currently supported:
   - `professional_services` (accounting, consulting, legal)
   - `trading_retail` (goods import/export, retail)
   - `technology` (SaaS, IT services, digital)
   - `hospitality_food` (F&B, hotels, tourism)
   - `construction_contracting`
   - `general` (use if sector unknown — widest band ranges)

   For `firm` subjects, use the firm-KPI benchmark set (professional services compliance norms).

2. **Compute subject metrics**
   - If raw financial data is provided, compute ratios using the same method as `client-data-analyzer`:
     - Gross margin: `(Revenue − CoS) / Revenue × 100`
     - Net margin: `Net Profit / Revenue × 100`
     - OpEx ratio: `Operating Expenses / Revenue × 100`
     - VAT recovery ratio: `Input VAT / Output VAT × 100`
     - Effective CT rate: `CT Liability / Net Profit × 100` (indicative — requires practitioner adjustment)
   - If pre-computed metrics are supplied, use directly

3. **Run gap analysis for each metric**
   - For each metric, compare subject value against: benchmark median, benchmark lower quartile (Q1), benchmark upper quartile (Q3)
   - Classify position:
     - ABOVE: subject > Q3 benchmark → strong performance
     - WITHIN: Q1 ≤ subject ≤ Q3 → within normal range
     - BELOW: subject < Q1 benchmark → underperforming vs. peers
   - Calculate gap to median: `gap = subject_value − benchmark_median`
   - Calculate gap to Q3 (upside to top-quartile): `upside = Q3 − subject_value` (positive = room to improve)

4. **Score overall performance**
   - Assign points per metric: ABOVE = 2, WITHIN = 1, BELOW = 0
   - Compute overall score: `total_points / (2 × number_of_metrics) × 100`
   - Grade: 80–100 = Strong, 60–79 = Satisfactory, 40–59 = Needs Attention, 0–39 = Underperforming

5. **Generate gap analysis table**
   - One row per metric
   - Columns: Metric, Subject Value, Benchmark Q1, Benchmark Median, Benchmark Q3, Position, Gap to Median, Upside to Q3

6. **Prioritise recommendations**
   - For each BELOW metric: produce a specific, actionable recommendation
   - Order by: (1) CT/compliance risk → (2) profitability impact → (3) operational efficiency
   - For ABOVE metrics: briefly note the strength (affirmation)
   - Limit to top 5 recommendations to keep the report actionable

7. **Produce benchmark report**
   - Overall score and grade
   - Gap analysis table
   - Prioritised recommendations
   - Benchmark data source note (internal Finanshels reference benchmarks — not published FTA data)

8. **Run the benchmark script**
   - Use `tools/benchmark-queries.py` to reproduce the gap analysis
   - Command: `python3 tools/benchmark-queries.py`
   - Script prints a full benchmark report from synthetic subject metrics vs. stored benchmarks

## Output format

```
FINANSHELS — BENCHMARK ANALYSIS REPORT
Client/Subject ID : [ID]
Sector            : [sector]
Revenue Tier      : [tier]
Period            : [period]
Generated         : [date]

═══════════════════════════════════════════════════════════════════
OVERALL BENCHMARK SCORE
═══════════════════════════════════════════════════════════════════
Score: [X / 100]    Grade: [Strong / Satisfactory / Needs Attention / Underperforming]

═══════════════════════════════════════════════════════════════════
GAP ANALYSIS TABLE
═══════════════════════════════════════════════════════════════════
Metric            | Subject | Bmark Q1 | Bmark Med | Bmark Q3 | Position | Gap to Med | Upside to Q3
──────────────────|---------|----------|-----------|----------|----------|------------|─────────────
Gross Margin %    |   42.0% |    35.0% |     43.0% |    55.0% | WITHIN   |      -1.0% |      +13.0%
Net Margin %      |   12.0% |    10.0% |     15.0% |    22.0% | BELOW    |      -3.0% |      +10.0%
OpEx Ratio %      |   22.0% |    18.0% |     22.0% |    28.0% | WITHIN   |       0.0% |      +6.0%
VAT Recovery %    |   47.0% |    30.0% |     45.0% |    60.0% | WITHIN   |      +2.0% |      +13.0%
Effective CT Rate |    5.5% |     3.0% |      5.0% |     8.0% | WITHIN   |      +0.5% |      +2.5%

═══════════════════════════════════════════════════════════════════
STRENGTHS
═══════════════════════════════════════════════════════════════════
- [Metric]: subject is above Q3 benchmark — [brief note]

═══════════════════════════════════════════════════════════════════
PRIORITISED RECOMMENDATIONS
═══════════════════════════════════════════════════════════════════
1. [Most important — CT/compliance risk first]
2. ...

═══════════════════════════════════════════════════════════════════
BENCHMARK DATA NOTE
═══════════════════════════════════════════════════════════════════
Benchmarks are Finanshels internal reference ranges derived from
aggregated anonymised client data and sector research. They are
indicative only and do not represent published FTA statistics.
Confirm any material findings against authoritative sources.
```

## Quality checklist

- [ ] Correct benchmark set selected for the subject type and sector
- [ ] All subject metrics computed consistently (same method as `client-data-analyzer`)
- [ ] Gap analysis table populated for every available metric
- [ ] Overall score and grade present
- [ ] Recommendations ordered by CT/compliance risk first, then profitability
- [ ] Top-5 recommendation limit respected — report is focused, not a laundry list
- [ ] Benchmark data note included; benchmarks not presented as FTA-published figures
- [ ] Effective CT rate flagged as indicative (pre-adjustment)
- [ ] No real client names or identifiers in output
- [ ] Output reviewed by a qualified Finanshels team member before client delivery

## Examples

- "Run a benchmark report for client C099 — professional services sector, Q4 2024 metrics attached."
- "How does the firm's compliance KPI score compare to best-practice benchmarks? Use last quarter's dashboard data."
- "I'm putting together a board pack for a tech client. I need a peer comparison on margins and VAT recovery."

## Guardrails

- Benchmark ranges are Finanshels internal reference data — indicative only. They must not be presented to clients as official FTA statistics, published industry surveys, or regulatory benchmarks.
- Effective CT rate comparisons are based on indicative (pre-adjustment) net profit. Full CT comparison requires adjusted taxable income computed by a qualified practitioner.
- For free zone clients: do not interpret benchmark CT rates as a target without first confirming QFZP qualifying income status with a practitioner.
- UAE jurisdiction only. Do not apply non-UAE benchmark data (e.g., UK HMRC sector statistics, US IRS data).
- All client data is confidential. Use anonymised client IDs in all outputs. Never log or transmit real client names, TRNs, or trade licence numbers.
- Output is a professional internal work product. Must be reviewed by a qualified Finanshels team member before being shared with clients or third parties.

## Reference

See ../_shared/finanshels-context.md for UAE tax facts, rates, and deadlines.
