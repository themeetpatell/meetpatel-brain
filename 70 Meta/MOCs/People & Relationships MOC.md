---
type: moc
tags: [moc, people, relationships, crm, navigation]
status: living
updated: 2026-05-17
owner: Meet Patel
---

# People & Relationships — Map of Content

> The relationships that compound the operating work. Family, founders, investors, operators, customers, mentors. This MOC is the navigation surface for `40 Areas/Relationships/`.

## Why this exists as a system

Most relationships die from invisibility, not intent. Capacity is finite. Without a system, the most important people fall behind the most loud people. The vault makes relationship work *legible* — and legible work is the only work that survives a busy quarter.

## Where things live

| What | Where |
|---|---|
| Person notes | `40 Areas/Relationships/People/` |
| Family OS | `40 Areas/Relationships/FamilyOS/` |
| People I want closer | `40 Areas/Relationships/27 People I Want Closer.md` |
| Relationship map | `20 Compass/Identity/11 Relationship Map.md` |
| Relationship-nudge prompt | `_AI/Prompts/personal/relationship-nudge.md` |
| 1:1 prep prompt | `_AI/Prompts/ops/team-1on1-frame.md` |

## Person note schema

Every person note in `40 Areas/Relationships/People/` should have frontmatter:

```yaml
---
type: person
name: [Full Name]
tier: A | B | C
relationship: [founder / investor / operator / customer / mentor / family / friend / advisor]
cadence_days: 14   # default; tighter for tier A
last_contact: YYYY-MM-DD
context: [where met, why important]
how_to_help: [what they want from me, what I can offer]
how_they_help: [what they offer, what I want from them]
notes_about: [anything personal worth remembering — kids, hobbies, recent move]
---
```

## Tier definitions

- **Tier A** — high mutual value. Touch every 1–2 weeks. ~15 people.
- **Tier B** — meaningful relationship, lower frequency. Touch monthly. ~50 people.
- **Tier C** — known but not active. Touch quarterly or by event. ~150+ people.

(Numbers are guidance, not law. Adjust per current life-stage.)

## Standing operating rules

1. **No "hey, how's it going" pings.** If you can't think of something specific to say, don't message. The relationship survives silence better than it survives drift.
2. **Capture after every meaningful conversation.** Update `last_contact`, add a 1-line note about what was discussed.
3. **Birthdays + milestones get calendar entries.** Vault tracks; calendar reminds.
4. **Tier A gets unprompted value 1x/month.** Send an article, an intro, a thought — without an ask attached.
5. **Annual relationship audit** — re-tier everyone. People drift into and out of tiers naturally.

## Cadence rituals

- **Monday:** run `relationship-nudge` prompt to see who's overdue
- **Friday (in weekly review):** name one person to reach out to next week
- **Monthly:** review tier A list — are these still the right 15?
- **Quarterly:** tier audit — promote / demote / archive
- **Annually:** read every person note, update where stale

## People I want closer

`40 Areas/Relationships/27 People I Want Closer.md`

This is the deliberate-investment list. Distinct from the Tier system — these are people Meet is *trying to build deeper relationship with* who may not yet be Tier A.

For each: what specifically would deepen the relationship? An intro? A coffee? A shared project? Track and execute.

## Family OS

`40 Areas/Relationships/FamilyOS/`

Family relationships get their own sub-OS because the cadence and rules differ from professional relationships. The FamilyOS plan covers: regular contact rituals, gifting, presence (physical visits), shared moments, support obligations.

## Standing search queries (Dataview, when populated)

**Overdue tier-A contacts:**
```dataviewjs
const today = dv.date("today");
const people = dv.pages('"40 Areas/Relationships/People"')
  .where(p => p.type === "person" && p.tier === "A");
const overdue = people.where(p => {
  const cadence = p.cadence_days || 14;
  if (!p.last_contact) return true;
  return (today - dv.date(p.last_contact)).as("days") > cadence;
});
dv.table(["Person", "Last", "Overdue by"], overdue.map(p => [
  p.file.link,
  p.last_contact || "never",
  p.last_contact ? Math.floor((today - dv.date(p.last_contact)).as("days") - (p.cadence_days || 14)) + "d" : "—"
]));
```

## Phase 2 work (Knowledge Atlas wave)

- Enrich top 50 person notes with full schema (currently many are sparse Notion imports)
- Add structured `how_to_help` / `how_they_help` to each (forces clarity on the asymmetry)
- Connect People to Ventures (which people are tied to which ventures)
- Add Investor sub-zone for current/prospective investors

## Cross-MOC links

- [[Ventures MOC]] — ventures need investor + advisor + customer relationships
- [[Life OS MOC]] — Relationships is one of 5 Life zones
- [[Brand & Content MOC]] — content invites new relationships in

## Related skills

- No specific skill yet. Use `_AI/Prompts/personal/relationship-nudge.md` and `_AI/Prompts/ops/team-1on1-frame.md`.

---

*Relationships compound on the same exponential as ventures. The system has to be as serious.*
