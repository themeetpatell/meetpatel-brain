---
name: client-success-scorecard
description: Use when assessing the health of a client engagement at Finanshels — triggered by requests like "how healthy is this client", "client health check", "at-risk clients", "engagement review", "satisfaction score", "which clients need attention", or any review of client relationship quality. Produces a health score (0–100) per client with RAG rating, broken down across responsiveness, deliverable timeliness, payment, and satisfaction, plus concrete intervention recommendations for low-scoring clients.
---

# Client Success Scorecard

Tracks engagement health per Finanshels client across four dimensions — responsiveness, deliverable timeliness, payment, and satisfaction — into a single health score with a RAG rating and targeted intervention triggers.

## When to use

- Monthly or quarterly client health review across the entire portfolio
- Identifying at-risk clients before they churn or escalate a complaint
- Pre-renewal or upsell conversation preparation (health score informs the approach)
- After a difficult engagement period (late deliverables, client complaints, payment issues)
- Onboarding review at the 30-day and 90-day marks for new clients
- Preparing a portfolio health summary for Finanshels leadership

## Inputs needed

**Required (per client being scored):**
- Client name and entity type
- Engaged services
- Scoring period (e.g. last 90 days, last quarter)
- Data for each of the four dimensions (see Workflow — Step 1 for what data is needed per dimension)

**Optional:**
- Engagement manager's qualitative assessment (free text)
- Client's last direct feedback (email, call note, NPS score if collected)
- Revenue value of the engagement (AED/month) — used to prioritize intervention effort
- Time since onboarding (new client flag: < 90 days)

## Workflow

### Step 1 — Score Each Dimension (0–25 points each, total 100)

Work through the four dimensions for the client. Each dimension uses objective data inputs plus a brief qualitative override option for the engagement manager.

---

#### Dimension 1: Responsiveness (0–25 pts)

Measures how quickly and reliably the client provides documents, approvals, and responses when Finanshels requests them.

| Score | Criteria |
|---|---|
| 23–25 | Responds within 1 business day consistently. Documents provided before or on the agreed date. No chasers needed. |
| 17–22 | Responds within 2–3 business days most of the time. Occasional reminder needed but cooperative. |
| 10–16 | Regularly requires 2+ chasers. Responses take 4–7 business days. Some deliverables delayed due to client latency. |
| 0–9 | Frequently unresponsive (7+ business days). Multiple chasers including escalation to senior contact. Deliverables materially delayed. |

**Data inputs needed:** Average response time (business days) over the scoring period; number of first, second, and escalation chasers sent; number of deliverables delayed specifically because of client document/approval latency.

---

#### Dimension 2: Deliverable Timeliness (0–25 pts)

Measures whether Finanshels has delivered on time — and where delays occurred, whether they were caused by Finanshels or by the client.

| Score | Criteria |
|---|---|
| 23–25 | All deliverables filed/delivered on or before the agreed date. Zero late filings. |
| 17–22 | 1 deliverable was late or close to deadline, but filed on time with the FTA. Driven by client latency. |
| 10–16 | 1–2 deliverables filed late to the FTA OR consistently delivered to the client after the agreed date, regardless of cause. |
| 0–9 | Multiple FTA late filings OR chronic delivery delays that have damaged client trust. |

**Note:** If a late filing was entirely caused by client non-response (documented), apply a partial uplift of +5 points and flag this in the notes — this is a responsiveness issue, not a Finanshels quality issue.

**Data inputs needed:** Number of deliverables due vs. filed on time; any FTA late filing penalties incurred; engagement manager's assessment of cause.

---

#### Dimension 3: Payment Health (0–25 pts)

Measures how promptly the client pays Finanshels invoices.

| Score | Criteria |
|---|---|
| 23–25 | All invoices paid within agreed payment terms (e.g. 30 days). No outstanding overdue invoices. |
| 17–22 | Pays within 31–45 days consistently. 1 reminder occasionally needed but resolves quickly. |
| 10–16 | Regularly pays 46–60 days after invoice. 2+ reminders per invoice cycle. Some months with overdue balance. |
| 0–9 | Invoices > 60 days overdue, recurring pattern. Formal demand sent or credit hold applied. |

**Data inputs needed:** Average days-to-pay over scoring period; number of outstanding overdue invoices (AED value); number of payment reminders sent.

---

#### Dimension 4: Satisfaction (0–25 pts)

Measures client satisfaction signals — both direct (NPS, feedback) and indirect (complaints, escalations, tone of communication).

| Score | Criteria |
|---|---|
| 23–25 | Client has expressed positive feedback, referred another client, or scored NPS 9–10. No complaints. Proactive and collaborative. |
| 17–22 | No major complaints. Communication is professional and cooperative. NPS 7–8 or no NPS collected. |
| 10–16 | 1 complaint raised and resolved. Client communication has become transactional or infrequent. NPS 5–6 or disengaged. |
| 0–9 | Formal complaint. Threatening to leave. Multiple unresolved issues. NPS < 5 or expressed dissatisfaction directly. |

