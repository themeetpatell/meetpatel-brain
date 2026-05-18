"""
test-matrix.py
--------------
UAE tax scenario test-matrix generator for Finanshels.

Generates a structured, boundary-aware test-case matrix covering:
  - Corporate Tax (CT): 0% / 9% threshold, Small Business Relief
  - Free zone QFZP: qualifying vs non-qualifying income
  - VAT: standard / zero-rated / exempt / out-of-scope classification
  - VAT registration: mandatory and voluntary thresholds

Runs on stdlib only — no pip dependencies required.

Usage:
    python3 test-matrix.py

Prints the full matrix to stdout and saves a JSON export to test_matrix.json
in the same directory.
"""

import json
import os
from decimal import Decimal, ROUND_HALF_UP
from typing import Dict, List, Optional

# ---------------------------------------------------------------------------
# Constants — UAE tax rules (verify against current FTA guidance)
# ---------------------------------------------------------------------------

CT_ZERO_RATE_THRESHOLD = Decimal("375000")       # AED — 0% up to and including
CT_RATE_ABOVE_THRESHOLD = Decimal("0.09")         # 9% on income above threshold
SBR_REVENUE_LIMIT = Decimal("3000000")            # AED — Small Business Relief cap
SBR_PERIOD_END = "2026-12-31"                     # Relief only for periods ending by this date

VAT_STANDARD_RATE = Decimal("0.05")               # 5%
VAT_MANDATORY_THRESHOLD = Decimal("375000")       # AED — mandatory registration
VAT_VOLUNTARY_THRESHOLD = Decimal("187500")       # AED — voluntary registration


# ---------------------------------------------------------------------------
# Tax computation helpers (reference implementations for test assertions)
# ---------------------------------------------------------------------------


def compute_ct_liability(taxable_income: Decimal) -> Decimal:
    """
    Compute UAE Corporate Tax payable on taxable income.
    0% on first AED 375,000; 9% on the excess.
    """
    if taxable_income <= CT_ZERO_RATE_THRESHOLD:
        return Decimal("0.00")
    excess = taxable_income - CT_ZERO_RATE_THRESHOLD
    return (excess * CT_RATE_ABOVE_THRESHOLD).quantize(
        Decimal("0.01"), rounding=ROUND_HALF_UP
    )


def qualifies_for_sbr(revenue: Decimal, tax_period_end: str) -> bool:
    """
    Return True if the entity qualifies for Small Business Relief.
    Conditions:
      - Revenue <= AED 3,000,000 for the tax period
      - Tax period ends on or before 31 Dec 2026
    """
    return revenue <= SBR_REVENUE_LIMIT and tax_period_end <= SBR_PERIOD_END


def compute_qfzp_ct(
    qualifying_income: Decimal,
    non_qualifying_income: Decimal,
) -> Dict[str, Decimal]:
    """
    Compute CT for a Qualifying Free Zone Person (QFZP).
    0% on qualifying income; 9% on non-qualifying income above the threshold.
    """
    ct_on_qualifying = Decimal("0.00")
    ct_on_non_qualifying = compute_ct_liability(non_qualifying_income)
    return {
        "ct_on_qualifying": ct_on_qualifying,
        "ct_on_non_qualifying": ct_on_non_qualifying,
        "total_ct": ct_on_qualifying + ct_on_non_qualifying,
    }


def compute_vat(net_amount: Decimal, category: str) -> Decimal:
    """
    Compute VAT amount given a net amount and UAE VAT category code.
    S = 5%, Z = 0%, E = 0%, OS = 0%
    """
    if category == "S":
        return (net_amount * VAT_STANDARD_RATE).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )
    return Decimal("0.00")


def vat_registration_status(
    taxable_supplies_12m: Decimal,
) -> str:
    """
    Determine VAT registration obligation based on trailing 12-month taxable supplies.
    Returns: MANDATORY, VOLUNTARY_ELIGIBLE, or NOT_REQUIRED
    """
    if taxable_supplies_12m > VAT_MANDATORY_THRESHOLD:
        return "MANDATORY"
    if taxable_supplies_12m > VAT_VOLUNTARY_THRESHOLD:
        return "VOLUNTARY_ELIGIBLE"
    return "NOT_REQUIRED"


# ---------------------------------------------------------------------------
# Test case builders
# ---------------------------------------------------------------------------


