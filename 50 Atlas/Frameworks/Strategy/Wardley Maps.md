---
type: framework
category: strategy
source: Simon Wardley
status: living
updated: 2026-05-17
tags: [framework, strategy, mapping, evolution]
---

# Wardley Maps

> Most strategy decks are lists. A map shows you *where* you are and *which way* things are moving. Wardley Maps are the only strategy tool that respects the landscape's evolution over time.

## When to use it
- Annual / quarterly strategy work
- When the team is arguing about *what to build* without a shared picture of *why*
- When evaluating whether to build, buy, or outsource a component
- When the question is "where will value move in this market in 2 years?"

## The framework

A Wardley Map is a diagram with two axes:
- **Y-axis (vertical):** *value chain* — user need at the top, infrastructure at the bottom
- **X-axis (horizontal):** *stage of evolution* — Genesis → Custom-built → Product (rental) → Commodity (utility)

You place every component of your business on this map and ask:
1. **What's the user's need at the top?**
2. **What components serve that need, in order?**
3. **What stage of evolution is each component at?**
4. **Which direction is each component moving?** (Components evolve right over time — they commodify.)

Then strategy = how do you position to ride the evolution, and where do you let go vs. invest?

## How to apply

### StartupOS — a sketched map

**User need (top):** "Founder makes faster, better strategic decisions while operating"

Components, ranked top to bottom:
- Decision support (current: custom-built; evolving toward: product) — **invest here**, this is the user-visible value
- Knowledge synthesis (current: product, ChatGPT/Claude wrappers; evolving toward: commodity) — **don't build, integrate**
- LLM inference (current: commodity utility; Anthropic, OpenAI) — **buy, never build**
- Vector storage (commodity utility) — **buy**
- Founder context capture (custom-built, no good product exists) — **invest, this is moat**

**Strategic implication:** Invest in decision support + founder context capture. Treat inference + storage as utilities. Don't waste time trying to "build our own model".

### Finanshels — what's commoditizing?

- AI-native bookkeeping classification → already commoditizing (rapid evolution right). Don't build proprietary models. Use commodity AI well.
- VAT filing automation → still custom-built / early product stage. Real differentiation possible here.
- Compliance checking → product stage but UAE-specific edge cases keep it from commodity.
- WhatsApp-first SMB sales motion → custom-built. Real moat if codified into a process power.

Strategic implication: focus build effort on the components that aren't yet commoditized + where UAE-specific edge creates a moat.

## Anti-patterns
- **Treating it as a one-time exercise.** Maps are alive. Re-draw quarterly.
- **Drawing maps without users in the room.** The map must start with the user need at the top, or it's just an org chart.
- **Mistaking "we built it" for "it's not commodity".** Many internally-built things are *already* available as commodity utilities. Map honestly.
- **Strategy by analogy.** Don't say "we'll be the Uber of X" — that skips the map. Draw your map. Look at what's actually evolving.

## Related frameworks
- [[7 Powers]] — Wardley Maps surface where powers can emerge along the value chain
- [[First Principles]] — both demand reasoning from the actual landscape, not from analogies
- [[Working Backwards]] — Wardley Maps + PR/FAQ together: where's the user value, and what does the world look like when we ship?

## Source
- Simon Wardley — *Wardley Maps* (Medium series, available free)
- learnwardleymapping.com
- onlinewardleymaps.com (free drawing tool)
