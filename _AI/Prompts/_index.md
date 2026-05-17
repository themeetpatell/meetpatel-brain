---
type: prompt-index
status: living
updated: 2026-05-17
tags: [prompts, index]
---

# Prompt Library — Index

> Single-shot prompts organized by job-to-be-done. Pick the closest match, edit the inputs, run. Each prompt is self-contained — agent context (`_AI/Contexts/`) is auto-loaded.

## Content (writing in Meet's voice)
- [[content/linkedin-post-from-observation|LinkedIn post from observation]]
- [[content/contrarian-take|Contrarian take on a popular opinion]]
- [[content/story-driven-post|Story-driven post with a lesson]]
- [[content/founder-thread|Founder thread (X / LinkedIn)]]

## Strategy (thinking work)
- [[strategy/portfolio-prioritization|Portfolio prioritization (which venture this week)]]
- [[strategy/wedge-selection|Wedge selection for a venture]]
- [[strategy/competitive-positioning|Competitive positioning sharpen]]
- [[strategy/kill-or-double-down|Quarterly kill-or-double-down call]]

## Ops (running the work)
- [[ops/weekly-l10-prep|Weekly L10 prep (EOS)]]
- [[ops/sop-from-mess|Turn messy process into clean SOP]]
- [[ops/quarterly-okr-set|Quarterly OKR setter]]
- [[ops/team-1on1-frame|1:1 prep frame]]

## Sales (revenue motion)
- [[sales/lead-qualification|Lead qualification (MEDDIC-style)]]
- [[sales/discovery-call-prep|Discovery call prep brief]]
- [[sales/deal-stuck-diagnostic|Deal stuck — what's actually blocking]]
- [[sales/objection-handler|Objection handler — written response]]

## Personal (life OS)
- [[personal/weekly-review|Weekly review (Friday close)]]
- [[personal/journal-extract|Extract insights from a journal entry]]
- [[personal/relationship-nudge|Who haven't I contacted that I should]]
- [[personal/energy-audit|Energy audit — what's draining vs feeding]]

## How to use

1. Open the prompt file
2. Replace `<<inputs>>` blocks with your context
3. Paste into Claude (or run via skill)
4. Output lands wherever the prompt's "filed at" field points

## Adding a prompt

Use this skeleton:

```markdown
---
type: prompt
category: [content|strategy|ops|sales|personal]
status: living
tags: [prompts, ...]
---

# Prompt: [Name]

**Use when:** [trigger]
**Reads:** `_AI/Contexts/meet.md`, [other context]
**Filed at:** [vault path for output]

## Inputs (replace these)
- <<input 1>>
- <<input 2>>

## Prompt body

[The actual prompt text — copy-paste into Claude]

## Output format
[Structure expected back]

## Example
[A sample input → output pair]
```

---

*If you find yourself re-typing a prompt for the third time, it belongs in this library.*
