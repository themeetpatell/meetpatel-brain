---
type: workflow
status: living
updated: 2026-05-17
tags: [ai, workflow, investor, update]
trigger: monthly OR quarterly per venture
duration: 1-2 hours
---

# Workflow: Investor Update

> Investor updates are a forcing function for honesty. Run them on cadence even when there's no exciting news. Especially when there's no exciting news.

## When to trigger
- Monthly: for existing investors in P0 ventures
- Quarterly: for prospective investors being warmed
- Ad-hoc: when a major event happens (round closed, major hire, key customer signed, key risk materialized)
- Scheduled task: `investor-update-[venture]-monthly`

## Inputs needed
- Last month/quarter's update (for delta)
- Current month's actual metrics (no estimates — pull from source of truth)
- Recent decisions made
- Recent wins shipped
- Recent losses / risks materialized
- Current ask (intro / hire / advice / feedback)

## Steps

### Step 1 — Pull the numbers (15 min, agent + Meet)
- Primary metric (revenue / users / engagement — venture-specific)
- Secondary metrics (whichever feed the primary)
- Burn + runway
- Pipeline status
- Compare to last update — what moved, what didn't, what surprised
- **No estimating.** If the data isn't ready, write "data ready by [date]" instead of guessing.

### Step 2 — Honest narrative (20 min, Meet)
- What we shipped this period (3–5 bullets, concrete)
- What we learned (1–3 bullets — honest, even if uncomfortable)
- What we missed (yes, explicitly — investors trust founders who name misses)
- What's next 30/90 days (concrete commitments)

### Step 3 — The ask (10 min)
Investor updates without asks waste the channel. Every update has one of:
- A specific intro (named person / company / role)
- A specific hire (named role + JD link)
- A specific advice ask (single sharp question)
- "No ask this month" — said explicitly, never as filler

### Step 4 — Run through investor-translator (10 min)
- Pass Steps 1–3 to `_AI/Agents/investor-translator.md`
- Get the polished version back in monthly-update format

### Step 5 — Re-read with cold eyes (5 min)
- Is the number up top?
- Is the bad news called out (not buried)?
- Is the ask specific?
- Is the tone investor-grade (not investor-pander)?
- Would I want to receive this if I were them?

### Step 6 — Ship (5 min)
- Send via the channel investors prefer (email, dedicated update tool, group thread)
- Log the send in `30 Ventures/[Venture]/Investors/Updates/YYYY-MM.md`

### Step 7 — Capture responses (rolling, after send)
- Track who replied with what
- Note any investor who consistently engages — they're a real ally
- Note any investor who never engages — quietly downgrade their priority

## Output of the workflow
- Sent investor update
- Logged at `30 Ventures/[Venture]/Investors/Updates/YYYY-MM.md`
- Response tracker updated

## Quality bar
- Number first. Always.
- At least one honestly named miss or risk.
- Specific ask or explicit "no ask".
- Length: ~300–500 words. Investors don't read longer. (Decks are separate.)
- Forbidden words: "exciting", "thrilled", "incredible", "game-changer".

## Maintenance
- Quarterly: review which investors engage. Tune the recipient list.
- Annually: review which updates predicted reality. Sharpen forecasting language.
