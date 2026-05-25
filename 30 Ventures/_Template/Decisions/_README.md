---
type: index
status: living
tags: [decisions, venture]
---

# Decisions — <Venture>

One file per material decision. Filename: `YYYY-MM-DD - decision title.md`.

Template:

```
---
type: decision
date: YYYY-MM-DD
status: open | committed | reversed
reviewable_by: YYYY-MM-DD
tags: [decision]
---

# Decision: <title>

**Question:**
**Options considered:**
**Chosen:**
**Why:**
**What would change my mind:**
**Review date:**
```

```dataview
TABLE status, date, reviewable_by FROM "30 Ventures/<NAME>/Decisions" WHERE type = "decision" SORT date DESC
```
