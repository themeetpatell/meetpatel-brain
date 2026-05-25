---
name: tax-metrics-dashboard
description: Use when a Finanshels team lead, operations manager, or analyst needs to define, compute, or review firm-wide tax-compliance KPIs across the client portfolio. Triggers include requests to measure on-time filing rates, registration completion rates, return accuracy, deadline misses, or to produce a compliance health snapshot for a given period. Produces a structured KPI framework document and populates it from engagement data.
---

# Tax Metrics Dashboard

Firm-wide metrics framework for Finanshels tax-compliance operations — covering VAT returns, Corporate Tax filings, and registration workstreams.

## When to use

- A team lead asks: "How are we tracking on filing deadlines this quarter?"
- Operations needs a KPI report to present in a leadership sync
- A new tax period begins and the firm wants to baseline current compliance performance
- Post-period retrospective: which engagement types or client segments missed deadlines?
- Tracking improvement after a process change (e.g., new EmaraTax workflow)
- Building a dashboard spec for internal tooling or a BI tool integration

## Inputs needed

**Required**
- Reporting period (e.g., Q2 2025, financial year ended 31 Dec 2024)
- Engagement data export: list of active tax engagements with fields: client ID, engagement type (VAT / CT / Registration), due date, submitted date (or null if outstanding), status (submitted / pending / overdue / cancelled)

**Optional**
- Prior-period data for trend comparison
- Client segment breakdown (mainland / free zone, revenue tier)
- Practitioner-level attribution (for individual performance metrics)
- Target thresholds per KPI (defaults provided in framework if not supplied)

## Workflow

1. **Load and validate engagement data**
   - Accept data as a CSV, JSON object, or structured text paste
   - Validate required fields: client_id, engagement_type, due_date, submitted_date, status
   - Flag any records with missing due dates or unrecognised status values
   - Exclude cancelled engagements from rate calculations (document exclusion count separately)

2. **Compute core KPIs**

   **KPI 1 — On-Time Filing Rate (OTFR)**
   - Definition: percentage of submitted returns/registrations where submitted_date ≤ due_date
   - Formula: `OTFR = (on_time_submissions / total_due_submissions) × 100`
   - Segment by engagement type: VAT returns, CT returns, registrations
   - Target: ≥ 95% per engagement type per period

   **KPI 2 — Registration Completion Rate (RCR)**
   - Definition: percentage of registration engagements with FTA-confirmed registration number by the client's statutory deadline
   - Formula: `RCR = (registrations_completed_on_time / total_registration_engagements) × 100`
   - Note: registration deadlines vary by licence-issuance month — confirm against FTA notice for each client
   - Target: ≥ 98% (registration delays carry penalty risk for clients)

   **KPI 3 — Return Accuracy Rate (RAR)**
   - Definition: percentage of submitted returns accepted by EmaraTax without amendment or FTA query within 30 days of submission
   - Formula: `RAR = (returns_accepted_clean / total_returns_submitted) × 100`
   - Requires amendment/query log as supplementary input
   - Target: ≥ 97%

   **KPI 4 — Deadline Miss Count (DMC)**
   - Definition: absolute count of engagements where submitted_date > due_date OR status = overdue at end of reporting period
   - Segment by: engagement type, client segment, practitioner (if attributed)
   - Report as raw count and as percentage of total portfolio (Deadline Miss Rate)
   - Target: ≤ 2% Deadline Miss Rate

   **KPI 5 — Portfolio Coverage Rate (PCR)**
   - Definition: percentage of active clients with at least one engagement record in the period
   - Formula: `PCR = (clients_with_engagement / total_active_clients) × 100`
   - Flags clients who may have been inadvertently excluded from workflow
   - Target: 100%

3. **Segment and slice**
   - Break each KPI down by: engagement type, client type (mainland / free zone), revenue tier (≤ AED 3M / AED 3M–50M / > AED 50M)
   - If practitioner data is present, produce per-practitioner OTFR and DMC
   - Identify top-5 overdue engagements by days overdue

4. **Trend comparison (if prior period supplied)**
   - Calculate period-over-period delta for each KPI
   - Flag any KPI that declined by more than 3 percentage points as a "trend alert"

