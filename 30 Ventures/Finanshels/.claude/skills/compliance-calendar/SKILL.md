---
name: compliance-calendar
description: Use when a Finanshels team member needs to build a filing-deadline calendar for a specific client, covering UAE Corporate Tax return and payment, VAT returns, CT and VAT registration deadlines, and other compliance obligations. Triggers include: new client onboarding, start of a new financial year, a client asking "when are my deadlines?", or preparing a compliance timeline for a CT or VAT engagement. Produces a chronological deadline calendar with reminder dates and a summary table by obligation type.
---

# Compliance Calendar

Builds a personalised UAE filing-deadline calendar for a client by entity type and financial year, covering CT, VAT, registration, and other compliance deadlines, with advance reminder dates.

## When to use

- New client onboarding: create a full-year compliance calendar as part of the welcome pack
- Start of a new financial year: refresh deadlines for the coming year
- A client asks "what are my deadlines for this year?"
- Before a CT or VAT filing: confirm the exact due date and whether the client is on track
- Setting up internal reminders in Finanshels project management or CRM
- Annual compliance review: checking whether all deadlines were met in the prior year

## Inputs needed

**Required**
- Entity type: mainland LLC / free zone (specify authority) / branch / natural person
- Financial year start and end dates (e.g. 1 Jan 2024 – 31 Dec 2024)
- CT registered: yes / no / pending
- VAT registered: yes / no / pending (if yes, filing frequency: quarterly / monthly)
- Approximate annual revenue (AED) — used to determine SBR eligibility, audit requirement, QFZP status

**Optional**
- CT registration date and TRN (to confirm registration-deadline compliance)
- VAT TRN and registration effective date
- Free zone licence details (for QFZP deadlines)
- Whether the entity has related-party transactions (triggers TP disclosure deadline)
- Any prior missed deadlines (to flag for penalty mitigation)
- Whether the entity employs UAE/GCC nationals (triggers GPSSA contribution deadlines)
- Whether payroll/WPS is in scope

## Workflow

1. **Confirm the tax period**
   The CT tax period is the financial year. Calculate:
   - Tax period start date
   - Tax period end date
   - CT return and payment due date = 9 months after tax period end
   Example: FY 1 Jan 2024 – 31 Dec 2024 → CT return due **30 September 2025**
   Example: FY 1 Apr 2024 – 31 Mar 2025 → CT return due **31 December 2025**
   Always verify with FTA for the specific entity; confirm no extensions have been announced.

2. **Determine CT registration deadline**
   CT registration on EmaraTax is mandatory. The FTA set staggered deadlines based on the month the trade licence was issued. If registration is not yet done, flag as urgent. If already registered, confirm the TRN is on file.

3. **Build VAT return schedule**
   VAT returns are due by the **28th of the month following the tax period end**.
   - Quarterly filer with FY = calendar year: due dates are 28 Apr, 28 Jul, 28 Oct, 28 Jan
   - Monthly filer: due 28th of every following month
   Confirm the client's assigned VAT period with EmaraTax if uncertain.

4. **Add VAT registration deadline (if not yet registered)**
   If taxable supplies have exceeded AED 375,000 in any 12-month period, or are expected to in the next 30 days, VAT registration is mandatory. Flag the date registration should have been / should be completed.

5. **Add other compliance deadlines**

   | Obligation | Deadline | Condition |
   |-----------|---------|-----------|
   | CT return + payment | 9 months after FY end | All CT-registered entities |
   | CT registration | FTA-staggered by licence month | All taxable persons — confirm with FTA |
   | VAT return + payment | 28th of month after tax period | All VAT-registered entities |
   | VAT registration | When threshold breached | Mandatory: AED 375K; Voluntary: AED 187.5K |
   | Audited financial statements | Typically required with CT return | QFZPs; entities with revenue > AED 50M |
   | TP disclosure form | Filed with CT return | Entities with related-party transactions |
   | UBO register update | Within 15 days of change (verify with registrar) | All entities — check with registrar |
   | GPSSA contributions | Monthly, by employer (verify GPSSA) | Entities employing UAE/GCC nationals |
   | WPS payroll | Monthly, within agreed WPS window | Entities with employees |
   | AML/CFT CDD refresh | Risk-based: annually (high risk) / 3 years (medium) | All DNFBP-adjacent obligations on Finanshels |

6. **Set reminder dates**
   For each deadline, add two advance reminders:
   - **60 days before** the deadline: preparation reminder (gather documents, start workpapers)
   - **14 days before** the deadline: filing reminder (workpaper sign-off, EmaraTax submission)

7. **Format the calendar**
   Produce both:
   - A **chronological list** sorted by due date (for month-by-month planning)
   - A **summary table** grouped by obligation type (for quick reference)

8. **Flag urgent items**
   Any deadline within 30 days of today's date: mark as URGENT. Any deadline already passed (if this is a retrospective review): mark as OVERDUE and note penalty exposure.

9. **Note key caveats**
   At the foot of every calendar:
   - All dates are based on current FTA guidance and must be confirmed against EmaraTax and the FTA website
   - Deadlines for new obligations (e.g. first-year CT return) may be subject to FTA transitional guidance
   - Finanshels will notify the client if any material deadline changes are announced

## Output format