def build_ct_threshold_cases() -> List[Dict]:
    """
    CT threshold test cases covering:
    - Zero income
    - Well below threshold
    - Just below threshold
    - Exactly at threshold (inclusive 0%)
    - One fils above threshold
    - One dirham above threshold
    - Typical SME income
    - High income
    - Null / invalid input cases
    """
    cases = [
        {
            "id": "CT-01",
            "area": "CT_THRESHOLD",
            "description": "Zero taxable income",
            "input": {"taxable_income_aed": "0"},
            "expected": {"ct_payable_aed": "0.00"},
            "rule": "0% applies on income ≤ AED 375,000 (inclusive)",
            "boundary": False,
        },
        {
            "id": "CT-02",
            "area": "CT_THRESHOLD",
            "description": "Income well below threshold (AED 100,000)",
            "input": {"taxable_income_aed": "100000"},
            "expected": {"ct_payable_aed": "0.00"},
            "rule": "0% on ≤ AED 375,000",
            "boundary": False,
        },
        {
            "id": "CT-03",
            "area": "CT_THRESHOLD",
            "description": "Income just below threshold (AED 374,999)",
            "input": {"taxable_income_aed": "374999"},
            "expected": {"ct_payable_aed": "0.00"},
            "rule": "0% on ≤ AED 375,000",
            "boundary": True,
        },
        {
            "id": "CT-04",
            "area": "CT_THRESHOLD",
            "description": "Income exactly at threshold (AED 375,000) — boundary inclusive",
            "input": {"taxable_income_aed": "375000"},
            "expected": {"ct_payable_aed": "0.00"},
            "rule": "0% on ≤ AED 375,000 (inclusive boundary)",
            "boundary": True,
        },
        {
            "id": "CT-05",
            "area": "CT_THRESHOLD",
            "description": "Income one fils above threshold (AED 375,000.01)",
            "input": {"taxable_income_aed": "375000.01"},
            "expected": {"ct_payable_aed": "0.00"},  # 0.01 × 9% = 0.0009 → rounds to 0.00
            "rule": "9% on excess; AED 0.01 excess → AED 0.00 after rounding",
            "boundary": True,
        },
        {
            "id": "CT-06",
            "area": "CT_THRESHOLD",
            "description": "Income one dirham above threshold (AED 375,001)",
            "input": {"taxable_income_aed": "375001"},
            "expected": {"ct_payable_aed": "0.09"},
            "rule": "9% on AED 1 excess = AED 0.09",
            "boundary": True,
        },
        {
            "id": "CT-07",
            "area": "CT_THRESHOLD",
            "description": "Typical SME income (AED 1,000,000)",
            "input": {"taxable_income_aed": "1000000"},
            "expected": {"ct_payable_aed": "56250.00"},
            "rule": "9% on AED 625,000 (1,000,000 − 375,000) = AED 56,250",
            "boundary": False,
        },
        {
            "id": "CT-08",
            "area": "CT_THRESHOLD",
            "description": "High income (AED 10,000,000)",
            "input": {"taxable_income_aed": "10000000"},
            "expected": {"ct_payable_aed": "866250.00"},
            "rule": "9% on AED 9,625,000 (10,000,000 − 375,000) = AED 866,250",
            "boundary": False,
        },
        {
            "id": "CT-09",
            "area": "CT_THRESHOLD",
            "description": "Negative income (loss) — CT payable must be zero, not negative",
            "input": {"taxable_income_aed": "-50000"},
            "expected": {"ct_payable_aed": "0.00"},
            "rule": "Tax loss carry-forward applies; no tax payable on a loss",
            "boundary": False,
        },
        {
            "id": "CT-10",
            "area": "CT_THRESHOLD",
            "description": "Null income — must raise a typed error",
            "input": {"taxable_income_aed": None},
            "expected": {"error": "ValueError or TypeError — input must be numeric"},
            "rule": "Input validation — never default null to zero silently",
            "boundary": False,
        },
    ]
    # Verify expected values against the reference implementation
    for case in cases:
        raw = case["input"].get("taxable_income_aed")
        if raw is not None:
            income = Decimal(str(raw))
            if income >= 0:
                actual = str(compute_ct_liability(income))
                case["_verified_expected"] = actual
    return cases


