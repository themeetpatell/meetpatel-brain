---
name: brand-consistency-guide
description: Use when reviewing or rewriting any Finanshels content — client emails, marketing copy, social posts, proposals, internal documents — to ensure it matches the Finanshels brand voice. Triggers include "review this email for brand", "rewrite in our voice", "does this sound like us", or any request to polish or align content. Produces a brand-compliant rewrite plus an itemised checklist of every change made.
---

# Brand Consistency Guide

Reviews and rewrites content so it sounds unmistakably like Finanshels: clear, confident, plain English, helpful, and precise — never alarmist, never jargon-heavy.

## When to use

- A team member drafts a client email and wants a brand check before sending
- Marketing copy (ads, landing pages, brochures) needs a tone pass
- A LinkedIn post or blog article draft needs alignment with Finanshels voice
- Internal documents (SOPs, onboarding guides) need a readable, consistent pass
- Any content that will carry the Finanshels name needs a final polish
- A new hire asks "does this sound like us?"

## Inputs needed

**Required**
- The raw content to review (paste in full or attach file path)
- Content type: email / social post / blog article / proposal / internal doc / other

**Optional**
- Audience: client-facing vs. internal vs. public marketing
- Target reader persona (e.g., "founder of a Dubai mainland trading company", "CFO of a free zone tech startup")
- Any specific concerns ("I think it sounds too formal" / "check if we're too salesy")
- Word count target or length constraints

## Workflow

1. **Classify the content**
   - Identify content type, target audience, and communication goal
   - Note the approximate reading level and formality the original uses

2. **Brand voice audit against Finanshels standards**
   The `master-brand` skill is the authority — load it first. Then run through every sentence and flag issues against `master-brand`, `brand-guidelines.md`, and `voice-tone.md`:
   - Content opens with WHAT we do instead of WHY it matters (master-brand requires WHY → WHAT order for client-facing and public content)
   - Missing proof point — public/marketing content should anchor to "7,000+ businesses served" or "150+ qualified accountants"
   - Jargon used without a short explanation (e.g., "QFZP", "taxable person", "input tax credit")
   - Alarmist or anxiety-inducing language ("you will be penalised", "urgent compliance failure")
   - Passive constructions that drain authority ("it should be noted that…")
   - Vague hedging that erodes trust ("might", "possibly", "you may or may not need to")
   - Missing empathy — pure regulatory recitation with no acknowledgement of client context
   - Inconsistent use of we/our (Finanshels writes in first-person plural: "we", "our team")
   - UK English spelling (Finanshels operates in the UAE; use British English conventions: "organisation", "recognised", "licence" noun / "license" verb)
   - Overly salesy language ("amazing", "best-in-class", "revolutionary")
   - Any reference to non-UAE jurisdictions (IRS, US state tax, CPE credits) that have crept in

3. **UAE-accuracy check**
   - Flag any tax figures, thresholds, or deadlines mentioned in the content
   - Cross-reference against `../_shared/finanshels-context.md`
   - If a figure cannot be verified, insert a `[VERIFY against current FTA guidance]` placeholder — do not silently leave an unverified number

4. **Produce the rewrite**
   Apply the Finanshels voice characteristics from `voice-tone.md`:
   - Lead with clarity: put the point first, explanation second
   - Use short sentences for complex regulatory ideas
   - Replace jargon with plain English, or explain jargon in parentheses on first use
   - Convert alarmist language to factual, solution-oriented phrasing
   - Ensure every paragraph either informs, reassures, or prompts a clear action
   - End client-facing content with a clear next step

5. **Produce the change log**
   After the rewrite, list every change made with:
   - Original phrase → Revised phrase
   - Reason (one of: Voice / Accuracy / Clarity / Empathy / UAE-spelling / CTA)

6. **Final quality pass**
   Run through the quality checklist below before delivering

## Output format

```
## Brand Review: [Content Type] — [Date]

### Audience: [who this is for]
### Goal: [what the content needs to do]

---

## Rewritten Content

[Full rewritten version, ready to use]

---

## Change Log

| # | Original | Revised | Reason |
|---|----------|---------|--------|
| 1 | "You must urgently file..." | "To stay on track, your VAT return is due by..." | Voice / Alarmist → factual |
| 2 | "QFZP entity" | "Qualifying Free Zone company (QFZP)" | Clarity / Jargon defined on first use |
| ... | | | |

---

## Summary
[2–3 sentences: overall brand alignment rating (Strong / Needs work / Major rework), biggest patterns fixed, any items flagged for the team to verify]
```

## Quality checklist

- [ ] No unexplained acronyms (FTA, QFZP, CT, VAT are acceptable if audience is familiar; always define on first use for general audiences)
- [ ] No alarmist language — regulatory facts stated calmly and with a solution
- [ ] First-person plural ("we", "our") used consistently
- [ ] Plain English: a smart non-accountant can follow the content
- [ ] All UAE tax figures carry a `[VERIFY]` note or were confirmed against the shared context
- [ ] No reference to non-UAE tax systems (IRS, HMRC, etc.) unless explicitly comparing
- [ ] Clear call-to-action or next step in every client-facing piece
- [ ] British English spelling throughout
- [ ] No superlatives or empty marketing claims
- [ ] Content length is appropriate for the medium (social post ≤ 300 words, email ≤ 400 words, article ≥ 600 words)
- [ ] Change log is complete and every change has a reason

## Examples

**Example 1 — Client email**
> "Here's an email we drafted telling a client their VAT registration has been approved. It feels a bit cold and uses a lot of acronyms. Can you rewrite it in our voice?"
> Client: Dubai mainland trading LLC, AED 4M annual revenue, newly VAT-registered.

**Example 2 — LinkedIn post**
> "I wrote a quick LinkedIn post about the UAE Corporate Tax deadline for free zone companies. Can you check it sounds like Finanshels and isn't too scary for founders?"
> Context: post targeting free zone startup founders unfamiliar with CT.

**Example 3 — Proposal section**
> "This is the 'Our Services' section of a new bookkeeping proposal. The client is a Sharjah mainland retailer with AED 8M turnover. Does the tone match our brand?"

## Guardrails

- This skill produces professional work product; a qualified Finanshels team member must review before content reaches clients
- Never include real client names, TRN numbers, or financial figures in skill outputs
- Tax figures and deadlines must be verified against current FTA guidance — this skill flags but does not guarantee accuracy
- This skill operates in the UAE context only; do not introduce non-UAE regulatory references
- If content contains what appears to be confidential client data, note this and redact before sharing the rewrite

## Reference

See `../_shared/finanshels-context.md` for UAE tax facts, rates, and deadlines.

See the `master-brand` skill — the single source of truth for Finanshels positioning, voice, taglines, proof points, and visual identity. This skill enforces what `master-brand` defines.
