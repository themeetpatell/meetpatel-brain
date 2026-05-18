---
name: financial-dashboard-brief
description: Use when Finanshels leadership needs a concise executive summary memo synthesizing the firm's monthly KPIs — revenue, utilisation, client count, margin, compliance delivery rate, and team metrics — into a clear, decision-ready brief. Accepts raw KPI data and produces a structured one-page memo suitable for a leadership meeting, investor update, or board pack. Trigger phrases include "write the monthly KPI summary", "prepare the management memo", "summarise this month's dashboard", or "draft the leadership brief".
---

# Financial Dashboard Brief

Turns monthly firm KPI data into a clear, concise executive memo — one page, decision-ready, consistent every month.

## When to use

- Monthly leadership or management meeting preparation
- Board or investor update requiring a firm performance summary
- End-of-month close — synthesizing numbers from finance, operations, and delivery into one document
- When a partner or director needs a fast read on how the business is performing
- Preparing a rolling MoM or YoY trend narrative alongside the numbers

## Inputs needed

**Required**
- `period`: Month and year (e.g. "April 2026")
- `revenue_aed`: Total revenue collected or recognised in the period (AED, excl. VAT)
- `gross_profit_aed`: Revenue minus direct service delivery cost (AED)
- `active_clients`: Number of active clients at month-end
- `team_headcount`: Total FTE at month-end

**Optional (include all available for a richer memo)**
- `revenue_prior_month_aed`: For MoM comparison
- `revenue_prior_year_aed`: For YoY comparison
- `target_revenue_aed`: Monthly revenue target, if set
- `billable_hours_total`: Total hours logged across all staff
- `billable_hours_target`: Target hours for the month
- `average_utilisation_pct`: Team utilisation rate (billable / available hours × 100)
- `new_clients_added`: Clients onboarded this month
- `clients_churned`: Clients who ended engagement this month
- `vat_returns_filed`: Number of VAT returns filed on time vs. total due
- `ct_returns_filed`: Number of CT returns filed on time vs. total due
- `outstanding_receivables_aed`: Accounts receivable balance at month-end
- `overdue_receivables_aed`: Receivables > 30 days overdue
- `cash_balance_aed`: Firm cash balance at month-end (if shared with the brief)
- `top_wins`: 1–3 notable events (new client won, service launched, deal closed)
- `key_risks`: 1–3 items the leadership team should be aware of
- `actions_from_last_month`: Status of last month's action items (provided as free text)

## Workflow

1. **Validate inputs and flag missing data**
   Before writing, check that the Required fields are present. If any are missing, list them and request before proceeding. For Optional fields, note in the memo where data was unavailable (e.g. "Utilisation data not provided this month").

2. **Calculate derived metrics**
   From the inputs, compute:
   - `gross_margin_pct`: gross_profit / revenue × 100
   - `revenue_per_client_aed`: revenue / active_clients
   - `revenue_per_fte_aed`: revenue / headcount
   - `mom_revenue_change_pct`: (current − prior_month) / prior_month × 100 (if prior month provided)
   - `yoy_revenue_change_pct`: (current − prior_year) / prior_year × 100 (if prior year provided)
   - `vs_target_pct`: (current − target) / target × 100 (if target provided)
   - `compliance_delivery_rate`: returns filed on time / total due × 100 (VAT and CT combined)
   - `receivables_overdue_pct`: overdue_receivables / outstanding_receivables × 100

3. **Write the narrative headline**
   One sentence that captures the single most important thing about this month's performance — positive or negative. Be direct. Examples:
   - "April delivered AED 187K revenue, 8% above target, on the back of three new client onboardings and strong VAT filing season throughput."
   - "March revenue came in at AED 142K, 11% below target, driven by two client pauses and lower-than-expected CT engagement starts."

4. **Write the section narratives**
   For each section in the output format, write 1–3 plain-English sentences that interpret the numbers — not just restate them. Focus on: what changed, why it changed, and what it means for next month. Flag any metric that is off-track or trending in the wrong direction with a clear, calm statement (not alarmist).

5. **Draft the actions and decisions section**
   Synthesize the key follow-up items. Each action must have an owner (by role, not name) and a deadline. Maximum 5 actions — if more exist, the most important 5 only.

6. **Final quality pass**
   - All numbers must be consistent (check that gross profit / revenue = stated margin %)
   - No jargon without explanation
   - Tone: confident, factual, helpful — not defensive or promotional
   - Length: fits on one page when printed at normal font size (~600–900 words in the narrative)

## Output format

