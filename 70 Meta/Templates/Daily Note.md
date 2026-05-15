---
type: daily
created: <% tp.date.now("YYYY-MM-DD") %>
focus: 
tags: [daily]
---

# <% tp.date.now("dddd, MMMM Do, YYYY") %>

## Top 3 Today
1. 
2. 
3. 

## Calendar


## Open Loops (next 7 days)
```dataview
TASK
FROM ""
WHERE !completed AND due AND due <= date(today) + dur(7 days)
SORT due ASC
```

## Notes


## Evening Reflection
- What worked: 
- What didn't: 
- Tomorrow's #1: 
