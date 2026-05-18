---
name: resource-planner
description: Use when Finanshels leadership needs to match current team capacity against projected workload for a quarter or full year — accounting for the UAE compliance calendar (VAT deadlines, CT filing peaks, audit season) — and produce a capacity forecast with hiring or load-balancing recommendations. Trigger phrases include "do we have enough capacity for Q3", "plan headcount for next year", "when will the team be overloaded", "CT filing season resourcing", or "should we hire another accountant".
---

# Resource Planner

Maps projected client workload against team capacity month by month, identifies overload periods driven by UAE compliance peaks, and produces a hiring or load-balancing forecast.

## When to use

- Annual or quarterly planning — building the headcount budget before the period starts
- Before accepting a batch of new clients — sense-checking whether the team can absorb them
- After a capacity crunch — diagnosing which months were over-allocated and why
- Filing-season preparation — VAT quarter-ends (Mar/Jun/Sep/Dec) and CT return peaks
- When a staff member leaves or goes on extended leave — rebalancing the remaining load
- Growth planning — calculating how many clients each new hire unlocks

## Inputs needed

**Required**
- `planning_period`: Quarter (Q1/Q2/Q3/Q4 + year) or full year (e.g. "FY2026")
- `team_roster`: For each team member:
  - Role: Accountant / Senior Accountant / Manager / Director
  - Available hours/month (default: 140 billable hrs/month per full-time staff member)
  - Any known leave, part-time arrangements, or planned absence
- `current_client_portfolio`: Number of active clients and estimated monthly hours per client (or total hours by service type per month)

**Optional**
- `pipeline_clients`: New clients expected to onboard during the planning period, with estimated start month and hours/month
- `service_mix`: Breakdown of portfolio by service type — bookkeeping, VAT, CT, CFO retainer, audit support
- `financial_year_ends`: List of client year-end months (to predict CT return demand spikes)
- `vat_filing_mix`: How many clients file quarterly vs. monthly, and which quarter-end months are busiest
- `target_utilisation_pct`: Desired billable utilisation (default: 75% — leaving 25% for admin, training, and buffer)
- `hiring_lead_time_weeks`: How many weeks from decision to hire being productive (default: 8 weeks)
- `notes`: Known special factors (e.g. "we expect to win a CFO retainer for 30 hrs/month in August")

## Workflow

1. **Calculate available capacity by role and month**
   For each staff member, compute monthly available billable hours:
   - Full-time: 140 hrs/month × utilisation target (default 75%) = 105 productive hrs/month
   - Deduct any leave or part-time hours in specific months
   - Sum by role tier: total Accountant hrs, total Senior hrs, total Manager hrs
   Express as a monthly capacity table for the planning period.

2. **Map the UAE compliance calendar onto the demand curve**
   Overlay the following recurring demand spikes — these are non-negotiable and must be staffed before discretionary work:

   **VAT filing peaks (quarterly filers — most common)**
   - Q1 returns: due 28 April — demand spike in April
   - Q2 returns: due 28 July — demand spike in July
   - Q3 returns: due 28 October — demand spike in October
   - Q4 returns: due 28 January — demand spike in January

   **VAT filing (monthly filers)**
   - Due 28th every month — steady load, no seasonal spike

   **Corporate Tax return peaks**
   - Returns due within 9 months of financial year-end
   - For 31 Dec year-ends (most common): CT return due by 30 September — demand spike Aug–Sep
   - For 31 Mar year-ends: CT return due by 31 December — demand spike Nov–Dec
   - Map each client's year-end to predict the CT demand month
   - CT registration deadlines: staggered by licence-issuance month — add to calendar if new registrations are pending

   **Audit support**
   - Typically Jan–Mar for Dec year-end clients (auditor fieldwork season)
   - Peaks 6–8 weeks before client's audit completion deadline

   **Payroll**
   - Steady monthly load; spike in December/January (annual leave payout, bonus processing)

