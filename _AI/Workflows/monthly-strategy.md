---
type: workflow
status: living
updated: 2026-05-17
tags: [ai, workflow, monthly, strategy]
trigger: first-saturday-of-month
duration: 2-3 hours
---

# Workflow: Monthly Strategy Session

> Step out of operating mode. Look at the portfolio, the personal OS, and the public brand from altitude. Quarterly is too rare to course-correct. Weekly is too close to see patterns.

## When to trigger
- First Saturday of the month, 9am–12pm UAE
- Scheduled task: `monthly-strategy-session`

## Inputs needed
- 4 weekly reviews from the past month
- `_AI/Contexts/current-state.md`
- Each P0 venture's `CLAUDE.md`
- `20 Compass/Vision/30 Next 90 Days.md`
- Any decision logs created this month
- Any premortems run this month

## Steps

### Step 1 — Read the month (20 min)
- Read all 4 weekly reviews in sequence
- Note: recurring themes, repeating misses, energy direction, where attention actually went vs intended
- Capture observations in scratch note

### Step 2 — Portfolio pulse (30 min)
For each P0 venture (Finanshels, StartupOS, Biggdate, ZeroHuman):
- Pull the primary metric trend
- Score on: trajectory, energy, market signal, opportunity cost
- Note: any decision that should be made this month
- If any venture is wobbling, queue it for a kill-or-double-down call at quarter-end

### Step 3 — Personal OS pulse (20 min)
- Run `_AI/Prompts/personal/energy-audit.md` lightweight version
- Review Health, Money, Brand, Relationships zones
- Note: anything trending wrong before it metastasizes

### Step 4 — Brand + content review (15 min)
- How many posts shipped this month vs target
- Which performed (engagement, comments, DMs received)
- Which fell flat — voice issue or topic issue?
- Pillars still right or drifting?

### Step 5 — Capital + commitments (15 min)
- Money OS: cash position, burn, runway across ventures
- Time OS: where deep-work hours actually went (vs intended)
- Hires planned, hires deferred

### Step 6 — Decisions to make this month (20 min)
Based on Steps 1–5, surface the 1–3 decisions that need to be made this month.
For each, run `_AI/Agents/decision-frame.md`.
File to `20 Compass/Decisions/YYYY-MM-DD-[slug].md`.

### Step 7 — Next month's themes (10 min)
- Pick 1–3 themes for the next month
- These become the lens for next month's weekly priority-setting
- Update `_AI/Contexts/current-state.md`

### Step 8 — Strategic write-up (15 min, optional)
- If something this month is worth a public essay, sketch it
- Pass to `content-engine` agent for first draft

## Output of the workflow
- Monthly strategy note at `10 Daily/Monthly/YYYY-MM.md`
- 0–3 decision frames filed
- Updated `current-state.md`
- 0–1 essay draft started
- 0–2 venture-level kill/double-down flags raised

## Quality bar
- Must surface at least one thing I'm currently doing on willpower.
- Must update the portfolio time allocation if drift is observed.
- Must close at least one open loop from the previous month, even if "closed = explicitly drop".

## Maintenance
- Quarterly: review whether monthly format still serves. Adjust step weights based on what gets used vs ignored.
