# Finanshels Claude Skills — Quick-Start Guide

**Start building your skills in 5 minutes!**

Created: May 18, 2026

---

## 📦 What You've Received

You now have a complete framework for building 36 Claude skills for Finanshels.

### Files Created (7 core files):

1. **[SKILLS_ROADMAP.md](SKILLS_ROADMAP.md)** ⭐
   - All 36 skills organized by business function
   - Priority build order (Phase 1-4)
   - Effort estimates
   - **What it does:** Shows the full roadmap

2. **[FILE_MANIFEST.md](FILE_MANIFEST.md)** 📁
   - Complete directory structure
   - 132 files to create across 36 skills
   - File dependencies
   - **What it does:** Blueprint for folder organization

3. **[SKILL_TEMPLATE.md](SKILL_TEMPLATE.md)** 🎨
   - Master template for every SKILL.md
   - All sections needed for a complete skill
   - Examples filled in
   - **What it does:** Copy-paste template for new skills

4. **[docs/SKILL_CREATION_GUIDE.md](docs/SKILL_CREATION_GUIDE.md)** 📚
   - Step-by-step process (5 steps)
   - Detailed instructions for each section
   - Common mistakes to avoid
   - Time estimates (45-60 min per skill)
   - **What it does:** Your how-to guide

5. **[docs/finanshels-context.md](docs/finanshels-context.md)** 🏢
   - Company overview & identity
   - Team structure
   - Brand voice & messaging
   - Key metrics & tools
   - **What it does:** Reference for skill creators (fill in blanks!)

6. **[docs/MASTER_CHECKLIST.md](docs/MASTER_CHECKLIST.md)** ✅
   - Track progress on all 36 skills
   - Organized by phase
   - Status indicators
   - **What it does:** Progress tracker

7. **[README_QUICKSTART.md](README_QUICKSTART.md)** ⚡
   - This file!
   - Everything you need in one place
   - Quick reference

---

## 🎯 Your Build Plan

### Phase 1: Quick Wins (2-3 weeks)
Build these 6 skills first — low effort, immediate business impact:

- [ ] `brand-consistency-guide` (Marketing) — Solve brand consistency challenge
- [ ] `prospect-qualification` (Sales) — Qualify leads faster
- [ ] `engagement-letter-generator` (Compliance) — Generate compliant letters
- [ ] `compliance-calendar` (Compliance) — Never miss a deadline
- [ ] `engagement-budget-calculator` (Finance) — Break down engagement costs
- [ ] `client-onboarding-guide` (Client Services) — Standardize onboarding

**Time required:** ~4-5 hours total (45-60 min per skill)

### Phase 2: Revenue & Operations (4-6 weeks)
Build 12 more skills for significant business impact

### Phase 3: Compliance & Risk (6-8 weeks)
Build 10 skills for strategic risk mitigation

### Phase 4: Advanced (Ongoing)
Build 8 advanced skills for long-term advantage

**Total: 36 skills across 4 phases over ~20-25 weeks**

---

## 🚀 Getting Started in 5 Steps

### Step 1: Read the Roadmap (5 min)
Open [SKILLS_ROADMAP.md](SKILLS_ROADMAP.md) and understand:
- All 36 skills across 9 business functions
- Priority order (Phase 1-4)
- Expected outcomes

### Step 2: Complete Company Context (30-60 min) ⚠️
**IMPORTANT:** Fill in [docs/finanshels-context.md](docs/finanshels-context.md) with:
- Your services offered
- Brand voice & tone examples
- Team structure
- Key metrics
- Tools you use
- Client FAQs

*This is crucial for skills to be Finanshels-specific, not generic.*

### Step 3: Choose Your First Skill (2 min)
Pick ONE Phase 1 skill from the list above. Start with:
- `brand-consistency-guide` — Most impactful for "consistency" challenge
- OR `prospect-qualification` — Quick sales win

### Step 4: Create the Skill Folder (2 min)
```bash
cd /Users/themeetpatel/My\ brain/Finanshels

# Example for brand-consistency-guide
mkdir -p skills/marketing-growth/brand-consistency-guide
```

### Step 5: Create the SKILL.md File (45-60 min)
1. Read [docs/SKILL_CREATION_GUIDE.md](docs/SKILL_CREATION_GUIDE.md)
2. Copy [SKILL_TEMPLATE.md](SKILL_TEMPLATE.md) to your new folder as `SKILL.md`
3. Fill it in following the guide
4. Create `examples.md` with example prompts

---

## 📋 Checklist Before You Start

- [ ] You've read [SKILLS_ROADMAP.md](SKILLS_ROADMAP.md)
- [ ] You've reviewed [FILE_MANIFEST.md](FILE_MANIFEST.md)
- [ ] You've looked at [SKILL_TEMPLATE.md](SKILL_TEMPLATE.md)
- [ ] You have access to [docs/SKILL_CREATION_GUIDE.md](docs/SKILL_CREATION_GUIDE.md)
- [ ] You're ready to fill in [docs/finanshels-context.md](docs/finanshels-context.md)
- [ ] You've chosen your first Phase 1 skill

**If all checked:** You're ready to start building!

---

## 🔍 File Organization

Here's where everything is:

```
/Users/themeetpatel/My brain/Finanshels/
│
├── README_QUICKSTART.md ................. This file (START HERE)
├── SKILLS_ROADMAP.md ................... Full roadmap (36 skills)
├── FILE_MANIFEST.md .................... Directory structure
├── SKILL_TEMPLATE.md ................... Master template
│
├── docs/
│   ├── SKILL_CREATION_GUIDE.md ......... How-to guide
│   ├── finanshels-context.md .......... Company context (FILL THIS IN!)
│   └── MASTER_CHECKLIST.md ........... Progress tracker
│
└── skills/ (empty until you start creating)
    ├── marketing-growth/
    │   └── brand-consistency-guide/ (you'll create these)
    ├── sales-bd/
    ├── compliance-risk/
    ├── finance-operations/
    └── ... (9 categories total)
```

---

## 💡 Pro Tips

### Tip 1: Fill in Company Context First
The skills will be generic without this. Spend 30-60 min filling in [docs/finanshels-context.md](docs/finanshels-context.md) before creating any skills.

### Tip 2: Do Phase 1 in Parallel
Don't build skills sequentially. Pick 2-3 Phase 1 skills and have different team members build them in parallel.

Example:
- Person A: `brand-consistency-guide`
- Person B: `prospect-qualification`
- Person C: `client-onboarding-guide`

This completes Phase 1 in ~2 weeks instead of 3.

### Tip 3: Test as You Go
Don't save all testing for the end. After completing a SKILL.md:
1. Try one of your example prompts with Claude
2. Check if the output matches your quality checklist
3. Adjust the skill if needed

### Tip 4: Use Your Actual Workflows
The best skills come from documenting YOUR actual processes:
- How do you really qualify prospects?
- What's the exact sequence of your onboarding?
- What questions DO clients ask most?

Don't make it generic. Make it Finanshels-specific.

### Tip 5: Version Control
If you use git, commit each completed skill:
```bash
git add skills/marketing-growth/brand-consistency-guide/
git commit -m "feat: add brand-consistency-guide skill"
```

---

## ❓ FAQ

**Q: How long does it take to build one skill?**
A: 45-60 minutes if you follow the template and have context filled in.

**Q: Can multiple people build skills in parallel?**
A: Yes! Each skill is independent. Assign Phase 1 skills to different people.

**Q: What if I don't know how to fill in a section?**
A: Look at the examples in [SKILL_TEMPLATE.md](SKILL_TEMPLATE.md). Each section has an example.

**Q: Can I skip Phase 1 and go straight to Phase 2?**
A: Possible, but not recommended. Phase 1 skills solve immediate problems and help you establish the pattern.

**Q: What if I need to change a skill after it's done?**
A: Track versions in [docs/MASTER_CHECKLIST.md](docs/MASTER_CHECKLIST.md). Update the SKILL.md and bump the version number.

**Q: Where do I store example prompts?**
A: Create `examples.md` in the same folder as SKILL.md. See Phase 1 structure.

**Q: How do I share skills with the team?**
A: Once complete, the skill folder goes into your team's Claude Profiles or shared documentation.

---

## 🎓 Learning Resources

**Before you create your first skill, read these in order:**

1. **5 min:** [SKILLS_ROADMAP.md](SKILLS_ROADMAP.md) — Understand the full landscape
2. **10 min:** [SKILL_TEMPLATE.md](SKILL_TEMPLATE.md) — See the template
3. **15 min:** [docs/SKILL_CREATION_GUIDE.md](docs/SKILL_CREATION_GUIDE.md) — Learn the process
4. **30-60 min:** Fill in [docs/finanshels-context.md](docs/finanshels-context.md)
5. **45-60 min:** Build your first skill using the template

**Total: ~2 hours before you're fully ready.**

---

## 🚀 Next Action: Right Now

1. **Open [SKILLS_ROADMAP.md](SKILLS_ROADMAP.md)** and skim it (5 min)
2. **Pick your first Phase 1 skill** from the list (2 min)
3. **Create the folder** for that skill (2 min)
4. **Read [docs/SKILL_CREATION_GUIDE.md](docs/SKILL_CREATION_GUIDE.md)** (15 min)
5. **Start filling in the SKILL.md** using the template (45-60 min)

**Total: ~1.5-2 hours to complete your first skill.**

---

## 📞 Support

**If you get stuck:**

1. **Re-read the relevant section** in [docs/SKILL_CREATION_GUIDE.md](docs/SKILL_CREATION_GUIDE.md)
2. **Look at an example** in [SKILL_TEMPLATE.md](SKILL_TEMPLATE.md)
3. **Check MASTER_CHECKLIST.md** to see if others have completed similar skills
4. **Ask:** What's the one thing preventing me from finishing this skill?

---

## 📊 Success Metrics

Once you've built a few skills, measure:

- **Adoption:** Are team members actually using the skills?
- **Time saved:** How much time do skills save per week?
- **Quality:** Do outputs meet the quality checklist?
- **Consistency:** Do outputs reflect Finanshels brand consistently?

Track these metrics in [docs/MASTER_CHECKLIST.md](docs/MASTER_CHECKLIST.md) to improve over time.

---

## 🎯 Your Mission

**Build 36 Claude skills that:**
- ✅ Solve real Finanshels problems
- ✅ Reflect your brand voice & processes
- ✅ Empower every team member
- ✅ Save time and increase quality
- ✅ Create competitive advantage

**Starting point:** Pick ONE Phase 1 skill and start building today.

**You've got this! 💪**

---

**Last updated:** May 18, 2026  
**Total skills to build:** 36  
**Estimated total time:** 20-25 weeks  
**Ready to start?** Open [SKILLS_ROADMAP.md](SKILLS_ROADMAP.md) now!
