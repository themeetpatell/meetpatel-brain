---
type: framework
category: ops-execution
source: Gino Wickman (Traction)
status: living
updated: 2026-05-17
tags: [framework, ops, eos, execution]
---

# EOS — Entrepreneurial Operating System

> Six components that turn a chaotic small business into a coherent operating machine. Vision, People, Data, Issues, Process, Traction. EOS works because it's *simple enough that the whole team can hold it*, not because it's clever.

## When to use it
- Any organization 10–250 people that needs operational discipline
- Companies where the founder is the bottleneck
- Teams where weekly meetings feel pointless ("status update theatre")
- Already in use at Finanshels — this framework note is the canonical reference

## The 6 components

### 1. Vision (shared by all)
Captured in the **Vision/Traction Organizer (V/TO)** — a 2-page document covering:
- Core values (3–7)
- Core focus (Why + What you do)
- 10-Year target
- Marketing strategy
- 3-Year picture
- 1-Year plan
- Quarterly Rocks
- Issues list

### 2. People (right people, right seats)
- **People Analyzer:** does each team member embody the core values (above-the-line / below-the-line)
- **GWC seat test:** does the person *Get it, Want it, have the Capacity* to do the role?
- Quarterly assessment, hard conversations when needed

### 3. Data (scorecard)
- Weekly scorecard with 5–15 numbers that predict the business
- *Leading indicators* (predict the future) over *lagging indicators* (describe the past)
- Every metric has an owner. Misses go to the IDS list immediately.

### 4. Issues (IDS — Identify, Discuss, Solve)
- Every issue raised goes on the issues list
- In weekly meetings, top 3 by impact get IDS'd
- Don't discuss without an outcome — IDS means *decide*

### 5. Process (documented, followed)
- Document the core processes (how we sell, how we onboard, how we deliver)
- Train everyone on them
- Follow them — deviations are the issues

### 6. Traction (Rocks + Meeting Pulse)
- **Quarterly Rocks:** 3–7 priorities for the quarter, per leader
- **Weekly L10:** structured 90-min meeting (Segue → Scorecard → Rocks → Headlines → To-dos → IDS → Conclude)
- **Quarterly Pulsing:** review the V/TO, set next quarter's Rocks
- **Annual Planning:** refresh the V/TO, set next year's annual plan

## How to apply

### Finanshels (active EOS adoption)
- **Vision:** V/TO already exists or in draft — confirm and circulate
- **People:** Each CoE team member assessed quarterly on Values + GWC
- **Data:** CoE Scorecard with metrics like: leads triaged, qualified, won, response time avg, filings completed on time, customer satisfaction
- **Issues:** Weekly L10 IDS list owned by Meet
- **Process:** SOPs (use `_AI/Prompts/ops/sop-from-mess.md` template) for lead triage, customer onboarding, monthly close, AML filing
- **Traction:** Quarterly Rocks per CoE function (sales, ops, training, dashboards)

Weekly L10 prep: use `_AI/Prompts/ops/weekly-l10-prep.md`.

### Cross-portfolio
EOS works at Finanshels because the team is real. For solo/pre-team ventures (StartupOS, Biggdate at concept stage), EOS is overkill. *Use OKRs instead* until team >5.

When ventures cross ~10 people, adopt EOS. Use the same playbook across the portfolio to enable Meet to operate as a portfolio CEO without code-switching between operating systems.

## Anti-patterns
- **V/TO without team buy-in.** A V/TO drafted by Meet alone and circulated = decoration. Workshop it with the leadership team.
- **Scorecard with too many metrics.** 5–15 max. More = no scorecard.
- **L10s that skip IDS.** "We didn't get to issues" = meeting failed. IDS is the meeting.
- **Rocks that aren't outcomes.** "Work on sales" is not a Rock. "Hit 50 qualified leads/week by Sept 30" is.
- **People decisions delayed.** EOS makes you confront who's in the wrong seat. The framework only works if you act on the People analyzer.
- **EOS as religion.** It's a tool. Adapt to context. If a specific component isn't serving Finanshels, modify it. Don't dogmatize.

## Where to use this in the vault
- `_AI/Prompts/ops/weekly-l10-prep.md` — L10 meeting prep
- `_AI/Prompts/ops/sop-from-mess.md` — Process documentation
- `_AI/Prompts/ops/quarterly-okr-set.md` — for venues where OKRs > Rocks
- Skill: `finanshels-coe` — operationalizes EOS for Finanshels specifically

## Related frameworks
- [[OKRs]] — alternative to Rocks; OKRs are more PM-friendly, Rocks are more ops-friendly
- [[4DX]] — narrower than EOS but very compatible (4DX focuses on the WIG layer)
- [[RAPID]] — useful inside the IDS process for clean decisions

## Source
- Gino Wickman — *Traction: Get a Grip on Your Business*
- Gino Wickman — *Get a Grip* (companion novel; faster read)
- EOS Worldwide community + EOS Implementer network
