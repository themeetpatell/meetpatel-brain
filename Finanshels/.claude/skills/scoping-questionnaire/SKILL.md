---
name: scoping-questionnaire
description: Use when a Finanshels sales or onboarding team member needs a tailored pre-sales discovery questionnaire to collect the exact inputs required to scope an engagement. Triggers include: "build a discovery questionnaire for this prospect", "what should I ask before scoping a VAT engagement", "create an intake form for a CT return prospect", "the prospect wants bookkeeping plus payroll — what do we need to know", "generate a scoping checklist for a free zone company". Produces a clean prospect-facing questionnaire plus an internal note mapping each answer to scoping inputs for engagement-budget-calculator and proposal-generator.
---

# Scoping Questionnaire

Generates a tailored pre-sales discovery questionnaire that collects exactly the inputs needed to scope an engagement — nothing more, nothing less.

## When to use
- A qualified prospect needs to be scoped before a proposal can be written
- A discovery call is booked and you want a structured intake before or during it
- The prospect is interested in a specific service mix and you need the right questions
- Feeding clean inputs into `engagement-budget-calculator` and `proposal-generator`
- Standardising intake so quotes are consistent and assumptions are documented

## Inputs needed
**Required**
- Services the prospect is interested in (bookkeeping, VAT, CT, payroll, CFO, audit support, formation)
- Entity type — mainland (DED) / free zone (which one) / offshore / not yet incorporated
- What is already known about the prospect (so questions already answered are dropped)

**Optional**
- Prospect's revenue band, if known
- Lead source and qualification notes (from `prospect-qualification`)
- Known deadline pressure (e.g. CT return due, VAT registration overdue)
- Whether the prospect has an existing accountant or system
- Preferred delivery format — form, email, or call-guide

## Workflow
### Step 1 — Select the relevant question modules
From `references/question-modules.md`, pick only the modules that match the services in scope. Always include Entity & Licensing and Revenue & Volume. Add VAT, CT, Payroll, Audit, Back-period/Catch-up, and Deadlines modules only when relevant. Do not send a module that does not apply.

### Step 2 — Drop already-known answers
Remove any question already answered by the inputs or by `prospect-qualification`. The prospect should never be asked something Finanshels already knows — it signals poor process.

### Step 3 — Phrase questions founder-friendly
Rewrite each module question in plain English a non-accountant founder can answer. Translate jargon (e.g. "taxable supplies" → "sales that VAT applies to"). Keep each question to one idea. Use multiple-choice or ranges where it lowers effort.

### Step 4 — Order for momentum
Sequence from easy and factual (entity, licence, financial year) to more involved (transaction volume, current bookkeeping state). Group by theme with short section headers. Add a one-line purpose statement at the top so the prospect knows why it matters.

### Step 5 — Mark scoping drivers
Internally tag which answers drive scope and pricing — transaction volume, number of bank accounts, VAT/CT status, back-period months, entity count, payroll headcount. These map directly to `engagement-budget-calculator` inputs.

### Step 6 — Build the internal mapping note
Produce an internal note pairing each scoping-driver answer with the input it feeds and the scoping logic (e.g. "monthly transaction volume → bookkeeping tier", "back-period months → catch-up scope"). Flag any answer that would need a follow-up call.

### Step 7 — Quality pass
Run the checklist. Confirm the prospect-facing version contains no internal tags, no pricing, and no jargon, and that it is short enough to actually be completed.

## Output format
```
=== PROSPECT-FACING DISCOVERY QUESTIONNAIRE ===
For: [prospect name / ref code]   Services in scope: [list]
Purpose: [one line — why we're asking]

SECTION 1 — About your company
[Q1...]
SECTION 2 — Your finances today
[Q...]
SECTION [n] — [VAT / CT / Payroll / Audit / Catch-up / Deadlines as applicable]
[Q...]
Anything else we should know? [open field]

=== INTERNAL SCOPING NOTE (not for prospect) ===
| Question / answer | Feeds | Scoping logic | Follow-up? |
|-------------------|-------|---------------|------------|
| [driver answer]   | [engagement-budget-calculator input] | [logic] | [Y/N] |
Open assumptions to confirm on the call: [...]
Recommended next step: [scope with engagement-budget-calculator → proposal-generator]
```

## Quality checklist
- [ ] Only modules relevant to the services in scope are included
- [ ] Entity & Licensing and Revenue & Volume modules always present
- [ ] Questions already answered upstream are removed
- [ ] Every question is plain English; jargon is translated
- [ ] Questions ordered easy-to-involved with clear section headers
- [ ] Scoping-driver answers are tagged in the internal note only
- [ ] Internal note maps each driver to an `engagement-budget-calculator` input
- [ ] Prospect-facing version contains no internal tags and no pricing
- [ ] Questionnaire is short enough to realistically be completed
- [ ] UAE terms used correctly (DED, free zone, EmaraTax, FTA)
- [ ] No tax rate, threshold, or deadline stated without a verify-with-FTA note
- [ ] Output marked as draft for team review before sending

## Examples
**Example 1** "Build a discovery questionnaire for a free zone trading company that wants bookkeeping and VAT filing."
**Example 2** "Create an intake form for a mainland startup that needs CT registration and its first CT return — they have 14 months of unrecorded transactions."
**Example 3** "Generate a scoping questionnaire for an SME wanting outsourced CFO support plus payroll for 30 staff."

## Guardrails
- UAE jurisdiction only — never reference IRS, US states, UK/EU tax regimes, or CPE.
- Output is professional work product — a Finanshels team member must review the questionnaire before it is sent to a prospect.
- AI does not set or confirm pricing — the questionnaire collects scoping inputs only; pricing is produced later by `engagement-budget-calculator` and confirmed by management.
- Never invent Finanshels credentials, client names, case studies, or numbers beyond the approved proof points.
- Treat all prospect data as confidential — never use real identifiers in examples; use reference codes.
- Verify any tax rate, threshold, or deadline referenced against current FTA guidance before relying on it.

## Reference
See `references/question-modules.md` for the full modular question bank by service line.
See ../_shared/finanshels-context.md for UAE tax facts, rates, and deadlines.
See the `master-brand` skill for voice and tone.
See the `prospect-qualification`, `engagement-budget-calculator`, and `proposal-generator` skills for the surrounding pre-sales flow.
