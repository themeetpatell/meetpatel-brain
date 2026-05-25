---
name: deliverable-tracker
description: Use when monitoring the status of client deliverables across all active Finanshels engagements — triggered by requests like "what's due this month", "show me at-risk filings", "VAT deadlines", "deliverable dashboard", "who's overdue", or "escalation report". Produces a structured status dashboard of all client deliverables (VAT returns, monthly books, CT filings, payroll, reports) with RAG (red/amber/green) status, days-to-deadline, responsible team member, and an escalation alert list for at-risk items.
---

# Deliverable Tracker

Monitors the status of all client deliverables across Finanshels engagements and produces a real-time status dashboard with RAG ratings and escalation alerts — so nothing slips through the cracks.

## When to use

- Weekly or monthly team review of all outstanding deliverables
- Before a VAT filing deadline (28th of the month) to confirm all returns are filed
- Identifying clients where a deliverable is at risk of being late
- Escalation reporting: which items need immediate action by the engagement manager
- Responding to a client asking "has my VAT return been filed?"
- Preparing an internal status update for the Finanshels leadership team
- After onboarding a new client to confirm their first deliverables are tracked

## Inputs needed

**Required:**
- Client list with engaged services (VAT, CT, monthly books, payroll, audit support)
- For each client: financial year-end date, VAT filing frequency (quarterly/monthly), and any known non-standard deadlines
- Current date (for days-to-deadline calculations)
- Status update for each deliverable (provided by the engagement team or pulled from the PM tool): Not started / In progress / With client / Filed/Submitted / Complete

**Optional:**
- Responsible team member per client per deliverable
- Blocker notes (e.g. "waiting for client bank statements", "client not responding")
- Priority flag: High / Standard
- Last communication date with the client (for responsiveness tracking)

## Workflow

### Step 1 — Compile the Deliverable Register

1. For each active client, list every deliverable due in the current period and the next 30 days:

   **VAT returns:** Due on the 28th of the month following the VAT period end.
   - Quarterly filers: 28 Jan, 28 Apr, 28 Jul, 28 Oct
   - Monthly filers: 28th of each month

   **Corporate Tax returns:** Due 9 months after financial year-end. Calculate per client (e.g. 31 Dec year-end → due 30 Sep; 31 Mar year-end → due 31 Dec).

   **Monthly bookkeeping / management accounts:** Typically due by the 15th of the following month (or per engagement agreement). Note the agreed delivery date.

   **Payroll / WPS:** Due per the agreed payroll run date — typically 2–3 business days before the client's salary payment date.

   **Audit support / financial statements:** Per the agreed engagement timeline.

   **CT registration (if pending):** Per the FTA-assigned deadline based on licence issuance month.

2. For each deliverable, record:
   - Client name and entity type
   - Deliverable type
   - Due date
   - Days remaining (positive = future, negative = overdue)
   - Current status
   - Responsible team member
   - Blocker or note

### Step 2 — Apply RAG Status

Assign a RAG (Red / Amber / Green) status to each deliverable:

| Status | Criteria |
|---|---|
| 🔴 RED — Escalate now | Overdue (past due date) OR due within 3 days AND status is Not started |
| 🟡 AMBER — Watch closely | Due within 7 days AND status is Not started or In progress with a blocker |
| 🟢 GREEN — On track | Due in 8+ days, OR status is Filed/Complete, OR in progress without blockers and sufficient time remains |

**Override rules:**
- Any item with a known blocker that hasn't been resolved in 5+ business days → escalate to AMBER regardless of days remaining
- Any item where the client has not responded to a document request for 7+ business days → flag as AMBER with "client unresponsive" note
- Any overdue CT or VAT filing → automatically RED — regulatory penalties apply

### Step 3 — Build the Escalation Alert List

Filter all RED and AMBER items into a separate escalation list. For each:
- Identify the specific risk (overdue FTA penalty, client not providing data, team bandwidth)
- Recommend the intervention (call the client, file for extension if available, escalate to senior manager)
- Assign an owner and a response-by date (default: next business day for RED, 2 business days for AMBER)

### Step 4 — Generate the Dashboard

Produce the status dashboard in the format below. Sort by: RED first, then AMBER, then GREEN. Within each group, sort by due date ascending.

