---
type: ai-readme
status: living
updated: 2026-05-17
tags: [ai, readme, system]
---

# _AI — the AI-native layer of My brain

> This folder is the surface where Claude, Cursor, and any agent reads my vault. Humans navigate from `70 Meta/Dashboards/Home.md`. Agents navigate from here.

## How it works

| Folder | Purpose | Read by |
|---|---|---|
| `Contexts/` | Who I am, how I write, what I'm building, current state | Every agent, every session, before doing anything |
| `Agents/` | Pre-built agent personalities for specific jobs (chief-of-staff, content engine, etc.) | Loaded by name when invoking that agent |
| `Prompts/` | Reusable single-shot prompts organized by job-to-be-done | Pulled by category when the job matches |
| `Workflows/` | Multi-step procedures (weekly review, investor update, etc.) | Run end-to-end when triggered |
| `Skills/` | Registry pointing to installed Claude skills | Reference layer — skills live outside the vault |

## Read order for any agent

1. `Contexts/meet.md` — identity, voice rules, what I want
2. `Contexts/voice.md` — voice examples + anti-patterns (only if writing as me)
3. `Contexts/ventures-overview.md` — portfolio snapshot
4. `Contexts/current-state.md` — what I'm working on this week
5. The specific Agent / Prompt / Workflow being invoked

## Conventions

- **Frontmatter is mandatory** on every note. Minimum: `type`, `tags`, `status`.
- **Wikilinks over URLs** inside the vault. URLs only for external sources.
- **Status values:** `draft`, `living`, `final`, `archived`, `awaiting-approval`.
- **Owner:** default Meet Patel. Override if delegating.
- **Living docs** get an `updated:` field maintained on edit.

## How to add a new agent

1. Create `Agents/<name>.md` with the agent template (see `Agents/_template.md`).
2. Define: trigger, inputs, output format, voice constraints, escalation path.
3. Link from `_index.md` if one exists in the folder.

## How to add a new prompt

1. Drop into the right `Prompts/<category>/` subfolder.
2. Use the prompt template (frontmatter + Task + Inputs + Output format + Examples).
3. Cross-link to related prompts.

## What goes here vs elsewhere

- **Here:** prompts, agent personalities, multi-step workflows, AI-readable context, voice rules, skill registry.
- **Not here:** raw knowledge (goes to `50 Atlas/`), venture content (goes to `30 Ventures/`), personal identity (lives in `20 Compass/`, this folder just distills it for agents).

## Maintenance

- `Contexts/current-state.md` — refresh every Monday (or via scheduled task).
- `Contexts/meet.md` — refresh whenever `20 Compass/Identity/` changes meaningfully.
- `Prompts/` — add as you discover repeating prompts in chat history.
- Quarterly: run `anthropic-skills:consolidate-memory` over the whole vault.

---

*This folder is the difference between an Obsidian vault and a founder OS.*
