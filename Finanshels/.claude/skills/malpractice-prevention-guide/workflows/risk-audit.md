# Risk Audit Workflow — Malpractice Prevention
## Finanshels Internal Process Guide

> This workflow is the operational companion to the `malpractice-prevention-guide` skill.
> Run this before starting any new engagement and at least annually on recurring engagements.

---

## Overview

Professional liability claims against accounting firms typically arise from:
1. **Scope disputes** — client expected more than the letter said.
2. **Reliance on bad data** — Finanshels filed on numbers the client provided that were wrong.
3. **Missed deadlines** — a regulatory penalty was incurred and the client blames the firm.
4. **Communication failures** — advice was given verbally and later denied.
5. **CDD gaps** — work was done for a client whose KYC was incomplete.

This workflow addresses each category systematically.

---

## Phase 1 — Pre-Engagement Gate (before any billable work)

### Step 1.1 — CDD/KYC Clearance

- [ ] Obtain trade licence / certificate of incorporation.
- [ ] Collect passport copies and Emirates IDs for all beneficial owners (>25% ownership).
- [ ] Collect UBO declaration form.
- [ ] Screen client and UBOs against: UAE Sanctions List, UN Consolidated List, OFAC SDN List.
- [ ] Record CDD outcome in the client file (PASS / ESCALATE / REJECT).
- [ ] If ESCALATE or REJECT: do not commence work. Refer to MLRO (Money Laundering Reporting Officer).

**Gate: Work cannot commence until CDD = PASS.**

### Step 1.2 — Engagement Letter Sign-off

- [ ] Use the current Finanshels engagement letter template for the service type.
- [ ] Ensure the letter includes: scope, fee, payment terms, liability cap, reliance on client data, termination, governing law.
- [ ] Obtain a wet or e-signature from an authorized signatory of the client.
- [ ] File the signed letter in the client record system (not just email).
- [ ] If the client requests scope changes before signing: update the letter; do not proceed on the amended scope until a revised letter is signed.

**Gate: No work commences without a signed engagement letter.**

### Step 1.3 — Scope Briefing

- [ ] Brief the delivery team on the exact scope in the engagement letter.
- [ ] Confirm: what is in scope; what is explicitly out of scope.
- [ ] Flag any client expectation that exceeds the written scope — resolve before commencing.

---

## Phase 2 — During Engagement (ongoing)

### Step 2.1 — Data Collection Protocol

For every regulatory filing (VAT return, CT return, payroll, WPS):

| Step | Action | Owner | Timing |
|------|--------|-------|--------|
| D1 | Send data-request checklist to client | Account Manager | T-25 business days before deadline |
| D2 | First chase if not received | Account Manager | T-15 business days |
| D3 | Escalation chase (senior) | Senior / Director | T-10 business days |
| D4 | Formal written notice: data not received, deadline at risk | Senior / Director | T-7 business days |
| D5 | If still not received: client confirms in writing they accept risk of late filing or extension | Account Manager | T-5 business days |

**Data-request checklist contents (VAT return example):**
- Bank statements for the period (all accounts).
- Sales invoices / revenue report.
- Purchase invoices / expense report.
- Reconciled trial balance.
- Any credit notes or adjustments.
- Confirmation that the list is complete and no invoices are missing.

### Step 2.2 — Data Verification Checkpoints

Before any regulatory return is submitted:

- [ ] Bank reconciliation completed and any differences documented.
- [ ] Revenue per books agrees to revenue per VAT / CT computation (or differences are explained).
- [ ] Material transactions (>AED 50,000) have supporting documentation on file.
- [ ] Client has signed a data-completeness confirmation (use the standard sign-off email template).
- [ ] Preparer and reviewer are different people (four-eyes principle).

### Step 2.3 — Written Communication Log

