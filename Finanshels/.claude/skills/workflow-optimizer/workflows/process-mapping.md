# Process Mapping Reference

> Internal reference for the `workflow-optimizer` skill.
> Use this file for standard benchmarks, swim-lane notation, and best-practice norms.

---

## 1. Swim-Lane Notation (plain text)

Use this format for all process maps. Keep it readable without special rendering.

```
[Role A]         [Role B]          [Role C]         [System]
─────────────────────────────────────────────────────────────
1. Step one   →
              2. Step two    →
                              3. Decision?
                              ├─ Yes → 4. Continue  →  [EmaraTax]
                              └─ No  → back to 2 (rework)
              5. Step five
              ↓
              6. Step six                           → [Email client]
```

Key conventions:
- `→` = handover or output passed to next role/system
- `←` = rework loop returning to earlier role
- `├─ / └─` = decision branch
- `[SYSTEM]` = automated or tool-mediated action, no manual effort
- `[NEW]` / `[REMOVED]` / `[AUTOMATED]` = To-Be change markers
- Number every step sequentially across all lanes

---

## 2. Standard Service Benchmarks

These are internal Finanshels targets. Flag any current-state process that materially exceeds them.

### Monthly Bookkeeping Close

| Milestone                            | Target (business days from month-end) |
|--------------------------------------|---------------------------------------|
| Client sends bank statements / data  | Day 3                                 |
| All transactions posted & reconciled | Day 5                                 |
| Manager review of ledger             | Day 7                                 |
| Management pack sent to client       | Day 10                                |
| Client queries resolved              | Day 12                                |
| Final sign-off                       | Day 13                                |

Total elapsed target: **13 business days** from month-end.
Active hours target (Tier 2 client): **10–16 hours/month**.

### VAT Return Preparation (quarterly)

| Milestone                            | Target (days before filing due date)  |
|--------------------------------------|---------------------------------------|
| VAT data gathering complete          | Day -14 (14 days before 28th)         |
| Output/input VAT reconciled          | Day -10                               |
| Accountant prepares draft return     | Day -8                                |
| Senior / Manager review              | Day -5                                |
| Client approval (where required)     | Day -3                                |
| Submission on EmaraTax               | Day -2                                |
| Payment confirmed                    | Day -1 or Day 0 (by 28th)            |

Total elapsed target: **12 business days** per return.
Active hours target (Tier 2 client): **6–10 hours/return**.

VAT return due: **28th of the month following the tax period** (verify on EmaraTax).

### CT Return (annual)

| Milestone                               | Target (months before CT due date) |
|-----------------------------------------|------------------------------------|
| Year-end financials finalised           | Month -7                           |
| CT computation drafted                  | Month -5                           |
| TP disclosure prepared (if applicable)  | Month -4                           |
| Manager / Director review               | Month -3                           |
| Client review and approval              | Month -2                           |
| Submission on EmaraTax                  | Month -1                           |
| Payment confirmed                       | By due date (9 months after year-end) |

CT return and payment due: **within 9 months of financial year-end** (verify on EmaraTax).

### Client Onboarding (new engagement)

| Milestone                                    | Target (business days from signed letter) |
|----------------------------------------------|-------------------------------------------|
| Welcome email + info request sent            | Day 1                                     |
| EmaraTax / accounting system access obtained | Day 3                                     |
| Chart of accounts and opening balances set up| Day 5                                     |
| Historical data migrated / catch-up plan agreed| Day 7                                   |
| First deliverable produced                   | Day 10                                    |

Total target: **10 business days** from signed engagement letter to first deliverable.

### Payroll Run (monthly)

| Milestone                            | Target (business days before WPS deadline) |
|--------------------------------------|--------------------------------------------|
| Client sends payroll inputs          | Day -5                                     |
| Payroll calculated and reviewed      | Day -3                                     |
| Client approves payroll              | Day -2                                     |
| WPS file submitted to bank           | Day -1                                     |
| Payslips issued to employees         | Day 0 (salary payment date)               |

---

## 3. Bottleneck Type Taxonomy

| Type                   | Description                                                                   | Common fix                                      |
|------------------------|-------------------------------------------------------------------------------|-------------------------------------------------|
| Client dependency      | Process stalls waiting for the client to send data or approve                 | Engagement-letter data SLA + late-submission clause |
| Single-point / key-person | Only one person can perform the step; no cover if absent                  | Cross-train, document, delegate                 |
| Over-skilled resource  | A Manager or Director spending time on Accountant-level work                  | Delegate with a lightweight review gate         |
| Manual re-entry        | Data entered into one system is manually typed into another                   | Integrate via API or shared export/import       |
| Rework loop            | Step is repeatedly sent back due to errors or missing information             | Add a pre-flight checklist before handover      |
| Unbatched work         | Each client processed one at a time when batch processing is possible         | Batch similar tasks (e.g. all Tier 1 VAT returns together) |
| Approval queue         | Steps pile up waiting for one reviewer across many clients                    | Tiered review: juniors approve small/simple, seniors approve complex |
| Compliance proximity   | Step falls too close to a hard FTA deadline (< 3 days buffer)                 | Extend data-gathering SLA; stagger filing schedule |

---

## 4. Automation Opportunities by Process

### Bookkeeping
- Bank feed auto-import (Xero, QuickBooks) — eliminates manual statement upload
- Recurring journal templates for rent, depreciation, payroll
- Auto-reconciliation rules for high-frequency, low-value transactions
- Auto-reminders to client for missing statements (scheduled email)

### VAT Filing
- EmaraTax portal calendar reminders (28-day rule)
- VAT report export from accounting system → direct import to EmaraTax (where supported)
- Standing payment instruction for VAT liability (client bank)

### CT Return
- Depreciation schedule auto-calculation in accounting system
- TP disclosure pre-population from related-party transaction log
- EmaraTax CT registration deadline tracker (by licence month)

### Payroll
- WPS file generation from payroll module (Zoho Payroll, Bayzat, etc.)
- Auto-payslip distribution via payroll system
- Gratuity accrual auto-posting from payroll run

### Client Onboarding
- Standardised information request checklist (shared via client portal or Google Form)
- EmaraTax sub-user access request template
- Chart of accounts template library by industry/entity type

---

## 5. Client Data SLA Clause (template language)

When a client delay is the primary bottleneck, recommend the following be added to the engagement letter (to be reviewed by management before use):

> "To meet regulatory filing deadlines, the Client agrees to provide all required financial data, bank statements, and approvals to Finanshels by [agreed date] each [month/quarter]. Where data is received after this date, Finanshels will make reasonable efforts to meet the deadline but cannot guarantee on-time filing. Any penalties arising from late data submission by the Client are the responsibility of the Client."

---

## 6. Improvement Effort Labels

| Label         | Definition                                              | Who owns implementation |
|---------------|---------------------------------------------------------|-------------------------|
| Quick Win     | Can be implemented in < 1 week, no new tools needed     | Team lead               |
| Medium Term   | 1–4 weeks; may need process documentation or minor tooling | Manager             |
| Strategic     | > 1 month; requires system change, training, or significant restructure | Director / leadership |
