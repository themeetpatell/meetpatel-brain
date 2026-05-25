---
name: content-planner-tax
description: Use when planning Finanshels content for a quarter or a full year — blog articles, LinkedIn posts, email newsletters, or social campaigns. Triggers include "plan our Q3 content", "what should we write about this quarter", "build a content calendar", or "map our posts to tax deadlines". Produces a full editorial calendar with topic clusters tied to the UAE compliance cycle (CT registration windows, VAT quarters, year-end) and Finanshels' audience priorities.
---

# Content Planner — UAE Tax & Accounting

Plans a quarterly (or annual) editorial calendar mapped to the UAE compliance cycle. Every topic cluster serves a real client question or deadline moment — not generic accounting content.

## When to use

- Quarterly content planning session (marketing or founder-driven)
- You need a structured calendar to hand to a content writer or social media manager
- Upcoming UAE compliance deadlines (CT return window, VAT quarter close, year-end) need coverage
- You want to build authority around a specific topic (e.g., free zone CT, VAT for e-commerce)
- A regulatory update (FTA cabinet decision, new EmaraTax feature) creates a content window
- The team wants to align social, email, and blog around the same theme each month

## Inputs needed

**Required**
- Target quarter (e.g., Q3 2026: July–September) or full financial year

**Optional**
- Primary content channels: LinkedIn / blog / email newsletter / Instagram / all
- Audience focus: founders (simplified) / finance leads (technical depth) / both
- Topics to prioritise or avoid (e.g., "we want more CT content", "skip payroll this quarter")
- Recent content already published (to avoid repetition)
- Any upcoming Finanshels product/service launches to tie in
- Frequency target (e.g., 3 posts/week on LinkedIn, 2 blog articles/month)

## Workflow

1. **Map the UAE compliance calendar for the quarter**
   Pull the relevant FTA deadlines from `../_shared/finanshels-context.md` and the UAE compliance cycle:
   - VAT return due dates: 28th of the month following each quarter-end (Q1=28 Apr, Q2=28 Jul, Q3=28 Oct, Q4=28 Jan)
   - CT return & payment: within 9 months of financial year-end (most common: 31 Dec year-end → 30 Sep deadline)
   - CT registration windows: tied to licence-issuance month (FTA publishes specific dates)
   - Year-end accounting close: typically Jan–Mar for 31 Dec year-ends
   - WPS payroll cycle: monthly
   - UBO register updates: annually or on change
   Note: [VERIFY all deadlines against current FTA guidance before publishing]

2. **Identify the three content jobs for the quarter**
   Every quarter has a mix:
   - **Deadline-driven:** Content that helps clients prepare for an imminent filing (VAT return reminder, CT payment checklist)
   - **Education:** Content that builds understanding and authority (explainer on CT for free zones, VAT on exports, what "taxable person" means)
   - **Lead generation / brand:** Content that attracts new clients (common mistakes UAE startups make, the true cost of non-compliance, why outsourced bookkeeping beats in-house at AED 5M revenue)

3. **Define topic clusters**
   Group content into 3–4 clusters for the quarter. Each cluster has a central theme and 4–8 pieces of content (LinkedIn posts, one blog article, one email newsletter topic). Clusters should map to:
   - A compliance deadline approaching this quarter
   - An audience pain point (e.g., "I don't know if I qualify for Small Business Relief")
   - A Finanshels service to highlight

4. **Build the weekly content calendar**
   Assign each piece to a specific week. For each content piece specify:
   - Week / date window
   - Channel (LinkedIn / blog / email / Instagram)
   - Format (short post / long-form article / carousel / infographic caption / newsletter section)
   - Topic (specific, not generic: "Why your VAT return due date might not be 28 July" not just "VAT article")
   - Audience (founder / finance lead / general)
   - Content job (deadline-driven / education / lead gen)
   - Linked service (VAT, CT, bookkeeping, payroll, etc.)
   - Notes / data hook (regulation, stat, or real scenario to anchor the piece)

