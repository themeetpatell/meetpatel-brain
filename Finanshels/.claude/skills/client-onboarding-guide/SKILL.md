---
name: client-onboarding-guide
description: Use when a new client is being onboarded to Finanshels — triggered by phrases like "new client", "onboard", "intake", "start engagement", "KYC", or "client setup". Produces a tailored onboarding checklist, document collection list, and kickoff agenda based on the client's entity type (mainland vs free zone), services engaged, and jurisdiction, fully aligned with UAE AML/CFT CDD requirements and Finanshels service scope.
---

# Client Onboarding Guide

Standardizes new-client intake for Finanshels: KYC/AML CDD, document collection, system access provisioning, and kickoff meeting preparation — for every new engagement, every time.

## When to use

- A new client engagement has been confirmed and needs to be set up
- Preparing for an initial client kickoff call
- Completing Customer Due Diligence (CDD) before work begins (mandatory per UAE AML/CFT obligations)
- Collecting entity documents for VAT, Corporate Tax, or bookkeeping engagements
- Setting up system access on EmaraTax, Xero/QuickBooks, or internal Finanshels tools
- A new service is being added to an existing client (partial re-onboarding)

## Inputs needed

**Required:**
- Client legal name and trade name (if different)
- Entity type: mainland DED-licensed / free zone / offshore / branch
- Free zone name (if applicable, e.g. DIFC, ADGM, RAKEZ, DMCC)
- Services engaged: bookkeeping, VAT, Corporate Tax, payroll, CFO, audit support, or combinations
- Primary contact name, role, email, phone
- Financial year-end date (or best estimate)
- Approximate annual revenue (AED range)

**Optional:**
- Existing VAT TRN (Tax Registration Number) — if already registered
- Existing CT registration number — if already registered
- Preferred accounting software (Xero, QuickBooks, Zoho, or to be set up fresh)
- Number of employees (for payroll scope)
- Prior accountant / prior books status (clean, needs catch-up, unknown)

## Workflow

### Phase 1 — Engagement Confirmation & CDD Trigger (Day 0–1)

1. Confirm signed engagement letter or service agreement is on file before proceeding. Do not begin work without this.
2. Open AML/CFT CDD checklist (see `workflows/onboarding-checklist.md`, Section A). Finanshels is a Designated Non-Financial Business and Profession (DNFBP) under UAE AML law — CDD is mandatory, not optional.
3. Screen client name and UBOs against UAE sanctions lists and goAML-registered screening tools. Document the outcome.
4. Assign a risk rating: Low / Medium / High. High-risk clients require Enhanced Due Diligence (EDD) and senior sign-off.
5. Record CDD completion date and responsible team member in the client file.

### Phase 2 — Document Collection (Day 1–5)

6. Send the client a document request list tailored to entity type:

   **All entities:**
   - Trade licence (valid, not expired)
   - Memorandum & Articles of Association (MoA / AoA)
   - Certificate of Incorporation
   - Passport copies + Emirates IDs for all shareholders ≥ 25% ownership and all authorized signatories
   - UBO declaration / UBO register extract
   - Proof of registered address (utility bill or tenancy contract ≤ 3 months)

   **Additional — Free Zone entities:**
   - Free zone licence + registration certificate
   - Share register from free zone authority
   - Confirmation of licence category (to assess QFZP eligibility under CT)

   **Additional — VAT-registered clients:**
   - VAT TRN certificate from FTA
   - Last 3 VAT return PDFs (if transferring from another agent)
   - VAT account login credentials (via EmaraTax agent access)

   **Additional — CT clients:**
   - CT registration certificate (if already registered)
   - Last audited financial statements (or draft accounts if new)
   - Chart of accounts from prior system

   **Additional — Payroll clients:**
   - WPS-registered bank account details
   - Current employee list with salaries, start dates, nationalities
   - Existing labour contracts (sample)

7. Set a document collection deadline of 5 business days. Chase on Day 3 if incomplete.
8. Upload all documents to the secure client folder (DMS / SharePoint / Dropbox). Never store client documents in personal email.

### Phase 3 — System Access & Setup (Day 3–7)

9. **EmaraTax:** Add Finanshels as authorized tax agent for the client's VAT and/or CT profile. Client must approve via EmaraTax portal — send them the agent-access request link and instructions.
10. **Accounting software:** If client has existing Xero/QuickBooks, request Adviser/Accountant access. If setting up fresh, create the company file with correct chart of accounts, VAT tax codes, and base currency (AED).
11. **Internal systems:** Create the client profile in Finanshels' project management tool, assign the engagement manager and bookkeeper, set up the recurring task schedule (monthly books, VAT return due dates, CT return due date).
12. **Calendar reminders:** Input all key deadlines for the first 12 months — VAT return due dates (28th of the month after the tax period), CT return due date (9 months after financial year-end), payroll WPS dates if applicable.