```
FINANSHELS — MONTHLY PERFORMANCE BRIEF
Period: [Month YYYY]          Prepared: [YYYY-MM-DD]
Confidential — Internal use only

─────────────────────────────────────────
HEADLINE

[One-sentence summary of the month]

─────────────────────────────────────────
1. REVENUE & MARGIN

Revenue:          AED XXX,XXX    [vs. AED XXX,XXX target — X% | vs. prior month +/-X% | vs. prior year +/-X%]
Gross profit:     AED XXX,XXX
Gross margin:     XX%
Revenue/client:   AED X,XXX
Revenue/FTE:      AED XX,XXX

[2–3 sentence narrative: what drove revenue this month, any notable variances, trend direction]

─────────────────────────────────────────
2. CLIENT PORTFOLIO

Active clients:   XX             [+N new | -N churned]
New onboarded:    N
Churned:          N              [reason if known]
Net movement:     +/-N

[1–2 sentence narrative: growth momentum, any churn risks on the horizon]

─────────────────────────────────────────
3. TEAM & UTILISATION

Headcount:           N FTE
Billable hours:      XXX hrs     [vs. XXX target — XX%]
Avg utilisation:     XX%         [target: XX%]

[1–2 sentence narrative: capacity headroom or pressure, any months ahead that will stress capacity]

─────────────────────────────────────────
4. COMPLIANCE DELIVERY

VAT returns:      XX filed / XX due   [XX% on time]
CT returns:       XX filed / XX due   [XX% on time]
Overall delivery rate: XX%

[1–2 sentence narrative: any late filings, cause, and corrective action taken. If 100% on time, state it clearly — this is a key quality signal.]

─────────────────────────────────────────
5. RECEIVABLES & CASH

Outstanding receivables:  AED XXX,XXX
Overdue (> 30 days):      AED XXX,XXX   [XX% of total]
Cash balance:             AED XXX,XXX   [if provided]

[1–2 sentence narrative: collections health, any clients requiring follow-up, cash runway if relevant]

─────────────────────────────────────────
6. HIGHLIGHTS

+ [Win or positive event 1]
+ [Win or positive event 2]
+ [Win or positive event 3]

─────────────────────────────────────────
7. RISKS & WATCH ITEMS

! [Risk or concern 1 — factual, one line]
! [Risk or concern 2]
! [Risk or concern 3]

─────────────────────────────────────────
8. ACTIONS & DECISIONS

#  Action                                Owner        Due
1  [Specific action]                     [Role]       [date]
2  [Specific action]                     [Role]       [date]
3  [Specific action]                     [Role]       [date]

─────────────────────────────────────────
LAST MONTH'S ACTIONS — STATUS UPDATE

[Item from last month]: [Done / In progress / Carried forward — brief status]
[Item from last month]: ...

─────────────────────────────────────────
All figures in AED, excl. VAT.
Verify FTA compliance deadlines against current EmaraTax guidance.
```

## Quality checklist

- [ ] Headline is one sentence and genuinely summarises the month (not generic)
- [ ] All stated percentages are mathematically consistent with the AED figures
- [ ] Each section has a narrative — not just numbers restated
- [ ] Compliance delivery rate is calculated and stated explicitly (this is a brand signal)
- [ ] Any metric off-target is named clearly with a factual explanation
- [ ] Actions section has no more than 5 items, each with an owner and deadline
- [ ] Last month's action items have a status update (if provided)
- [ ] Tone is confident and factual — no defensive language, no inflation of wins
- [ ] Length is suitable for a one-page leadership read (~600–900 words narrative)
- [ ] "Confidential — Internal use only" is on the document

## Examples

**Example 1**
> "Here are April 2026 numbers: revenue AED 193K (target AED 180K), gross profit AED 89K, 47 active clients (3 new, 1 churned), team of 8, utilisation 78%, 22 VAT returns all on time, receivables AED 41K with AED 8K overdue. Highlights: won a new CFO retainer client. Risk: one large client has paused for two months."

Expected: Full memo with all 8 sections, headline noting above-target revenue, compliance section stating 100% on-time, risk section flagging the paused client with a revenue impact estimate.

**Example 2**
> "Write the May brief. Revenue AED 154K (target AED 175K, prior month AED 168K), margin 41%, 44 clients, headcount 7, utilisation 82%, 18 of 19 VAT returns filed on time (one late due to client data delay), overdue receivables AED 22K."

Expected: Headline acknowledges below-target month, revenue section explains MoM and vs-target gaps, compliance section notes the one late filing and its cause, actions include a collections follow-up and client data SLA review.

**Example 3**
> "Monthly brief for Q4 planning context — October 2026. Highlight that CT return season for Dec year-ends is 11 months away and capacity planning should start now."

Expected: Standard brief plus a specific risk/action item noting that December year-end CT returns will be due by September 2027 — capacity planning and client financial year-end prep should begin Q1 2027.

## Guardrails

- UAE jurisdiction only. All figures in AED. Never reference IRS, US states, or CPE.
- This memo is for internal leadership use only. It must not be shared externally without Director approval.
- Mark every output "Confidential — Internal use only."
- Do not include individual staff names — use role titles only.
- Compliance delivery metrics are a quality and brand signal — report them honestly, even if the result is unflattering.
- This is a professional work product to be reviewed by the responsible Director before distribution.

## Reference

See `../_shared/finanshels-context.md` for UAE tax facts, rates, and deadlines.
