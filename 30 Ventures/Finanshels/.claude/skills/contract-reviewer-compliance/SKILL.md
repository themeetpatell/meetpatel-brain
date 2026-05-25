---
name: contract-reviewer-compliance
description: Use when a Finanshels team member needs to review a client or vendor contract for compliance gaps, liability risks, and obligations relevant to a UAE accounting firm. Triggers include phrases like "review this contract", "check this agreement", "flag liability issues", "is this engagement letter compliant", or when a draft MSA, vendor SLA, or services agreement is pasted or uploaded. Produces a structured risk matrix with severity ratings, specific clause recommendations, and a pass/flag/fix summary.
---

# Contract Reviewer — UAE Compliance & Liability Risk

Reviews client-engagement, vendor, and sub-contractor contracts for risks material to a UAE accounting and bookkeeping firm: scope creep, liability exposure, data-protection obligations, AML/CFT duties, payment terms, and regulatory compliance triggers.

## When to use

- A new client engagement letter or master services agreement (MSA) needs review before signing.
- A vendor, software provider, or sub-contractor sends a contract for Finanshels to sign.
- An existing agreement is being renewed and the team wants a fresh compliance pass.
- An internal template is being updated and needs a compliance quality-check.
- A contract contains clauses about financial data, tax filings, AML reporting, or regulatory deliverables — any area where Finanshels has professional obligations.

## Inputs needed

**Required**
- Full contract text (paste inline or describe key clauses section by section).
- Contract type (e.g. client engagement letter, vendor SLA, data-processing agreement, sub-contractor agreement, NDA).
- Counterparty type (client / vendor / sub-contractor / regulator / bank).

**Optional**
- Jurisdiction of the counterparty (mainland UAE, free zone name, foreign entity).
- Known deal context: fixed fee vs. retainer, scope summary, sensitive data types involved.
- Any specific clauses the team is already concerned about.

## Workflow

1. **Identify contract type and governing law**
   - Confirm the governing law clause. For Finanshels contracts the default should be UAE law (specifically DIFC Courts or UAE mainland courts, or an agreed free zone forum).
   - Flag if governing law is a foreign jurisdiction — this is a HIGH risk for enforceability of UAE regulatory obligations.
   - Note whether the contract references a specific dispute-resolution mechanism (arbitration, DIFC Courts, onshore courts).

2. **Parse scope of services**
   - Extract the exact services listed. Compare against what Finanshels is actually delivering.
   - Flag any undefined, open-ended, or "and such other services as agreed" language as MEDIUM risk (scope creep).
   - Confirm whether the scope explicitly excludes services outside the mandate (e.g. legal advice, investment advice, actuary work).
   - For engagement letters: verify the scope aligns with the applicable FTA-regulated services if Corporate Tax or VAT filing is included.

3. **Review liability and indemnity clauses**
   - Identify the liability cap. Flag any uncapped liability provisions as CRITICAL.
   - Standard position for Finanshels: liability should be capped at fees paid in the preceding 12 months (or a fixed AED amount).
   - Flag any mutual indemnity obligations — especially those that could bind Finanshels to indemnify a client for regulatory penalties the client caused.
   - Check for consequential-loss exclusion. If missing, flag as HIGH.
   - Review whether professional indemnity insurance requirements are stated and are achievable.

4. **AML/CFT and DNFBP obligations**
   - Finanshels is a DNFBP under UAE AML law. Check whether the contract:
     - Permits Finanshels to terminate if the client fails CDD/KYC.
     - Does NOT restrict Finanshels from filing SAR/STR reports (such restriction would be illegal).
     - Does NOT create confidentiality obligations that would prevent goAML reporting.
   - Flag any confidentiality clause that says "do not disclose any information about this engagement to any third party including regulators" as CRITICAL — this conflicts with mandatory AML reporting duties.

5. **Data protection and confidentiality**
   - UAE does not yet have a comprehensive federal personal data protection law equivalent to GDPR, but the **Dubai International Financial Centre (DIFC) Data Protection Law** and **Abu Dhabi Global Market (ADGM) Data Protection Regulations** apply within those free zones.
   - For mainland contracts: assess whether any sector-specific data rules apply (MOHRE for payroll data, FTA for tax data).
   - Confirm: who owns the data and work product; whether client data can be used for benchmarking/anonymized analysis; how data is destroyed on termination.
   - Flag any clause that claims ownership of Finanshels' working papers, methodology, or proprietary tools as HIGH.

6. **Payment terms and late payment**
   - Standard UAE commercial practice: 30-day payment terms. Flag anything beyond 60 days as MEDIUM.
   - Check for a late-payment interest clause. UAE courts enforce contractual interest; ensure the rate is specified and reasonable.
   - Verify invoicing currency is AED or a stated FX rate mechanism. Flag ambiguous currency as MEDIUM.
   - Flag any "pay-when-paid" provisions (sub-contractor pays only when they are paid) as HIGH.

