---
type: prompt
category: personal
status: living
tags: [prompts, personal, relationships, crm]
---

# Prompt: Who haven't I contacted that I should

**Use when:** Monday morning, or anytime I want a nudge to do the relationship work. Most relationship work fails because it's invisible.
**Reads:** `_AI/Contexts/meet.md`, `40 Areas/Relationships/People/`, last 30 days of daily notes for any mentions
**Filed at:** Output goes to today's daily note as a section + creates touchpoint logs in person files

## Inputs
- <<this week's energy>>: [How much relationship bandwidth I have — light / medium / heavy]
- <<focus>> (optional): [Founders / investors / family / old friends / mentors / team / customers]
- <<exclude>> (optional): [Anyone I just talked to that wouldn't show "overdue"]

## Prompt body

Read `_AI/Contexts/meet.md`. Scan `40 Areas/Relationships/People/` for all person notes. Apply cadence rules.

Energy: <<this week's energy>>
Focus: <<focus>>
Exclude: <<exclude>>

Logic:
- Default cadence per person = `cadence_days` field in their note (or 14 if not set)
- Overdue = `today - last_contact > cadence_days`
- Score = overdue-ness × person's importance tier (A/B/C)
- Surface top 5 (light), top 10 (medium), top 20 (heavy)

Return:

```
# Relationship Nudge — [Date]

## People overdue, ranked
| Person | Tier | Last contact | Days overdue | Suggested ping |
|---|---|---|---|---|
| ... | A | YYYY-MM-DD | 12 | [specific opener] |

## Suggested pings — drafted, ready to send
### [Person 1]
Channel: [WhatsApp / email / voice note / DM]
Opener:
> [Draft message in my voice — natural, specific, references something only I would know about them, no "hope you're well" filler]

### [Person 2]
...

## People with milestones this week (birthdays, anniversaries, big events)
- [Name] — [Event] — [Optional: drafted message]

## People I should consider closer (from `20 Compass/Identity/27 People I Want Closer.md`)
- [Name] — last contact: [...] — proposed move: [...]

## People to maybe step back from
- [Name] — pattern: I'm initiating 90%+ — worth a quiet pause?

## After sending — capture
- Update `last_contact` field on each person note I actually messaged
- Log the touchpoint in the person's file
```

Don't draft generic openers. If I can't think of something specific to say, the right move is to NOT message — relationships die from "hey, how's it going" pings.

## Output format
See above.

## Example
*(populate after first run + first 5 actual sends)*