### Step 5 — Distribution (optional)

If this output is being shared in a team meeting:
- Highlight all RED items at the top of the meeting agenda
- Assign owners to each escalation action live in the meeting
- Update the tracker after the meeting with agreed actions and owners

## Output format

```
## Finanshels Deliverable Status Dashboard
Generated: [Date] | Period: [Month/Year]
Prepared by: [Team member or "system"] | Reviewed by: [Engagement Manager]

---

### Summary
| Status | Count |
|---|---|
| 🔴 RED — Escalate | [N] |
| 🟡 AMBER — Watch | [N] |
| 🟢 GREEN — On track | [N] |
| Total active deliverables | [N] |

---

### 🔴 ESCALATION ALERTS — Action Required

| # | Client | Entity Type | Deliverable | Due Date | Days | Status | Blocker | Owner | Action Required |
|---|---|---|---|---|---|---|---|---|---|
| 1 | [Client] | [Mainland/FZ] | VAT Return Q2 | 28 Jul | -2 (OVERDUE) | Not filed | Awaiting client approval | [Name] | File immediately / call client |
| 2 | ... | | | | | | | | |

---

### 🟡 AMBER — Watch Closely

| # | Client | Entity Type | Deliverable | Due Date | Days | Status | Note | Owner |
|---|---|---|---|---|---|---|---|---|
| 1 | [Client] | [Mainland/FZ] | Monthly Books May | 15 Jun | 5 | In progress | Waiting bank statements from client | [Name] |
| 2 | ... | | | | | | | |

---

### 🟢 GREEN — On Track

| # | Client | Deliverable | Due Date | Days | Status | Owner |
|---|---|---|---|---|---|---|
| 1 | [Client] | VAT Return Q3 | 28 Oct | 62 | Not started | [Name] |
| 2 | ... | | | | | |

---

### Recently Completed (Last 14 Days)
| Client | Deliverable | Filed/Completed Date | Filed by |
|---|---|---|---|
| [Client] | VAT Return Q2 | [Date] | [Name] |

---

### Open Actions from This Review
| # | Action | Owner | Due by |
|---|---|---|---|
| 1 | Call [Client] re: overdue VAT — file today | [Name] | Today |
| 2 | Chase [Client] for May bank statements | [Name] | [Date] |
```

## Quality checklist

- [ ] Every active client and engaged service is represented in the dashboard
- [ ] VAT due dates are correct: 28th of the month following the period end
- [ ] CT due dates are correct: 9 months after each client's financial year-end
- [ ] RAG status applied consistently using the criteria above
- [ ] All RED items have a specific owner and action with a response-by date
- [ ] AMBER items with a "client unresponsive" note have a follow-up date set
- [ ] Dashboard is sorted: RED → AMBER → GREEN, then by due date ascending
- [ ] Recently completed items are captured (confirms filings are tracked end-to-end)
- [ ] Summary counts match the detail rows
- [ ] Reviewed by an engagement manager before distribution

## Examples

**Example 1:**
"Show me the full deliverable dashboard for all clients as of today. I want to see what's due in the next 30 days and anything that's overdue."

**Example 2:**
"We have three clients with VAT returns due on 28 July — a Dubai mainland FMCG company, a DMCC free zone SaaS company, and an Abu Dhabi mainland consultancy. All quarterly filers. Give me a status check and flag anything at risk."

**Example 3:**
"Generate an escalation report for this week. Which clients are at risk of missing a deadline and what do we need to do about each one by end of day?"

## Guardrails

- UAE jurisdiction only. All VAT dates reference UAE FTA rules (28th filing rule); CT dates reference the 9-month rule from financial year-end.
- This dashboard is an internal management tool. Do not send the full dashboard to clients — prepare a client-facing version with only their own deliverables.
- Overdue regulatory filings (VAT, CT) are always RED. Do not downgrade them even if the team believes a penalty is unlikely — escalate first, assess risk second.
- Deliverable status must come from the team or PM system — this skill structures and interprets the data, it does not have independent visibility into what has been filed.
- All client data in the tracker is confidential. The dashboard is for internal Finanshels use only.

## Reference

See ../_shared/finanshels-context.md for UAE tax facts, rates, and deadlines.
