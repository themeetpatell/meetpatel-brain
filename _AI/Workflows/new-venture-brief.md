---
type: workflow
status: living
updated: 2026-05-17
tags: [ai, workflow, venture, brief]
trigger: when-considering-new-venture-or-pivot
duration: 4-6 hours over 2-3 days
---

# Workflow: New Venture Brief

> Before committing real time or money to a new venture (or a meaningful pivot), run this workflow. The output is either a green-light brief or a no-go memo. No "let's just see".

## When to trigger
- Considering starting a new venture
- Considering a major pivot of an existing one (P0 venture re-direction)
- An investor / partner asks "what about doing X"
- A customer signal suggests an adjacent opportunity worth evaluating

## Inputs needed
- The venture idea, in one paragraph
- Who's potentially involved (co-founders, key hires)
- What's the bet — what would need to be true for this to be worth $X-million outcome
- Who would the first paying customer be (real name if possible)

## Steps

### Step 1 — Sharpen the question (30 min, Meet alone)
- Write the venture in 4 forms: 1-sentence, 1-paragraph, 1-page, 5-pages
- If you can't write the 1-sentence version, the idea isn't ready
- Save raw output to `30 Ventures/_Considering/[venture-slug]-raw.md`

### Step 2 — Thesis frame (1 hour, with `_AI/Agents/chief-of-staff`)
Generate a thesis frame:
- **Wave** — what shift makes this possible now that wasn't 5 years ago?
- **Wedge** — what specific first product / first customer / first geo?
- **Moat** — once we win the wedge, what's defensible?
- **Adjacent** — where do we expand after the wedge?
- **Outcome** — what does success look like in 5 years (revenue, exit, category, leverage)?
- **Skill `venture-architect` should be loaded for this step.**

### Step 3 — Market reality (1–2 hours)
- TAM/SAM/wedge bottom-up
- 5–10 competitor scan (use `_AI/Agents/competitive-scout`)
- 5 customer-discovery conversations (real humans — record + transcribe)
- UAE/GCC layer: regulatory, licensing, cultural fit, distribution feasibility
- **Skill `uae-gcc-strategy-intelligence` should be loaded for this step.**

### Step 4 — Premortem (45 min)
- Run `_AI/Agents/premortem.md` on the venture
- Be honest about failure modes
- If 3+ failure modes are high-likelihood × fatal → re-scope or abandon

### Step 5 — Portfolio fit (30 min)
- Does this compound with Finanshels / StartupOS / Biggdate / ZeroHuman?
- Or is this a standalone bet competing for the same Meet-hours?
- If standalone — what's the opportunity cost in current venture progress?

### Step 6 — Resource shape (30 min)
- Capital required to reach next milestone
- Founders / hires required
- Time required from Meet (realistic, not optimistic)
- Compare against what's actually available

### Step 7 — Decision frame (30 min)
Run `_AI/Agents/decision-frame.md` with 3 options:
- A: Build it now (committed)
- B: Park it (write the thesis, don't act, revisit in 90 days)
- C: Pass entirely (explicit kill with reason)

### Step 8 — Brief output
File at `30 Ventures/_Considering/[venture-slug]-BRIEF.md` with:
- Decision: A / B / C
- One-paragraph rationale
- If A: 90-day plan + kill criteria
- If B: review-by date + what would need to change to upgrade to A
- If C: file the thesis to `99 Archive` with a note

## Output of the workflow
- Either: new venture launched with brief committed
- Or: parked venture with explicit review-by date
- Or: killed venture with clean memo

## Quality bar
- The brief must specify a kill condition. No open-ended commitments.
- The market reality step must include at least 3 real customer conversations. Theory alone does not pass.
- The premortem must surface at least one uncomfortable observation.

## Maintenance
- Quarterly: review all "parked" ventures in `30 Ventures/_Considering/`. Upgrade, downgrade, or archive.
- Annually: track outcomes of greenlit ventures vs predicted brief. Calibrate the workflow.
