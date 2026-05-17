---
type: prompt
category: ops
status: living
tags: [prompts, ops, 1on1, management]
---

# Prompt: 1:1 prep frame

**Use when:** Before any 1:1 — direct report, peer, or skip-level. Want to walk in with a structured prep, not wing it.
**Reads:** `_AI/Contexts/meet.md`, person's note in `40 Areas/Relationships/People/`, last 1:1 log
**Filed at:** `40 Areas/Relationships/People/[Person]/1on1-YYYY-MM-DD.md`

## Inputs
- <<person>>: [Name]
- <<their context>>: [Role, current work, recent wins/losses]
- <<my open loops with them>>: [Things I owe them, decisions I owe them]
- <<their potential blockers>>: [What I think might be slowing them — best guess]
- <<meeting goal>>: [If different from default — default is care + clarity + connection]

## Prompt body

Read `_AI/Contexts/meet.md` and the person's relationship note. Generate a 1:1 prep doc using the Manager Tools / High Output Management hybrid.

Person: <<person>>
Context: <<their context>>
My open loops: <<my open loops with them>>
Suspected blockers: <<their potential blockers>>
Goal: <<meeting goal>>

Return:

```
# 1:1 — [Person] — [Date]

## Mode
- [Standing 1:1 / Project sync / Career conversation / Hard feedback / Recovery]

## My open loops to close
- [Decision I owe them]
- [Answer I owe them]

## Things to actively ask
1. [Open-ended question to surface unsurfaced]
2. [Specific question on a known concern]
3. [Career / growth question — at least once a month]

## Things to surface (if they don't bring up)
- [Concern I have]
- [Pattern I've noticed — positive or negative]

## Pre-decided don'ts
- Don't fill silence. Wait.
- Don't pre-empt their agenda. Let them lead first 10 minutes if they want.
- Don't deliver hard feedback in the last 5 minutes — frontload.

## Care moment (specific)
- [Something personal I should remember to ask about — family, health, side project]

## After the meeting — capture
- Decisions made: [...]
- Action items (mine): [...]
- Action items (theirs): [...]
- Pattern noted for relationship file: [...]
- Next 1:1 trigger to set: [...]
```

If this is a hard-feedback meeting, separately prepare:
- The single sentence you must say
- The behavior (not the person) you're naming
- The path forward (not just the problem)

## Output format
See above.

## Example
*(populate after first real run)*
