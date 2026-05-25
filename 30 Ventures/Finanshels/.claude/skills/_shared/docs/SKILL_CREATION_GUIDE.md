# Skill Creation Guide — Finanshels

**Step-by-step guide for building Claude Skills for Finanshels.**

Created: May 18, 2026

---

## 📋 Quick Checklist

Before you start building a skill, make sure you have:

- [ ] Skill name from the roadmap (SKILLS_ROADMAP.md)
- [ ] SKILL_TEMPLATE.md (master template)
- [ ] finanshels-context.md (company facts)
- [ ] Clear understanding of the workflow/process
- [ ] 30-60 minutes to document it

---

## 🚀 Building a Skill (5 Steps)

### Step 1: Choose Your Skill

**From SKILLS_ROADMAP.md, select a skill to build.**

Examples:
- `brand-consistency-guide`
- `client-onboarding-guide`
- `proposal-generator`

**Questions to answer:**
- What does this skill do?
- Who will use it?
- What problem does it solve?

---

### Step 2: Create the Directory Structure

Create a folder for your skill:

```bash
mkdir -p /Users/themeetpatel/My\ brain/Finanshels/skills/[category]/[skill-name]
```

**Categories:**
- `sales-bd`
- `marketing-growth`
- `finance-operations`
- `compliance-risk`
- `client-services`
- `product-engineering`
- `hr-people`
- `legal-contracts`
- `data-analytics`

**Example:**
```bash
mkdir -p /Users/themeetpatel/My\ brain/Finanshels/skills/marketing-growth/brand-consistency-guide
```

---

### Step 3: Create SKILL.md

Copy SKILL_TEMPLATE.md and customize it for your skill.

**Key sections to fill:**

#### Section A: Frontmatter (YAML)
```yaml
---
name: [skill-name]
description: Use when [concrete triggers]. Produces [output].
---
```

**Use ONLY `name` and `description` — any other field breaks skill discovery.**
`name` must equal the skill directory name. Fill this first. Takes 5 minutes.

#### Section B: Purpose & Output
- **Purpose:** Why does this skill exist?
- **What it produces:** Specific, measurable outputs

**Guide:** Read what problem this solves. What does the user want?

#### Section C: Use Cases / Triggers
"When would someone use this skill?"

**Guide:** Think of 3-5 real scenarios where this skill would help. Write them down.

**Example (Brand Consistency Guide):**
- Marketing team needs to write a press release
- Sales team is drafting a proposal
- Client success team writing an update email

#### Section D: Workflow Steps
"How does the skill work?"

**Guide:**
1. **List the major steps** (3-5 typically)
2. **For each step, describe what Claude does**
3. **List sub-steps** (if complex)
4. **State what you get** (output) from each step

**Example (Brand Consistency):**
- Step 1: Extract key brand guidelines from existing documents
- Step 2: Analyze the user's draft for tone/voice alignment
- Step 3: Suggest specific rewrites to match brand voice
- Step 4: Provide brand tone checklist for final review

#### Section E: Quality Checklist
"How do we know the output is good?"

**Guide:** List 5-7 checkboxes for validating the output.

**Example:**
- [ ] All recommendations include specific tax impact (AED)
- [ ] Complies with current UAE tax law and FTA guidance
- [ ] Written in Finanshels' professional yet approachable tone
- [ ] Includes implementation timeline
- [ ] No jargon without explanation

#### Section F: Example Prompts
"Show me how to use this skill."

**Guide:**
1. Write 3-5 realistic example prompts
2. For each, show what Claude should output
3. Make examples specific to Finanshels

**Format:**
```
### Example 1: [Scenario]

**Prompt:**
[Copy-paste example]

**Expected Output:**
[What Claude should produce]
```

---

### Step 4: Create Supporting Files

In the same skill folder, create these files:

#### `examples.md` (Prompt Library)
- Copy of example prompts from SKILL.md
- More real-world examples
- Different variations

#### `workflows/workflow-1.md` (If Complex)
- Step-by-step guide for users
- Decision trees if there are multiple paths
- Detailed instructions

#### `templates/template.md` (If Applicable)
- Reusable template output
- Format users should follow
- Example filled template

#### `tools/script.py` (If Applicable)
- Helper Python script
- Data validation
- Calculation utility

---

### Step 5: Test & Refine

**Before marking it complete:**

1. **Read it yourself** — Does it make sense? Is it clear?
2. **Show it to a team member** — Can they understand it without asking questions?
3. **Try a prompt** — Test one of your example prompts with Claude
4. **Check the quality checklist** — Does the output pass all checks?
5. **Document what you learned** — Any tips to add? Edge cases?

---

## 🎨 Writing Style Guide

When creating skills, follow this style:

