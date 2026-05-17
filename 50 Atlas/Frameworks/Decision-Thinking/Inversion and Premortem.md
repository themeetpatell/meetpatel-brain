---
type: framework
category: decision-thinking
source: Carl Jacobi / Charlie Munger / Gary Klein
status: living
updated: 2026-05-17
tags: [framework, decision, premortem, inversion]
---

# Inversion + Premortem

> "Tell me where I'm going to die so I can avoid going there." Charlie Munger's whole career is one applied inversion. The premortem is its operational sibling — imagine the failure first, then work backwards to prevent it.

## When to use it
- Before any consequential decision (new venture, major hire, fundraise, pivot)
- When everyone in the room agrees too quickly (sign of groupthink — invert)
- Annual planning — "what would make next year a disaster?"
- Personal life decisions — "what do I want to avoid more than what I want to gain?"

## Inversion — the thinking move

Most strategy asks: *"How do we succeed?"* The inverted question: *"How do we fail?"*

Inversion is more powerful because:
- Failure modes are easier to enumerate than success paths
- Avoiding catastrophic failure is more reliably valuable than maximizing upside
- Most success comes from avoiding stupidity, not from being brilliant
- The unstated failure modes are usually where the actual risk sits

### Inversion applied to Meet's portfolio

- **"How do I make the portfolio worth 10x in 5 years?"** → speculative, many paths
- **"How does the portfolio die in 5 years?"** → 5–10 concrete failure modes, all addressable now

Inversion narrows the question. The answers are actionable.

## Premortem — the operational version

The premortem is a structured group exercise:

1. **Setup:** "Imagine it is [date 12 months out]. The [decision/project/venture] failed. Failed badly. Why?"
2. **Individual writing (5 min):** Each participant writes their best guesses for failure causes
3. **Round-robin sharing:** Each person reads one cause; rotate until exhausted
4. **Clustering:** Group similar causes
5. **Severity × likelihood scoring:** Rank by combined risk
6. **Mitigations:** For top failure modes, identify pre-commit changes + in-flight monitoring

The structure forces honesty that "what could go wrong" discussions don't. Asking people to *predict* failure unlocks information they'd normally suppress (out of optimism, loyalty, or politeness).

## How to apply

### Finanshels — premortem on the AI demand engine

*"It is May 2027. The AI demand engine project failed. Why?"*

Failure modes might include:
- AI bot quality dropped — too many leads incorrectly qualified → sales team distrust → manual override → AI engine abandoned within 6 months
- Build took 9 months instead of 3 → opportunity cost too high
- Customers reacted negatively to "talking to a bot" first — brand damage in trust-heavy regulated category
- Engineering bandwidth pulled into AI engine → other Finanshels priorities slipped → CFO killed the project
- The team Meet hired to own the AI engine couldn't operate Finanshels-grade quality standards

**Mitigations to apply now (pre-commit):**
- Define quality gates (sales-accept rate floor) before launch — kill switch ready
- Phase delivery: 4-week MVP first, then 8-week scale, with go/no-go gates
- Brand voice testing on AI conversations before going live to general inbound
- Ring-fence engineering bandwidth; protect non-AI priorities
- Hire ownership with specific Finanshels-trust-context background, not generic AI engineering

### Biggdate — inversion before launch

*"How could Biggdate fail in year 1?"*

- Trust & safety incident with public visibility → brand cannot recover in dating category
- Cannot reach critical mass in a single city/segment → no liquidity → users churn after 2 months
- Paid-only model gets undercut by Hinge dropping their premium price → can't compete on price; need to compete on category
- Founder-led brand consumes Meet's bandwidth → other ventures (Finanshels) suffer
- Confusion between Biggdate and Soulmap blurs both brands

Each failure mode → a current decision sharpens.

### Personal — inversion on Meet's 90-day plan

*"In 90 days, what would make this period a failure?"*

- Vault godmode upgrade stalls because Phase 2 is too big to ship
- Public posting cadence never starts because Meet keeps waiting for "perfect" first post
- Health/Money OS stays empty for the whole quarter
- Finanshels Q3 plan slips because attention went to vault
- A relationship breaks because cadence wasn't honored

**Mitigations (now):**
- Set 4DX-style WIG with weekly lead measures
- Force a "first post" by Wednesday this week — break the perfection trap
- Seed Health + Money OS this week with stubs, not exhaustive plans
- Schedule Finanshels Q3 planning before vault work continues
- Run relationship-nudge prompt every Monday

## Anti-patterns
- **Premortem as exercise theater.** If the findings don't change the plan, the exercise was decoration.
- **Mortem-mode (after the fact only).** Premortem must be done *before* commitment. Postmortems are valuable too, but different tool.
- **Premortem in groups where dissent is unsafe.** People won't surface real failure modes if culture punishes them. May need anonymous written input.
- **Optimism bias dressed up.** "Worst case: we only hit 80% of target" is not a premortem. Worst case = catastrophic failure.
- **Listing 50 failure modes and acting on none.** Severity × likelihood scoring matters. Top 3, mitigate. Rest, watch.

## Where to use this in the vault
- `_AI/Agents/premortem.md` — the agent prompt
- `_AI/Workflows/new-venture-brief.md` — premortem is Step 4 of the workflow
- `20 Compass/Decisions/` — file completed premortems here

## Related frameworks
- [[First Principles]] — both demand reasoning from base facts; inversion is the negative-space version
- [[Type 1 vs Type 2 Decisions]] — premortems are mandatory for Type 1; lighter for Type 2
- [[Decision Frame]] — premortem outputs feed the decision frame's "what would change my mind" section

## Source
- Charlie Munger — annual letter speeches; the *Poor Charlie's Almanack* anthology
- Gary Klein — *Performing a Project Premortem* (Harvard Business Review)
- Carl Jacobi — *invert, always invert* (original mathematical formulation)
