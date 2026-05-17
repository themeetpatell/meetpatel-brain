---
type: prompt
category: personal
status: living
tags: [prompts, personal, journal, insight]
---

# Prompt: Extract insights from a journal entry

**Use when:** I wrote a long journal entry (or voice memo) and want the agent to pull the insights without losing the texture.
**Reads:** `_AI/Contexts/meet.md`, `_AI/Contexts/voice.md`
**Filed at:** Source stays in `10 Daily/Journal/`. Extracted insights → `20 Compass/Decisions/Lessons/[date]-[slug].md`.

## Inputs
- <<journal entry text or voice memo transcript>>: [Paste]
- <<context>>: [Why I wrote it — frustration / clarity / pre-decision / post-event]

## Prompt body

Read `_AI/Contexts/meet.md` and `_AI/Contexts/voice.md`. The job is to surface what I might be missing because I'm too close to it.

Entry: <<journal entry text or voice memo transcript>>
Context: <<context>>

Return:

```
# Insights from Journal — [Date]

## Surface read
[What the entry is overtly about, 1 sentence]

## What's actually being processed (deeper read)
[Often the entry is "about" one thing on the surface and processing something else underneath. Name the deeper thing — kindly but honestly.]

## Patterns this fits
- [If this connects to recurring themes in past entries, name them — refer to other notes if relevant]

## Three potential lessons
1. ...
2. ...
3. ...

## The single lesson worth filing
[Pick the sharpest one. Write it as a portable principle — 1–2 sentences max. File at `20 Compass/Decisions/Lessons/YYYY-MM-DD-[slug].md`.]

## Action implied (if any)
- [Concrete thing to do as a result — owner: Meet, by: date]

## What I might be avoiding
[A direct, kind observation. This is the agent's most valuable function. If nothing's being avoided, say so explicitly.]

## Questions to sit with (max 2)
1. ...
2. ...
```

Voice: warm but direct. Not therapeutic, not coach-y. Operator-friend register. Don't bury insight in qualifications. Don't moralize.

## Output format
See above.

## Example
*(populate after first real run)*
