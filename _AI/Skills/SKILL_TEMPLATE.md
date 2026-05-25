# SKILL.md Template — Finanshels

Copy this structure to create a new skill. A skill is a directory at
`.claude/skills/<skill-name>/` containing a `SKILL.md` file.

> The 37 built skills live in [`.claude/skills/`](.claude/skills/README.md).
> This template matches their format exactly — follow it so a new skill is
> consistent with the rest.

---

## Critical: the frontmatter

Claude Code only recognises a skill if `SKILL.md` begins with YAML frontmatter
containing **exactly these two fields** — nothing else:

```markdown
---
name: skill-name
description: Use when ... — describe the concrete triggers AND what the skill produces.
---
```

- `name` **must equal the directory name**, lowercase-hyphenated.
- `description` is what Claude reads to decide when to auto-invoke the skill.
  Start with "Use when…", name concrete triggers, and state the output. Be
  specific and keyword-rich. 1–3 sentences.
- **Do not** add `tags`, `category`, `priority`, `effort`, or dates to the
  frontmatter. Extra fields break skill discovery. (Category belongs in the
  README index, not the frontmatter.)

---

## Body structure

After the frontmatter, write these sections in this order:

```markdown
# Human-Readable Title

One-line summary of what this skill is for.

## When to use

- Concrete trigger scenario 1
- Concrete trigger scenario 2

## Inputs needed

**Required**
- Data point the skill cannot run without

**Optional**
- Context that improves the output

## Workflow

1. **First step** — what the skill does, in detail.
2. **Second step** — UAE-specific, genuinely actionable.
3. **Final step** — produces the deliverable.

## Output format

The exact structure / sections of the deliverable.

## Quality checklist

- [ ] Output criterion 1
- [ ] Output criterion 2

## Examples

**Example 1 — [scenario]**
> A realistic prompt a Finanshels team member would type, using a synthetic
> client (e.g. "a Dubai mainland trading LLC, AED 4M revenue") — never a real name.

## Guardrails

- UAE jurisdiction only — FTA, Corporate Tax, VAT, EmaraTax. Never IRS/US.
- Output is professional work product to be reviewed by a qualified Finanshels
  team member before it reaches a client — not final tax/legal advice.
- Verify rates and deadlines against current FTA guidance.
- Keep client data confidential; never use real client identifiers.

## Reference

See `../_shared/finanshels-context.md` for UAE tax facts, rates, and deadlines.
See the `master-brand` skill for brand voice, positioning, and visual identity.
```

---

## Supporting files (optional)

Add subfolders only when they add real value:

```
<skill-name>/
├── SKILL.md          ← required
├── templates/        ← fill-in-ready templates
├── checklists/       ← review checklists
├── workflows/        ← detailed step-by-step processes
├── resources/        ← reference data
└── tools/            ← runnable Python utilities (stdlib only)
```

Reference them from `SKILL.md` by relative path. Python tools must be
stdlib-only, runnable with `python3 <file>`, and include a `main()` with example
usage on synthetic data.

---

## Quality bar

- A `SKILL.md` should be substantive (~90–200 lines) — a real working tool, not
  a hollow template.
- UAE-accurate. Rates and deadlines must match `_shared/finanshels-context.md`.
  When unsure, tell the user to confirm with the FTA rather than inventing a number.
- Brand voice: clear, confident, plain English, helpful, precise, never alarmist.
  Client-facing content follows the `master-brand` skill.
- Don't duplicate facts — reference the shared context and `master-brand`.
