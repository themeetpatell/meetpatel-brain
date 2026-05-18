# Client Tax Analysis Workflow

Use this document to run a structured tax analysis for a Finanshels client or prospect. Work through each section in order. Incomplete sections should be flagged as "information needed" rather than skipped.

---

## Section 1 — Entity Profile

| Field | Value |
|-------|-------|
| Entity / trading name | |
| Licence type | Mainland (DED) / Free Zone (specify) / Offshore |
| Free zone authority (if applicable) | e.g. DMCC, JAFZA, DIFC, ADGM, RAKEZ |
| Date of incorporation | |
| Financial year-end | |
| Current CT tax period | e.g. 1 Jan 2025 – 31 Dec 2025 |
| CT return due date | 9 months after financial year-end |
| Principal activity | |
| Secondary activities (if any) | |

**Notes / flags from entity profile:**

---

## Section 2 — Revenue & Financial Position

| Field | Value |
|-------|-------|
| Estimated annual revenue (AED) | |
| Revenue breakdown (qualifying vs non-qualifying, if free zone) | |
| Estimated taxable income (AED) | |
| Accounting standards in use | IFRS / IFRS for SMEs / Cash basis |
| Audited financials prepared? | Yes / No / In progress |
| Auditor name (if applicable) | |

**CT rate calculation:**
- Income ≤ AED 375,000 → 0%
- Income above AED 375,000 → 9% on excess
- Estimated CT liability (before reliefs): AED ________

**Small Business Relief check:**
- Revenue ≤ AED 3M? → Yes / No
- Tax period ends on or before 31 Dec 2026? → Yes / No
- SBR available? → Yes / No / Borderline (verify with FTA)

---

## Section 3 — Corporate Tax Registration

| Field | Value |
|-------|-------|
| CT registration status | Registered / Not yet registered / Unknown |
| EmaraTax TRN (if registered) | |
| Date of CT registration | |
| First CT return filed? | Yes / No / Upcoming |
| Any FTA correspondence received? | Yes (describe) / No |

**Registration urgency:**
- [ ] Already registered — no action needed on registration itself
- [ ] Not registered — URGENT: mandatory registration via EmaraTax; late registration attracts administrative penalties. Advise client to register immediately.
- [ ] Uncertain — request copy of EmaraTax account confirmation

---

## Section 4 — Free Zone / QFZP Assessment

*Complete this section only if the entity holds a free zone licence.*

| QFZP Condition | Status | Notes |
|---|---|---|
| 1. Qualifying activities generating qualifying income | Met / Not met / Unclear | |
| 2. Adequate substance in free zone (employees, premises, decisions made in FZ) | Met / Not met / Unclear | |
| 3. De minimis non-qualifying income (≤ 5% of revenue or AED 5M, whichever is lower — verify current FTA guidance) | Met / Not met / Unclear | |
| 4. Audited financial statements prepared | Met / Not met / Unclear | |

**Overall QFZP assessment:**
- [ ] All four conditions met → likely QFZP; recommend formal confirmation and maintain audited financials
- [ ] One or more conditions not met → QFZP status at risk; 9% applies to all income
- [ ] Borderline → formal QFZP eligibility review recommended before filing

---

## Section 5 — VAT Position

| Field | Value |
|-------|-------|
| VAT registration status | Registered / Not registered / Exempt activity |
| VAT TRN (if registered) | |
| Taxable supplies (trailing 12 months, AED) | |
| Taxable supplies (next 30 days forecast, AED) | |
| Mandatory registration threshold (AED 375,000) breached? | Yes / No / Approaching |
| Voluntary registration threshold (AED 187,500) breached? | Yes / No |
| Filing frequency | Quarterly / Monthly |
| Most recent VAT return filed | Period: |
| Any overdue returns? | Yes (list) / No |
| Supply classification | Mostly standard-rated / Partially zero-rated / Mixed / Exempt |

**VAT action flags:**
- [ ] Registered and current — review supply classification and ensure partial recovery rules applied correctly (if mixed supplies)
- [ ] Not registered but above AED 375,000 → mandatory registration required immediately; backdated liability risk
- [ ] Not registered, between AED 187,500 and AED 375,000 → consider voluntary registration to reclaim input tax on costs
- [ ] Not registered, below AED 187,500 → no action required; monitor revenue growth

---

## Section 6 — Transfer Pricing & Related Parties

| Field | Value |
|-------|-------|
| Related-party transactions present? | Yes / No / Unknown |
| Types of related-party transactions | Loans / Management fees / IP licence / Intragroup sales / Other |
| Estimated AED value of related-party transactions | |
| Master file / local file prepared? | Yes / No / Not applicable |
| Transfer pricing disclosure included in CT return? | Yes / No / Not yet applicable |

**TP flag:** If related-party transactions exist, the arm's-length principle applies under UAE CT. A related-party disclosure form is required with the CT return. Above prescribed thresholds (confirm with FTA), master file and local file documentation is mandatory.

---

## Section 7 — Other Compliance

| Obligation | Status | Notes |
|---|---|---|
| UBO register filed with registrar | Done / Pending / Unknown | |
| AML/CFT (if client is a DNFBP) | Registered on goAML / N/A | |
| WPS payroll processing | In use / Not in use | |
| End-of-service gratuity tracked | Yes / No | |
| Record retention (7 years) policy | In place / Not in place | |
| ESR (historical, 2019–2022 periods only) | Filed / N/A / To check | |

---

## Section 8 — Analysis Summary & Flags

After completing sections 1–7, summarise:

**Critical flags (immediate action required):**
1.
2.

**High-priority flags (action this quarter):**
1.
2.

**Optimization opportunities:**
1.
2.
3.

**Information still needed from client:**
1.
2.

---

*Next step: take this completed analysis into `strategy-recommendation.md` to build the recommendation set, then populate `templates/tax-strategy-template.md` for the client-facing memo.*

> Verify all rates and deadlines against current FTA guidance before finalising any client communication.
> See ../../_shared/finanshels-context.md for UAE tax facts, rates, and deadlines.
