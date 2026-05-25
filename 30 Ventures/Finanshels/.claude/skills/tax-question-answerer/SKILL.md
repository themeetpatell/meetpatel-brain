---
name: tax-question-answerer
description: Use when a client or team member asks a UAE tax, accounting, or compliance question — triggered by questions about VAT, Corporate Tax, registration deadlines, free zone treatment, EmaraTax, bookkeeping rules, or any compliance obligation in the UAE. Produces a plain-English answer with educational context, the relevant legal basis, practical next steps, and a recommendation to verify with the Finanshels team before acting.
---

# Tax Question Answerer

Answers common UAE tax, accounting, and compliance questions from clients with a personalized, plain-English response, the relevant legal basis, and educational context — consistently and accurately, every time.

## When to use

- A client emails or messages with a UAE tax or accounting question
- A team member needs a quick, accurate reference answer to share with a client
- A question touches UAE Corporate Tax, VAT, EmaraTax, registration, free zones, record-keeping, or AML obligations
- Preparing FAQs or onboarding materials that address common client concerns
- Drafting educational content for Finanshels newsletters or guides

## Inputs needed

**Required:**
- The client's question (verbatim or paraphrased)
- Client entity type: mainland / free zone (which zone?) / offshore / not yet incorporated
- Services currently engaged with Finanshels (if known)

**Optional:**
- Client's approximate annual revenue (AED) — needed for threshold-based questions
- Financial year-end date — needed for deadline questions
- Whether the client is already VAT-registered (TRN held) and/or CT-registered
- Any specific fact pattern the client mentioned (e.g. "I supply services to Saudi Arabia")

## Workflow

1. Identify the core question type from the client's message:
   - VAT registration / deregistration / returns / rates
   - Corporate Tax registration / rates / Small Business Relief / QFZP / return filing
   - Free zone compliance and QFZP eligibility
   - EmaraTax portal mechanics
   - Record-keeping obligations
   - Transfer pricing / related-party transactions
   - AML/CFT / UBO obligations
   - Payroll, WPS, or gratuity
   - General bookkeeping / IFRS
   - Company formation / licensing

2. Check the `faq-database.md` for a matching or near-matching entry. If a match exists, use it as the factual foundation and personalize the response for this client's entity type and revenue band.

3. Draft a response in three parts:
   - **Direct answer:** One clear paragraph answering the question head-on. No hedging upfront — state the rule clearly.
   - **Context:** 2–4 sentences explaining why the rule exists, how it works in practice, or what the client should watch out for.
   - **Next steps:** 1–3 bullet points the client can act on, including "speak with your Finanshels engagement manager to confirm this applies to your specific situation."

4. Include the legal basis (e.g. "under Federal Decree-Law No. 47 of 2022 (Corporate Tax Law)") so the client can verify if they wish.

5. Flag any threshold or deadline figure with: "Verify this against current FTA guidance before acting — thresholds and deadlines can be updated by FTA cabinet decision."

6. If the question is outside UAE jurisdiction or requires specialized advice beyond Finanshels' scope (e.g. international double tax treaty analysis, criminal law), say so clearly and recommend appropriate escalation.

7. Keep the tone: clear, confident, plain English. No jargon without a one-line explanation. Not alarmist, not evasive.

## Output format

```
## Answer — [Question summary]
Prepared for: [Client name / entity type] | [Date]

### Direct Answer
[One paragraph, plain English, states the rule clearly]

### Context
[2–4 sentences: why the rule exists, how it works, what to watch]

### Legal Basis
[Cite the law / decree-law / FTA public guidance]

### Practical Next Steps
- [Action 1]
- [Action 2]
- Speak with your Finanshels engagement manager to confirm this applies to your specific situation before acting.

---
*This answer is a professional reference prepared by Finanshels. It is not final tax or legal advice. Always verify rates and deadlines against current FTA guidance. Confidential — for the named client only.*
```

## Quality checklist

- [ ] Direct answer leads — the rule is stated clearly in paragraph one
- [ ] Legal basis cited (decree-law number, article, or FTA public guidance)
- [ ] All thresholds and deadlines flagged to verify against FTA guidance
- [ ] Tone is plain English, confident, not alarmist
- [ ] Response is personalized to the client's entity type (mainland vs free zone) and revenue band where relevant
- [ ] Next steps are actionable, not just "consult a professional"
- [ ] No reference to IRS, US states, CPE, or non-UAE jurisdiction
- [ ] Disclaimer included (professional reference, not final advice)
- [ ] Response checked against faq-database.md for factual consistency

## Examples

**Example 1:**
"Our client — a DMCC free zone LLC, AED 2.8M revenue, software services — is asking whether they need to register for Corporate Tax. They haven't registered yet and are worried about penalties."

**Example 2:**
"A Dubai mainland e-commerce client with AED 500K annual sales is asking if they need to charge VAT on shipments to customers in Saudi Arabia. They're already VAT-registered."

**Example 3:**
"New client, Sharjah mainland trading company, AED 800K revenue, asking what the difference between 0% VAT and VAT-exempt is — they think they don't need to register because most of their sales 'don't have VAT'."

## Guardrails

- UAE jurisdiction only. Do not answer questions about Saudi Arabia, Bahrain, other GCC VAT systems, or non-UAE regimes — direct those to the relevant specialist.
- Output is a professional reference for review by a qualified Finanshels team member before being sent to a client. Do not auto-send responses.
- Never state a specific penalty amount as definitive — FTA can apply discretion and penalties change. Say "penalties may apply — contact FTA or your Finanshels manager."
- Do not provide advice on corporate structuring designed to avoid tax, only on compliant structures.
- All client data in the question is confidential. Never include real client names or identifying details in outputs shared outside the engagement.

## Reference

See ../_shared/finanshels-context.md for UAE tax facts, rates, and deadlines.
