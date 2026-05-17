---
type: prompt
category: content
status: living
tags: [prompts, content, thread]
---

# Prompt: Founder thread (X / LinkedIn)

**Use when:** The idea is genuinely multi-step and a single post would compress out the value. Threads only when the idea earns it.
**Reads:** `_AI/Contexts/meet.md`, `_AI/Contexts/voice.md`
**Filed at:** `60 Outputs/Content/YYYY-MM/[slug]-thread.md`

## Inputs
- <<thesis>>: [The single claim the whole thread defends]
- <<steps or proof points>>: [3–7 sub-points, each strong enough to be its own tweet]
- <<land>>: [The takeaway / call-to-action line]
- <<surface>>: X or LinkedIn

## Prompt body

Read `_AI/Contexts/meet.md` and `_AI/Contexts/voice.md` first.

Thesis: <<thesis>>
Proof points: <<steps or proof points>>
Land: <<land>>
Surface: <<surface>>

Draft a thread. Constraints:
- Tweet 1 = hook + thesis. No "🧵" or "thread:" marker. Hook earned by specificity.
- Each subsequent tweet = one proof point, self-contained (could screenshot it alone and it stands).
- Last tweet = the land — the operative move or sharp closer.
- Tweet count = number of proof points + 2 (hook + land). No filler tweets.
- X: under 280 chars per tweet. LinkedIn: each "tweet" can be a paragraph.

Return: numbered tweets only. Then a one-line "why this works".

## Output format
1/n through n/n + why-this-works note.

## Example

Input:
- thesis: "The vault you read once a year is not a second brain. It's a graveyard."
- proof points:
  - "Capture without retrieval is hoarding"
  - "MOCs are the difference between vault and graveyard"
  - "Daily notes are the heartbeat"
  - "AI surface is the multiplier"
- land: "Stop building bigger vaults. Build smaller, more readable ones."
- surface: X

Output (truncated):
> 1/ The vault you read once a year is not a second brain. It's a graveyard.
>
> 2/ Capture without retrieval is hoarding. If you can't find a note in 4 seconds, the note doesn't exist.
>
> 3/ Maps of Content (MOCs) are the difference. One MOC per domain. Every important note has a home.
> ...
> 6/ Stop building bigger vaults. Build smaller, more readable ones.