3. **Calculate projected demand by month**
   For each month in the planning period, sum:
   - Recurring monthly hours (bookkeeping, CFO retainers, monthly VAT filers)
   - Periodic hours (quarterly VAT filings in peak months, CT returns, audit support)
   - Onboarding hours for pipeline clients in their start month
   - Any known ad-hoc / project work
   Separate demand by role tier where staff allocation data is available.

4. **Compute the capacity gap**
   For each month:
   - `gap_hours = demand_hours − available_capacity_hours`
   - Positive gap = overloaded (demand exceeds capacity)
   - Negative gap = underutilised (capacity available for new clients or projects)
   Calculate utilisation rate: `demand / available_capacity × 100%`
   Flag any month where utilisation exceeds **90%** as a red alert (high overload risk).
   Flag months between **75–90%** as amber (watch closely).

5. **Identify hiring or load-balancing actions**
   For each red or amber month:

   **Option A — Hire**
   - Calculate how many additional FTE (or part-time) are needed to bring utilisation below 80%
   - Apply hiring lead time (default 8 weeks): if overload is in month M, hire decision needed by M − 8 weeks
   - Specify the required role tier (Accountant for volume work, Senior for review-heavy months)

   **Option B — Load-balance**
   - Pull forward preparation work from peak month to the preceding lighter month (e.g. gather CT data in July for a September filing)
   - Stagger client VAT filing frequencies where allowed (move some quarterly filers to reduce April/July/October bunching)
   - Reassign lower-complexity clients from Senior to Accountant to free up review capacity

   **Option C — Defer or decline**
   - If overload is severe (> 110% utilisation) and hiring lead time cannot close the gap: flag specific pipeline clients or service expansions that should be deferred or referred out

6. **Build the capacity forecast table**
   Produce month-by-month output for the full planning period.

7. **Produce the hiring plan**
   If hiring is recommended, specify:
   - Role to hire
   - Month when hire must be productive (i.e. start by M − 8 weeks)
   - Hours unlocked per month by the new hire
   - Estimated additional revenue capacity at blended rate (new hire hours × AED/hr)

## Output format

```
RESOURCE & CAPACITY FORECAST
Period: [planning period]
Prepared: [YYYY-MM-DD]
Team size: [N FTE]   Target utilisation: [X]%   Billable hrs assumption: 140/mo/FTE

─────────────────────────────────────────
1. TEAM CAPACITY SUMMARY

Role               Headcount   Hrs/mo available   Planning period total
─────────────────────────────────────────────────────────────────────
Accountant         N           XXX                XXX
Senior Accountant  N           XXX                XXX
Manager            N           XXX                XXX
Director           N           XXX                XXX
──────────────────────────────────────────────────────
TOTAL              N           XXX                XXX

─────────────────────────────────────────
2. MONTHLY CAPACITY vs. DEMAND

Month    Available hrs   Demand hrs   Gap hrs   Utilisation   Status
──────────────────────────────────────────────────────────────────────
Jan      XXX             XXX          +/-XX     XX%           GREEN/AMBER/RED
Feb      XXX             XXX          +/-XX     XX%           ...
[... all months in planning period]

UAE compliance peak notes:
  - [Month]: VAT Q[N] returns due 28th — [N] clients filing
  - [Month]: CT returns due — [N] clients (Dec year-end)
  - [Month]: Audit support peak — [N] clients

─────────────────────────────────────────
3. OVERLOAD ANALYSIS

Red months (>90% utilisation): [list]
Amber months (75–90%): [list]
Root causes: [e.g. "July: VAT Q2 peak + 2 CT returns overlapping"]

─────────────────────────────────────────
4. RECOMMENDATIONS

# Action 1: [Hire / Load-balance / Defer]
Month affected: [X]
Option chosen: [A/B/C]
Detail: [specific action]
Decision deadline: [date — if hiring, 8 weeks before needed]
Impact: [e.g. "reduces July utilisation from 97% to 78%"]

# Action 2: ...

─────────────────────────────────────────
5. HIRING PLAN (if applicable)

Role to hire: [Accountant / Senior Accountant / Manager]
Must be productive by: [Month YYYY]
Hire decision needed by: [Month YYYY] (8-week lead time)
Hours unlocked/month: XXX
Additional revenue capacity: AED XX,XXX/month at AED [X]/hr blended

─────────────────────────────────────────
6. NEW CLIENT CAPACITY

Available hrs after current portfolio + compliance calendar: [X hrs/month average]
Equivalent new clients supportable: [N] × Tier [X] clients
[Broken down by month where headroom varies significantly]

─────────────────────────────────────────
ASSUMPTIONS
- Billable hours: 140/mo per FTE
- Target utilisation: [X]% ([Y] productive hrs/mo)
- Hiring lead time: 8 weeks
- VAT deadlines: 28th of month following tax period
- CT deadlines: 9 months after financial year-end
- Verify all FTA deadlines on EmaraTax before communicating to clients
- Hours sourced from: [time-tracking system / estimates — flag if estimated]
```

