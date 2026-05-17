---
type: skill-registry
status: living
updated: 2026-05-17
tags: [skills, registry, ai]
---

# Skill Registry — installed Claude skills

> The skills themselves live at `/var/folders/.../claude-hostloop-plugins/skills/`. This file is the in-vault index so I (and agents) know what's available without leaving the vault.

## Personal / operating skills

| Skill | When to trigger |
|---|---|
| `meet-operating-system` | ANY task involving Meet, his ventures, voice, strategy, content, decisions. Load first. |
| `founder-execution-chief-of-staff` | Messy notes, voice memos, transcripts, dumps → structured execution clarity |
| `content-and-voice-engine` | LinkedIn posts, comments, newsletters, carousels, captions, founder essays, voice scoring |
| `linkedin-comment-generator` | Five-flavor comment options for a LinkedIn post |
| `internal-comms` | Status reports, leadership updates, 3P, FAQ, incident reports |

## Venture-specific skills

| Skill | When to trigger |
|---|---|
| `finanshels-coe` | Finanshels ops, CoE, pre-sales, SOPs, scorecards, WhatsApp lead workflows, EOS systems |
| `venture-architect` | Any venture design, validation, GTM, fundraise, ICP, 90-day roadmap |
| `biggdate-brand-voice` | BiggDate/Soulmap copy, product UX, ads, social, onboarding, positioning |
| `biggdate-social-image` | BiggDate social visuals — IG, LinkedIn, X, carousels, statement cards |
| `uae-gcc-strategy-intelligence` | UAE/GCC market entry, Dubai GTM, regional strategy, investor positioning, NRI segments |
| `ai-native-product-builder` | AI product strategy, Claude API workflows, agent design, UX logic, MVP planning |

## Build / output skills

| Skill | When to trigger |
|---|---|
| `docx` | Anything that needs to ship as a Word document |
| `pptx` | Anything involving .pptx — pitch decks, slides, presentations |
| `xlsx` | Spreadsheets, financial models, tabular data |
| `pdf` | PDF read / merge / split / form / extract / create |
| `canvas-design` | Posters, static visuals, design pieces as PNG/PDF |
| `theme-factory` | Apply themed styling to artifacts (slides, docs, HTML) |
| `brand-guidelines` | Anthropic brand colors / typography on artifacts |

## Meta skills

| Skill | When to trigger |
|---|---|
| `skill-creator` | Build new skills, edit existing ones, run evals |
| `mcp-builder` | Build MCP servers (Python FastMCP or Node/TypeScript MCP SDK) |
| `consolidate-memory` | Reflective pass over memory — merge duplicates, fix stale facts, prune the index. **Run monthly.** |
| `setup-cowork` | Guided Cowork plugin installation |
| `schedule` | Create or update scheduled tasks |

## Skill load order for common tasks

| If I ask for... | Load in this order |
|---|---|
| LinkedIn post | `meet-operating-system` → `content-and-voice-engine` |
| BiggDate carousel | `meet-operating-system` → `biggdate-brand-voice` → `biggdate-social-image` |
| Finanshels SOP | `meet-operating-system` → `finanshels-coe` |
| New venture brief | `meet-operating-system` → `venture-architect` → `uae-gcc-strategy-intelligence` |
| Pitch deck | `meet-operating-system` → `venture-architect` → `pptx` (after research) |
| Internal update | `meet-operating-system` → `internal-comms` |

## Adding a new skill

1. Build it under `/var/.../claude-hostloop-plugins/skills/<name>/` using `skill-creator`.
2. Add the row to the table above.
3. Update the load-order list if it changes a common workflow.

---

*Skills are the abilities. This registry tells agents which ability to reach for.*
