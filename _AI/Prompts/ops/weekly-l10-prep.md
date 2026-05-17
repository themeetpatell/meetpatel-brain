---
type: prompt
category: ops
status: living
tags: [prompts, ops, eos, l10]
---

# Prompt: Weekly L10 prep (EOS)

**Use when:** Before the weekly Level 10 meeting (EOS). Want a tight agenda with scorecard signal, rocks status, and issues list pre-prioritized.
**Reads:** `_AI/Contexts/meet.md`, venture `CLAUDE.md`, scorecard data, rocks tracker
**Filed at:** `30 Ventures/[Venture]/Meetings/L10-YYYY-MM-DD.md`

## Inputs
- <<venture>>: [Finanshels usually]
- <<scorecard snapshot>>: [Last week's metrics + targets]
- <<rocks status>>: [On-track / off-track per rock]
- <<headlines>>: [Customer / employee wins this week]
- <<known issues>>: [Anything already raised by team]

## Prompt body

Read `_AI/Contexts/meet.md` and the venture `CLAUDE.md`. Apply EOS L10 structure.

Scorecard: <<scorecard snapshot>>
Rocks: <<rocks status>>
Headlines: <<headlines>>
Known issues: <<known issues>>

Generate:

```
# L10 — [Venture] — [Date]

## Segue (5 min)
- Personal best + business best this week (round-robin)

## Scorecard (5 min)
| Metric | Target | This week | Status |
|---|---|---|---|
| ... | ... | ... | ✓ / ✗ |

Off-track metrics → goes to IDS list.

## Rock Review (5 min)
| Rock | Owner | Status | Notes |
|---|---|---|---|
| ... | ... | on-track / off-track | ... |

Off-track rocks → goes to IDS list.

## Customer + Employee Headlines (5 min)
- [Customer headline]
- [Employee headline]

## To-Do List (5 min)
[Carry-over from last week — quick check, complete/incomplete]

## IDS — Identify, Discuss, Solve (60 min)
**Issues list (prioritized by impact × urgency):**
1. [Issue — owner — proposed frame]
2. ...

For each top-3 issue:
- **Identify:** [the real issue under the surface symptom]
- **Discuss:** [10 min max, surface options]
- **Solve:** [decision + owner + by-when]

## Conclude (5 min)
- New to-do's captured
- Cascading messages: [what gets communicated to the wider team]
- Rating: 1–10 (everyone rates the meeting)
```

Keep IDS to 3 issues. The rest go to next week or async resolution.

## Output format
See above.

## Example
*(populate after first real L10)*
