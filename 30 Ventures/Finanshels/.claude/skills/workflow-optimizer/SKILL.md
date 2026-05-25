---
name: workflow-optimizer
description: Use when a Finanshels team member wants to document, analyze, or improve an internal operational process — such as the monthly bookkeeping close, VAT return preparation, CT return workflow, client onboarding, or payroll run. Accepts a process name and current-state description, then produces a structured process flowchart, bottleneck analysis, and concrete improvement recommendations tailored to a UAE accounting firm context.
---

# Workflow Optimizer

Documents an internal process end-to-end, identifies bottlenecks, and delivers prioritized recommendations to improve speed, accuracy, and capacity.

## When to use

- A recurring process feels slow, error-prone, or inconsistently executed across the team
- Preparing a new Standard Operating Procedure (SOP) for a recently formalised service
- Onboarding new staff and needing a clear process map to hand over
- Month-end or filing season is creating capacity pressure and management wants to find time savings
- A quality failure or client complaint has occurred and root-cause requires process review
- The firm is scaling a service line and needs to document the process before delegating or automating

## Inputs needed

**Required**
- `process_name`: Short name, e.g. "Monthly Bookkeeping Close", "VAT Return Preparation", "Client Onboarding", "Payroll Run", "CT Return Workflow"
- `current_state_description`: Narrative or bullet-point description of how the process currently works, who does what, what tools are used, and roughly how long each step takes

**Optional**
- `pain_points`: Known issues — errors, delays, handover gaps, repeated rework
- `team_roles_involved`: List of roles participating (e.g. Accountant, Senior Accountant, Manager, Client)
- `tools_and_systems`: e.g. Xero, QuickBooks, EmaraTax, Google Sheets, email, WhatsApp
- `sla_or_deadline`: External deadline that anchors the process (e.g. VAT due 28th, CT return 9 months after year-end)
- `volume`: How many clients or transactions this process handles per cycle
- `target_improvement`: What the team wants — faster turnaround / fewer errors / less manager time / better client communication

## Workflow

1. **Parse and structure the current-state description**
   Read the input narrative and extract:
   - Every distinct step in the process
   - Who performs each step (role, not name)
   - What tool or system is used
   - Estimated time for each step (use input figures; flag where duration is unknown)
   - Any decision points (yes/no branches) or approval gates
   - Handovers between people or systems

2. **Draw the As-Is process map (text-based swim-lane format)**
   Lay out the process as a swim-lane diagram in plain text using the format in `workflows/process-mapping.md`. Each lane is one role or system. Steps are numbered. Handovers are shown with arrows (→). Decision points use diamond notation.

3. **Calculate process metrics**
   For each step where duration is known or can be estimated:
   - Total elapsed time (calendar days from trigger to completion)
   - Total active working hours
   - Wait time ratio = wait time / total elapsed time × 100%
   - Number of handovers
   - Number of manual data re-entry points (rework risk)

4. **Identify bottlenecks**
   Flag steps that exhibit any of the following:
   - Longest single-step duration
   - Highest wait time (queue before action)
   - Dependent on a single person with no backup (key-person risk)
   - Manual data entry that duplicates what a system already holds
   - Client-dependent delays (information not arriving on time)
   - Steps performed by a senior/high-cost role that could be done by junior staff
   - Repeated error-correction loops (rework)
   - UAE compliance deadline proximity (steps that land close to the 28th VAT deadline or CT 9-month window)

5. **Benchmark against best-practice norms**
   Compare to the standard Finanshels service delivery benchmarks documented in `workflows/process-mapping.md`. Flag where the current process materially exceeds expected duration or effort.

6. **Generate To-Be recommendations**
   For each bottleneck, produce one or more recommendations:
   - **Eliminate**: Remove steps that add no value
   - **Automate**: Flag steps suitable for rule-based automation (bank feeds, recurring journal templates, auto-reconciliation, EmaraTax scheduled reminders)
   - **Delegate down**: Steps where a junior role can own with a lightweight review gate
   - **Parallel-ise**: Steps that are currently sequential but have no dependency (e.g. preparing the VAT reconciliation while waiting for the client to confirm a transaction)
   - **Standardise**: Steps that differ by client/staff member and should be templated
   - **Client SLA**: Where client delays are the bottleneck, recommend a data-submission deadline clause in the engagement letter with a defined late-submission surcharge or filing-delay disclaimer
   Label each recommendation: Quick Win (< 1 week to implement) / Medium Term (1–4 weeks) / Strategic (> 1 month or requires tooling investment).

7. **Draft the To-Be process map**
   Redraw the swim-lane diagram with the recommended changes applied. Mark changed steps with `[NEW]` or `[REMOVED]` or `[AUTOMATED]`.

8. **Quantify the improvement opportunity**
   Estimate the expected saving per cycle:
   - Hours saved (and AED value at blended rate)
   - Reduction in calendar days to completion
   - Reduction in handover count
   Present as: "Estimated saving: X hours/cycle (AED Y,XXX/month at blended rate)"

## Output format

