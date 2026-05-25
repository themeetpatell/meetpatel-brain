---
name: nda-generator
description: Use when a Finanshels team member needs to generate a UAE-appropriate non-disclosure agreement (NDA) draft for sharing confidential financial, business, or client data with a counterparty. Triggers include phrases like "draft an NDA", "create a confidentiality agreement", "we need an NDA before sharing client data", "generate an NDA for a vendor", "NDA for a prospective client", or "confidentiality agreement for a new hire". Produces a complete NDA draft populated with the provided details, ready for legal review before execution.
---

# NDA Generator — UAE Non-Disclosure Agreement

Generates a tailored UAE-law NDA draft for client/vendor data sharing, prospective client discussions, employee onboarding, and sub-contractor engagements. Ensures AML/CFT carve-outs, appropriate confidentiality scope, and UAE-enforceable terms.

## When to use

- Before sharing confidential financial data or Finanshels' methodology with a prospective client.
- Before a vendor or software provider is given access to client data or Finanshels' internal systems.
- Before engaging a sub-contractor or freelancer on a client engagement.
- When a new employee or consultant joins and needs a standalone confidentiality agreement before their employment contract is finalized.
- When a partnership, referral, or integration discussion involves sharing proprietary business information.
- When a client asks for a mutual NDA before engaging Finanshels.

## Inputs needed

**Required**
- Disclosing party name and type (Finanshels / client / vendor / both = mutual).
- Receiving party name, type (individual / company), and jurisdiction (mainland UAE / free zone — specify / foreign entity).
- Purpose of disclosure (1–2 sentences describing why confidential information is being shared).
- NDA type: one-way (Finanshels discloses) / one-way (Finanshels receives) / mutual.

**Optional**
- Duration of confidentiality obligation (default: 3 years from date of agreement; or "indefinite" for trade secrets).
- Specific categories of information to be protected (financial data, client lists, software, methodology, pricing — default is broad).
- Whether the receiving party may engage sub-processors/sub-contractors with access to the information.
- Governing law preference (default: UAE mainland courts unless both parties are in a named free zone).
- Any specific carve-outs the requester has in mind (e.g. "exclude publicly known information").

## Workflow

1. **Confirm NDA type and parties**
   - Establish whether this is a one-way or mutual NDA.
   - For one-way: identify who is the Disclosing Party and who is the Receiving Party.
   - For mutual: both parties are simultaneously disclosing and receiving.
   - Confirm whether the counterparty is an individual (natural person) or a legal entity. This affects how authority to sign is established.
   - If the counterparty is a foreign entity: flag that UAE-law NDA enforceability against a foreign party may be limited — recommend including an arbitration clause with a recognized seat (e.g. DIAC, ICC Dubai).

2. **Define the confidential information**
   - Use the inputs to specify categories of information covered.
   - Default broad definition: "any information, data, know-how, financial records, client information, business plans, pricing, or methodology disclosed by the Disclosing Party, whether in written, oral, electronic, or any other form."
   - If the engagement involves specific data types (e.g. payroll data, FTA correspondence, client bank details), add those explicitly.
   - Standard exclusions to include: (a) information in the public domain through no fault of the Receiving Party; (b) information the Receiving Party independently developed; (c) information received from a third party without restriction; (d) information required to be disclosed by law or a competent authority.

3. **Draft AML/CFT and regulatory carve-out**
   - This clause is mandatory for Finanshels as a DNFBP.
   - The NDA must include: "Nothing in this Agreement shall prevent either party from disclosing Confidential Information to the extent required by applicable law, regulation, a court of competent jurisdiction, or a competent regulatory or law enforcement authority, including but not limited to disclosures required under UAE Federal Decree-Law No. 20 of 2018 on Anti-Money Laundering and Combating the Financing of Terrorism or any successor legislation."
   - This protects Finanshels' ability to file SAR/STR reports on the goAML portal without breaching the NDA.

4. **Set obligations of the Receiving Party**
   - Use the information only for the stated purpose.
   - Restrict access to employees/consultants who need to know and who are bound by equivalent obligations.
   - Not copy, reproduce, or distribute without consent.
   - Notify the Disclosing Party promptly upon discovery of any unauthorized disclosure.
   - Return or destroy confidential materials on request or on termination of the agreement.

5. **Set duration and term**
   - Agreement term: typically 1–2 years for business discussions; the NDA can survive the end of the discussion.
   - Confidentiality obligation duration: 3 years from disclosure is standard; trade secrets and client lists should be "indefinite" or "for so long as the information remains confidential."
   - Apply the requested duration from inputs, or use the default if not specified.

