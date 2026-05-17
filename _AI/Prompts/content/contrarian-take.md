---
type: prompt
category: content
status: living
tags: [prompts, content, contrarian]
---

# Prompt: Contrarian take on a popular opinion

**Use when:** I want to publish a sharp disagreement with consensus advice that's circulating in founder / AI / UAE / dating circles.
**Reads:** `_AI/Contexts/meet.md`, `_AI/Contexts/voice.md`
**Filed at:** `60 Outputs/Content/YYYY-MM/[slug].md`

## Inputs
- <<popular opinion>>: [What "everyone" is saying]
- <<my actual belief>>: [What I actually think, with evidence]
- <<receipt>>: [Specific lived experience or data point that proves my belief]

## Prompt body

Read `_AI/Contexts/meet.md` and `_AI/Contexts/voice.md` first.

Popular opinion: <<popular opinion>>
My actual belief: <<my actual belief>>
Receipt: <<receipt>>

Draft a LinkedIn post in my voice that:
1. States the popular opinion in line 1 — neutrally, no strawman
2. Disagrees in line 2 — direct, specific
3. Defends with the receipt — a number, a story, a regulation, a deal, something concrete
4. Lands with the operative move — what I'd do differently because of the belief
5. Does NOT call anyone out by name. Disagree with the idea, not the person.

Constraints: 8–14 lines, no emojis, no closing summary, no "not X but Y" construction.

Return: the draft, plus a "what could go wrong" note (is this take provable, defensible, mature).

## Output format
Draft + risk note + 1 alternative hook.

## Example

Input:
- popular opinion: "Founders should focus on one venture at a time."
- my actual belief: "Six of mine teach the other two. The question isn't how many, it's which ones compound."
- receipt: "Finanshels operating discipline is what made StartupOS thesis sharp. Without the lab, the OS would be theory."

Output draft:
> "Focus on one venture at a time." Standard advice. I run eight. I keep being told this is wrong.
>
> It's half right. Six of my eight teach the other two. Finanshels — the revenue venture — is the operating lab that made StartupOS thesis sharp. Without the lab, the OS is theory.
>
> Kill the wrong six and you don't get focus, you get a smaller version of the same problem.
>
> The question isn't how many. It's which ones compound into each other. That's the one I keep asking.