def build_sbr_cases() -> List[Dict]:
    """
    Small Business Relief test cases.
    Conditions: revenue ≤ AED 3,000,000 AND tax period ends on or before 31 Dec 2026.
    """
    return [
        {
            "id": "SBR-01",
            "area": "SMALL_BUSINESS_RELIEF",
            "description": "Revenue well below limit, within relief period",
            "input": {"revenue_aed": "500000", "tax_period_end": "2024-12-31"},
            "expected": {"qualifies": True, "taxable_income_treated_as": "0"},
            "rule": "Revenue ≤ AED 3,000,000 and period ends ≤ 31 Dec 2026",
            "boundary": False,
        },
        {
            "id": "SBR-02",
            "area": "SMALL_BUSINESS_RELIEF",
            "description": "Revenue exactly at limit (AED 3,000,000) — boundary inclusive",
            "input": {"revenue_aed": "3000000", "tax_period_end": "2025-12-31"},
            "expected": {"qualifies": True, "taxable_income_treated_as": "0"},
            "rule": "Revenue ≤ AED 3,000,000 (inclusive)",
            "boundary": True,
        },
        {
            "id": "SBR-03",
            "area": "SMALL_BUSINESS_RELIEF",
            "description": "Revenue one dirham above limit (AED 3,000,001) — does NOT qualify",
            "input": {"revenue_aed": "3000001", "tax_period_end": "2025-12-31"},
            "expected": {"qualifies": False},
            "rule": "Revenue > AED 3,000,000 → no relief",
            "boundary": True,
        },
        {
            "id": "SBR-04",
            "area": "SMALL_BUSINESS_RELIEF",
            "description": "Revenue qualifies but period ends 31 Dec 2026 — last eligible date",
            "input": {"revenue_aed": "1000000", "tax_period_end": "2026-12-31"},
            "expected": {"qualifies": True},
            "rule": "Relief available for periods ending on or before 31 Dec 2026",
            "boundary": True,
        },
        {
            "id": "SBR-05",
            "area": "SMALL_BUSINESS_RELIEF",
            "description": "Revenue qualifies but period ends 1 Jan 2027 — first ineligible date",
            "input": {"revenue_aed": "1000000", "tax_period_end": "2027-01-01"},
            "expected": {"qualifies": False},
            "rule": "Relief NOT available for periods ending after 31 Dec 2026",
            "boundary": True,
        },
        {
            "id": "SBR-06",
            "area": "SMALL_BUSINESS_RELIEF",
            "description": "Entity elected out of SBR — does not qualify regardless of revenue",
            "input": {"revenue_aed": "500000", "tax_period_end": "2025-12-31", "sbr_election": False},
            "expected": {"qualifies": False},
            "rule": "SBR is an election; entity can opt out",
            "boundary": False,
        },
    ]


def build_qfzp_cases() -> List[Dict]:
    """
    QFZP (Qualifying Free Zone Person) test cases.
    0% on qualifying income; 9% on non-qualifying income above CT threshold.
    """
    return [
        {
            "id": "QFZP-01",
            "area": "QFZP",
            "description": "All income is qualifying — zero CT",
            "input": {"qualifying_income_aed": "5000000", "non_qualifying_income_aed": "0"},
            "expected": {"ct_on_qualifying": "0.00", "ct_on_non_qualifying": "0.00", "total_ct": "0.00"},
            "rule": "0% on all qualifying income for QFZP",
            "boundary": False,
        },
        {
            "id": "QFZP-02",
            "area": "QFZP",
            "description": "Non-qualifying income below CT threshold — zero CT on both",
            "input": {"qualifying_income_aed": "2000000", "non_qualifying_income_aed": "300000"},
            "expected": {"ct_on_qualifying": "0.00", "ct_on_non_qualifying": "0.00", "total_ct": "0.00"},
            "rule": "Non-qualifying income ≤ AED 375,000 → 0% CT applies",
            "boundary": False,
        },
        {
            "id": "QFZP-03",
            "area": "QFZP",
            "description": "Non-qualifying income above CT threshold — 9% on excess only",
            "input": {"qualifying_income_aed": "3000000", "non_qualifying_income_aed": "1000000"},
            "expected": {"ct_on_qualifying": "0.00", "ct_on_non_qualifying": "56250.00", "total_ct": "56250.00"},
            "rule": "9% on non-qualifying income above AED 375,000",
            "boundary": False,
        },
        {
            "id": "QFZP-04",
            "area": "QFZP",
            "description": "Non-qualifying income exactly at CT threshold — still zero CT",
            "input": {"qualifying_income_aed": "1000000", "non_qualifying_income_aed": "375000"},
            "expected": {"ct_on_qualifying": "0.00", "ct_on_non_qualifying": "0.00", "total_ct": "0.00"},
            "rule": "CT threshold is inclusive; AED 375,000 non-qualifying → 0%",
            "boundary": True,
        },
        {
            "id": "QFZP-05",
            "area": "QFZP",
            "description": "De minimis: non-qualifying income > 5% of total income — QFZP status lost",
            "input": {
                "qualifying_income_aed": "900000",
                "non_qualifying_income_aed": "100000",
                "de_minimis_breached": True,
            },
            "expected": {"qfzp_status": "LOST", "note": "All income taxed as regular taxable person"},
            "rule": "De minimis threshold breach → entire QFZP benefit lost for the period",
            "boundary": True,
        },
    ]