### Phase 4 — Kickoff Meeting Preparation (Day 5–10)

13. Prepare a kickoff agenda covering:
    - Introduction to the Finanshels team (engagement manager, bookkeeper, point of contact)
    - Scope walk-through: confirm exactly what is in and out of scope
    - Document handover: confirm any remaining items
    - Process overview: how books are handled, how client approves invoices/expenses, communication cadence
    - Upcoming deadlines: first VAT return due date, CT registration deadline if not yet done
    - Questions from client
14. Conduct the kickoff call (video or in-person). Record notes.
15. Send a post-kickoff email summary within 24 hours: agreed actions, owners, deadlines.

### Phase 5 — Onboarding Sign-Off (Day 10–14)

16. Confirm CDD file is complete and signed off by engagement manager.
17. Confirm all system accesses are live and tested.
18. Confirm opening trial balance is loaded or the first bookkeeping period is defined.
19. Mark onboarding complete in the internal tracker. Notify client.
20. Schedule a 30-day check-in call.

## Output format

Produce a structured **Onboarding Pack** containing:

```
## Onboarding Pack — [Client Name] — [Date]

### 1. Client Summary
Entity: [Name, type, free zone/mainland, licence number]
Services: [List]
Engagement Manager: [Name]
Financial Year-End: [Date]
Revenue Band: [AED range]
VAT TRN: [Number or "not yet registered"]
CT Registration: [Number or "pending" or "not required — Small Business Relief"]

### 2. CDD Status
Risk Rating: [Low / Medium / High]
Screening completed: [Date]
EDD required: [Yes / No]
CDD file signed off by: [Name, Date]

### 3. Document Collection Status
[Table: Document | Required? | Received? | Notes]

### 4. System Access Status
[Table: System | Action | Status | Date completed]

### 5. Key Deadlines — First 12 Months
[Table: Deliverable | Due Date | Owner]

### 6. Kickoff Meeting Notes
Date: [Date]
Attendees: [List]
Key decisions: [Bullet list]
Open actions: [Owner | Action | Due date]

### 7. Onboarding Sign-Off
Engagement Manager sign-off: [Name / Date]
CDD sign-off: [Name / Date]
Onboarding complete: [Yes / Pending — reason]
```

## Quality checklist

- [ ] Engagement letter is signed before any CDD or document collection begins
- [ ] CDD completed and risk-rated before work starts
- [ ] Sanctions screening documented with date and tool used
- [ ] EDD performed and signed off if risk rating is High
- [ ] Trade licence is valid (not expired) and matches the services scope
- [ ] UBO information collected and matches licence/MoA
- [ ] All entity-type-specific documents collected (free zone extra docs if applicable)
- [ ] EmaraTax agent access confirmed for VAT and/or CT
- [ ] Accounting software access is live (not just requested)
- [ ] All deadlines for first 12 months are in the internal calendar
- [ ] Kickoff meeting held and post-kickoff email sent within 24 hours
- [ ] Opening trial balance or first bookkeeping period defined
- [ ] 30-day check-in call scheduled

## Examples

**Example 1:**
"We've just signed a new client — Dubai mainland LLC, trading company, AED 4M revenue, engaging us for bookkeeping + VAT + Corporate Tax. Owner is Indian national, 2 shareholders. Run the onboarding."

**Example 2:**
"New DMCC free zone client, SaaS startup, AED 800K revenue, wants VAT registration and monthly books. They have a Xero account already. What do we need to collect and what are their first deadlines?"

**Example 3:**
"Onboard a new payroll-only client — Abu Dhabi mainland, construction, 45 employees, AED 12M revenue. Already has an accountant but needs WPS processing from us."

## Guardrails

- This skill covers mainland UAE and UAE-registered free zone entities only.
- CDD is a legal obligation under UAE AML/CFT law. Do not skip or abbreviate it, regardless of how well the client is known.
- Output is a professional work product. It must be reviewed and signed off by a qualified Finanshels engagement manager before being sent to or actioned on behalf of a client.
- Verify EmaraTax agent-access procedures against current FTA guidance — the portal UI changes periodically.
- Never store or log client document copies or credentials in this skill's output. Reference where they are stored, not what they contain.
- Risk ratings and EDD decisions require human judgment and senior sign-off. This skill provides a framework, not a regulatory determination.

## Reference

See ../_shared/finanshels-context.md for UAE tax facts, rates, and deadlines.
