---
type: prompt
category: content
status: living
tags: [prompts, content, linkedin]
---

# Prompt: LinkedIn post from observation

**Use when:** I notice something at work / in the market / in a conversation that's worth a post but the draft hasn't formed yet.
**Reads:** `_AI/Contexts/meet.md`, `_AI/Contexts/voice.md`
**Filed at:** `60 Outputs/Content/YYYY-MM/[slug].md`

## Inputs
- <<observation>>: [The raw thing I noticed]
- <<context>>: [Why it matters, what triggered it]
- <<angle>> (optional): [contrarian / story / framework / numbers]

## Prompt body

Read `_AI/Contexts/meet.md` and `_AI/Contexts/voice.md` first.

I noticed: <<observation>>
Context: <<context>>
Angle: <<angle>>

Draft a LinkedIn post in my voice. Constraints:
- 6–14 lines
- Hook in line 1 — specific, not abstract
- One insight, not three
- No emojis, no "not X but Y", no AI throat-clearing, no closing summary
- Land in the last line
- If the observation references a specific number or company, keep it specific in the post

Return: the draft only, then a "why this works" bullet, then 2 alternative hooks.

## Output format
See `_AI/Agents/content-engine.md` output format.

## Example

Input:
- observation: "Customer cancelled and told me exactly why — pricing was fine, but we never set up their AML monthly cadence."
- context: "Finanshels onboarding miss — we cared about acquisition, not the first 30 days."
- angle: confession + lesson

Output draft:
> Customer cancelled this week. Told me exactly why.
>
> Not pricing. Not product. We forgot to set up their AML monthly cadence after onboarding. They paid us for three months thinking we were doing the work. We weren't.
>
> Onboarding ends when the second invoice goes out, not when the contract is signed. That's the rule we're writing today.
