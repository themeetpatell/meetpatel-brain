---
type: framework
category: decision-thinking
source: Dave Snowden
status: living
updated: 2026-05-17
tags: [framework, decision, cynefin, complexity]
---

# Cynefin Framework

> Different problems require different decision approaches. Treating a complex problem as if it's complicated, or a chaotic one as if it's complex, is how good decisions become wrong. Cynefin (pronounced *kuh-NEV-in*) is a sense-making framework that helps you match approach to problem type.

## When to use it
- Big decisions with no clear "right" answer
- Org / portfolio decisions that feel like they keep getting re-litigated
- When a previous approach (lots of data, careful analysis) keeps failing — the problem might not be the type you assumed
- Strategic planning — different parts of the strategy live in different Cynefin domains

## The 5 domains

### 1. Clear (formerly Obvious / Simple)
- Cause and effect are evident and predictable
- Best practice applies
- **Approach:** Sense → Categorize → Respond
- Example: filing a VAT return for a known entity. Process is defined; follow it.

### 2. Complicated
- Cause and effect exist but require expertise to find
- Good practice applies (not "best", because multiple correct answers exist)
- **Approach:** Sense → Analyze → Respond
- Example: optimizing the Finanshels CoE staffing model. Real expertise solves it; analysis works.

### 3. Complex
- Cause and effect can only be deduced *in retrospect*
- No right answer exists in advance; emergent practice
- **Approach:** Probe → Sense → Respond
- Example: choosing the StartupOS wedge. You can hypothesize, but the right answer reveals itself through running small tests.

### 4. Chaotic
- No clear cause and effect; the situation is breaking
- Novel practice required; act first, then sense
- **Approach:** Act → Sense → Respond
- Example: a major trust & safety incident on Biggdate. First contain the harm, then learn.

### 5. Confused / Disorder (the centre)
- You don't know which domain the problem is in
- **Approach:** decompose the problem into pieces, place each piece in a domain, treat each appropriately
- Most messy real-world strategy lives here at first

## The crucial insight

The framework's most useful contribution: **stop applying the wrong domain's approach to a problem**.

- Treating a complex problem (StartupOS wedge) as if it's complicated (gather more data, decide rationally) = paralysis, never enough data
- Treating a complicated problem (Finanshels staffing) as if it's complex (probe with experiments) = unnecessary chaos, wastes expertise
- Treating a chaotic problem (active incident) as if it's complex (let's run experiments) = catastrophe

## How to apply

### Meet's portfolio decisions through Cynefin

| Decision | Domain | Right approach |
|---|---|---|
| Should we hire a 3rd pre-sales analyst at Finanshels? | Complicated | Analyze (CoE data, response-time math) → decide |
| Which StartupOS wedge to lock? | Complex | Probe (3 customer-dev experiments) → sense → respond |
| Should Biggdate stay paid-only? | Complex | Probe (small test of free trial cohort) → sense |
| Trust & safety incident response | Chaotic | Act first (remove harm), then sense |
| Monthly VAT filing for Finanshels customer X | Clear | Run the process |
| Annual portfolio capital allocation | Complex (multiple feedback loops) | Probe small allocations, sense outcomes |
| Kill MealVerse? | Complicated (analysis-solvable) | Sense → analyze → decide |
| Should we use Twilio or Meta direct for WhatsApp? | Complicated | Sense → analyze → decide (RAPID it) |

### Finanshels CoE — domain map

Most CoE operating work is **Clear** (process-driven) or **Complicated** (expert-driven). The CoE's job is to keep it that way — moving things out of complex/chaotic into well-defined process.

When something feels chaotic at the CoE (an incident, a confusion), the right move is:
1. **Act** to contain
2. Then **sense** what happened
3. Then **respond** with process improvement to prevent recurrence

### StartupOS — most work is Complex

Pre-PMF, almost everything is complex. The Cynefin discipline: *don't try to decide your way to PMF*. Probe, sense, respond. Run small experiments. Let the right answer emerge.

This is also why "more strategy decks" doesn't help in the complex domain — you can't analyze your way to clarity. You have to probe.

## Anti-patterns
- **Forcing complex problems into complicated treatment.** Endless analysis, no decision. Common in founder-MBAs.
- **Applying chaotic treatment to complex problems.** Acting too fast on complex situations = wasted bets. The probing should be small + cheap.
- **Treating clear problems with too much rigor.** Don't run an experiment on what time the daily standup should be. Just decide.
- **Skipping Disorder.** Most real problems start in Disorder. Naming "I don't know which domain this is" is the first move.

## Cynefin + other frameworks

- **First Principles** is most useful in Complicated (where the underlying physics matter) and Complex (where you have to derive new approaches)
- **Premortem** is most useful in Complicated (you can foresee failure modes) — less useful in pure Chaotic
- **Working Backwards / PR-FAQ** lives in Complex (you're betting on a future you can't fully analyze)
- **EOS / OKRs** assume Complicated and Clear domains — when applied to Complex situations, they degrade into theater

## Related frameworks
- [[Type 1 vs Type 2 Decisions]] — orthogonal axis (reversibility); combine with Cynefin for full decision shape
- [[First Principles]] — best applied in Complicated + Complex; risky in Chaotic
- [[Inversion and Premortem]] — domain-specific usefulness varies

## Source
- Dave Snowden — *A Leader's Framework for Decision Making* (Harvard Business Review)
- Cognitive Edge — Cynefin training and tools