def build_vat_calculation_cases() -> List[Dict]:
    """
    VAT calculation test cases: standard, zero-rated, exempt, out-of-scope.
    Includes rounding edge cases.
    """
    return [
        {
            "id": "VAT-CALC-01",
            "area": "VAT_CALCULATION",
            "description": "Standard-rated (S): clean round amount",
            "input": {"net_amount_aed": "10000.00", "vat_category": "S"},
            "expected": {"vat_amount_aed": "500.00"},
            "rule": "5% × AED 10,000 = AED 500.00",
            "boundary": False,
        },
        {
            "id": "VAT-CALC-02",
            "area": "VAT_CALCULATION",
            "description": "Standard-rated (S): amount producing recurring decimal",
            "input": {"net_amount_aed": "100.00", "vat_category": "S"},
            "expected": {"vat_amount_aed": "5.00"},
            "rule": "5% × AED 100.00 = AED 5.00",
            "boundary": False,
        },
        {
            "id": "VAT-CALC-03",
            "area": "VAT_CALCULATION",
            "description": "Standard-rated (S): AED 1.00 — minimum meaningful invoice",
            "input": {"net_amount_aed": "1.00", "vat_category": "S"},
            "expected": {"vat_amount_aed": "0.05"},
            "rule": "5% × AED 1.00 = AED 0.05",
            "boundary": True,
        },
        {
            "id": "VAT-CALC-04",
            "area": "VAT_CALCULATION",
            "description": "Standard-rated (S): amount that rounds to 3 decimal places before rounding",
            "input": {"net_amount_aed": "33.33", "vat_category": "S"},
            "expected": {"vat_amount_aed": "1.67"},
            "rule": "5% × 33.33 = 1.6665 → rounds to 1.67 (half-up)",
            "boundary": True,
        },
        {
            "id": "VAT-CALC-05",
            "area": "VAT_CALCULATION",
            "description": "Zero-rated (Z): VAT must be AED 0.00",
            "input": {"net_amount_aed": "50000.00", "vat_category": "Z"},
            "expected": {"vat_amount_aed": "0.00"},
            "rule": "Zero-rated supply: 0% — supply is taxable but VAT = 0",
            "boundary": False,
        },
        {
            "id": "VAT-CALC-06",
            "area": "VAT_CALCULATION",
            "description": "Exempt (E): VAT must be AED 0.00; no input tax recovery",
            "input": {"net_amount_aed": "20000.00", "vat_category": "E"},
            "expected": {"vat_amount_aed": "0.00", "input_tax_recoverable": False},
            "rule": "Exempt supply: 0% — supply is not taxable; cannot recover input VAT",
            "boundary": False,
        },
        {
            "id": "VAT-CALC-07",
            "area": "VAT_CALCULATION",
            "description": "Out of scope (OS): VAT must be AED 0.00; excluded from VAT return",
            "input": {"net_amount_aed": "5000.00", "vat_category": "OS"},
            "expected": {"vat_amount_aed": "0.00", "included_in_vat_return": False},
            "rule": "Out-of-scope supply: not subject to UAE VAT; excluded from Box 1",
            "boundary": False,
        },
        {
            "id": "VAT-CALC-08",
            "area": "VAT_CALCULATION",
            "description": "Large amount — rounding on AED 999,999.99",
            "input": {"net_amount_aed": "999999.99", "vat_category": "S"},
            "expected": {"vat_amount_aed": "50000.00"},
            "rule": "5% × 999,999.99 = 49,999.9995 → rounds to 50,000.00",
            "boundary": True,
        },
        {
            "id": "VAT-CALC-09",
            "area": "VAT_CALCULATION",
            "description": "Invalid category code — must raise error",
            "input": {"net_amount_aed": "1000.00", "vat_category": "X"},
            "expected": {"error": "ValueError — 'X' is not a valid UAE VAT category"},
            "rule": "Only S, Z, E, OS are valid UAE VAT category codes",
            "boundary": False,
        },
        {
            "id": "VAT-CALC-10",
            "area": "VAT_CALCULATION",
            "description": "Negative net amount (credit note, standard-rated)",
            "input": {"net_amount_aed": "-1000.00", "vat_category": "S"},
            "expected": {"vat_amount_aed": "-50.00"},
            "rule": "Credit notes carry negative VAT; reversal of original invoice",
            "boundary": False,
        },
    ]


