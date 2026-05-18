---
name: tax-law-monitor
description: Use when a Finanshels team member needs to process FTA or UAE Ministry of Finance announcements, new decisions, or regulatory updates into a structured internal compliance bulletin. Triggers include: new Cabinet Decisions, FTA public clarifications, EmaraTax system notices, ministerial circulars, or a scheduled weekly compliance review. Produces a formatted bulletin summarising what changed, who is affected (by entity type and revenue tier), and concrete action items for the Finanshels team.
---

# Tax Law Monitor

Converts FTA and UAE Ministry of Finance updates into a structured weekly internal compliance bulletin — summarising changes, client impact, and required actions.

## When to use

- A new Cabinet Decision or Federal Decree-Law is published affecting CT or VAT
- The FTA issues a public clarification, guide update, or EmaraTax notice
- A Ministerial Decision amending CT or VAT regulations is released
- Preparing the weekly compliance bulletin sent to the Finanshels internal team
- A client asks "did anything change recently?" and you need a verified summary
- Onboarding a new team member who needs a regulatory catch-up

## Inputs needed

**Required**
- Source material: paste the full text, a URL, or a summary of the FTA/MoF notice/decision
- Effective date of the change (or "unknown — check FTA")
- Your name / preparer initials (for the bulletin footer)

**Optional**
- Previous bulletin to check for overlap / prior coverage of the same topic
- List of current Finanshels clients affected (entity types, revenue range) — used to personalise impact section
- Urgency flag: `urgent` (same-day action needed) | `standard` (next weekly bulletin)

## Workflow

1. **Read the source material carefully**
   Parse the full text of the FTA notice, Cabinet Decision, or Ministerial Decision. Identify:
   - The governing law being amended (e.g. Federal Decree-Law No. 47/2022 for CT; No. 8/2017 for VAT)
   - The specific article(s) or provision(s) changed
   - The effective date (financial-year start, calendar date, or "upon publication")
   - Whether the change is retrospective

2. **Classify the update**
   Tag the update with one or more categories:
   - `CT-rate` | `CT-registration` | `CT-return` | `CT-freezone` | `CT-TP` | `CT-SBR`
   - `VAT-rate` | `VAT-registration` | `VAT-return` | `VAT-exemption` | `VAT-zero-rating`
   - `AML-CFT` | `UBO` | `EmaraTax-system` | `Penalty` | `General`

3. **Assess client impact**
   Map the change to Finanshels client segments (cross-reference `../_shared/finanshels-context.md`):
   - Mainland LLC (any revenue)
   - Free Zone entity (QFZP eligible vs. non-qualifying)
   - Small Business Relief clients (revenue ≤ AED 3M, periods ending on/before 31 Dec 2026)
   - Natural persons with business turnover > AED 1M
   - Large MNEs subject to DMTT (consolidated revenue ≥ EUR 750M)
   Clearly state "Not affected" for segments where the change has no bearing.

4. **Extract action items**
   For each affected segment, list:
   - What the client must do (register, amend return, update TP documentation, etc.)
   - Deadline (cite the FTA source; state "confirm with FTA" if unclear)
   - Who at Finanshels owns the action (CT team / VAT team / bookkeeping / compliance officer)
   - Priority: HIGH (< 30 days) / MEDIUM (30–90 days) / LOW (> 90 days or advisory only)

5. **Draft the bulletin**
   Use the template at `./templates/bulletin-template.md`. Fill every section. Do not leave placeholders unfilled — if data is unavailable, write "Not yet confirmed — verify with FTA."

6. **Add a plain-English client communication snippet**
   Write 3–5 sentences a Finanshels account manager can paste into a client WhatsApp or email. No jargon. Friendly but precise.

7. **Quality-check before finalising**
   Run through the Quality checklist below. Confirm no UAE-specific rates or deadlines are quoted from memory — every figure must trace to the shared context file or the source material provided.

8. **Save or share**
   Name the file: `bulletin-YYYY-MM-DD-<topic-slug>.md` (e.g. `bulletin-2026-05-18-ct-sbr-extension.md`)

## Output format

```
# Finanshels Compliance Bulletin
**Date:** YYYY-MM-DD
**Prepared by:** [Name / Initials]
**Urgency:** Urgent | Standard
**Categories:** [tags from step 2]

---

## What Changed
[1–3 paragraph plain-English summary of the change. Cite the exact Decision/Decree number and article.]

## Effective Date
[Date or "Confirm with FTA"]

## Who Is Affected

| Client Segment | Affected? | Why |
|---------------|-----------|-----|
| Mainland LLC (any revenue) | Yes / No | ... |
| Free Zone (QFZP) | Yes / No | ... |
| Free Zone (non-QFZP) | Yes / No | ... |
| SBR clients (≤ AED 3M) | Yes / No | ... |
| Natural persons (> AED 1M turnover) | Yes / No | ... |
| Large MNE / DMTT | Yes / No | ... |

## Action Items

| # | Action | Owner | Deadline | Priority |
|---|--------|-------|----------|----------|
| 1 | ... | CT Team | DD-MMM-YYYY | HIGH |
| 2 | ... | VAT Team | ... | ... |

## Client Communication Snippet
[3–5 sentences for account managers]

## Source Links
- [Decision/Decree title](URL or "FTA website — search [reference]")

---
*This bulletin is an internal Finanshels work product. Verify all rates and deadlines
against current FTA guidance before advising clients.*
```

## Quality checklist

- [ ] Every rate and threshold cited traces to the shared context file or the source document
- [ ] Effective date stated (not assumed)
- [ ] All six client segments addressed (even if "Not affected")
- [ ] Action items have an owner and a deadline
- [ ] Client communication snippet is jargon-free and ≤ 5 sentences
- [ ] Bulletin file named with the date and topic slug
- [ ] No reference to IRS, US states, or CPE
- [ ] No invented figures — "confirm with FTA" used when uncertain

## Examples

**Example 1 — CT Small Business Relief extension**
> "The FTA just published a Ministerial Decision extending Small Business Relief to tax periods ending on or before 31 Dec 2027. Prepare this week's bulletin."

**Example 2 — New VAT public clarification on crypto**
> "FTA released VATP031 clarifying VAT treatment of crypto-asset transfers. Our clients include two Dubai mainland fintech startups. Generate a bulletin and flag which of our clients need a VAT position review."

**Example 3 — EmaraTax system update**
> "EmaraTax sent a notice that CT return submission for FY2024 entities closes 30 Sep 2025. Some clients haven't filed. Prepare an urgent bulletin with a list of required actions."

## Guardrails

- Output is an internal Finanshels work product; it must be reviewed by a qualified team member before being shared with clients or acted on.
- Never invent rates, deadlines, or thresholds. If the source material does not confirm a figure, write "verify with FTA."
- This skill applies to UAE jurisdiction only. Do not reference non-UAE tax regimes.
- All client information used in inputs is confidential; do not include real client names in bulletin examples or templates.

## Reference

See `../_shared/finanshels-context.md` for UAE tax facts, rates, and deadlines.
