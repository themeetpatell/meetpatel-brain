---
name: engagement-letter-generator
description: Use when a Finanshels team member needs to draft a professional engagement letter for a new or existing client covering a specific service scope. Triggers include: onboarding a new client for bookkeeping, UAE CT registration, CT return filing, VAT registration or return filing, outsourced CFO, payroll/WPS, AML compliance, or audit support. Produces a complete, ready-to-review engagement letter using the Finanshels standard template with all required scope, fee, and compliance disclosures.
---

# Engagement Letter Generator

Drafts a Finanshels-branded engagement letter for a defined service scope, including all required professional, legal, and UAE-specific disclosures, ready for partner review and client signature.

## When to use

- New client onboarding: any service engagement
- Scope change or expansion: adding services to an existing engagement
- Annual renewal: refreshing the engagement letter for a continuing client
- Specific project engagement: CT registration, FTA audit support, restructuring advice
- Creating a master engagement letter covering multiple services

Service scopes this skill handles:
- Bookkeeping and accounting (monthly / quarterly / annual)
- UAE Corporate Tax: registration, advisory, return preparation and filing
- UAE VAT: registration, advisory, return preparation and filing
- Outsourced / fractional CFO and management reporting
- Payroll processing and WPS compliance
- AML/CFT compliance services (for clients that are also DNFBPs)
- Audit support and audit-ready financials preparation
- Company formation and PRO support
- Transfer pricing documentation

## Inputs needed

**Required**
- Client legal name and entity type (mainland LLC / free zone / branch / natural person)
- Trade licence number and issuing authority
- Client address (registered office)
- Services to be provided (list from the service scopes above)
- Proposed start date of engagement
- Proposed fee structure (fixed monthly / quarterly / project / hourly) with amounts in AED
- Name and title of Finanshels engagement partner or manager
- Name and title of client signatory (authorised to sign on behalf of the entity)

**Optional**
- Financial year end (needed for CT and VAT scope sections)
- Prior accountant / tax agent details (if this is a takeover engagement — transition clause needed)
- Specific exclusions from scope (e.g. "excludes transfer pricing documentation")
- Payment terms preference (default: 30 days from invoice)
- Any special conditions or limitations agreed with the client

## Workflow

1. **Confirm scope**
   List each service being engaged. For each service, determine:
   - What Finanshels will do (deliverables, frequency)
   - What the client must provide (records, access, approvals) — client responsibilities are critical for engagement letters; they limit professional liability
   - What is explicitly excluded from scope

2. **Select the correct registration and compliance disclosures**
   Based on services in scope, include the mandatory disclosure sections:
   - **CT services:** Disclosure that UAE CT advice is based on Federal Decree-Law No. 47 of 2022 and current FTA guidance, subject to change; returns are prepared based on information provided by the client
   - **VAT services:** Disclosure that UAE VAT advice is based on Federal Decree-Law No. 8 of 2017 and current FTA guidance
   - **AML/CFT (if Finanshels is supporting a client who is itself a DNFBP):** Disclosure of the nature of the AML advisory service; note that the client retains responsibility for filing STRs/SARs on goAML
   - **All letters:** Professional indemnity disclosure; limitation of liability clause; confidentiality; data protection; anti-bribery and anti-corruption compliance

3. **Draft the engagement letter**
   Use the template at `./templates/engagement-letter.md`. Fill every section. Do not leave any placeholder unfilled.

4. **Write the scope-of-services section**
   For each service:
   - 3–5 bullet points describing what Finanshels will deliver
   - 2–3 bullet points describing what the client must provide / do
   - Explicit statement of what is not included

5. **Write the fees section**
   State:
   - Fee for each service (AED, VAT-exclusive — note that Finanshels charges VAT at 5% on its fees)
   - Payment frequency and method
   - Late-payment clause (default: interest or suspension of services after 60 days)
   - Out-of-pocket expenses policy

6. **Write the term and termination clause**
   - Start date and initial term (typically 12 months for retainer services)
   - Renewal: auto-renewal clause with written notice period to terminate (typically 30 or 60 days)
   - Termination-for-cause clause
   - Handover obligations on termination (records returned to client)