**Data inputs needed:** Last NPS score (if collected); any formal or informal complaints in the scoring period; engagement manager's qualitative read on relationship health; referrals given.

---

### Step 2 — Calculate Total Health Score and RAG Rating

Sum the four dimension scores (max 100).

| Score Range | RAG | Label | Action |
|---|---|---|---|
| 80–100 | 🟢 GREEN | Healthy | Maintain quality, consider upsell/referral ask |
| 60–79 | 🟡 AMBER | Watch | Investigate root cause, proactive engagement |
| 40–59 | 🔴 RED | At Risk | Immediate intervention — see Step 3 |
| 0–39 | 🔴 CRITICAL | Crisis | Executive-level intervention, retention plan |

**New client override:** If the client has been onboarded within the last 90 days, apply a minimum floor of AMBER unless the score is below 40. Early-stage relationship patterns need time to normalize.

---

### Step 3 — Generate Intervention Recommendations

For AMBER and RED/CRITICAL clients, apply the intervention matrix from `workflows/scoring-logic.md` to produce 2–4 specific, actionable recommendations. Each recommendation should name:
- The specific problem signal
- The recommended action
- Who owns the action (engagement manager / senior partner / finance team)
- A target resolution date

---

### Step 4 — Build the Scorecard

Produce the scorecard in the Output Format below. For portfolio reviews, produce one summary table then individual cards for all AMBER and RED clients.

## Output format

```
## Client Success Scorecard — [CLIENT NAME]
Period: [SCORING PERIOD] | Entity: [TYPE] | Services: [LIST]
Engagement Manager: [NAME] | Scored by: [NAME] | Date: [DATE]

### Scores
| Dimension | Score | Max | Notes |
|---|---|---|---|
| 1. Responsiveness | [X] | 25 | [Brief note] |
| 2. Deliverable Timeliness | [X] | 25 | [Brief note] |
| 3. Payment Health | [X] | 25 | [Brief note] |
| 4. Satisfaction | [X] | 25 | [Brief note] |
| **TOTAL** | **[X]** | **100** | |

### Health Rating: [🟢 GREEN / 🟡 AMBER / 🔴 RED / 🔴 CRITICAL] — [LABEL]

### Engagement Manager Assessment
[Free text — 2–4 sentences on the overall relationship]

### Intervention Recommendations
[Only for AMBER / RED / CRITICAL:]
1. [Signal] → [Action] | Owner: [Name] | By: [Date]
2. [Signal] → [Action] | Owner: [Name] | By: [Date]
3. ...

### Trend (if prior scores available)
Previous score: [X] ([PERIOD]) → Current: [X] → [Improving / Stable / Declining]
```

**Portfolio Summary Table (for multi-client reviews):**
```
| Client | Entity | EM | Resp | Timeliness | Payment | Satisfaction | Total | RAG |
|---|---|---|---|---|---|---|---|---|
| [Name] | Mainland | [Name] | 20 | 22 | 25 | 18 | 85 | 🟢 |
| [Name] | Free Zone | [Name] | 10 | 14 | 18 | 8 | 50 | 🔴 |
```

## Quality checklist

- [ ] All four dimensions scored with objective data, not just intuition
- [ ] Data sources noted for each dimension (e.g. "based on PM tool chase log")
- [ ] Late deliverables caused by client documented separately from Finanshels-caused delays
- [ ] New client (< 90 days) flag applied where relevant
- [ ] Intervention recommendations are specific — not "improve communication" but "schedule a call by Friday to address the March accounts complaint"
- [ ] Intervention recommendations have named owners and target dates
- [ ] Portfolio summary produced for reviews covering 3+ clients
- [ ] Trend data included where prior period scores are available
- [ ] Reviewed by engagement manager before being shared with leadership

## Examples

**Example 1:**
"Run a health check on our biggest client — an Abu Dhabi mainland holding company, AED 18M revenue, on full service (books + VAT + CT + payroll). They've been slow to respond lately and we had to file their Q1 VAT return on the last day. Monthly fee is AED 8,500."

**Example 2:**
"Score all 12 active clients for the Q2 review. Give me the portfolio summary table and individual scorecards for anyone in AMBER or RED."

**Example 3:**
"New client check-in — a Sharjah free zone client onboarded 6 weeks ago, retail e-commerce, AED 3.2M revenue. We've had to chase them twice for documents already and their first invoice is 12 days overdue. How healthy is this engagement?"

## Guardrails

- Scoring is based on the data provided — garbage in, garbage out. Engagement managers must input accurate data, not scores that make the relationship look better than it is.
- Health scores are internal tools. Never share the raw score with the client — use them to prepare better conversations, not to label or shame clients.
- A RED or CRITICAL score is a trigger for intervention, not for terminating the engagement. Escalate first, assess second.
- This skill supports engagement management judgment — it does not replace it. The engagement manager's qualitative override carries weight, especially for context that data cannot capture.
- All client data is confidential. Portfolio scorecards are for internal Finanshels leadership use only.

## Reference

See ../_shared/finanshels-context.md for UAE tax facts, rates, and deadlines.
