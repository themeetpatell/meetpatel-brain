---
name: rfp-response-builder
description: Use when a Finanshels team member needs to structure a response to a formal RFP, tender, or request for proposal — for example from a larger SME, a corporate group, a free zone authority, or a VC fund's portfolio mandate. Triggers include: "respond to this RFP", "we got a tender for group accounting", "build a compliance matrix for this RFP", "draft our proposal response to this fund's mandate", "answer these RFP questions". Produces a requirements compliance matrix, a structured RFP response document anchored in proof points, and a submission checklist — with the pricing section planned for management.
---

# RFP Response Builder

Turns a formal RFP, tender, or portfolio mandate into a structured, compliant, proof-anchored response that a Finanshels team member can finalise and submit.

## When to use
- A formal RFP or tender document has been received and needs a structured response
- A VC fund or corporate group invites Finanshels to bid for a multi-entity accounting mandate
- A free zone authority issues a tender for accounting/tax services for its members
- An existing larger client runs a formal re-tender of their finance services
- You need a requirements compliance matrix before deciding whether to bid

## Inputs needed
**Required**
- The RFP document — its requirements, questions, and sections (paste or summarise)
- Submission deadline
- Services in scope of the RFP

**Optional**
- Evaluation criteria and weightings, if stated
- Issuer type — corporate group, SME, free zone authority, VC fund / portfolio
- Number of entities and their structure (mainland / free zone / offshore)
- Any mandatory format, page limits, or document requirements
- Known incumbent or competitive context
- Internal capacity or staffing constraints to flag

## Workflow
### Step 1 — Parse the RFP and build the requirements matrix
Extract every discrete requirement, question, and mandatory item into a numbered list. For each, capture the section reference, what is asked, and whether it is mandatory or scored. This becomes the compliance matrix — the spine of the response.

### Step 2 — Map each requirement to a Finanshels capability
For each requirement, state how Finanshels meets it, citing the relevant service (bookkeeping, VAT, CT, payroll, CFO, audit support, compliance) and approved proof points. Mark each as Fully meets / Partially meets / Gap. Use `templates/rfp-response-template.md` as the structure.

### Step 3 — Flag gaps and clarifications
List every Partial or Gap item explicitly. For each, note what is needed — a clarification question to the issuer, a partner/subcontract arrangement, or a management decision. Never paper over a gap with an invented capability.

### Step 4 — Draft the response answers
Write each answer in plain, confident English. Lead WHY → WHAT where appropriate, anchor at least one approved proof point per major section (7,000+ businesses, 150+ qualified accountants, AI-native delivery, trusted by Abwaab / Silkhause / Dubai Future District Fund / Cotu Ventures). Address the evaluation criteria directly if known.

### Step 5 — Assemble the response document
Build the full document: cover letter, executive summary, company overview, methodology / delivery approach, team & capability, the compliance matrix, and a pricing section placeholder. Match any mandatory format and page limits.

### Step 6 — Plan the pricing section for management
Do not price. Create a pricing section outline showing what management must complete — fee structure, per-entity pricing, payment terms, validity period. Note which scoping inputs (use `engagement-budget-calculator`) feed it. Mark clearly: "PRICING — to be completed by management."

### Step 7 — Build the submission checklist and quality pass
Produce a submission checklist: every mandatory document, signature, format requirement, and the deadline with a buffer. Run the quality checklist before hand-off.

## Output format
```
RFP RESPONSE PACK — [issuer / ref code]
Submission deadline: [date + time]   Services in scope: [list]
Prepared by: [team member]   Status: DRAFT — management review & pricing required

=== 1. REQUIREMENTS COMPLIANCE MATRIX ===
| # | RFP ref | Requirement | Mandatory? | Finanshels response | Status |
|---|---------|-------------|------------|---------------------|--------|
| 1 | [§]     | [...]       | [Y/N]      | [capability + proof]| [Full/Partial/Gap] |

=== 2. RFP RESPONSE DOCUMENT ===
Cover letter | Executive summary | Company overview | Delivery methodology |
Team & capability | Compliance matrix (above) | Pricing section [PLACEHOLDER]

=== 3. GAPS & CLARIFICATIONS ===
- [Item — what's needed — owner]

=== 4. PRICING SECTION — TO BE COMPLETED BY MANAGEMENT ===
Fields: fee structure, per-entity pricing, payment terms, validity period
Scoping inputs needed: [from engagement-budget-calculator]

=== 5. SUBMISSION CHECKLIST ===
- [ ] [Mandatory document / signature / format item]
- [ ] Submitted before [deadline] with buffer
```

## Quality checklist
- [ ] Every RFP requirement and question is captured in the compliance matrix
- [ ] Each requirement is mapped to a real Finanshels capability and marked Full / Partial / Gap
- [ ] All Partial and Gap items are listed in the gaps section with a named owner
- [ ] No invented capability, certification, client, case study, or number is used
- [ ] At least one approved proof point anchors each major response section
- [ ] Evaluation criteria are addressed directly where they are known
- [ ] Mandatory format, page limits, and document requirements are respected
- [ ] Pricing section is a placeholder marked for management — no figures invented
- [ ] Submission checklist lists every mandatory item plus a deadline buffer
- [ ] Tone is confident, plain English, founder/issuer-first, never alarmist
- [ ] UAE jurisdiction only — no foreign-tax references
- [ ] Output marked DRAFT for management review before submission

## Examples
**Example 1** "Respond to a VC fund's RFP for outsourced accounting and CT compliance across 12 portfolio companies — deadline in 10 days."
**Example 2** "Build a compliance matrix for a free zone authority tender offering discounted bookkeeping and VAT to its member companies."
**Example 3** "Draft our RFP response for a corporate group re-tendering bookkeeping, payroll, and audit support for 4 UAE entities."

## Guardrails
- UAE jurisdiction only — never reference IRS, US states, UK/EU tax regimes, or CPE.
- Output is professional work product — a Finanshels team member must review the full pack, and management must complete pricing, before submission.
- AI does not set or confirm pricing — the pricing section is a placeholder for management; never invent fees, rates, or discounts.
- Never invent Finanshels credentials, capabilities, client names, case studies, testimonials, or numbers beyond the approved proof points; flag genuine gaps honestly.
- Treat all RFP, issuer, and client data as confidential — never use real identifiers in examples; use reference codes.
- Verify any tax rate, threshold, or deadline referenced against current FTA guidance before relying on it.

## Reference
See `templates/rfp-response-template.md` for the response document and matrix structure.
See ../_shared/finanshels-context.md for UAE tax facts, rates, and deadlines.
See the `master-brand` skill for positioning, voice, proof points, and brand colours.
See the `engagement-budget-calculator` and `proposal-generator` skills for the pricing and proposal flow.