```
# Compliance Calendar — [Client Internal ID]
**Entity type:** [Mainland LLC / Free Zone / etc.]
**Financial year:** [DD MMM YYYY – DD MMM YYYY]
**Prepared by:** [Name]
**Date:** YYYY-MM-DD

---

## Chronological Deadline List

| Due Date | Obligation | Filing / Action Required | Status | Reminder 1 (60 days) | Reminder 2 (14 days) |
|----------|-----------|--------------------------|--------|----------------------|----------------------|
| DD MMM YYYY | CT Registration | Register on EmaraTax | ✓ Done / Pending / URGENT | | |
| DD MMM YYYY | VAT Return Q1 | File & pay via EmaraTax | Upcoming | DD MMM | DD MMM |
| DD MMM YYYY | VAT Return Q2 | File & pay via EmaraTax | Upcoming | DD MMM | DD MMM |
| DD MMM YYYY | VAT Return Q3 | File & pay via EmaraTax | Upcoming | DD MMM | DD MMM |
| DD MMM YYYY | VAT Return Q4 | File & pay via EmaraTax | Upcoming | DD MMM | DD MMM |
| DD MMM YYYY | Audited Financial Statements | Finalise and approve | N/A or Upcoming | DD MMM | DD MMM |
| DD MMM YYYY | CT Return + Payment | File & pay via EmaraTax | Upcoming | DD MMM | DD MMM |
| As required | UBO Register | Update if ownership changes | Ongoing | — | — |
| Monthly | WPS Payroll | Process via WPS-approved channel | Ongoing | — | — |

---

## Summary by Obligation Type

### Corporate Tax
| Item | Date | Notes |
|------|------|-------|
| CT registration deadline | DD MMM YYYY | Confirm with FTA; staggered by licence month |
| Tax period end | DD MMM YYYY | FY end date |
| CT return + payment due | DD MMM YYYY | 9 months after FY end |
| TP disclosure (if applicable) | Same as CT return | Filed with return |

### VAT
| Period | Return Due Date | Payment Due Date | Notes |
|--------|----------------|-----------------|-------|
| Q1 (Jan–Mar) | 28 Apr YYYY | 28 Apr YYYY | |
| Q2 (Apr–Jun) | 28 Jul YYYY | 28 Jul YYYY | |
| Q3 (Jul–Sep) | 28 Oct YYYY | 28 Oct YYYY | |
| Q4 (Oct–Dec) | 28 Jan YYYY | 28 Jan YYYY | |

### Other Obligations
| Obligation | Frequency | Notes |
|-----------|-----------|-------|
| Audited financial statements | Annual | Required if QFZP or revenue > AED 50M |
| UBO register update | On change | File with registrar within 15 days of change (verify) |
| GPSSA contributions | Monthly | Entities with UAE/GCC national employees |
| WPS payroll | Monthly | MOHRE-approved channel |
| AML/CFT CDD refresh | Risk-based | Finanshels internal obligation |

---

## Urgent / Overdue Items

| Obligation | Due Date | Status | Recommended Action |
|-----------|---------|--------|-------------------|
| [Any items due within 30 days or already overdue] | | URGENT / OVERDUE | |

---

## Important Notes
- All dates are based on current FTA guidance as at [today's date]. Verify each deadline on EmaraTax before relying on it.
- CT return deadlines for entities with non-standard financial years should be confirmed directly with the FTA.
- Finanshels will monitor for FTA announcements of deadline extensions and notify clients accordingly.
- Small Business Relief (revenue ≤ AED 3M, periods ending on/before 31 Dec 2026): CT return must still be filed; SBR election is made on the return.

---
*Internal Finanshels work product. Not for external distribution without review.*
```

## Quality checklist

- [ ] CT return due date correctly calculated (9 months after FY end date, not calendar year end)
- [ ] All four quarterly VAT due dates listed (or monthly, if applicable) using 28th-of-month rule
- [ ] CT registration status addressed (done / pending / urgent)
- [ ] Audited financials requirement assessed (QFZP or revenue > AED 50M)
- [ ] SBR eligibility noted if revenue ≤ AED 3M and period ends on/before 31 Dec 2026
- [ ] Reminder dates set 60 days and 14 days before each deadline
- [ ] Urgent/overdue items flagged separately
- [ ] Caveats section included ("verify with FTA / EmaraTax")
- [ ] No deadline invented — all traced to shared context or FTA source

## Examples

**Example 1 — Standard mainland LLC, calendar FY**
> "New client: Dubai mainland trading LLC, AED 4M revenue, FY 1 Jan 2024 – 31 Dec 2024, quarterly VAT filer, CT registered. Build the full compliance calendar for 2024/2025."

**Example 2 — Free zone QFZP, non-calendar FY**
> "JAFZA technology company, AED 15M revenue, FY 1 April 2024 – 31 March 2025, quarterly VAT filer, claiming QFZP. Build the compliance calendar and flag the audited-financials deadline."

**Example 3 — Small startup, first CT year**
> "RAK mainland consultancy, AED 900K revenue, FY 1 June 2024 – 31 May 2025, not yet VAT registered, just CT registered. Build the calendar. SBR likely applicable."

## Guardrails

- All deadlines must be verified against current FTA guidance and EmaraTax before being communicated to a client. Deadlines are subject to change by FTA announcement.
- Do not guarantee that no other deadlines apply — this skill covers the standard obligations; specialist obligations (e.g. CbCR for large MNEs, customs, excise) may apply and are not covered here.
- UAE jurisdiction only. Do not reference non-UAE filing obligations.
- Output is a Finanshels work product for internal use and client advisory purposes. It is not a legal guarantee of compliance.

## Reference

See `../_shared/finanshels-context.md` for UAE tax facts, rates, and deadlines.
