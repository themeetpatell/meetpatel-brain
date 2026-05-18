---
name: prospect-qualification
description: Use when a Finanshels sales or business development team member needs to evaluate an inbound lead and decide how to prioritize and respond. Triggers include: a new enquiry via website, referral, or event; a discovery call debrief; reviewing a list of leads before outreach. Takes lead information (company type, revenue, compliance status, pain points) and produces a scored lead profile with ICP fit rating, recommended service bundles, and concrete next-step instructions.
---

# Prospect Qualification

Scores inbound leads against Finanshels' Ideal Client Profile and produces a prioritized action plan for the sales team.

## When to use

- A new enquiry comes in and you need to decide: book a call now, nurture, or decline
- Post-discovery-call debrief: capture what you learned and get a structured score
- Reviewing a batch of leads from an event, campaign, or referral list
- Account manager deciding whether to upsell an existing client into new services
- Weekly pipeline review: re-score stale leads with new information

## Inputs needed

**Required**
- Company name (or reference code if anonymising)
- UAE entity type: mainland / free zone (which free zone) / offshore / not yet incorporated
- Estimated annual revenue (AED) or revenue band: <500K / 500K–2M / 2M–10M / 10M–50M / >50M
- Industry / principal activity
- Current compliance status (what they have, what they're missing — as much as known)
- Primary pain point or reason for enquiry

**Optional**
- Number of employees
- Enquiry source (website, referral, event, cold outreach)
- Current accountant or bookkeeper (if any)
- Decision-maker name and title
- Urgency signal (e.g. "CT deadline in 2 months", "just got a VAT penalty notice")
- Budget indication

## Workflow

### Step 1 — Capture the lead profile
Fill in every known field. Mark unknown fields explicitly — gaps are scored as neutral, not positive. Do not guess at revenue or compliance status; if uncertain, note it and flag for follow-up.

### Step 2 — Score against ICP dimensions
Score each dimension 1–5 using the rubrics below. Sum the scores. Divide by maximum (25) to get an ICP fit percentage.

**Dimension 1: Revenue band fit (max 5 points)**
| Revenue | Score |
|---|---|
| AED 500K – AED 10M (sweet spot) | 5 |
| AED 10M – AED 50M | 4 |
| AED 0 – AED 500K | 3 |
| > AED 50M (likely too complex or price-sensitive) | 2 |
| Not UAE-revenue / unclear | 1 |

**Dimension 2: Entity type fit (max 5 points)**
| Entity type | Score |
|---|---|
| UAE mainland (DED licence) | 5 |
| UAE free zone — mid-tier (DMCC, JAFZA, RAKEZ, etc.) | 5 |
| UAE free zone — premium (DIFC, ADGM) | 4 (higher complexity, good fit if CT/advisory heavy) |
| Not yet incorporated — needs company formation | 4 (formation lead, upsell potential) |
| Offshore / holding company only | 2 |
| Non-UAE entity | 1 |

**Dimension 3: Compliance urgency (max 5 points)**
| Urgency signal | Score |
|---|---|
| CT not registered / deadline imminent | 5 |
| VAT non-compliant / penalty received | 5 |
| First CT return due within 3 months | 5 |
| Behind on bookkeeping / no clean financials | 4 |
| Currently compliant but looking to optimise | 3 |
| No compliance gaps identified | 2 |
| Compliance handled in-house, exploring only | 1 |

**Dimension 4: Service bundle potential (max 5 points)**
*How many Finanshels service lines are relevant?*
| Potential service lines identified | Score |
|---|---|
| 4 or more (e.g. bookkeeping + CT + VAT + payroll) | 5 |
| 3 service lines | 4 |
| 2 service lines | 3 |
| 1 service line | 2 |
| Unclear / single ad-hoc task only | 1 |

**Dimension 5: Decision-maker access & buying intent (max 5 points)**
| Signal | Score |
|---|---|
| Founder / CFO / finance director contacted directly, explicit ask for proposal | 5 |
| Founder / CFO enquired, no explicit ask yet | 4 |
| Finance manager / office manager, founder aware | 3 |
| Gatekeeper only, DM not yet identified | 2 |
| Unknown or passive enquiry (e.g. downloaded a guide) | 1 |

### Step 3 — Classify the lead
| ICP Fit % | Tier | Action |
|---|---|---|
| 80–100% | Tier 1 — Hot | Respond within 2 hours; book discovery call same day; assign senior account manager |
| 60–79% | Tier 2 — Warm | Respond within 24 hours; book discovery call this week; standard account manager |
| 40–59% | Tier 3 — Nurture | Respond within 48 hours; add to nurture sequence; qualify further before call |
| < 40% | Tier 4 — Low fit | Polite response; refer out if possible; do not allocate sales time |

### Step 4 — Identify recommended service bundle
Based on the lead profile, select the relevant Finanshels service bundles:

**Starter bundle** (typically revenue < AED 2M, early-stage):
- Bookkeeping (IFRS for SMEs)
- CT registration + annual CT return
- VAT registration + quarterly VAT return

**Growth bundle** (typically revenue AED 2M–10M):
- All Starter bundle items
- Monthly management accounts
- Payroll & WPS
- Audit-ready financials (annual)

**Advisory bundle** (typically free zone, CT-complex, or multi-entity):
- All Growth bundle items
- CT advisory (QFZP review, transfer pricing)
- Outsourced CFO / financial controller
- Audit support

**Compliance catch-up** (urgency-driven):
- Back-period bookkeeping
- Voluntary disclosure (VAT or CT)
- Penalty mitigation support
- CT registration (if outstanding)

### Step 5 — Identify objections or risks
Flag any signals that suggest the deal may stall:
- Price sensitivity signals ("just looking for someone cheap")
- Incumbent accountant they seem happy with
- Very early stage with no revenue yet
- Offshore / non-UAE entity with no UAE compliance needs
- Overly complex structure that exceeds Finanshels' current scope (e.g. Big 4-level TP work)
- Signs of existing FTA dispute that requires specialist tax litigation

### Step 6 — Write up the lead score card
Use the output format below. This is what goes into the CRM and what is shared in pipeline review.

## Output format

```
LEAD SCORE CARD — [Company / Reference]
Date scored: [Date] | Scored by: [Team member]

LEAD PROFILE
- Entity type: [Mainland / Free zone / TBC]
- Revenue band: AED [X]
- Industry: [X]
- Pain point: [X]
- Enquiry source: [X]
- Decision-maker: [Name, Title / Unknown]

ICP SCORE

| Dimension | Score (/5) | Notes |
|---|---|---|
| Revenue band fit | /5 | |
| Entity type fit | /5 | |
| Compliance urgency | /5 | |
| Service bundle potential | /5 | |
| Decision-maker access & intent | /5 | |
| TOTAL | /25 | ICP Fit: __% |

TIER: [Tier 1 Hot / Tier 2 Warm / Tier 3 Nurture / Tier 4 Low fit]

RECOMMENDED SERVICE BUNDLE
- [Service 1]
- [Service 2]
- [Service 3]

ESTIMATED MONTHLY RETAINER RANGE
[Low: AED X | High: AED X — internal use only, do not share with prospect]

RISKS / OBJECTIONS TO WATCH
- [Risk 1]
- [Risk 2]

NEXT STEPS
- Immediate action: [What to do in the next 2 hours / 24 hours]
- Discovery call agenda focus: [Top 2-3 questions to ask]
- Proposal needed? [Yes — use proposal-generator skill / No / After discovery call]
- Owner: [Team member name]
- Follow-up date: [Date]

NOTES
[Any free-text context that does not fit the above]
```

## Quality checklist

- [ ] All five ICP dimensions scored (not left blank)
- [ ] Total score and ICP fit % calculated correctly
- [ ] Tier assigned matches the ICP fit % band
- [ ] Recommended service bundle is specific (not "all services")
- [ ] Next steps include a named owner and a follow-up date
- [ ] Risks / objections section is not empty (at least one flag or "none identified")
- [ ] No real client data used in examples or scores
- [ ] Revenue and entity type are UAE-specific (not US / UK / EU framing)
- [ ] Discovery call agenda questions are tailored to the prospect's gap, not generic

## Examples

**Example 1**
"We just got an enquiry from a Dubai mainland trading LLC, AED 4M revenue, 12 employees. They got a VAT penalty notice last week and their bookkeeper quit. Founder emailed us directly asking for a proposal. Score them."

Expected output: Likely Tier 1 (High urgency + right revenue band + direct DM contact). Recommended bundle: Compliance catch-up + Growth bundle. Discovery call focus: scope of VAT gap, CT registration status, back-period bookkeeping needed.

**Example 2**
"A DMCC free zone SaaS company, AED 2.8M revenue, asked about CT on our website. They haven't registered yet. Finance manager filled the form; founder not involved yet."

Expected output: Likely Tier 2 (Warm — good fit but DM not engaged). Recommended bundle: Starter + CT Advisory (QFZP review). Risk: need founder buy-in before deal closes.

**Example 3**
"A pre-revenue startup, 2 founders, not yet incorporated, asking about setting up in a free zone and what accounting they'll need."

Expected output: Likely Tier 3 (Nurture — no revenue yet, formation lead, good upsell potential long-term). Recommended bundle: Company formation intro → Starter bundle once incorporated. Risk: no near-term revenue from this lead; add to nurture sequence.

## Guardrails

- UAE jurisdiction only. Do not reference UK/US/EU accounting or tax requirements.
- Lead score cards are internal Finanshels documents — do not share the score or tier classification directly with the prospect.
- Estimated retainer ranges are for internal pipeline planning only.
- Do not include real prospect names, email addresses, or financial data in examples.
- If a prospect appears to have serious FTA disputes or requires litigation support, flag this as out of scope and refer to a specialist.
- Output is a professional work product to be reviewed by a Finanshels team lead before informing commercial decisions.

## Reference

See ../_shared/finanshels-context.md for UAE tax facts, rates, and deadlines.