def build_vat_registration_cases() -> List[Dict]:
    """
    VAT registration threshold test cases.
    Mandatory: > AED 375,000 in taxable supplies in past 12 months.
    Voluntary: > AED 187,500.
    """
    return [
        {
            "id": "VAT-REG-01",
            "area": "VAT_REGISTRATION",
            "description": "Supplies well below voluntary threshold — not required",
            "input": {"taxable_supplies_12m_aed": "100000"},
            "expected": {"registration_status": "NOT_REQUIRED"},
            "rule": "Supplies ≤ AED 187,500 → no registration obligation or eligibility",
            "boundary": False,
        },
        {
            "id": "VAT-REG-02",
            "area": "VAT_REGISTRATION",
            "description": "Supplies just above voluntary threshold (AED 187,501)",
            "input": {"taxable_supplies_12m_aed": "187501"},
            "expected": {"registration_status": "VOLUNTARY_ELIGIBLE"},
            "rule": "AED 187,500 < supplies ≤ AED 375,000 → voluntary registration eligible",
            "boundary": True,
        },
        {
            "id": "VAT-REG-03",
            "area": "VAT_REGISTRATION",
            "description": "Supplies exactly at voluntary threshold (AED 187,500)",
            "input": {"taxable_supplies_12m_aed": "187500"},
            "expected": {"registration_status": "NOT_REQUIRED"},
            "rule": "AED 187,500 is the lower bound for voluntary eligibility (exclusive)",
            "boundary": True,
        },
        {
            "id": "VAT-REG-04",
            "area": "VAT_REGISTRATION",
            "description": "Supplies exactly at mandatory threshold (AED 375,000)",
            "input": {"taxable_supplies_12m_aed": "375000"},
            "expected": {"registration_status": "VOLUNTARY_ELIGIBLE"},
            "rule": "Mandatory threshold is exceeded at > AED 375,000, not at exactly AED 375,000",
            "boundary": True,
        },
        {
            "id": "VAT-REG-05",
            "area": "VAT_REGISTRATION",
            "description": "Supplies one dirham above mandatory threshold (AED 375,001)",
            "input": {"taxable_supplies_12m_aed": "375001"},
            "expected": {"registration_status": "MANDATORY"},
            "rule": "Supplies > AED 375,000 → mandatory registration required",
            "boundary": True,
        },
        {
            "id": "VAT-REG-06",
            "area": "VAT_REGISTRATION",
            "description": "Supplies well above mandatory threshold (AED 2,000,000)",
            "input": {"taxable_supplies_12m_aed": "2000000"},
            "expected": {"registration_status": "MANDATORY"},
            "rule": "Supplies > AED 375,000 → mandatory",
            "boundary": False,
        },
    ]


# ---------------------------------------------------------------------------
# Matrix assembler
# ---------------------------------------------------------------------------


