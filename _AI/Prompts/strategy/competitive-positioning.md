---
type: prompt
category: strategy
status: living
tags: [prompts, strategy, positioning, competitive]
---

# Prompt: Competitive positioning sharpen

**Use when:** A venture's positioning feels generic, or a competitor just moved and we need to re-anchor.
**Reads:** `_AI/Contexts/meet.md`, target venture's `CLAUDE.md`, `50 Atlas/Competitive/[venture]/`
**Filed at:** `30 Ventures/[Venture]/Notes/Positioning.md`

## Inputs
- <<venture>>: [Venture name]
- <<current positioning statement>>: [What we say today]
- <<top 3 competitors>>: [Names]
- <<trigger>>: [Why we're re-positioning now — competitor move, sales objection pattern, investor feedback]

## Prompt body

Read `_AI/Contexts/meet.md`, `30 Ventures/<<venture>>/CLAUDE.md`, and any competitor dossiers in `50 Atlas/Competitive/<<venture>>/` first.

Current positioning: <<current positioning statement>>
Top 3 competitors: <<top 3 competitors>>
Trigger: <<trigger>>

Build the positioning using April Dunford's frame, adapted:

1. **Competitive alternatives** — what would customers use if we didn't exist? (Be honest. "Excel" counts.)
2. **Unique attributes** — what we have that the alternatives don't (verifiable, not aspirational)
3. **Value (so what)** — what the unique attributes enable for the customer
4. **Best fit customer** — who has the strongest reason to care about that value
5. **Market category** — what frame of reference makes us look strongest

Return:

```
# Positioning — [Venture]

## Sharpened positioning statement (one sentence)
[For [who], [Venture] is the [category] that [unique value], unlike [alternative] which [contrast].]

## Why this beats the old version
- [Specific weakness in old positioning that this addresses]

## Competitive alternatives (honest list)
1. [Alternative + why customers default to it]

## Unique attributes (verifiable)
- [Attribute] — proof: [...]

## Value (so what) — translated to buyer language
- [Outcome the buyer cares about]

## Best fit customer profile
- [Concrete segment, not abstract persona]

## Market category recommendation
- [Category to anchor in, and why]

## Messaging house (3 levels)
- Headline: [one line — for landing page hero]
- Subhead: [the explainer]
- Proof bullets: [3 concrete proof points]

## What we are NOT
- [3 things we explicitly are not, to sharpen the position]
```

## Output format
See above.

## Example
*(populate after first real run)*
