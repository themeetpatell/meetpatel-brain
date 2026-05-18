# Risk Scoring Rubric — UAE Tax Risk Assessment

> Used by the `risk-assessment-tax` skill to assign consistent, defensible scores
> to each CT and VAT risk factor.

---

## Scoring Scale

Scores run from 1 (lowest risk) to 10 (highest risk).

| Score | RAG | What It Means |
|-------|-----|---------------|
| 1–3 | GREEN | Position appears compliant based on information provided. No immediate action required. Standard monitoring applies. |
| 4–6 | AMBER | Potential issue identified. Requires investigation or corrective action before the next filing. Penalty exposure possible if unresolved. |
| 7–10 | RED | Likely non-compliance or significant FTA audit risk. Immediate corrective action required. Material penalty exposure. |

---

## How to Assign a Score

Work through each factor below. For each, read the criteria and pick the score band that best matches the client's situation. When evidence is unavailable, default to the higher end of the band — incomplete information is itself a risk indicator.

---

## CT Risk Factor Scoring Criteria

### 1. Taxable Income Calculation

| Score | Evidence Standard |
|-------|------------------|
| 1–3 | Management accounts or trial balance reviewed; clearly disallowed deductions identified and added back; no significant unusual items |
| 4–6 | Accounts available but not reviewed for CT adjustments; or one area of uncertainty (e.g. provisions, entertainment expenses not split) |
| 7–10 | No accounts available, or significant disallowed items likely included (fines, non-arm's-length payments, entertainment > 50%), or no CT workpaper exists |

### 2. Related-Party and Connected-Person Transactions

| Score | Evidence Standard |
|-------|------------------|
| 1–3 | Complete list of related-party transactions; arm's-length analysis documented; TP disclosure form prepared; master/local file prepared if thresholds met |
| 4–6 | Related-party transactions identified but arm's-length analysis incomplete or informal; TP disclosure form drafted but not finalised |
| 7–10 | Related-party transactions not identified or not documented; no TP disclosure form; intercompany charges at non-arm's-length rates; thresholds likely exceeded with no documentation |

### 3. Free Zone QFZP Conditions

*Only score this factor if the entity is a free zone person claiming QFZP status. If not applicable, mark N/A.*

| Score | Evidence Standard |
|-------|------------------|
| 1–3 | Adequate substance demonstrated; all income is qualifying income; de minimis non-qualifying income test met (≤ 5% of revenue or AED 5M, whichever is lower — verify threshold with FTA); audited financials in place; election made on CT return |
| 4–6 | One condition uncertain (e.g. de minimis test close to limit, or audited financials not yet finalised); substance partially documented |
| 7–10 | Multiple QFZP conditions not met or untested; non-qualifying income likely above de minimis; no audited financials; election not made; mainland income treated as qualifying |

### 4. Small Business Relief (SBR)

*Only score if entity is claiming or eligible for SBR (revenue ≤ AED 3M, tax periods ending on/before 31 Dec 2026). If not applicable, mark N/A.*

| Score | Evidence Standard |
|-------|------------------|
| 1–3 | Revenue confirmed ≤ AED 3M across all sources; SBR election noted on CT return; entity not part of a group that would disqualify SBR |
| 4–6 | Revenue close to AED 3M threshold; sources not all confirmed; or entity structure not fully assessed for group disqualification |
| 7–10 | Revenue likely exceeds AED 3M but SBR claimed; related entities not identified; or SBR election not made despite eligibility being assumed |

### 5. Loss Relief

| Score | Evidence Standard |
|-------|------------------|
| 1–3 | Tax losses carried forward correctly per CT workpaper; restrictions reviewed (e.g. 75% cap on offset per period — verify with FTA); no change-of-ownership issues |
| 4–6 | Loss position identified but cap or restriction analysis not complete |
| 7–10 | Losses carried forward without analysis; or losses from pre-CT periods incorrectly included; or ownership change not assessed |

### 6. Exempt Income (Participation Exemption)

| Score | Evidence Standard |
|-------|------------------|
| 1–3 | Dividends and capital gains from qualifying participations identified; conditions checked (ownership %, holding period, subsidiary not in low-tax jurisdiction) |
| 4–6 | Exempt income present but conditions only partially reviewed |
| 7–10 | Exempt income claimed without conditions being tested; or significant dividend/disposal income not reviewed for qualification |

### 7. CT Registration Timing

| Score | Evidence Standard |
|-------|------------------|
| 1–3 | EmaraTax CT registration confirmed; registration date aligns with FTA-mandated deadline for the entity's licence-issuance month |
| 4–6 | Registration confirmed but deadline compliance not verified; or registration completed close to the deadline |
| 7–10 | Registration missing or confirmed late; AED 10,000 late-registration penalty likely accrued (confirm current amount with FTA) |

### 8. CT Return Deadline

| Score | Evidence Standard |
|-------|------------------|
| 1–3 | 9-month deadline calculated and tracked; return filed on time or filing is at least 60 days away |
| 4–6 | Deadline known but return preparation not yet started with < 60 days remaining |
| 7–10 | Deadline missed or less than 30 days away with return not in progress; late-filing penalty risk |

---

## VAT Risk Factor Scoring Criteria

### 1. Output Tax Completeness

| Score | Evidence Standard |
|-------|------------------|
| 1–3 | All revenue lines reviewed; standard-rated, zero-rated, and exempt supplies correctly classified; no missed invoices; output tax agrees to accounting records |
| 4–6 | Majority of revenue reviewed but some lines (e.g. recharges, commissions) not assessed; minor classification uncertainty |
| 7–10 | Output tax derived from summary figures only; revenue lines not individually reviewed; suspected under-declaration; significant one-off supplies (asset sales, deemed supplies) not assessed |

### 2. Input Tax Recovery

| Score | Evidence Standard |
|-------|------------------|
| 1–3 | All input tax claims supported by valid tax invoices; blocked categories (entertainment, motor vehicles for private use) excluded; partial exemption calculated if applicable |
| 4–6 | Input tax broadly reviewed but entertainment or motor vehicle expenses not split; partial exemption not calculated or only estimated |
| 7–10 | Input tax claimed on blocked categories; no invoice review; VAT on imports not addressed; partial exemption methodology absent |

### 3. Place of Supply — Cross-Border

| Score | Evidence Standard |
|-------|------------------|
| 1–3 | Cross-border services and imports identified; reverse charge applied where required; export zero-rating conditions documented |
| 4–6 | Some cross-border transactions identified but place-of-supply analysis incomplete; one uncertain area |
| 7–10 | No cross-border analysis performed despite international transactions; reverse charge not applied; export zero-rating claimed without documentation |

### 4. Invoice Compliance

| Score | Evidence Standard |
|-------|------------------|
| 1–3 | Sample of sales invoices reviewed; all FTA-required fields present (TRN of supplier, date, description, amounts, tax amount separately stated) |
| 4–6 | Invoices broadly compliant but not formally reviewed; some invoices may lack TRN or tax breakdown |
| 7–10 | Invoice format not reviewed; known issues with missing TRN, combined amounts, or incorrect tax rate |

### 5. VAT Registration Threshold

| Score | Evidence Standard |
|-------|------------------|
| 1–3 | Registration history confirmed; threshold breach date checked; registration effective from correct date |
| 4–6 | Registration in place but effective date not reconciled to threshold breach; or voluntary registration not considered despite eligible supplies |
| 7–10 | No VAT registration despite taxable supplies likely exceeding AED 375,000 in the past 12 months; or retrospective registration not addressed |

### 6. Return Filing and Payment

| Score | Evidence Standard |
|-------|------------------|
| 1–3 | All VAT returns filed by the 28th; payments cleared; no outstanding FTA correspondence on late filings |
| 4–6 | Broadly on time but one late filing in the period; or payment slightly delayed |
| 7–10 | Multiple late filings or payments; FTA penalties already assessed or likely; EmaraTax account shows outstanding liabilities |

### 7. Designated Zones

*Only score if the entity operates in or trades with a UAE designated zone. If not applicable, mark N/A.*

| Score | Evidence Standard |
|-------|------------------|
| 1–3 | Designated zone supplies correctly treated (neither imports nor exports for most goods moving between designated zones); exceptions (certain goods treated as imports/exports) identified and applied |
| 4–6 | Designated zone transactions present but treatment not formally reviewed |
| 7–10 | Designated zone transactions treated the same as mainland without analysis; likely output-tax errors |

---

## Overall Rating Derivation

1. Collect all individual scores (exclude N/A factors).
2. Apply this logic:

| Condition | Overall Rating |
|-----------|---------------|
| Any factor scores 7–10 | RED |
| Two or more factors score 4–6 (and none score 7–10) | AMBER |
| One factor scores 4–6 (and none score 7–10) | AMBER (low) |
| All factors score 1–3 | GREEN |

3. State the rating in the Executive Summary with the top 3 contributing factors.

---

## Penalty Reference (UAE FTA — verify current amounts)

| Violation | Indicative Penalty | Source |
|-----------|-------------------|--------|
| Late CT registration | AED 10,000 | FTA — confirm current amount |
| Late CT return filing | AED 500/month (first year) then AED 1,000/month — confirm with FTA | FTA penalty schedule |
| Late VAT registration | AED 20,000 — confirm with FTA | FTA penalty schedule |
| Late VAT return | AED 1,000 first time, AED 2,000 subsequent — confirm with FTA | FTA penalty schedule |
| Tax evasion | Up to 5x the evaded tax — confirm with FTA | FTA |
| Failure to keep records | AED 10,000 first offence — confirm with FTA | FTA |

> **All penalty amounts are indicative only.** Always verify the current schedule
> on the FTA website or EmaraTax before quoting figures to a client.

---

*See `../../_shared/finanshels-context.md` for UAE tax facts, rates, and deadlines.*
