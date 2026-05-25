---
name: malpractice-prevention-guide
description: Use when a Finanshels team member wants to audit an engagement, workflow, or process for professional-liability risk before work begins or after an incident. Triggers include phrases like "are we protected on this engagement", "audit this workflow for risk", "what could go wrong professionally", "engagement letter risk", "deadline exposure", "client reliance on unverified data", or "malpractice risk". Produces a structured risk checklist graded by severity with concrete mitigation steps and a go/no-go recommendation.
---

# Malpractice Prevention Guide — Professional Liability Risk Audit

Audits a Finanshels engagement or internal process for professional-liability exposure: unclear scope, missing documentation, unverified client data reliance, regulatory deadline risk, and communication failures that can become claims.

## When to use

- Before onboarding a new client or starting a new engagement type.
- When an engagement letter is being drafted or a scope is being agreed verbally.
- When a client provides data late, incompletely, or in an unusual format and work must proceed anyway.
- When a regulatory deadline is approaching and the team is unsure whether the engagement is properly documented.
- After a near-miss, client complaint, or dispute — to understand what protection exists.
- Periodic review of a recurring engagement (e.g. annual CT return workflow) to check the process is still sound.
- When sub-contractors or freelancers are being used on a client engagement.

## Inputs needed

**Required**
- Brief description of the engagement or process (service type, client type, scope summary).
- Current documentation status: engagement letter signed? Scope agreed in writing?
- Any known risk factors (tight deadline, client slow to respond, complex structure, new service area).

**Optional**
- Copy or summary of the engagement letter or scope document.
- The regulatory deadline(s) involved (e.g. CT return due date, VAT period).
- Whether sub-contractors or third parties are involved.
- History of any prior disputes or complaints on similar engagements.

## Workflow

