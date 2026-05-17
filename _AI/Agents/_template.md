---
type: agent-template
status: living
tags: [ai, agent, template]
---

# Agent Template

Copy this file when adding a new agent. Replace each block.

---

## Agent: [Name]

**One-line job:** [What this agent does in one sentence.]

**Trigger:** [When Meet (or another agent) invokes it. e.g., "weekly Monday 6am", "on user prompt: 'summarize call'", "when a new lead lands in CRM".]

**Reads (context):**
- `_AI/Contexts/meet.md` (always)
- [other vault paths the agent should load before acting]

**Inputs:**
- [Required input 1]
- [Required input 2 — optional]

**Output format:**
- [Exact structure of what the agent returns. Be precise.]

**Voice constraints:**
- Follow `_AI/Contexts/voice.md`.
- [Any extra constraints — e.g., "max 200 words", "always include numbers", "never use jargon".]

**Escalation:**
- [When the agent should stop and ask Meet vs proceed autonomously.]

**Examples (good vs bad):**

Good output:
> [paste an example]

Bad output:
> [paste a counter-example with what's wrong]

**Maintenance:**
- Review monthly. Tighten if drift observed.
