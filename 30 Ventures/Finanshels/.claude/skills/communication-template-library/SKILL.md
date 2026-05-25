---
name: communication-template-library
description: Use when drafting or selecting a client-facing communication from Finanshels — triggered by requests like "draft an email to the client", "send a status update", "follow up on documents", "deliverable ready to send", "chase the client", "write a message to [client]", or any outbound client communication need. Produces a ready-to-send, brand-consistent email or message by selecting the right template, filling in the client-specific details, and adjusting the tone to the situation.
---

# Communication Template Library

Provides brand-consistent, ready-to-send client communication templates for every common Finanshels scenario — status updates, deliverable handovers, document follow-ups, deadline reminders, and more — so every touchpoint sounds like one firm.

## When to use

- Sending a client their completed VAT return, management accounts, or CT filing confirmation
- Following up on outstanding documents or approvals needed from a client
- Sending a proactive deadline reminder before a VAT or CT due date
- Updating a client on the status of work in progress
- Responding to a client who has asked for a status update
- Sending a welcome / kickoff follow-up after onboarding
- Any outbound email or WhatsApp message to a client that should sound professional and on-brand

## Inputs needed

**Required:**
- Template type (or describe the situation and let the skill select)
- Client name and the name of their primary contact at Finanshels
- The specific deliverable or topic (e.g. "Q2 VAT return", "April management accounts", "outstanding bank statements")
- Any key dates, amounts, or specific details to include

**Optional:**
- Tone adjustment: Standard (default) / Urgent / Warm (long-term relationship) / Formal (new or sensitive context)
- Deadline date (for reminder emails)
- Action required from the client (e.g. approve, send documents, pay invoice)
- Attachment list (to mention in the email body)

## Workflow

1. Identify the template type from the situation:

   | Situation | Template |
   |---|---|
   | Work complete, sending deliverable | `templates/deliverable-email.md` |
   | Proactive status update (in progress) | `templates/status-update.md` |
   | Chasing client for documents, approval, or response | `templates/follow-up.md` |
   | Deadline reminder (VAT, CT, payroll) | `templates/follow-up.md` — Section B |
   | Welcome / post-kickoff | Adapt `templates/status-update.md` — Section C |

2. Pull the relevant template section and fill in all `[PLACEHOLDER]` fields with the client-specific details provided.

3. Apply tone adjustment if specified:
   - **Urgent:** Shorten the opening pleasantry, move the action/deadline to the first sentence, bold the key date or action.
   - **Warm:** Add a brief personal note ("Hope the business is going well!"), soften imperatives ("When you get a chance, could you…").
   - **Formal:** Remove any informal openers, use full names, passive constructions where appropriate.

4. Review the draft against the quality checklist below.

5. Output the ready-to-send email with subject line, body, and closing — no further editing needed beyond confirming the client's email address.

## Output format

```
## Communication Draft — [Template Type] — [Client Name]

**Template used:** [Template name / section]
**Tone:** [Standard / Urgent / Warm / Formal]
**Prepared by:** [Team member] | **Date:** [Date]

---

**To:** [Client contact name] <[email if provided]>
**Subject:** [Subject line]

---

[Email body — ready to send]

---

**Checklist before sending:**
- [ ] Client name and contact are correct
- [ ] Deliverable name / period is correct
- [ ] Dates and deadlines are accurate — verify against FTA guidance
- [ ] Attachments listed in the email are actually attached
- [ ] Reviewed by engagement manager (for sensitive or first-time communications)
```

## Quality checklist

- [ ] All `[PLACEHOLDER]` fields are filled in — none left blank
- [ ] Subject line is specific (not generic like "Update from Finanshels")
- [ ] The primary action or information is in the first 2 sentences
- [ ] Tone is consistent throughout (not warm opening → abrupt closing)
- [ ] Deadlines and figures are accurate — verify VAT due dates (28th rule) and CT due dates (9-month rule)
- [ ] No jargon without a brief explanation (clients vary in accounting knowledge)
- [ ] Sign-off includes the sender's name, role, and Finanshels contact details
- [ ] No confidential financial data is included that the recipient doesn't need
- [ ] UAE jurisdiction only — no reference to non-UAE tax regimes
- [ ] Reviewed by engagement manager before sending sensitive communications

## Examples

**Example 1:**
"Draft an email to send to our Dubai mainland client, a retail trading LLC, to let them know their Q2 VAT return has been filed. Their engagement manager is Sara Al Mansoori. VAT period was April–June, filed today, AED 18,400 payable."

**Example 2:**
"We need to chase a DMCC free zone SaaS client for their April bank statements — we've already asked once five days ago. Monthly books are due in 3 days. Draft a follow-up that's professional but makes clear we need it today."

**Example 3:**
"A client who joined 2 months ago is asking for a status update on their first management accounts (for March). They're 80% done — we're waiting on one supplier invoice to be confirmed. Draft a brief status email."

## Guardrails

- Templates are a starting point — always fill in all placeholders and verify facts before sending.
- Never include unverified tax figures, penalty amounts, or regulatory statements in client emails. If unsure, say "our team will confirm the exact amount" rather than guessing.
- All outbound communications represent Finanshels. Maintain the brand voice: clear, confident, plain English, never alarmist.
- Communications about overdue payments or regulatory risk must be reviewed by the engagement manager before sending.
- Client financial details in these communications are confidential — use BCC or direct addressing, never CC other clients.

## Reference

See ../_shared/finanshels-context.md for UAE tax facts, rates, and deadlines.

See the `master-brand` skill for Finanshels voice and tone — all client communications must be clear, confident, founder-first ("you/your"), and never alarmist, per the channel tone rules in `master-brand`.