7. **Add the mandatory professional and legal clauses**
   These must appear in every letter:
   - Confidentiality
   - Data protection (reference to UAE PDPL, Federal Decree-Law No. 45 of 2021)
   - Limitation of liability (cap on Finanshels liability to fees paid in the prior 12 months, unless gross negligence)
   - Anti-bribery and anti-corruption (client and Finanshels compliance with UAE law)
   - Professional indemnity insurance disclosure
   - Governing law: UAE; disputes subject to courts of [emirate] or agreed arbitration

8. **Review before finalising**
   - All client details correct
   - All fee amounts stated in AED
   - VAT at 5% on Finanshels fees noted
   - Scope exclusions explicitly stated
   - Client responsibility section clear and specific
   - All mandatory clauses present
   - Partner sign-off block included

## Output format

The output is a complete engagement letter document following the structure in `./templates/engagement-letter.md`:

```
FINANSHELS
[Address | TRN | Contact]

[Date]

[Client signatory name and title]
[Client legal name]
[Client registered address]

Dear [Title + Surname],

Re: Engagement Letter — [Service(s)] — [Client legal name]

---
1. Introduction and Purpose
2. Scope of Services
   2.1 [Service 1]
   2.2 [Service 2]
   ...
3. Client Responsibilities
4. Exclusions from Scope
5. Fees and Payment Terms
6. Term and Termination
7. Confidentiality
8. Data Protection
9. Limitation of Liability
10. Anti-Bribery and Anti-Corruption
11. Governing Law and Disputes
12. Professional Indemnity
13. Acceptance

Yours sincerely,
[Partner name, title]
Finanshels

---
ACCEPTANCE
[Client signature block]
```

## Quality checklist

- [ ] All client details (legal name, trade licence, address, signatory) completed
- [ ] Every service in scope has a deliverables list and a client-responsibilities list
- [ ] Scope exclusions explicitly stated (no ambiguity about what is not included)
- [ ] Fees stated in AED; VAT at 5% on Finanshels fees noted
- [ ] Payment terms and late-payment clause included
- [ ] Term, renewal, and termination clauses present
- [ ] All 6 mandatory professional clauses included (confidentiality, PDPL, liability cap, anti-bribery, professional indemnity, governing law)
- [ ] CT disclosure references Federal Decree-Law No. 47 of 2022 (if CT in scope)
- [ ] VAT disclosure references Federal Decree-Law No. 8 of 2017 (if VAT in scope)
- [ ] Client acceptance and signature block at the end
- [ ] Letter reviewed by a qualified Finanshels team member before sending

## Examples

**Example 1 — Full-service onboarding**
> "New client: a Dubai mainland e-commerce LLC, AED 5M revenue, FY ending 31 December. They want bookkeeping, monthly management accounts, VAT quarterly filing, and CT return for FY2024. Generate the engagement letter. Fees: AED 3,500/month for bookkeeping + management accounts, AED 2,000/quarter for VAT, AED 5,000 for the CT return."

**Example 2 — CT registration only**
> "A RAK free zone tech startup just crossed the AED 375K threshold. They need CT registration only right now. Generate a short-form engagement letter for a one-off CT registration service, AED 1,500 fixed fee."

**Example 3 — Audit support for QFZP**
> "A JAFZA logistics company, AED 30M revenue, needs audit-ready financial statements prepared because they're claiming QFZP status. Generate an engagement letter covering audit support and financial statement preparation, AED 15,000 fixed fee."

## Guardrails

- This skill produces a draft engagement letter for review by a qualified Finanshels team member and, where appropriate, legal counsel before it is sent to a client.
- Do not include specific legal warranties or representations beyond those in the standard template.
- Fee amounts are as provided by the requesting team member — this skill does not determine pricing.
- UAE jurisdiction only. Governing law is UAE; do not reference other legal systems.
- Do not include real client data from prior engagements in examples or templates.

## Reference

See `../_shared/finanshels-context.md` for UAE tax facts, rates, and deadlines.