1. **Engagement documentation check**
   - Confirm whether a signed engagement letter exists for this specific engagement.
   - If no engagement letter: flag as CRITICAL. Work should not proceed without one.
   - Confirm the engagement letter covers: scope, fee, timeline, reliance on client data, liability cap, termination, and governing law.
   - Check whether the engagement letter is current (not a stale letter from a prior year that hasn't been re-signed).
   - Flag any verbal-only scope expansions since the last signed letter as HIGH.

2. **Scope clarity audit**
   - Map the exact deliverables expected against what is written in the engagement letter.
   - Identify any gap between what the client expects and what Finanshels has committed to in writing.
   - Common gap: client expects "full compliance advice" but the engagement only covers bookkeeping.
   - Flag unclear deliverables as MEDIUM; flag deliverables outside Finanshels' licensed scope as CRITICAL.
   - Confirm whether the engagement involves any regulated activity outside Finanshels' authorizations (legal advice, investment advice, regulatory consulting that requires separate licensing).

3. **Client data reliability assessment**
   - Identify the data sources Finanshels is relying on: bank feeds, client-provided spreadsheets, scanned invoices, ERP exports, payroll reports.
   - For each source, assess: Has Finanshels verified completeness and accuracy? Is there an acknowledgement from the client that the data is complete?
   - Flag any engagement where Finanshels is filing a regulatory return (VAT, CT) based on unverified or partially verified client data as HIGH.
   - Confirm whether reconciliation steps are built into the workflow (e.g. bank reconciliation before VAT return).
   - Document data gaps that have been communicated to the client in writing.

4. **Regulatory deadline exposure**
   - List every regulatory deadline relevant to this engagement (CT return, VAT return, payroll WPS, UBO register, company licence renewal).
   - For each deadline: confirm whether Finanshels has received all required client inputs with enough lead time.
   - Calculate the buffer: if the client has not delivered data with at least [X] days buffer, flag as HIGH and trigger client escalation.
   - Standard buffers (adjust for complexity):
     - VAT return: client data 10 business days before the 28th of the filing month.
     - CT return: client data 6 weeks before the 9-month deadline.
     - Payroll WPS: data 3 business days before salary date.
   - Flag any deadline where Finanshels is dependent on a third party (e.g. auditor, bank, free zone authority) and that dependency has not been confirmed.

5. **Communication and audit trail**
   - Confirm that all material instructions, scope changes, and data requests are documented in writing (email or the Finanshels client portal).
   - Flag any significant client instruction received verbally only as MEDIUM.
   - Check whether deadline reminders and data-request chasers are logged.
   - Confirm whether the client has acknowledged receipt of any advisory memos or risk warnings.

6. **Sub-contractor and third-party exposure**
   - If sub-contractors are used: confirm they have signed a sub-contractor agreement covering scope, confidentiality, AML obligations, and error liability.
   - Flag any sub-contractor engagement without a written agreement as HIGH.
   - Confirm whether Finanshels remains liable to the client for sub-contractor errors (it usually does under the engagement letter — the sub-contractor agreement should provide back-to-back recourse).
   - For any third-party systems (cloud accounting software, payroll platforms): confirm data security and access controls are appropriate.

7. **Client onboarding and KYC status**
   - Confirm CDD/KYC has been completed for this client before engagement commencement.
   - Verify the client is not on any sanctions list (UAE, UN, OFAC).
   - Flag incomplete CDD as CRITICAL — work should not commence until satisfied.
   - Confirm UBO information has been collected and is on file.

8. **Fee and payment risk**
   - Assess whether outstanding fees create a conflict of interest or pressure to overlook errors.
   - Flag any engagement where fees are significantly overdue and work is continuing as MEDIUM (creates leverage risk and independence concerns).
   - Confirm whether fee disputes could be used by the client as leverage in a malpractice claim.

9. **Compile risk checklist and mitigation plan**
   - Summarize all findings in the output format below.
   - For each CRITICAL or HIGH item: provide a specific, actionable mitigation step.
   - Produce a go/no-go recommendation with conditions.

## Output format

```
MALPRACTICE RISK AUDIT — [Engagement / Process Name]
Date: [date]
Prepared by: Finanshels (internal draft — not for client distribution)

GO / NO-GO: [GO | GO WITH MITIGATIONS | HOLD PENDING CRITICAL FIXES]

CRITICAL ACTIONS REQUIRED BEFORE PROCEEDING:
1. [Action + owner + deadline]
2. [Action + owner + deadline]

---

RISK CHECKLIST

| # | Area | Finding | Severity | Mitigation |
|---|------|---------|----------|------------|
| 1 | Engagement Letter | No signed engagement letter | CRITICAL | Obtain signed letter before any billable work. Use standard Finanshels template. |
| 2 | Client Data | VAT return being prepared on unreconciled bank data | HIGH | Complete bank reconciliation; get written client sign-off on data completeness. |
| 3 | Deadline | CT return data not received; 14 days to filing deadline | HIGH | Issue formal written deadline notice to client; document in CRM. If data not received by [date], notify client of inability to file and confirm instruction. |
| 4 | Scope | Client expects tax advisory; letter only covers return preparation | MEDIUM | Clarify scope in writing; issue supplemental engagement letter or written confirmation. |
| 5 | ... | ... | ... | ... |

---

PROCESS IMPROVEMENT NOTES:
- [Systemic observation: e.g. "This pattern of late client data on CT returns suggests a template chase sequence should be built into the workflow."]

---

DISCLAIMER: This audit is an internal professional tool for Finanshels team use. It is not legal advice and does not constitute a legal opinion on professional liability. Matters involving actual or threatened claims should be referred to Finanshels' legal counsel and professional indemnity insurer immediately.
```

## Quality checklist

- [ ] Engagement letter status confirmed — CRITICAL flagged if absent.
- [ ] Scope gap between letter and client expectations identified.
- [ ] Data sources and verification status assessed.
- [ ] All regulatory deadlines listed with buffer calculations.
- [ ] Written communication trail assessed.
- [ ] Sub-contractor agreements verified if applicable.
- [ ] CDD/KYC status confirmed for the client.
- [ ] Every CRITICAL and HIGH item has a specific mitigation with an owner.
- [ ] Go/no-go recommendation is explicit.
- [ ] Disclaimer included on output.

## Examples

- "We're about to file a CT return for a client who gave us their trial balance 10 days before the deadline and we haven't reconciled it yet. Audit the risk."
- "A client is asking us to do VAT advisory in addition to the bookkeeping we normally do for them. No new engagement letter has been signed. What's our exposure?"
- "We're using a freelance bookkeeper to help with a large client's month-end. Is our process properly protected from a malpractice perspective?"

## Guardrails

- **Internal use only.** This output must never be shared with the client — it is an internal risk assessment and could constitute an admission if shared in a dispute.
- **Not legal advice.** This is a professional risk-management tool. Any actual or threatened claim, regulatory investigation, or dispute must immediately be referred to Finanshels' legal counsel and professional indemnity insurer.
- **UAE jurisdiction only.** Regulatory deadlines, standards of care, and AML obligations referenced are UAE-specific. Do not apply foreign professional standards.
- **Verify current deadlines.** FTA deadlines and regulatory requirements change. Always confirm against current FTA guidance and the relevant decree-law before relying on any deadline stated here.
- **No client names in examples.** Use placeholders only.

## Reference

See ../_shared/finanshels-context.md for UAE tax facts, rates, and deadlines.
See workflows/risk-audit.md for the step-by-step risk audit workflow template.
