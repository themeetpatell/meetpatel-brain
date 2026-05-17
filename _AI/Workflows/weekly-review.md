---
type: workflow
status: living
updated: 2026-05-17
tags: [ai, workflow, weekly, ritual]
trigger: friday-evening OR saturday-morning
duration: 30-45 minutes
---

# Workflow: Weekly Review

> The single most important recurring ritual. If only one workflow ever runs, it's this one.

## When to trigger
- Default: Friday 5pm UAE OR Saturday 9am UAE
- Manual: anytime the week feels unprocessed
- Scheduled task: `friday-weekly-review` (set up via `mcp__scheduled-tasks`)

## Inputs needed
- Access to last 5–7 daily notes
- Access to `_AI/Contexts/current-state.md` (last Monday's top 3)
- Access to last week's review (for delta)

## Steps

### Step 1 — Aggregate the raw signal (5 min, agent does this)
- Read all daily notes for the week
- Read any journal entries for the week
- Read any meeting notes captured
- Read any decision logs created
- Build a working summary of: wins, losses, decisions made, decisions open, threads dropped

### Step 2 — Run the weekly review prompt (10 min, Meet + agent)
- Use `_AI/Prompts/personal/weekly-review.md`
- Fill in the inputs from Step 1
- Agent drafts, Meet edits
- Save to `10 Daily/Weekly/YYYY-Www.md`

### Step 3 — Extract any lesson worth keeping (5 min)
- If a lesson surfaced, file it as its own note at `20 Compass/Decisions/Lessons/YYYY-MM-DD-[slug].md`
- Cross-link from the weekly review

### Step 4 — Update current-state.md (10 min, Meet)
- Open `_AI/Contexts/current-state.md`
- Rewrite "This week" → "Last week" (briefly)
- Draft next Monday's top 3 priorities
- Update open loops
- Update energy read
- Save

### Step 5 — People nudge (5 min)
- Run `_AI/Prompts/personal/relationship-nudge.md`
- Pick 2–3 people to reach out to next week
- Drop drafted messages into next week's planning

### Step 6 — Content scan (5 min)
- Was there a moment from the week worth a post?
- If yes → run `_AI/Prompts/content/story-driven-post.md`
- Draft now while the moment is fresh, even if publishing later

### Step 7 — Forward-look (5 min)
- Open next week's calendar
- Identify the 1–2 most consequential moments
- Pre-prep notes (use `1on1-frame` or `discovery-call-prep` as needed)

## Output of the workflow
- `10 Daily/Weekly/YYYY-Www.md` (weekly review)
- Updated `_AI/Contexts/current-state.md`
- 0–1 new lesson note in `20 Compass/Decisions/Lessons/`
- 0–3 drafted relationship messages
- 0–1 drafted content post

## Quality bar
- Weekly review must contain at least one *uncomfortable* observation. If everything reads fine, the review wasn't honest.
- Top 3 priorities must be specific (not "work on Finanshels"). They must be the kind of thing that could be done or not done.

## Skip permission
- Acceptable to skip 1 week per quarter (travel, recovery, vacation).
- 2+ skips in a quarter triggers a review of whether this ritual still fits.

## Maintenance
- Quarterly: review whether the steps still earn their time. Tighten or expand.
- Annually: re-read all weekly reviews. Look for patterns.
