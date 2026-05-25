---
name: client-profitability-analyzer
description: Use when a Finanshels manager or director wants to assess profitability by client or client segment — comparing revenue against service hours and internal cost to identify which engagements are profitable, break-even, or loss-making. Produces a ranked profitability table, flags unprofitable clients, and recommends specific pricing or scope actions. Trigger phrases include "which clients are losing us money", "is this engagement profitable", "review our client portfolio margins", or "where should we reprice".
---

# Client Profitability Analyzer

Calculates gross margin by client or segment, surfaces unprofitable engagements, and recommends concrete pricing or scope actions.

## When to use

- Quarterly or annual portfolio review — understanding which clients drive profit and which drain it
- Before a renewal conversation — confirming whether the current fee covers actual hours
- After a team capacity crunch — identifying whether low-margin clients are consuming disproportionate resource
- When considering a fee increase — building the internal case with data
- When evaluating whether to offboard a client — backing the decision with margin analysis
- Segment analysis — comparing profitability by service type, entity type, or revenue band

## Inputs needed

**Required**
- `client_list`: A table or list with, for each client:
  - Client code (internal reference)
  - Monthly or annual fee (AED, excl. VAT)
  - Actual hours logged per month or per year
  - Primary service type(s): bookkeeping / VAT / CT / CFO / audit support
- `blended_hourly_rate_aed`: Internal cost rate to use (default: AED 200/hr if not provided)

**Optional**
- `staff_allocation`: Which role(s) service each client (Accountant / Senior / Manager) — enables more precise cost calculation using role-specific rates
- `engagement_tier`: Tier 1–5 classification per client (if already known)
- `entity_type`: Mainland / Free Zone / Branch
- `complexity_flags`: Any known flags (multi-currency, QFZP, related-party, catch-up) that explain high hours
- `target_margin_pct`: Desired gross margin percentage (default: 40% if not provided)
- `period`: The month, quarter, or year being analysed

## Workflow

1. **Build the profitability table**
   For each client, calculate:
   - `revenue_aed`: Fee received for the period (excl. VAT)
   - `cost_aed`: Hours logged × blended rate (or role-specific rate if staff allocation is provided)
   - `gross_profit_aed`: revenue − cost
   - `gross_margin_pct`: gross_profit / revenue × 100
   - `effective_rate_aed_per_hr`: revenue / hours logged
   Sort the table from highest to lowest gross margin.

2. **Segment the portfolio**
   Group clients into four buckets:
   - **Healthy** (gross margin ≥ target, typically ≥ 40%): No immediate action needed
   - **At Risk** (gross margin 20–39%): Monitor; schedule renewal review
   - **Break-Even** (gross margin 0–19%): Fee increase or scope reduction required
   - **Loss-Making** (gross margin < 0%): Urgent — escalate to Director

3. **Identify root causes for underperforming clients**
   For each At Risk / Break-Even / Loss-Making client, investigate and label the likely cause:
   - **Scope creep**: Hours consistently exceed engagement scope (unbounded requests, ad-hoc queries)
   - **Underpricing**: Fee was set too low at outset relative to actual complexity
   - **Inefficiency**: Hours are high but comparable clients take less time — process or staff issue
   - **Complexity uplift not charged**: Client has complexity flags (multi-currency, catch-up) not reflected in the fee
   - **Relationship/anchor client**: Deliberately priced low for strategic reasons — document and ring-fence
   Flag where the root cause is unclear and a conversation with the engagement owner is needed.

4. **Calculate portfolio-level metrics**
   - Total portfolio revenue (AED)
   - Total portfolio cost (AED)
   - Overall portfolio gross margin (%)
   - Revenue concentration: top 3 clients as % of total revenue (flag if > 50% — concentration risk)
   - % of clients in each bucket (Healthy / At Risk / Break-Even / Loss-Making)
   - Weighted average effective rate (AED/hr)

5. **Generate recommendations**
   For each underperforming client, produce a specific action:
   - **Fee increase**: Calculate the fee required to reach target margin; express as % increase and AED delta
   - **Scope cap**: Recommend a monthly hour cap or scope clause to prevent further overrun
   - **Scope reduction**: Identify which service components could be removed or made ad-hoc
   - **Efficiency target**: Where inefficiency is the cause, set a target hours reduction (e.g. "reduce from 20 to 14 hrs/month by implementing bank feed automation")
   - **Offboard review**: Where the client is loss-making, complexity flags are high, and a fee increase is unlikely to be accepted — flag for Director-level decision on whether to continue the engagement
   Label each recommendation: **Immediate** (this billing cycle) / **Next renewal** / **Review meeting needed**.

6. **Produce the segment summary and action register**
   Compile the output as described below.

## Output format

