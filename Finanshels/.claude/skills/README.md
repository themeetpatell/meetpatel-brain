# Finanshels Claude Skills

37 Claude skills that give the Finanshels team a consistent, expert way to do
their work — from qualifying a lead to filing a VAT return to writing a LinkedIn
post. Every skill is tuned to **UAE accounting and tax compliance** and to the
Finanshels brand.

---

## How these skills work

Each subdirectory here is a **real Claude Code skill**. When you ask Claude to do
something that matches a skill's `description`, Claude loads that skill's
`SKILL.md` and follows its workflow. You don't invoke skills manually — just
describe the task in plain language and the right skill activates.

> Example: *"Qualify this inbound lead — a Dubai mainland trading LLC, AED 4M
> revenue, no accountant yet"* → the `prospect-qualification` skill activates.

Skills live in the project (`.claude/skills/`), so the whole team gets them
through git. They are shared, version-controlled, and improve over time.

**Two foundation files everything builds on:**

- [`master-brand/`](master-brand/SKILL.md) — single source of truth for
  positioning, voice, taglines, proof points, and visual identity.
- [`_shared/finanshels-context.md`](_shared/finanshels-context.md) — accurate UAE
  tax facts (CT, VAT, thresholds, deadlines). Every skill references this so
  facts stay correct in one place.

---

## The 37 skills by function

### Foundation

| Skill | What it does |
|-------|--------------|
| `master-brand` | The brand bible — positioning, voice, taglines, proof points, colours, fonts. All client-facing content conforms to it. |

### Sales & Business Development

| Skill | What it does |
|-------|--------------|
| `tax-advisory-consultant` | Analyses a prospect's UAE tax situation and produces a sales-ready optimisation plan. |
| `prospect-qualification` | Scores an inbound lead against the ICP and recommends next steps. |
| `proposal-generator` | Drafts a tailored, one-page compliance/accounting service proposal. |

### Marketing & Growth

| Skill | What it does |
|-------|--------------|
| `brand-consistency-guide` | Reviews and rewrites any content to match Finanshels voice, with a change log. |
| `content-planner-tax` | Plans a quarterly UAE tax content calendar mapped to the compliance cycle. |
| `seo-tax-compliance` | Builds a UAE tax keyword map and SEO content roadmap. |
| `thought-leadership-writer` | Turns a tax insight into a ready-to-post LinkedIn post or blog article. |

### Finance & Operations

| Skill | What it does |
|-------|--------------|
| `engagement-budget-calculator` | Breaks an engagement into hours, AED fees, and timeline. |
| `workflow-optimizer` | Maps an internal process and flags bottlenecks with fixes. |
| `client-profitability-analyzer` | Calculates margin per client and flags pricing actions. |
| `resource-planner` | Matches team capacity to the workload calendar; forecasts hiring. |
| `financial-dashboard-brief` | Synthesises monthly KPIs into an executive memo. |

### Compliance & Risk

| Skill | What it does |
|-------|--------------|
| `tax-law-monitor` | Turns FTA/MoF updates into a weekly internal compliance bulletin. |
| `risk-assessment-tax` | Scores a client's CT/VAT position for FTA audit risk with a mitigation plan. |
| `audit-workpaper-reviewer` | Reviews workpapers against quality and compliance standards. |
| `documentation-auditor` | Checks client documentation for gaps against UAE record-keeping rules. |
| `engagement-letter-generator` | Drafts a compliant engagement letter for a service scope. |
| `compliance-calendar` | Builds a filing-deadline calendar by entity type. |

### Client Services & Support

| Skill | What it does |
|-------|--------------|
| `client-onboarding-guide` | Standardises new-client intake (CDD, documents, kickoff). |
| `tax-question-answerer` | Answers common UAE tax/compliance questions in plain English. |
| `deliverable-tracker` | Tracks all client deliverables and raises escalation alerts. |
| `communication-template-library` | Brand-consistent, ready-to-send client message templates. |
| `client-success-scorecard` | Scores engagement health with intervention triggers. |

### Product & Engineering

| Skill | What it does |
|-------|--------------|
| `tax-data-validator` | Validates and standardises client financial/tax data; quality report. |
| `code-reviewer-tax-software` | Reviews tax/accounting code for correctness and tax-rule risk. |
| `api-documentation-writer` | Documents tax & accounting APIs with usage examples. |
| `testing-guide-tax-scenarios` | Generates a test matrix covering UAE tax edge cases. |

### HR & People Operations

| Skill | What it does |
|-------|--------------|
| `onboarding-checklist-team` | New-hire onboarding playbook and 90-day plan. |
| `training-plan-tax-updates` | Internal training curriculum on UAE tax/regulatory changes. |
| `performance-review-guide` | Structures evaluations with a competency rubric. |

### Legal & Contracts

| Skill | What it does |
|-------|--------------|
| `contract-reviewer-compliance` | Reviews contracts for compliance/liability risk; risk matrix. |
| `malpractice-prevention-guide` | Audits engagements for professional-liability risk. |
| `nda-generator` | Drafts a UAE-appropriate NDA for data sharing. |

### Data & Analytics

| Skill | What it does |
|-------|--------------|
| `tax-metrics-dashboard` | Defines firm-wide compliance KPIs and computes them. |
| `client-data-analyzer` | Extracts trends and insights from client financial data. |
| `benchmark-analyzer-tax` | Compares performance against industry benchmarks; gap analysis. |

---

## Skill anatomy

```
<skill-name>/
├── SKILL.md          ← required: name + description frontmatter, then the workflow
├── templates/        ← optional: fill-in-ready templates
├── checklists/       ← optional: review checklists
├── workflows/        ← optional: detailed step-by-step processes
├── resources/        ← optional: reference data (keyword banks, deadline tables)
└── tools/            ← optional: runnable Python utilities (stdlib only)
```

Every `SKILL.md` follows the same structure: **When to use → Inputs needed →
Workflow → Output format → Quality checklist → Examples → Guardrails →
Reference**. That consistency *is* the brand.

---

## Adding a new skill

1. Create `.claude/skills/<skill-name>/SKILL.md`. The directory name must equal
   the `name` in the frontmatter (lowercase-hyphenated).
2. Use **only** `name` and `description` in the YAML frontmatter — see
   [`../../SKILL_TEMPLATE.md`](../../SKILL_TEMPLATE.md). Extra fields break
   skill discovery.
3. Write a `description` that starts with "Use when…" and names concrete
   triggers — that is what Claude reads to auto-invoke the skill.
4. Reference `_shared/finanshels-context.md` for tax facts; reference
   `master-brand` for any brand/voice rules. Never hardcode either.

---

## Guardrails (apply to every skill)

- **UAE only** — Federal Tax Authority, Corporate Tax, VAT, EmaraTax. Never IRS/US.
- **Not final advice** — outputs are professional work product to be reviewed by
  a qualified Finanshels team member before reaching a client.
- **Verify the numbers** — tax law changes; confirm rates and deadlines against
  current FTA guidance.
- **Confidential** — never put real client identifiers in skill outputs or examples.
