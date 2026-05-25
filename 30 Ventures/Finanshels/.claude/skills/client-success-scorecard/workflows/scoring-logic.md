# Finanshels — Client Success Scoring Logic & Intervention Matrix

> Reference for the `client-success-scorecard` skill. Use this to score each
> dimension consistently and to select the right intervention for AMBER and RED clients.

---

## Scoring Reference Cards

### Dimension 1: Responsiveness

**What to measure over the scoring period:**
- Average client response time (in business days) to document requests or approval requests
- Number of first chasers sent (scheduled follow-up)
- Number of second chasers sent (overdue follow-up)
- Number of escalation chasers sent (to a senior contact)
- Number of deliverables where Finanshels had to file/deliver using incomplete information

**Scoring guide:**

| Avg Response | Chasers Needed | Score |
|---|---|---|
| ≤ 1 business day | None / rarely | 23–25 |
| 2–3 business days | First chase occasionally | 17–22 |
| 4–7 business days | First + second chase regularly | 10–16 |
| 7+ business days | Second chase + escalation | 0–9 |

**Adjustment:** If the client's industry or role is known to create seasonal response delays (e.g. Ramadan, audit season), note this as context but do not adjust the score — score what happened, note the reason.

---

### Dimension 2: Deliverable Timeliness

**What to measure over the scoring period:**
- Total deliverables due
- Deliverables filed/delivered on time
- Deliverables filed late to the FTA (regulatory late filing)
- Deliverables delivered late to the client vs. agreed internal date
- Root cause: Finanshels delay vs. client-caused delay (documented)

**Scoring guide:**

| On-Time Rate | FTA Late Filings | Score |
|---|---|---|
| 100% on time | 0 | 23–25 |
| 90–99%, or 1 near-miss | 0 | 17–22 |
| 75–89%, or 1–2 FTA late | 0–1 (client-caused) | 10–16 |
| < 75%, or multiple FTA late | 1+ (any cause) | 0–9 |

**Client-caused delay uplift:** If a late delivery is 100% attributable to the client failing to provide documents after multiple chasers (documented in PM tool), add +5 to this dimension score and move the deduction to the Responsiveness score instead. This keeps accountability accurate.

---

### Dimension 3: Payment Health

**What to measure over the scoring period:**
- Average days from invoice date to payment date
- Number of invoices with at least one payment reminder sent
- Number of invoices currently overdue (and by how many days)
- Total overdue AED balance

**Scoring guide:**

| Avg Days to Pay | Overdue Invoices | Score |
|---|---|---|
| ≤ 30 days | None | 23–25 |
| 31–45 days | None or 1 resolved quickly | 17–22 |
| 46–60 days | 1–2 outstanding | 10–16 |
| > 60 days | Multiple or formal demand | 0–9 |

**Revenue-weight flag:** If a client scores 0–9 on payment and is a high-value account (monthly fee > AED 5,000), escalate to senior partner for a direct conversation before issuing a formal notice.

---

### Dimension 4: Satisfaction

**What to measure over the scoring period:**
- NPS score if collected (0–10 scale)
- Formal complaints (raised via email, call, or written notice)
- Informal complaints (mentioned in a call, frustrated tone in email)
- Referrals given to Finanshels by this client
- Engagement manager's read: Is the client collaborative, transactional, or disengaged?

**Scoring guide:**

| NPS / Signals | Complaints | Score |
|---|---|---|
| NPS 9–10 / strongly positive feedback / referred a client | None | 23–25 |
| NPS 7–8 / neutral, cooperative | None | 17–22 |
| NPS 5–6 / infrequent contact / transactional tone | 1 minor, resolved | 10–16 |
| NPS < 5 / expressed dissatisfaction / threatening to leave | 1+ unresolved | 0–9 |

---

## Intervention Matrix

Use this when a client scores AMBER (60–79) or RED/CRITICAL (< 60).

### Responsiveness Interventions

| Signal | Intervention | Owner | Timing |
|---|---|---|---|
| 2+ second chasers in one period | Switch to WhatsApp / phone-first contact instead of email | Engagement Manager | Immediate |
| 4–7 day avg response time | Set a "documents deadline" protocol: request docs with a firm date, warn of filing risk | Engagement Manager | Next document request cycle |
| Escalation chasers sent | Engagement Manager calls the primary contact directly; establishes new protocol | Engagement Manager | Within 2 business days |
| Senior contact also unresponsive | Review whether the engagement is viable; consider a formal letter re: risk to compliance | Senior Partner | Within 5 business days |

---

### Deliverable Timeliness Interventions

| Signal | Intervention | Owner | Timing |
|---|---|---|---|
| 1 near-miss (filed last day) | Root-cause review: was it a Finanshels bandwidth issue or client latency? Fix the root cause. | Engagement Manager | Within 1 week |
| 1 FTA late filing (client-caused) | Send the client a formal written notice of the risk and what is needed to prevent recurrence | Engagement Manager | Within 2 business days of the late filing |
| 1 FTA late filing (Finanshels-caused) | Internal review; notify the client; check if FTA penalty applies; remediate | Senior Partner | Immediately |
| Chronic late delivery pattern | Review workload allocation; consider reassigning the bookkeeper or adjusting timelines | Team Lead | Within 2 weeks |

---

### Payment Health Interventions

| Signal | Intervention | Owner | Timing |
|---|---|---|---|
| 31–45 day avg, improving | Send a polite payment reminder 7 days before due date on all invoices | Accounts Receivable | Next invoice cycle |
| 46–60 day avg | Engagement Manager calls the finance contact; understands the reason | Engagement Manager | Within 3 business days of invoice going > 45 days |
| > 60 days overdue | Issue a formal payment demand with a 10-day cure period | Senior Partner | Immediately |
| Persistent > 60 days | Review whether to continue the engagement; escalate to leadership | Senior Partner | Within 5 business days |

---

### Satisfaction Interventions

| Signal | Intervention | Owner | Timing |
|---|---|---|---|
| NPS 5–6 or transactional tone | Schedule a 15-minute check-in call (not billed) to understand concerns | Engagement Manager | Within 1 week |
| 1 complaint (any kind) | Acknowledge within 24 hours; investigate; close the loop with the client in writing | Engagement Manager | 24 hours to acknowledge |
| Complaint unresolved > 5 days | Escalate to Senior Partner; issue a formal response | Senior Partner | Within 5 days of complaint |
| Client expressing intent to leave | Senior Partner + Engagement Manager joint retention call | Senior Partner | Within 2 business days |
| No NPS collected (> 6 months) | Send a brief satisfaction survey (2–3 questions) | Engagement Manager | Next client touchpoint |

---

## Portfolio Health Summary — Thresholds

When reviewing the full client portfolio, flag these as requiring leadership discussion:

| Threshold | Action |
|---|---|
| > 20% of clients in AMBER | Review team capacity and processes — systemic issue |
| Any client in CRITICAL (< 40) | Immediate senior partner review |
| 3+ clients with Dimension 3 (payment) score < 17 | Review invoicing and accounts receivable process |
| Any FTA late filing in the period | Mandatory post-mortem within 1 week |
| New client (< 90 days) scoring AMBER | Assign a senior engagement check-in at the 30-day mark |

---

*Finanshels internal use only. Confidential. Scoring data informs engagement management decisions — not client-facing communications.*