### Tone
- **Professional yet approachable** (like Finanshels brand)
- **Clear, not jargon-heavy**
- **Specific, not vague**
- **Action-oriented**

### Structure
- **Short paragraphs** (2-3 sentences max)
- **Bullet points** for lists
- **Headings** to organize sections
- **Examples** to clarify instructions

### Language
❌ **Avoid:**
- "might be helpful"
- "consider possibly thinking about"
- "in some cases, you may want to"

✅ **Use:**
- "This will increase..."
- "Follow these steps..."
- "The output includes..."

---

## 🔍 Common Mistakes to Avoid

| Mistake | Problem | Solution |
|---------|---------|----------|
| **Workflow too vague** | User doesn't know how to use it | Make each step concrete with examples |
| **Quality checklist missing** | No way to validate output | List 5-7 specific, measurable criteria |
| **No examples** | "How do I actually use this?" | Include 3-5 real example prompts |
| **Too complicated** | User gets overwhelmed | Break into 2-3 simpler skills instead |
| **No context** | Doesn't fit Finanshels | Reference company facts from finanshels-context.md |
| **Incomplete structure** | Looks amateur | Use SKILL_TEMPLATE.md exactly as is |

---

## 📊 Time Estimates

| Component | Time |
|-----------|------|
| Metadata + Purpose | 5 min |
| Workflow design | 10 min |
| Quality checklist | 5 min |
| Example prompts (3-5) | 15 min |
| Support files | 10-20 min |
| **Total per skill** | **45-60 min** |

**For Phase 1 (6 skills):** ~4-5 hours total

---

## 🔄 Skill Development Workflow

```
1. Choose skill from SKILLS_ROADMAP.md
   ↓
2. Create directory in skills/[category]/[skill-name]
   ↓
3. Copy SKILL_TEMPLATE.md to SKILL.md
   ↓
4. Fill in Metadata (YAML)
   ↓
5. Document Purpose & Output
   ↓
6. List Use Cases/Triggers
   ↓
7. Design Workflow Steps
   ↓
8. Create Quality Checklist
   ↓
9. Write Example Prompts
   ↓
10. Create support files (examples.md, workflows/, templates/)
   ↓
11. Self-review: Does it make sense?
   ↓
12. Test one example prompt
   ↓
13. Mark complete in MASTER_CHECKLIST.md
   ↓
14. Move to next skill
```

---

## 💡 Tips for Better Skills

### Tip 1: Be Specific
❌ "Help with proposals"  
✅ "Generate 1-page tax compliance service proposals with pricing, timeline, and deliverables"

### Tip 2: Include Real Examples
❌ "The skill works on any client type"  
✅ "Example: For a small manufacturing business, the skill analyzes S-corp vs. LLC tax positioning"

### Tip 3: Connect to Finanshels
❌ Generic skill that could apply anywhere  
✅ Specific to Finanshels' clients, processes, or brand voice

### Tip 4: Show Quality Criteria
❌ Hope the output is good  
✅ "Output is good if it meets these 5 checks: [list]"

### Tip 5: Make it Repeatable
❌ Skill works once, then needs tweaking  
✅ Anyone on the team can run this skill and get consistent results

---

## 📋 Skill Review Checklist

Before you mark a skill as "complete," check all of these:

- [ ] **Metadata complete** — All YAML front matter filled
- [ ] **Purpose is clear** — Someone reading the first paragraph gets it
- [ ] **Output is specific** — Describes exactly what you'll get (not vague)
- [ ] **Workflow has 3+ steps** — Each step is concrete
- [ ] **Quality checklist has 5+ items** — Can validate the output
- [ ] **3+ example prompts** — Real scenarios, not generic
- [ ] **Written clearly** — No jargon, short sentences
- [ ] **Finanshels context** — Feels specific to your firm
- [ ] **Related skills listed** — Connects to other skills
- [ ] **Support files created** — examples.md + workflows/templates if needed

**If all checked:** Skill is ready to deploy. Mark in MASTER_CHECKLIST.md.

---

## 🚀 Next Steps

1. **Pick Phase 1 skill** — Choose 1 from SKILLS_ROADMAP.md (Low effort, high impact)
2. **Create directory** — `skills/[category]/[skill-name]`
3. **Copy SKILL_TEMPLATE.md** — Rename to SKILL.md
4. **Fill it out** — Following this guide
5. **Create examples.md** — Copy of example prompts
6. **Self-review** — Check the review checklist above
7. **Mark complete** — Update MASTER_CHECKLIST.md
8. **Move to next** — Pick another Phase 1 skill, repeat

---

**Questions while building a skill? Refer back to SKILL_TEMPLATE.md or this guide.**

**Ready to start? Pick your first skill now and create the folder!**
