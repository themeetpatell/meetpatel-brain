---
type: framework
category: ops-execution
source: Bain & Company
status: living
updated: 2026-05-17
tags: [framework, ops, decision, rapid]
---

# RAPID — Bain's Decision Framework

> Most decisions stall because nobody knows who decides. RAPID assigns five distinct roles to every consequential decision so it actually gets made — without the decision being re-litigated weekly.

## When to use it
- Any cross-functional decision involving 3+ stakeholders
- Recurring decisions that mysteriously never close
- Setting up a new venture's decision rights
- Hiring decisions (especially senior)
- Resource allocation decisions (capital, headcount, time)

## The framework — 5 roles, 5 letters

- **R — Recommend** — proposes the decision; gathers input; presents the recommendation
- **A — Agree** — must formally agree (or escalate the disagreement). Limited to people whose work the decision affects materially (e.g., legal for a contract, finance for a spend)
- **P — Perform** — executes the decision once made
- **I — Input** — consulted; their views are heard but not binding
- **D — Decide** — single individual with final authority; commits resources, accepts consequences

**The single most important rule:** D is ONE person. Not a committee. Not "we'll all decide together". One. Person.

## How to apply

### Finanshels — example decision: "Should we move WhatsApp BSP from Twilio to Meta direct?"

- **R (Recommend):** Head of Engineering (gathers technical + commercial data, builds the case)
- **A (Agree):** Head of Operations (this changes the lead-triage flow); CFO (this changes cost structure)
- **P (Perform):** Engineering team executes migration; Ops team retrains
- **I (Input):** Sales team (impacts their tooling); customer support (impacts user-facing experience)
- **D (Decide):** Meet (as CoE Head)

Without RAPID: this decision can sit for months while everyone discusses. With RAPID: Meet sees the recommendation, the Agreers sign off (or escalate), Meet decides. Done.

### StartupOS — example: "Should we adopt model X as our default LLM?"

- **R:** Founder + advisor
- **A:** No formal Agree (small team)
- **P:** Founder + engineering
- **I:** Beta users (preference data)
- **D:** Founder

Solo-founder ventures benefit less from RAPID. But for any decision where Meet wants to be *forced to commit*, naming himself as D in writing helps avoid endless re-deliberation.

### Cross-venture portfolio decision: "Which venture gets capital reinvestment this quarter?"

- **R:** Meet (proposes the allocation based on portfolio review)
- **A:** Co-founders / leads of each venture (must agree to deprioritization if applicable)
- **P:** Each venture lead executes within their allocation
- **I:** Advisors, key investors (consulted, not binding)
- **D:** Meet (portfolio-level decisions are Meet's)

## When to use RAPID vs just deciding

**Don't use RAPID for:**
- Two-way-door decisions (just decide — see [[Type 1 vs Type 2 Decisions]])
- Solo-founder personal decisions
- Decisions inside a single person's role (the role's owner decides)
- Decisions made every day operationally (process owns these, not RAPID)

**Use RAPID for:**
- One-way-door decisions
- Cross-functional decisions involving 3+ stakeholders
- Decisions that have stalled
- Recurring decisions that need a clear owner
- Strategic decisions where the team wants to know who actually has the call

## Anti-patterns
- **Multiple Deciders.** Two D's = no D. The whole framework breaks.
- **No clear A.** Without formal Agreers, the decision can be undone by a disgruntled stakeholder after the fact. Name Agreers explicitly.
- **Conflating I with A.** People with Input cannot block the decision. People with Agree can. Mixing these = political mess.
- **Re-RAPIDing every decision.** Build standing RAPID maps for recurring decision types ("hiring decisions: D = function head; new venture commits: D = Meet").
- **Ignoring RAPID after assigning it.** The framework only works if respected. If Meet (as D) overrides without consulting Agreers, the team learns RAPID is theater.

## Quick RAPID map for Meet's portfolio

| Decision type | D | A | R |
|---|---|---|---|
| Hire (junior, single function) | Function head | Meet | Function head |
| Hire (senior, cross-functional) | Meet | Function heads affected | Function head + Meet |
| New venture commit | Meet | Cofounders if applicable | Meet |
| Kill venture | Meet | Cofounders if applicable | Meet |
| Strategic pivot inside venture | Venture lead | Meet | Venture lead |
| Capital allocation (portfolio) | Meet | None (sole owner) | Meet |
| Major pricing change (Finanshels) | Meet (CoE Head) | Finanshels CEO/CFO | Pricing analyst + Sales |
| Brand voice change | Meet | None | Brand owner |

## Related frameworks
- [[Type 1 vs Type 2 Decisions]] — use RAPID for Type 1; just decide for Type 2
- [[Decision Frame]] — the agent prompt that operationalizes structured decisions
- [[EOS]] — EOS's IDS process can use RAPID for the "Solve" step

## Source
- Paul Rogers & Marcia Blenko (Bain) — *Who Has the D?* (Harvard Business Review)
- Bain & Co. — *Decide & Deliver*