5. **Produce dashboard output**
   - Summary scorecard table (all KPIs, current value, target, RAG status)
   - Segmented breakdown tables
   - Top-5 overdue list with days overdue and responsible practitioner (if known)
   - Trend chart data (period labels + KPI values array) formatted for import into a BI tool or spreadsheet

6. **Recommendations**
   - For each KPI below target, produce one specific, actionable recommendation
   - Examples: "3 CT registration engagements are > 14 days overdue — escalate to senior practitioner and notify clients of FTA penalty risk"; "RAR of 94% is below 97% target — review amendment log for common error patterns"

7. **Run the metrics script**
   - Use `tools/metrics-framework.py` to compute KPIs from a CSV or inline synthetic data
   - Command: `python3 tools/metrics-framework.py`
   - Script prints the full KPI table and overdue list to stdout

## Output format

```
FINANSHELS — TAX COMPLIANCE METRICS DASHBOARD
Reporting Period: [period]
Generated: [date]

═══════════════════════════════════════════════════════
KPI SCORECARD
═══════════════════════════════════════════════════════
KPI                          | Value  | Target | Status
─────────────────────────────|--------|--------|───────
On-Time Filing Rate (OTFR)   | 96.2%  | ≥ 95%  | GREEN
  — VAT returns              | 97.1%  |        |
  — CT returns               | 94.0%  |        | AMBER
  — Registrations            | 98.5%  |        |
Registration Completion Rate | 98.5%  | ≥ 98%  | GREEN
Return Accuracy Rate         | 96.0%  | ≥ 97%  | AMBER
Deadline Miss Count          | 4      | ≤ 2%   | GREEN
  Deadline Miss Rate         | 1.8%   |        |
Portfolio Coverage Rate      | 100%   | 100%   | GREEN

═══════════════════════════════════════════════════════
TOP OVERDUE ENGAGEMENTS
═══════════════════════════════════════════════════════
Client ID | Type | Due Date   | Days Overdue | Practitioner
──────────|───---|────────────|──────────────|─────────────
...

═══════════════════════════════════════════════════════
RECOMMENDATIONS
═══════════════════════════════════════════════════════
1. [Specific action for each AMBER/RED KPI]

═══════════════════════════════════════════════════════
TREND vs PRIOR PERIOD
═══════════════════════════════════════════════════════
[Table if prior period data supplied]
```

RAG thresholds: GREEN = at or above target; AMBER = within 3pp below target; RED = more than 3pp below target.

## Quality checklist

- [ ] All five KPIs computed and presented
- [ ] Each KPI segmented by engagement type (at minimum)
- [ ] Cancelled engagements excluded from rate denominators and documented
- [ ] Deadline Miss Count cross-checks against OTFR calculation (both consistent)
- [ ] Every AMBER/RED KPI has at least one concrete recommendation
- [ ] No real client names or identifiers in the output — client IDs only
- [ ] All dates in DD/MM/YYYY format (UAE business convention)
- [ ] Currency figures in AED
- [ ] Trend section present if prior-period data was supplied
- [ ] Output reviewed by a qualified Finanshels team member before sharing externally

## Examples

- "Give me the compliance dashboard for our VAT and CT portfolio for Q1 FY2025 — here's the engagement CSV."
- "We had three CT registrations overdue last month. Run the metrics so I can see where we stand overall and what's driving it."
- "I need the KPI scorecard for the leadership meeting on Friday — compare this quarter to last quarter."

## Guardrails

- Output is a professional internal work product. Must be reviewed by a qualified Finanshels team member before presentation to clients or management outside the immediate team.
- UAE jurisdiction only. No reference to IRS, US tax forms, CPE credits, or non-UAE deadlines.
- All client data is confidential. Use anonymised client IDs in all outputs. Never record, log, or repeat real client names or trade licence numbers.
- KPI targets listed here are Finanshels internal operational targets, not FTA thresholds. Do not present them as regulatory requirements.
- Penalty risk guidance (e.g., late filing penalties) must always direct the user to verify current FTA penalty schedules — rates change.

## Reference

See ../_shared/finanshels-context.md for UAE tax facts, rates, and deadlines.
