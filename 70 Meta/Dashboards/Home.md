---
type: dashboard
tags: [dashboard, home]
---

# Operator Dashboard

> **Today** — `=dateformat(date(today), "EEEE, MMMM d, yyyy")`

## Today's Focus

```dataviewjs
const today = window.moment().format("YYYY-MM-DD");
const page = dv.page(`10 Daily/Daily/${today}`);
if (page) {
    dv.paragraph(`**Focus:** ${page.focus || "(not set)"}`);
    dv.paragraph(`[Open today's note →](${page.file.path})`);
} else {
    dv.paragraph(`*No daily note yet for today.* Press \`Cmd+Shift+D\` to create one.`);
}
```

## Inbox

```dataviewjs
const items = dv.pages('"00 Inbox"').where(p => p.file.name !== "Home");
dv.paragraph(`**${items.length}** item${items.length === 1 ? "" : "s"} waiting`);
if (items.length > 0) {
    dv.list(items.sort(p => -p.file.ctime).limit(10).file.link);
}
```

## Open Loops (next 7 days)

```dataview
TASK
FROM ""
WHERE !completed AND due AND due <= date(today) + dur(7 days)
SORT due ASC
```

## Decisions Due for Review

```dataview
LIST "review on " + review_date
FROM "20 Compass/Decisions"
WHERE status = "open" AND review_date AND review_date <= date(today)
SORT review_date ASC
```

## Venture Pulse

```dataviewjs
const ventures = ["Finanshels", "Biggdate", "StartupOS", "ZeroHuman", "MealVerse", "Soulmap"];
const today = dv.date("today");
const rows = ventures.map(v => {
    const notes = dv.pages(`"30 Ventures/${v}"`);
    if (!notes.length) return [v, "—", "—", "no notes yet"];
    const lastUpdate = notes.file.mtime.values.reduce((a, b) => a > b ? a : b);
    const openTasks = notes.file.tasks.where(t => !t.completed).length;
    const daysSince = Math.floor((today - lastUpdate).as("days"));
    const stale = daysSince > 7 && openTasks > 0 ? " ⚠ stale" : "";
    return [
        `[[30 Ventures/${v}/${v}|${v}]]`,
        openTasks,
        `${daysSince}d ago`,
        stale || "ok"
    ];
});
dv.table(["Venture", "Open", "Last update", "Status"], rows);
```

## Content Pipeline

```dataview
TABLE status, format, audience
FROM "60 Outputs/Content"
WHERE status != "published"
SORT created DESC
LIMIT 20
```

## People to Nurture

```dataviewjs
const today = dv.date("today");
const people = dv.pages('"40 Areas/Relationships"').where(p => p.type === "person");
const overdue = people.where(p => {
    const cadence = p.cadence_days || 14;
    if (!p.last_contact) return true;
    return (today - dv.date(p.last_contact)).as("days") > cadence;
});
dv.paragraph(`**${overdue.length}** overdue (vs cadence)`);
if (overdue.length > 0) {
    const rows = overdue.sort(p => p.last_contact, "asc").limit(10).map(p => [
        p.file.link,
        p.last_contact ? `${Math.floor((today - dv.date(p.last_contact)).as("days"))}d ago` : "never",
        p.cadence_days || 14
    ]);
    dv.table(["Person", "Last contact", "Cadence"], rows);
}
```

## This Week

```dataviewjs
const week = window.moment().format("YYYY-[W]ww");
const wr = dv.page(`10 Daily/Weekly/${week}`);
if (wr) {
    dv.paragraph(`[Open this week's review →](${wr.file.path})`);
} else {
    dv.paragraph(`*No weekly review yet for ${week}.*`);
}
```
