---
type: framework
category: product-growth
source: Sean Ellis (ICE) / Intercom (RICE)
status: living
updated: 2026-05-17
tags: [framework, growth, prioritization]
---

# ICE and RICE — Prioritization Scoring

> A backlog without a scoring rule becomes "whatever the loudest person wanted yesterday". ICE and RICE force the question: of all the things we could do, which has the best expected value relative to the cost?

## When to use it
- Prioritizing growth experiments
- Choosing the next feature to build
- Ranking marketing initiatives
- Deciding which venture initiative wins the week (combined with [[_AI/Prompts/strategy/portfolio-prioritization]])

## The frameworks

### ICE (simpler, faster)

Score each idea on three dimensions, 1–10:
- **Impact** — if it works, how big is the win?
- **Confidence** — how confident are we it'll work? (use data, not vibes)
- **Ease** — how easy / cheap to ship?

ICE Score = (Impact × Confidence × Ease) / 3 — gives a roughly 0–10 number.

### RICE (more rigorous, especially for product backlogs)

Score each idea on:
- **Reach** — how many users / events in a defined time period (e.g., per quarter)
- **Impact** — per-event magnitude (3 = massive, 2 = high, 1 = medium, 0.5 = low, 0.25 = minimal)
- **Confidence** — % (100% = high, 80% = medium, 50% = low)
- **Effort** — person-months (or weeks) of work

RICE Score = (Reach × Impact × Confidence) / Effort

The output is a comparable number across initiatives. Sort. Pick from the top.

## How to apply

### Finanshels — example RICE scoring (quarter backlog)

| Initiative | Reach | Impact | Confidence | Effort | RICE |
|---|---|---|---|---|---|
| AI lead-qualification bot | 500 leads/qtr | 3 | 70% | 4w | 263 |
| WhatsApp template overhaul | 1500 customers | 1 | 80% | 1w | 1200 |
| Channel partner portal | 50 partners | 3 | 50% | 8w | 9.4 |
| Pricing experiment (SMB tier) | 800 prospects | 2 | 60% | 1w | 960 |
| AI demand engine v1 | 2000 leads/qtr | 2 | 50% | 12w | 167 |

Highest RICE = WhatsApp template overhaul + Pricing experiment. Lowest = Channel partner portal (high effort, narrow reach). Re-scope the portal or push to next quarter.

### Biggdate — example ICE scoring (pre-launch experiments)

| Experiment | Impact | Confidence | Ease | ICE |
|---|---|---|---|---|
| Founder-led "why I'm building Biggdate" essay | 8 | 9 | 9 | 7.2 |
| Waitlist landing page A/B test | 7 | 8 | 8 | 4.7 |
| Diaspora WhatsApp community partnerships | 9 | 6 | 4 | 7.2 |
| Press push to Khaleej Times | 7 | 4 | 5 | 4.7 |

## Anti-patterns
- **Scoring without honest confidence numbers.** Most ideas get inflated confidence because the proposer believes in them. Use data, not aspiration.
- **Confusing "feels easy" with "actually easy".** Effort estimates should come from the person who'd build it.
- **Re-scoring weekly.** Score, commit, ship, then re-score. Constant re-scoring is procrastination.
- **Picking only the highest-score items.** Sometimes a 2nd-tier RICE item *unlocks* a 1st-tier item. Read the list, don't just sort it.
- **Ignoring strategic context.** A high-RICE feature that violates your strategic positioning is still wrong. Use scoring as input, not output.

## When ICE vs RICE
- **ICE** for growth experiments, marketing tests, content ideas. Faster, looser.
- **RICE** for product backlog, larger features, multi-quarter initiatives. Slower, more rigorous.

## Related frameworks
- [[Bullseye Framework]] — Bullseye is essentially ICE applied to channel selection
- [[OKRs]] — high-RICE items often become Key Result drivers
- [[Type 1 vs Type 2 Decisions]] — RICE for Type 2 decisions, deeper analysis for Type 1

## Source
- Sean Ellis — ICE in early growth-hacker community
- Intercom Product team — *RICE: Simple prioritization for product managers* (2016 essay)