6. **Governing law and dispute resolution**
   - Default: UAE law; disputes subject to the exclusive jurisdiction of the courts of [Dubai / Abu Dhabi / named free zone courts].
   - If foreign counterparty or if both parties prefer: DIAC arbitration (Dubai International Arbitration Centre) or ICC arbitration seated in Dubai.
   - Add: "The parties agree that the courts of [jurisdiction] shall have exclusive jurisdiction over any dispute arising out of or in connection with this Agreement."

7. **Remedies clause**
   - Include: "The Receiving Party acknowledges that a breach of this Agreement would cause irreparable harm to the Disclosing Party for which monetary damages would be an inadequate remedy, and the Disclosing Party shall be entitled to seek injunctive relief and specific performance in addition to any other remedy available at law."
   - This is important because UAE courts can grant injunctions in commercial disputes.

8. **Populate the NDA template**
   - Fill in all details from inputs into the template at `templates/nda-template.md`.
   - Highlight all fields that require final confirmation (marked with `[CONFIRM: ...]` in the template).
   - Flag any inputs that are missing — the NDA cannot be finalized without them.

9. **Produce output**
   - Generate the complete NDA draft.
   - List any open items requiring confirmation before the NDA is ready for signature.
   - Include a summary of key commercial terms for the requester.

## Output format

```
NDA DRAFT — [One-Way / Mutual] — [Counterparty Name/Type]
Date: [date]
Prepared by: Finanshels (DRAFT — requires qualified legal review before execution)

KEY TERMS SUMMARY:
- Type: [One-way / Mutual]
- Disclosing Party: [name]
- Receiving Party: [name]
- Purpose: [purpose]
- Information covered: [categories]
- Duration of obligation: [X years / indefinite for trade secrets]
- Governing law: [UAE mainland / DIFC / ADGM / named jurisdiction]
- Dispute resolution: [courts / arbitration body]

OPEN ITEMS BEFORE SIGNING:
1. [Missing item or item requiring confirmation]

---

[FULL NDA TEXT — see template below — populated with the above details]

---
DISCLAIMER: This NDA is a draft prepared by Finanshels for internal use and review purposes. It is NOT legal advice and does NOT constitute a final, legally binding document. This draft MUST be reviewed and approved by a qualified UAE-licensed legal practitioner before execution. Law and regulatory requirements change — verify against current UAE legislation before relying on any provision.
```

## Quality checklist

- [ ] Parties correctly identified (legal names, types, jurisdictions).
- [ ] NDA type correct (one-way vs. mutual) and obligations drafted accordingly.
- [ ] Confidential information defined broadly with appropriate specific additions.
- [ ] Standard exclusions present (public domain, independent development, third-party disclosure, legal compulsion).
- [ ] AML/CFT and regulatory carve-out included (mandatory for Finanshels).
- [ ] Obligations of the Receiving Party cover: use limitation, need-to-know access, no copying, notification of breach, return/destruction.
- [ ] Duration of confidentiality obligation specified.
- [ ] Governing law and dispute resolution specified.
- [ ] Remedies clause (injunctive relief) included.
- [ ] All `[CONFIRM: ...]` placeholders identified in the output.
- [ ] Key terms summary produced.
- [ ] Disclaimer included on output.

## Examples

- "Draft a mutual NDA between Finanshels and a potential technology partner who wants to see our client onboarding methodology. We'll be sharing some proprietary workflow data."
- "Generate a one-way NDA for a freelance bookkeeper we're bringing in to help with a large client. Finanshels is disclosing client financial data to them."
- "A prospective client wants an NDA before they share their financial records for a scoping call. Draft one that protects their data and includes our standard AML carve-out."

## Guardrails

- **Draft only — not legal advice.** This NDA is a professional draft for internal review. It MUST be reviewed and approved by a qualified UAE-licensed legal practitioner before any party signs it. Finanshels does not provide legal services.
- **UAE jurisdiction only.** This template is designed for UAE-governed agreements. Do not use it as-is for agreements governed by foreign law without qualified legal review.
- **AML/CFT carve-out is non-negotiable.** The regulatory carve-out clause must remain in every NDA Finanshels signs. Removing it would risk conflicting with Finanshels' obligations as a DNFBP.
- **Verify enforceability of arbitration.** If the counterparty is foreign, confirm the chosen arbitration or court mechanism is practical for enforcement in that counterparty's jurisdiction.
- **No real client data in the NDA draft.** Use counterparty names only — do not include underlying client financial data or client names in NDA drafts.
- **Confidentiality of this output.** The NDA draft itself should be treated as confidential until executed.

## Reference

See ../_shared/finanshels-context.md for UAE tax facts, rates, and deadlines.
See templates/nda-template.md for the full NDA template to populate.