```
PROCESS OPTIMISATION REPORT
Process: [name]
Prepared: [YYYY-MM-DD]
Version: 1.0 (draft — for internal review)

─────────────────────────────────────────
1. PROCESS OVERVIEW
[2–3 sentences: purpose, frequency, who owns it, external deadline it must meet]

─────────────────────────────────────────
2. AS-IS PROCESS MAP

[Client]          [Accountant]       [Senior / Manager]   [System / Tool]
───────────────────────────────────────────────────────────────────────
Step 1: ...        →
                   Step 2: ...        →
                                      Step 3: ... (gate)
                   ←  Step 4: rework if rejected
                   Step 5: ...                              → [EmaraTax]
...

Total steps: N   |   Handovers: N   |   Estimated elapsed: N days   |   Active hrs: N

─────────────────────────────────────────
3. PROCESS METRICS

Metric                        Current    Target
──────────────────────────────────────────────
Total elapsed time (days)     X          Y
Active working hours          X          Y
Wait time ratio               X%         Y%
Number of handovers           X          Y
Manual re-entry points        X          Y
Rework loops                  X          Y

─────────────────────────────────────────
4. BOTTLENECK ANALYSIS

# Bottleneck 1: [Step name]
Type: [Wait / Rework / Key-person / Client dependency / Over-skilled resource]
Impact: [Adds X days / X hours / creates compliance deadline risk]
Detail: [1–2 sentences explaining why this is a problem]

# Bottleneck 2: ...

─────────────────────────────────────────
5. RECOMMENDATIONS

Priority | Recommendation                  | Type          | Owner         | Est. saving
──────────────────────────────────────────────────────────────────────────────────────
1        | [Action]                         | Quick Win     | [Role]        | X hrs/cycle
2        | [Action]                         | Medium Term   | [Role]        | X hrs/cycle
3        | [Action]                         | Strategic     | [Role]        | X hrs/cycle

─────────────────────────────────────────
6. TO-BE PROCESS MAP

[Updated swim-lane with changes marked [NEW] / [REMOVED] / [AUTOMATED]]

Total steps: N   |   Handovers: N   |   Estimated elapsed: N days   |   Active hrs: N

─────────────────────────────────────────
7. IMPROVEMENT SUMMARY

Estimated saving per cycle: X hours (AED Y,XXX/month at blended rate)
Reduction in elapsed time: X days → Y days
Compliance risk reduction: [describe]
Key dependencies to unlock: [e.g. client data deadline clause, Xero automation setup]

─────────────────────────────────────────
NOTES & ASSUMPTIONS
- [List any assumptions made about step durations, volume, or roles]
- This report is a draft for internal review. Validate with the process owner before implementing changes.
```

## Quality checklist

- [ ] Every step in the current-state description is captured in the As-Is map
- [ ] Swim lanes clearly assigned (client vs. internal roles vs. system)
- [ ] UAE compliance deadline(s) are anchored in the timeline (VAT 28th, CT 9-month window)
- [ ] Each bottleneck has a labelled type and quantified impact
- [ ] Every recommendation is labelled Quick Win / Medium Term / Strategic
- [ ] To-Be map reflects the recommendations (not just a copy of As-Is)
- [ ] Improvement summary includes an AED savings estimate
- [ ] Client-data dependency addressed where applicable (SLA recommendation)
- [ ] Process map is readable in plain text (no special rendering required)

## Examples

**Example 1**
> "Map and optimise our monthly bookkeeping close process. Currently: client sends bank statements on the 5th, accountant posts entries by 10th, manager reviews by 12th, management pack sent to client by 15th. Main pain point: clients send statements late and we miss the 15th target."

Expected: As-Is map, bottleneck #1 flagged as client dependency, recommendation to add data-submission deadline clause in engagement letter, Quick Win automation of bank feed setup to eliminate manual statement collection.

**Example 2**
> "Document our VAT return preparation workflow for a portfolio of 40 quarterly-filing clients. We use Xero, EmaraTax. Senior Accountant reviews every return. Process takes 3 weeks which leaves no buffer before the 28th deadline."

Expected: Swim-lane with 40-client scale context, bottleneck flagged at single Senior Accountant review gate, recommendation to introduce tiered review (Accountant self-reviews Tier 1–2, Senior only reviews Tier 3+), parallel workstream for data gathering vs. prior-period reconciliation.

**Example 3**
> "We onboard new clients slowly — takes 4 weeks from signed engagement letter to first deliverable. There's no checklist, everyone does it differently. We need a standard SOP."

Expected: Recommended To-Be onboarding process with standardised steps, a client information request template, EmaraTax access handover checklist, and a target of 10 business days from signed letter to first deliverable.

## Guardrails

- UAE jurisdiction only. Never reference US, UK, or other country processes.
- This report is a professional work product for internal use — it must be reviewed by the process owner before any changes are implemented.
- Do not recommend removing compliance-required steps (e.g. manager sign-off on CT returns, VAT reconciliation review).
- Automation recommendations should specify the tool; do not assume the firm has systems it has not listed.
- Client financial data is confidential. Never include real client names or volumes in examples.

## Reference

See `../_shared/finanshels-context.md` for UAE tax facts, rates, and deadlines.