## Quality checklist

- [ ] All UAE VAT quarterly peaks (Jan, Apr, Jul, Oct filings) are reflected in demand spikes
- [ ] CT return peaks are mapped to the correct months based on client year-ends
- [ ] Audit support demand is included for Dec year-end clients (Jan–Mar peak)
- [ ] Utilisation is calculated against productive hours (140 × utilisation %), not raw hours
- [ ] Every red month (> 90%) has at least one recommendation
- [ ] Hiring recommendations include a decision deadline (8-week lead time)
- [ ] New client capacity section states how many additional clients can be absorbed
- [ ] Leave and part-time arrangements are deducted from individual capacity
- [ ] Revenue impact of recommended hire is quantified in AED
- [ ] Assumptions section clearly states if hours are tracked vs. estimated

## Examples

**Example 1**
> "Plan capacity for Q3 2026 (Jul–Sep). We have 3 accountants (140 hrs/mo each) and 1 senior (140 hrs/mo). 20 quarterly VAT clients (Q2 returns due Jul 28), 8 CT returns due in September (Dec year-ends). Also expecting to onboard 3 new bookkeeping clients in August."

Expected: July flagged red (VAT peak), September flagged red (CT peak), August amber (onboarding load). Recommendation: hire one Accountant — decision needed by end of May to be productive by late July.

**Example 2**
> "Do we have capacity for the full year 2027? Team: 2 accountants, 2 seniors, 1 manager. Current portfolio: 35 clients, average 14 hrs/month each. Pipeline: 10 new clients by mid-year."

Expected: Monthly capacity table showing Q1 (audit season) and Q3 (CT peak for Dec year-ends) as amber/red, recommendation to hire 1 Accountant by Q2 and 1 Senior by Q4, new-client capacity calculation.

**Example 3**
> "We are losing a Senior Accountant at end of August. Can we cover September CT filing season without them?"

Expected: Capacity recalculated without the leaver, September flagged red, specific load-balancing options (pull forward CT prep to July/August, redistribute clients to remaining Seniors), hiring recommendation with August decision deadline.

## Guardrails

- UAE jurisdiction only. Compliance calendar is anchored to FTA rules — never reference US, UK, or other tax deadlines.
- This forecast is an internal planning tool. Verify all FTA filing deadlines on EmaraTax before building client-facing schedules.
- Hours data quality determines forecast reliability. Clearly flag if hours are estimated rather than pulled from a time-tracking system.
- Headcount and salary data is sensitive — treat as confidential and do not include in client-facing documents.
- This output is a professional work product for management review, not a commitment to specific staffing actions.

## Reference

See `../_shared/finanshels-context.md` for UAE tax facts, rates, and deadlines.
