---
type: weekly
created: <% tp.date.now("YYYY-MM-DD") %>
week: <% tp.date.now("YYYY-[W]ww") %>
tags: [weekly]
---

# Week of <% tp.date.now("MMMM Do, YYYY") %>

## Wins


## Lessons


## Decisions Made This Week
```dataview
LIST
FROM "20 Compass/Decisions"
WHERE created >= date(today) - dur(7 days)
SORT created DESC
```

## Open Loops Carried Over


## Per-Venture Status
- **Finanshels** — 
- **Biggdate** — 
- **StartupOS** — 
- **ZeroHuman** — 
- **MealVerse** — 
- **Soulmap** — 

## Next Week's Focus
1. 
2. 
3. 