def build_full_matrix() -> Dict:
    """Build the complete test matrix across all UAE tax areas."""
    ct_cases = build_ct_threshold_cases()
    sbr_cases = build_sbr_cases()
    qfzp_cases = build_qfzp_cases()
    vat_calc_cases = build_vat_calculation_cases()
    vat_reg_cases = build_vat_registration_cases()

    all_cases = ct_cases + sbr_cases + qfzp_cases + vat_calc_cases + vat_reg_cases

    return {
        "title": "UAE Tax Scenario Test Matrix",
        "jurisdiction": "UAE (FTA)",
        "law_references": [
            "Federal Decree-Law No. 47 of 2022 (Corporate Tax)",
            "Federal Decree-Law No. 8 of 2017 (VAT)",
        ],
        "disclaimer": (
            "Verify all thresholds and rates against current FTA guidance before "
            "relying on this matrix for compliance sign-off. Tax law changes."
        ),
        "summary": {
            "total_cases": len(all_cases),
            "boundary_cases": sum(1 for c in all_cases if c.get("boundary")),
            "by_area": {
                "CT_THRESHOLD": len(ct_cases),
                "SMALL_BUSINESS_RELIEF": len(sbr_cases),
                "QFZP": len(qfzp_cases),
                "VAT_CALCULATION": len(vat_calc_cases),
                "VAT_REGISTRATION": len(vat_reg_cases),
            },
        },
        "cases": all_cases,
    }


# ---------------------------------------------------------------------------
# Printers
# ---------------------------------------------------------------------------


def print_section(title: str, cases: List[Dict]) -> None:
    """Print one section of the matrix as an ASCII table."""
    sep = "-" * 80
    print(f"\n{'=' * 80}")
    print(f"  {title}  ({len(cases)} cases)")
    print("=" * 80)
    print(f"  {'ID':<12} {'BOUNDARY':<10} {'Description':<45} {'Expected'}")
    print(sep)
    for case in cases:
        boundary_flag = "BOUNDARY" if case.get("boundary") else ""
        expected_str = json.dumps(case["expected"])
        if len(expected_str) > 30:
            expected_str = expected_str[:27] + "..."
        desc = case["description"]
        if len(desc) > 43:
            desc = desc[:40] + "..."
        print(f"  {case['id']:<12} {boundary_flag:<10} {desc:<45} {expected_str}")


def print_matrix(matrix: Dict) -> None:
    """Print the full test matrix to stdout."""
    print(f"\n{'#' * 80}")
    print(f"  {matrix['title']}")
    print(f"  Jurisdiction: {matrix['jurisdiction']}")
    print(f"  {matrix['disclaimer']}")
    print(f"{'#' * 80}")

    s = matrix["summary"]
    print(
        f"\n  Total test cases : {s['total_cases']}"
        f"\n  Boundary cases   : {s['boundary_cases']}"
    )
    for area, count in s["by_area"].items():
        print(f"    {area:<30} {count} cases")

    # Group cases by area and print each section
    areas = [
        ("CT Threshold (0% / 9%)", "CT_THRESHOLD"),
        ("Small Business Relief", "SMALL_BUSINESS_RELIEF"),
        ("Free Zone QFZP", "QFZP"),
        ("VAT Calculation", "VAT_CALCULATION"),
        ("VAT Registration Thresholds", "VAT_REGISTRATION"),
    ]
    for title, area_key in areas:
        section_cases = [c for c in matrix["cases"] if c["area"] == area_key]
        print_section(title, section_cases)

    print(f"\n{'#' * 80}\n")


def print_pytest_stubs(matrix: Dict, language: str = "python") -> None:
    """Print pytest-style test stubs for all cases."""
    print("\n# ---- pytest stubs (Python) ----\n")
    print("import pytest")
    print("from decimal import Decimal\n")

    for case in matrix["cases"]:
        fn_name = case["id"].lower().replace("-", "_")
        print(f"def test_{fn_name}():")
        print(f'    """')
        print(f'    {case["description"]}')
        print(f'    Rule: {case["rule"]}')
        print(f'    """')

        # Print inputs as comments
        for k, v in case["input"].items():
            print(f"    {k} = {repr(v)}")

        # Print expected as comment
        print(f"    # Expected: {json.dumps(case['expected'])}")
        print(f"    # TODO: call your implementation and assert the expected output")
        print(f"    pass\n")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> None:
    """
    Build and display the complete UAE tax scenario test matrix,
    then save it as test_matrix.json in the current directory.
    """
    print("Finanshels — UAE Tax Scenario Test Matrix Generator")

    matrix = build_full_matrix()
    print_matrix(matrix)

    # Save JSON export
    output_path = os.path.join(os.path.dirname(__file__), "test_matrix.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(matrix, f, indent=2, default=str)
    print(f"JSON matrix saved to: {output_path}")

    # Print pytest stubs
    print_pytest_stubs(matrix)


if __name__ == "__main__":
    main()
