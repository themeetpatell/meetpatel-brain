# SKILL.md Template — Finanshels

**Use this template as a base for every SKILL.md you create.**

Copy this file and replace all `[SKILL_NAME]`, `[description]`, `[workflow steps]` placeholders with your specific skill content.

---

```yaml
---
name: [skill-name]
description: Use when [concrete trigger scenarios — name the phrases and situations that should activate this skill]. Produces [one sentence on the output].
---
```

**Use ONLY `name` and `description`.** Any other field (tags, category, priority, related_skills, dates) breaks skill discovery — do not add them. The `name` must exactly equal the skill's directory name (lowercase-hyphenated). The `description` is the text Claude reads to auto-invoke the skill: start it with "Use when…" and name concrete triggers and the output.

## Purpose

[Clear statement of why this skill exists and what problem it solves]

**Example:** 
This skill solves the consistency challenge by helping all team members write and communicate in Finanshels' brand voice. It's used when drafting client communications, marketing copy, and internal documentation.

---

## What This Skill Produces

[Specific, measurable outputs]

**Example outputs:**
- ✅ Tax optimization strategy (2-page plan with 3-5 recommendations)
- ✅ Client-ready tax summary with dollar impacts
- ✅ Risk assessment and implementation timeline
- ✅ Cost-benefit analysis for each recommendation

---

## When to Use This Skill

**Triggers / Use Cases:**

1. **Trigger 1:** [Specific scenario when someone would invoke this skill]
2. **Trigger 2:** [Another use case]
3. **Trigger 3:** [Another use case]

**Example:**
1. Sales team is qualifying a new prospect
2. Running initial discovery call needs to assess fit
3. Need to estimate engagement scope for proposal

---

## How It Works

### Input Requirements

**Required Information:**
- [Data point 1]
- [Data point 2]
- [Data point 3]

**Optional Information:**
- [Additional context that improves output]

**Example:**
- Client industry & revenue
- Current tax situation (entity type, # of employees)
- Previous year tax return
- Known business challenges

---

### Workflow Steps

#### Step 1: [First Major Step]
[What the skill does in this step]
- [Sub-step 1]
- [Sub-step 2]
- [Sub-step 3]

**Output:** [What you get from this step]

---

#### Step 2: [Second Major Step]
[What the skill does in this step]
- [Sub-step 1]
- [Sub-step 2]

**Output:** [What you get from this step]

---

#### Step 3: [Third Major Step]
[What the skill does in this step]

**Output:** [Final deliverable]

---

## Quality Checklist

Use this to validate the skill's output:

- [ ] [Quality criterion 1]
- [ ] [Quality criterion 2]
- [ ] [Quality criterion 3]
- [ ] [Quality criterion 4]
- [ ] [Quality criterion 5]

**Example:**
- [ ] All recommendations include a specific AED impact
- [ ] Risk assessment addresses FTA audit likelihood
- [ ] Implementation steps are realistic for client complexity
- [ ] References current UAE tax law and FTA guidance
- [ ] Written in Finanshels brand voice

---

## Example Prompts

Copy and modify these prompts to try this skill:

### Example 1
```
[Give full example prompt to Claude that would invoke this skill]

[Optional: expected output structure]
```

### Example 2
```
[Another example]
```

### Example 3
```
[Another example]
```

---

## Success Metrics

How to measure if this skill is working well:

- **Metric 1:** [What to measure]
  - Target: [Goal]
  - Current: [Baseline if known]

- **Metric 2:** [What to measure]
  - Target: [Goal]

**Example:**
- **Faster sales cycle:** Sales team closes 30% faster with this analysis
- **Higher close rate:** Fewer objections because all questions are pre-answered
- **Time saved:** Each analysis takes <30 mins instead of 2 hours
- **Client satisfaction:** Prospects feel well understood before first call

---

## Tips & Tricks

### Do's ✅
- [Best practice 1]
- [Best practice 2]
- [Best practice 3]

### Don'ts ❌
- [Common mistake 1]
- [Common mistake 2]
- [Common mistake 3]

---

## Related Workflows / Skills

**Workflows that use this skill:**
- [Workflow name]
- [Workflow name]

**Skills that complement this:**
- [Related skill name]
- [Related skill name]

---

## Files in This Skill

```
[skill-name]/
├── SKILL.md ..................... This file (main skill definition)
├── examples.md .................. Copy-paste prompt examples
├── workflows/
│   ├── workflow-1.md ........... Step-by-step process guide
│   └── workflow-2.md
├── templates/
│   └── template-1.md ........... Reusable templates
└── tools/ (if applicable)
    └── python-script.py ........ Utility code
```

---

## Version History

| Date | Version | Changes |
|------|---------|---------|
| 2026-05-18 | 1.0 | Initial creation |

---

## Questions?

**Before you use this skill:**
1. Read through all steps
2. Check the quality checklist
3. Try one of the example prompts
4. Provide feedback to improve it

**To improve this skill:**
- Note what works well
- Note what needs clarification
- Suggest additional workflows
- Flag gaps or edge cases
