---
type: monthly
created: <% tp.date.now("YYYY-MM-DD") %>
month: <% tp.date.now("YYYY-MM") %>
tags: [monthly]
---

# <% tp.date.now("MMMM YYYY") %>

## Theme of the Month


## Key Decisions
```dataview
LIST
FROM "20 Compass/Decisions"
WHERE created >= date(today) - dur(30 days)
SORT created DESC
```

## Content Shipped
```dataview
LIST
FROM "60 Outputs/Content"
WHERE status = "published" AND created >= date(today) - dur(30 days)
```

## Relationships Nurtured


## Per-Venture North-Star Metrics
- **Finanshels** — 
- **Biggdate** — 
- **StartupOS** — 
- **ZeroHuman** — 
- **MealVerse** — 
- **Soulmap** — 

## What I'm Carrying Into Next Month
