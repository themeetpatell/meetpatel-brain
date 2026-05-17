---
type: prompt
category: content
status: living
tags: [prompts, content, story]
---

# Prompt: Story-driven post with a lesson

**Use when:** Something concrete happened — a meeting, a deal, a moment — and the lesson is hiding inside the specifics.
**Reads:** `_AI/Contexts/meet.md`, `_AI/Contexts/voice.md`
**Filed at:** `60 Outputs/Content/YYYY-MM/[slug].md`

## Inputs
- <<the moment>>: [What actually happened. Time, place, person, words exchanged.]
- <<the lesson>>: [What I took away. One sentence.]
- <<the operative move>>: [What I'll do differently — or what others should]

## Prompt body

Read `_AI/Contexts/meet.md` and `_AI/Contexts/voice.md` first.

The moment: <<the moment>>
The lesson: <<the lesson>>
The operative move: <<the operative move>>

Draft a LinkedIn post in my voice. Structure:
- Line 1: drop the reader inside the moment. Tense: past. Specific.
- Lines 2–6: tell what happened, in plain words, no lesson yet
- Line 7–9: name the lesson, once, sharply
- Last line: the operative move

Constraints:
- Keep proper nouns where they sharpen the moment, anonymize where they create risk
- No "I learned that..." soft openers — show, then state
- Max 14 lines

Return: the draft + a "what could go wrong" check (is this story honest, kind, useful).

## Output format
Draft + risk note + 1 alternative opener.

## Example

Input:
- the moment: "Walked into the office at 7am Tuesday. Three of the team were already there. I asked why. They said the WhatsApp leads from the weekend hadn't been triaged."
- the lesson: "Standards don't trickle down. They are observed at the top and copied silently."
- the operative move: "I will be in by 7 every Tuesday for the next quarter."

Output draft:
> Walked in at 7am Tuesday. Three of the team were already there. I asked why.
>
> "The WhatsApp leads from the weekend weren't triaged."
>
> They were doing the thing I'd been talking about doing for three months. I'd told them response time was the priority. I hadn't shown them.
>
> Standards aren't trickle-down. They're copied silently from whoever shows up.
>
> 7am Tuesdays for the rest of the quarter. No memo about it. They'll notice or they won't.