7. **Termination and notice**
   - Confirm termination-for-convenience provisions exist for both parties.
   - Flag any lock-in beyond 12 months without a break clause as MEDIUM.
   - Check whether termination triggers Finanshels' handover obligations (returning records, access to EmaraTax, etc.) and whether timelines are realistic.
   - Confirm that outstanding fee obligations survive termination.

8. **Regulatory and filing obligations**
   - For any contract covering CT or VAT work: confirm the contract states Finanshels acts as an agent/authorized representative, not as guarantor of tax outcomes.
   - Flag any language that makes Finanshels liable for penalties arising from client-provided incorrect data as HIGH.
   - Confirm a "reliance on client information" clause is present — Finanshels' accuracy is contingent on the client supplying complete and correct data.

9. **Produce risk matrix**
   - Compile findings into the output format below.
   - Assign severity: CRITICAL / HIGH / MEDIUM / LOW.
   - For each finding: state the clause (if identifiable), the risk, and the recommended fix or negotiating position.

10. **Produce summary recommendation**
    - Overall verdict: APPROVE / APPROVE WITH CONDITIONS / DO NOT SIGN PENDING REVISIONS.
    - List the minimum conditions that must be met before signing.

## Output format

```
CONTRACT REVIEW — [Contract Type] — [Counterparty Name or Type]
Date reviewed: [date]
Reviewed by: Finanshels (draft — requires qualified legal review before reliance)

SUMMARY VERDICT: [APPROVE / APPROVE WITH CONDITIONS / DO NOT SIGN PENDING REVISIONS]

MINIMUM CONDITIONS BEFORE SIGNING:
1. [Condition]
2. [Condition]

---

RISK MATRIX

| # | Clause / Section | Issue | Severity | Recommendation |
|---|-----------------|-------|----------|----------------|
| 1 | [e.g. Clause 8 — Liability] | Uncapped liability | CRITICAL | Insert cap at 12 months' fees or AED [X] |
| 2 | [e.g. Clause 12 — Confidentiality] | Blanket confidentiality may restrict AML reporting | CRITICAL | Add carve-out: "Nothing in this clause restricts either party from complying with applicable law or regulatory obligations." |
| 3 | ... | ... | HIGH | ... |

---

POSITIVE FINDINGS (clauses that are well-drafted):
- [Clause reference]: [Why it is good]

---

DRAFTING NOTES FOR NEGOTIATION:
- [Specific suggested replacement language for the top 2-3 issues]

---
DISCLAIMER: This review is a professional draft prepared by Finanshels for internal use. It is not legal advice. All contracts must be reviewed by a qualified UAE-licensed legal practitioner before execution.
```

## Quality checklist

- [ ] Governing law and dispute resolution identified.
- [ ] Liability cap reviewed and flagged if uncapped or inadequate.
- [ ] Consequential-loss exclusion checked.
- [ ] AML/CFT carve-out in confidentiality clause verified.
- [ ] SAR/STR reporting not restricted.
- [ ] Scope clearly defined, open-ended language flagged.
- [ ] Reliance-on-client-data clause present for tax/accounting work.
- [ ] Data ownership and destruction clauses assessed.
- [ ] Payment terms and late-payment mechanism confirmed.
- [ ] Termination provisions and handover obligations checked.
- [ ] Risk matrix has severity for every finding.
- [ ] Disclaimer included on output.

## Examples

- "Review this engagement letter from a new mainland client — they've added a clause making us liable for any FTA penalties. Flag the risk."
- "Our new cloud accounting software vendor sent us their standard SLA. Check it for data-protection issues and liability gaps from a UAE firm's perspective."
- "We're renewing a sub-contractor agreement with a freelance bookkeeper. Does it cover AML obligations and protect us if they make errors?"

## Guardrails

- **UAE jurisdiction only.** Do not apply GDPR, US contract law, or any non-UAE framework unless the contract explicitly invokes a foreign law and that is itself the issue being flagged.
- **Draft only — not legal advice.** This output is a professional internal work product. It MUST be reviewed by a qualified UAE-licensed legal practitioner before any contract is signed or any legal position is adopted. Finanshels does not provide legal services.
- **No real client names in output.** Use placeholders (e.g. "Client A", "Vendor X") if a name appears in the contract text.
- **Verify current law.** UAE commercial and data protection law evolves. Confirm AML/CFT obligations against the current UAE AML framework and FTA guidance before relying on this review.
- **Client data is confidential.** Treat any financial, operational, or personal data in a contract as strictly confidential.

## Reference

See ../_shared/finanshels-context.md for UAE tax facts, rates, and deadlines.
See checklists/compliance-checklist.md for the full clause-by-clause checklist.