5. **Identify 3 anchor pieces**
   Pick 3 cornerstone articles or posts for the quarter — high-effort, high-value content that can be repurposed into multiple shorter formats. These anchor the cluster.

6. **Repurposing map**
   For each anchor piece, show how it breaks down into smaller content:
   - 1 blog article → 3–4 LinkedIn posts + 1 email newsletter section + 1 Instagram carousel
   - 1 regulatory explainer → FAQ doc + 1 LinkedIn Q&A post + 1 email subject-line test

7. **Output the calendar** using the template at `templates/content-calendar.md`

## Output format

```
## Finanshels Content Calendar — [Quarter] [Year]

### Compliance anchor dates this quarter
[List of FTA deadlines relevant to this quarter — all marked VERIFY]

---

### Topic Clusters

#### Cluster 1: [Theme]
[2-sentence brief]
Linked service: [Service]
Audience: [Founder / Finance lead / Both]

**Anchor piece:** [Title and format]
**Supporting pieces:** [List 4–6 pieces with channel and format]

#### Cluster 2: [Theme]
...

#### Cluster 3: [Theme]
...

---

### Weekly Calendar

| Week | Date | Channel | Format | Topic | Audience | Job | Service |
|------|------|---------|--------|-------|----------|-----|---------|
| W1   | ...  | LinkedIn | Post | ... | Founder | Education | CT |
...

---

### Repurposing Map
[Anchor pieces → derivative formats]

---

### Notes for content writers
[Any specific instructions: brand voice reminder, regulation citations to include, CTAs to use]
```

## Quality checklist

- [ ] Every content piece is mapped to a specific week — no floating ideas
- [ ] At least one deadline-driven cluster per quarter
- [ ] All FTA deadline dates are marked `[VERIFY]` or confirmed against current FTA guidance
- [ ] Each topic is specific enough for a writer to start immediately (not just "CT article")
- [ ] No piece references non-UAE tax systems
- [ ] Brand voice guidance from `../brand-consistency-guide/brand-guidelines.md` referenced in writer notes
- [ ] At least 3 pieces target founders (simplified language)
- [ ] At least 2 pieces target finance leads (technical depth)
- [ ] Repurposing map covers at least 2 anchor pieces
- [ ] Calendar frequency is realistic for the team (don't over-commit)

## Examples

**Example 1 — Q3 planning for CT return season**
> "Plan our Q3 2026 content calendar. We want to focus on LinkedIn and our blog. Our clients are mostly Dubai mainland SMEs with 31 December year-ends, so CT returns are due 30 September. We publish about 3 LinkedIn posts a week and one blog article per fortnight."

**Example 2 — Q1 planning with VAT emphasis**
> "Build a content calendar for Q1 2026 (January–March). We want to focus on VAT because January starts a new VAT quarter and many of our free zone clients are confused about what's in and out of scope. Mix of founders and finance managers."

**Example 3 — Full year overview**
> "Give me a high-level annual content plan for 2026 mapped to the UAE compliance calendar. We serve Abu Dhabi and Dubai mainland companies, AED 2M–20M revenue. Just the cluster themes and anchor pieces for each quarter — we'll drill down quarterly."

## Guardrails

- All deadline dates are illustrative; verify against current FTA and EmaraTax guidance before publishing
- Content is editorial planning, not legal or tax advice — final content must be reviewed by a qualified Finanshels team member
- Do not include real client names, financials, or case details in editorial briefs
- UAE context only — do not reference non-UAE tax deadlines or systems
- If referencing specific regulatory developments (new Cabinet Decision, FTA public consultation), note the source and confirm it is current

## Reference

See `../_shared/finanshels-context.md` for UAE tax facts, rates, and deadlines.

See the `master-brand` skill for Finanshels positioning, voice, taglines, and proof points — every planned piece must lead WHY → WHAT and anchor a proof point (7,000+ businesses / 150+ accountants).