- [ ] All material advice is followed up by email within 24 hours of any verbal discussion.
- [ ] All scope changes are documented as written variations (email confirmation at minimum; formal variation order for changes >AED 5,000 in fees).
- [ ] All risk warnings to the client (e.g. "your VAT registration threshold has been exceeded") are in writing and the client's acknowledgement is obtained.
- [ ] Deadline reminders to clients are logged in the CRM with timestamp.

### Step 2.4 — Sub-Contractor Management

If a sub-contractor or freelancer is used on this engagement:

- [ ] Sub-contractor agreement signed covering: scope, confidentiality, AML obligations, error liability, IP ownership.
- [ ] Sub-contractor has been briefed on the client's scope and data-security requirements.
- [ ] All sub-contractor work product is reviewed by a Finanshels employee before delivery to the client.
- [ ] Client is aware (as required by the engagement letter) that sub-contractors may be used.

---

## Phase 3 — Pre-Submission Review

Before submitting any regulatory filing or delivering any significant work product:

### Step 3.1 — Technical Review

- [ ] Preparer completes self-review checklist for the applicable return type.
- [ ] Senior reviewer signs off using the Finanshels review-and-approve workflow.
- [ ] Any material judgement calls (e.g. VAT treatment of a complex transaction) are documented and the rationale recorded.
- [ ] If a judgement call is uncertain: internal escalation or external specialist opinion obtained and documented.

### Step 3.2 — Client Sign-off on Material Items

For CT returns and any filing with a material judgement call:

- [ ] Summary of key items sent to client for confirmation before submission.
- [ ] Client confirmation received in writing.
- [ ] Confirmation filed with the engagement record.

### Step 3.3 — Final Deadline Check

- [ ] Confirm the submission deadline against the FTA portal (EmaraTax) — do not rely solely on a calendar reminder.
- [ ] Allow minimum 24-hour buffer for system issues; 48 hours for first-time filings.
- [ ] If submission is within 48 hours and any open item remains: escalate immediately.

---

## Phase 4 — Post-Engagement & Annual Review

### Step 4.1 — Engagement Closure

- [ ] Deliverables filed/delivered and confirmed.
- [ ] Filing confirmation / acknowledgement from FTA (EmaraTax confirmation) saved to client file.
- [ ] All original client documents returned or destruction confirmed per data retention policy.
- [ ] Outstanding fees collected or payment plan agreed.

### Step 4.2 — Annual Engagement Review (recurring clients)

Once per year, or before renewal of an annual engagement:

- [ ] Re-confirm CDD is current (re-screen for sanctions, update if UBO has changed).
- [ ] Re-sign engagement letter (or issue a formal renewal confirmation).
- [ ] Review whether the scope has expanded informally — if so, issue a supplemental engagement letter.
- [ ] Review whether the liability cap in the existing letter is still adequate given the size/complexity of the work.

---

## Severity Reference

| Level | Definition | Required Response |
|-------|-----------|-------------------|
| CRITICAL | Work cannot safely proceed; regulatory, legal, or financial exposure is high | Stop. Fix before proceeding. Escalate to Director. |
| HIGH | Significant risk; must be mitigated before filing/delivery | Assign owner; resolve within 48 hours or escalate. |
| MEDIUM | Notable risk; should be addressed | Assign owner; resolve within 1 week. |
| LOW | Minor; monitor | Note in file; review at next engagement checkpoint. |

---

## Escalation Contacts

| Situation | Escalate to |
|-----------|-------------|
| CDD failure / sanctions hit | MLRO immediately — do not proceed, do not inform client |
| Actual or threatened client complaint | Director + Legal Counsel |
| Suspected fraud in client data | MLRO + Legal Counsel immediately |
| Regulatory inquiry from FTA | Director + Legal Counsel |
| Near-miss (error caught before delivery) | Director; document in lessons-learned log |

---

> **Disclaimer:** This workflow is an internal operational tool. It is not legal advice.
> Matters involving actual or threatened claims, regulatory investigations, or AML concerns
> must be referred to Finanshels' legal counsel and MLRO immediately.
> Regulatory requirements and deadlines change — verify against current FTA and UAE government guidance.