```
CLIENT PROFITABILITY ANALYSIS
Period: [month/quarter/year]
Prepared: [YYYY-MM-DD]
Blended rate used: AED [X]/hr    Target margin: [X]%

─────────────────────────────────────────
1. PORTFOLIO SUMMARY

Total revenue:          AED XXX,XXX
Total cost:             AED XXX,XXX
Gross profit:           AED XXX,XXX
Portfolio margin:       XX%
Weighted avg rate:      AED XXX/hr
Revenue concentration:  Top 3 clients = XX% of revenue [flag if > 50%]

Bucket breakdown:
  Healthy (≥40%):       N clients — AED XXX,XXX revenue
  At Risk (20–39%):     N clients — AED XXX,XXX revenue
  Break-Even (0–19%):   N clients — AED XXX,XXX revenue
  Loss-Making (<0%):    N clients — AED XXX,XXX revenue

─────────────────────────────────────────
2. CLIENT PROFITABILITY TABLE (ranked by margin)

Code   Service type   Revenue    Hours   Cost      GP        Margin   Rate/hr   Bucket
─────────────────────────────────────────────────────────────────────────────────────
A001   BK + VAT       AED 3,500  12      AED 2,400 AED 1,100  31%    AED 292   At Risk
A002   BK only        AED 2,000  16      AED 3,200 AED (1,200) (60%) AED 125   Loss-Making
...

─────────────────────────────────────────
3. UNDERPERFORMING CLIENT ANALYSIS

## Client [code] — [Bucket]
Service: [type]   Fee: AED X,XXX/mo   Actual hrs: XX   Margin: XX%
Root cause: [Scope creep / Underpricing / Inefficiency / Complexity not charged / Strategic]
Detail: [1–2 sentences]
Recommendation: [specific action]
Target fee: AED X,XXX/mo (to achieve [target]% margin)   Increase: +AED XXX/mo (+XX%)
Priority: [Immediate / Next renewal / Review meeting needed]

## Client [code] — ...

─────────────────────────────────────────
4. ACTION REGISTER

Priority   Client code   Action                         Owner      Deadline
─────────────────────────────────────────────────────────────────────────
Immediate  A002          Fee increase discussion        Manager    [date]
Immediate  A002          Scope cap clause in letter     Manager    [date]
Next renewal A007        Reprice at renewal             Acct Mgr   [date]
Review     A011          Director decision: continue?   Director   [date]

─────────────────────────────────────────
NOTES & ASSUMPTIONS
- Cost calculated at AED [X]/hr blended [or role-specific rates listed]
- Hours sourced from [time-tracking system / team input / estimate — flag if estimated]
- Clients marked Strategic are excluded from reprice recommendations pending Director sign-off
- VAT not included in revenue or fee figures
- This analysis is for internal use only. Validate with engagement owners before actioning.
```

## Quality checklist

- [ ] All clients in the input list appear in the output table
- [ ] Gross margin formula is correctly applied (revenue − cost, not revenue alone)
- [ ] Blended rate used is stated clearly in the output header
- [ ] Each underperforming client has a labelled root cause (not just a number)
- [ ] Each recommendation specifies the target fee in AED (not just a percentage)
- [ ] Revenue concentration risk flagged if top 3 clients > 50% of portfolio
- [ ] Loss-Making clients are flagged for Director escalation
- [ ] Action register includes owner and deadline for each action
- [ ] VAT excluded from all fee and revenue figures (stated in notes)
- [ ] Strategic/anchor clients are ring-fenced and noted separately

## Examples

**Example 1**
> "Analyse profitability for our bookkeeping portfolio of 12 clients. I'll paste in the client codes, monthly fees, and hours. Blended rate is AED 210/hr. Target margin is 40%."

Expected: Ranked table of 12 clients, portfolio margin calculated, 3–4 clients flagged as At Risk or worse, specific fee-increase amounts recommended for each, action register with owners.

**Example 2**
> "Is our VAT filing service profitable? We have 25 quarterly-filing clients averaging AED 1,800/filing fee and 9 hours per return. Senior Accountant rate AED 260/hr."

Expected: Quick per-client calculation showing AED 2,340 cost vs. AED 1,800 revenue = (AED 540) loss per filing, root cause: underpricing, recommendation to reprice to AED 2,800–3,200/filing to achieve 40% margin.

**Example 3**
> "Run a segment comparison: are our free zone clients more or less profitable than mainland clients? Mix of bookkeeping and CT engagements, AED 200/hr blended."

Expected: Side-by-side segment table (free zone vs. mainland), portfolio margin for each segment, hypothesis on why free zone clients may be less profitable (QFZP complexity, audit requirement, TP disclosure), recommendations by segment.

## Guardrails

- UAE jurisdiction only. All fees in AED. Never reference IRS, US states, or CPE.
- This analysis is a professional work product for internal management use. It must be reviewed by a Director or manager before any client pricing conversation takes place.
- Do not share profitability data for one client with another client or with the client themselves.
- Root-cause labels are hypotheses based on numbers — always validate with the engagement owner before taking action.
- Hours data quality directly determines the reliability of this analysis. Flag clearly if hours are estimated rather than tracked.
- Client financial data is confidential. Never include real client names or identifiers in outputs.

## Reference

See `../_shared/finanshels-context.md` for UAE tax facts, rates, and deadlines.
