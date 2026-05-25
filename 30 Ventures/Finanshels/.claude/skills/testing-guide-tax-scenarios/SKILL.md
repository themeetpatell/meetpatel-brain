---
name: testing-guide-tax-scenarios
description: Use when you need to create comprehensive test cases for UAE tax scenarios in code — including Corporate Tax 0% vs 9% threshold, Small Business Relief eligibility, free zone QFZP qualifying and non-qualifying income, VAT standard/zero-rated/exempt/out-of-scope classification, and VAT registration thresholds. Triggers on phrases like "write test cases for CT logic", "generate a test matrix for VAT", "what edge cases should I test for Small Business Relief", "test the QFZP income split", "what scenarios should we cover for the VAT threshold". Produces a structured test matrix with input conditions, expected outputs, and pass/fail criteria covering all boundary and edge cases, plus a runnable test-matrix generator script.
---

# Testing Guide — UAE Tax Scenarios

Creates comprehensive, boundary-aware test cases for UAE Corporate Tax and VAT logic, producing a test matrix that engineers can implement directly in their test suite.

## When to use

- Writing unit tests for a CT taxable-income calculation function.
- Defining acceptance criteria for a VAT return aggregation service.
- Reviewing whether an existing test suite covers all UAE tax edge cases.
- Onboarding a new engineer to the tax rules so they can write meaningful tests.
- Before merging any code that computes CT rates, applies Small Business Relief, splits QFZP income, or classifies VAT supplies.
- QA sign-off on a compliance-critical feature.

## Inputs needed

**Required**
- Tax area(s) to cover — one or more of: `CT_THRESHOLD`, `SMALL_BUSINESS_RELIEF`, `QFZP`, `VAT_CALCULATION`, `VAT_REGISTRATION`, `VAT_CATEGORIES`.
- What the code under test does (e.g. "function `computeCTLiability(taxableIncome)` returns the CT amount payable").

**Optional**
- Programming language and test framework (Python/pytest, TypeScript/Jest, etc.) — used to format example test stubs.
- Specific edge cases the developer is worried about.
- Whether to include negative test cases (invalid inputs, error handling).
- Output format preference: Markdown table, JSON, or code stubs.

## Workflow

1. **Identify the tax scenarios in scope**
   - Map the requested tax area(s) to the relevant UAE law thresholds and rules (from the shared context file).
   - List all boundary values — the exact threshold numbers are the most important test inputs.

2. **Generate the test matrix**
   - For each scenario, define: test ID, description, input(s), expected output, pass criterion, and the UAE rule being tested.
   - Cover: happy path, lower boundary (at threshold), upper boundary (just above threshold), well-below threshold, well-above threshold, and invalid/edge inputs.
   - Run `tools/test-matrix.py` to generate the canonical matrix for standard scenarios.

3. **Annotate boundary cases explicitly**
   - UAE tax boundaries are inclusive on the lower end in most cases (e.g. AED 375,000 taxable income → 0% CT; AED 375,001 → 9% on AED 1 only). Make this crystal clear in each test case.

4. **Add negative / error test cases**
   - Null/None inputs, negative amounts, non-AED currencies, invalid date ranges, missing TRNs.

5. **Format as implementable test stubs**
   - For the requested language/framework, output `# TODO: implement` stubs with the exact input values and expected outputs already filled in.

6. **Output the test matrix** (see Output format below).

## Output format

```
## Test Matrix — [Tax Area(s)]
**Code under test:** [function/service name]
**Generated:** [date]
**Total test cases:** N

### CT Threshold Tests

| ID | Scenario | Input: taxableIncome (AED) | Expected: ctPayable (AED) | Rule |
|----|----------|---------------------------|---------------------------|------|
| CT-01 | Zero income | 0 | 0.00 | 0% on ≤ 375,000 |
| CT-02 | Below threshold | 200,000 | 0.00 | 0% on ≤ 375,000 |
| CT-03 | Exactly at threshold | 375,000 | 0.00 | 0% on ≤ 375,000 (inclusive) |
| CT-04 | One dirham above | 375,001 | 0.09 | 9% on 1 AED above threshold |
| CT-05 | Typical SME | 1,000,000 | 56,250.00 | 9% on 625,000 |
| ... | | | | |

### Test stubs (Python/pytest)
[formatted stubs]
```

## Quality checklist

- [ ] Boundary at exactly AED 375,000 tested (inclusive → 0% CT)
- [ ] Boundary at AED 375,001 tested (1 AED of 9% tax)
- [ ] Small Business Relief at exactly AED 3,000,000 (qualifies) and AED 3,000,001 (does not)
- [ ] Small Business Relief period boundary: tax period ending 31 Dec 2026 vs 1 Jan 2027
- [ ] QFZP qualifying income produces 0%; non-qualifying produces 9%
- [ ] VAT standard rate: 5% applied correctly with 2 d.p. rounding
- [ ] VAT zero-rated: 0% with vatAmount = 0.00
- [ ] VAT exempt: 0% with vatAmount = 0.00; no input tax credit
- [ ] VAT registration mandatory threshold: AED 375,000 (supplies in past 12 months)
- [ ] VAT registration voluntary threshold: AED 187,500
- [ ] Null/None inputs produce a typed error, not a silent zero
- [ ] Each test case has a UAE rule citation

## Examples

- "Generate test cases for our CT taxable income calculator. I need to cover the 0%/9% threshold and Small Business Relief."
- "What test scenarios should we write for the QFZP qualifying income split? We have a free zone client who has both qualifying and non-qualifying revenues."
- "Create a VAT test matrix for our invoice classifier — it takes an invoice and outputs S/Z/E/OS. I want boundary cases and invalid inputs."

## Guardrails

- UAE jurisdiction only. All thresholds and rates come from UAE law — never substitute US, UK, or EU equivalents.
- This matrix is a starting point. A qualified Finanshels team member should review the test cases against current FTA guidance before the test suite is relied upon for compliance sign-off.
- Tax law changes. If a rate or threshold in this matrix differs from current FTA guidance, the FTA guidance wins.
- Do not use real client data as test inputs. All values in the matrix must be synthetic.

## Reference

See ../_shared/finanshels-context.md for UAE tax facts, rates, and deadlines.
