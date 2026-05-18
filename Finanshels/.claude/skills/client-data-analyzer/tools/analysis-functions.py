"""
analysis-functions.py
---------------------
Finanshels — Client Financial Data Analyzer

Provides runnable analysis functions for client financial data:
  - Revenue trend and CAGR
  - Profitability ratios (gross margin, OpEx ratio, net margin)
  - VAT input/output pattern analysis
  - Corporate Tax indicative estimate (UAE CT tiers)
  - Summary statistics (mean, median, min, max, volatility)
  - Visualization-ready JSON output

Runs standalone with synthetic data.

Usage:
    python3 analysis-functions.py

stdlib only — no pip dependencies.
"""

import json
import statistics
from dataclasses import dataclass, field
from typing import Optional


# ---------------------------------------------------------------------------
# UAE CT constants (verify against current FTA guidance before use)
# ---------------------------------------------------------------------------

CT_ZERO_RATE_THRESHOLD_AED = 375_000   # 0% on income up to this
CT_STANDARD_RATE = 0.09                 # 9% above threshold
SBR_REVENUE_CEILING_AED = 3_000_000    # Small Business Relief ceiling
VAT_MANDATORY_THRESHOLD_AED = 375_000  # mandatory VAT registration
VAT_VOLUNTARY_THRESHOLD_AED = 187_500  # voluntary VAT registration
THRESHOLD_WARNING_PCT = 0.20           # warn if within 20% of a threshold


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------

@dataclass
class PeriodRecord:
    """Single-period financial record for one client."""
    period_label: str            # e.g. "Q1 2024"
    revenue: float               # AED
    cost_of_sales: float         # AED
    operating_expenses: float    # AED
    finance_costs: float         # AED
    output_vat: float            # VAT charged on sales (AED)
    input_vat: float             # VAT recoverable on purchases (AED)


@dataclass
class PeriodResult:
    """Computed metrics for one period."""
    period_label: str
    revenue: float
    gross_profit: float
    ebitda: float
    net_profit: float
    gross_margin_pct: Optional[float]
    opex_ratio_pct: Optional[float]
    net_margin_pct: Optional[float]
    output_vat: float
    input_vat: float
    net_vat_payable: float
    vat_recovery_pct: Optional[float]
    qoq_revenue_growth_pct: Optional[float] = None
    yoy_revenue_growth_pct: Optional[float] = None


# ---------------------------------------------------------------------------
# Synthetic sample data
# ---------------------------------------------------------------------------

SAMPLE_DATA: list[PeriodRecord] = [
    PeriodRecord("Q1 2023", 280_000,  120_000,  80_000,  5_000,  14_000,  6_000),
    PeriodRecord("Q2 2023", 310_000,  135_000,  85_000,  5_000,  15_500,  7_000),
    PeriodRecord("Q3 2023", 295_000,  128_000,  82_000,  5_000,  14_750,  6_500),
    PeriodRecord("Q4 2023", 340_000,  150_000,  90_000,  5_500,  17_000,  8_000),
    PeriodRecord("Q1 2024", 365_000,  158_000,  95_000,  6_000,  18_250,  9_000),
    PeriodRecord("Q2 2024", 420_000,  182_000, 105_000,  6_000,  21_000, 10_500),
    PeriodRecord("Q3 2024", 390_000,  168_000,  98_000,  6_000,  19_500,  9_800),
    PeriodRecord("Q4 2024", 460_000,  200_000, 112_000,  6_500,  23_000, 11_000),
]


# ---------------------------------------------------------------------------
# Core computation
# ---------------------------------------------------------------------------

def compute_period_metrics(records: list[PeriodRecord]) -> list[PeriodResult]:
    """Compute derived metrics for each period; attach QoQ and YoY growth."""
    results: list[PeriodResult] = []

    for i, r in enumerate(records):
        gross_profit = r.revenue - r.cost_of_sales
        ebitda = gross_profit - r.operating_expenses
        net_profit = ebitda - r.finance_costs
        net_vat = r.output_vat - r.input_vat

        gross_margin = (gross_profit / r.revenue * 100) if r.revenue else None
        opex_ratio = (r.operating_expenses / r.revenue * 100) if r.revenue else None
        net_margin = (net_profit / r.revenue * 100) if r.revenue else None
        vat_recovery = (r.input_vat / r.output_vat * 100) if r.output_vat else None

        results.append(PeriodResult(
            period_label=r.period_label,
            revenue=r.revenue,
            gross_profit=gross_profit,
            ebitda=ebitda,
            net_profit=net_profit,
            gross_margin_pct=round(gross_margin, 1) if gross_margin is not None else None,
            opex_ratio_pct=round(opex_ratio, 1) if opex_ratio is not None else None,
            net_margin_pct=round(net_margin, 1) if net_margin is not None else None,
            output_vat=r.output_vat,
            input_vat=r.input_vat,
            net_vat_payable=net_vat,
            vat_recovery_pct=round(vat_recovery, 1) if vat_recovery is not None else None,
        ))

    # QoQ growth
    for i in range(1, len(results)):
        prior = results[i - 1].revenue
        current = results[i].revenue
        if prior and prior != 0:
            results[i].qoq_revenue_growth_pct = round((current - prior) / prior * 100, 1)

    # YoY growth (4 periods back for quarterly data)
    step = 4
    for i in range(step, len(results)):
        prior = results[i - step].revenue
        current = results[i].revenue
        if prior and prior != 0:
            results[i].yoy_revenue_growth_pct = round((current - prior) / prior * 100, 1)

    return results


def compute_cagr(start_revenue: float, end_revenue: float, years: float) -> Optional[float]:
    """Compound Annual Growth Rate."""
    if start_revenue <= 0 or years <= 0:
        return None
    return round(((end_revenue / start_revenue) ** (1.0 / years) - 1) * 100, 2)


def compute_summary_stats(values: list[float], label: str) -> dict:
    """Return mean, median, min, max, and coefficient of variation."""
    if not values:
        return {}
    mean = statistics.mean(values)
    cv = (statistics.stdev(values) / mean * 100) if len(values) > 1 and mean != 0 else 0.0
    volatility = "low" if cv < 15 else ("medium" if cv < 30 else "high")
    return {
        "label": label,
        "mean": round(mean, 2),
        "median": round(statistics.median(values), 2),
        "min": round(min(values), 2),
        "max": round(max(values), 2),
        "coefficient_of_variation_pct": round(cv, 1),
        "volatility": volatility,
    }


def t12m_revenue(results: list[PeriodResult]) -> float:
    """Sum of revenue for the last 4 quarters (trailing 12 months)."""
    last_four = results[-4:] if len(results) >= 4 else results
    return sum(r.revenue for r in last_four)


def check_vat_thresholds(t12m: float) -> list[str]:
    """Return threshold warning messages for VAT registration."""
    warnings = []
    if t12m >= VAT_MANDATORY_THRESHOLD_AED:
        warnings.append(
            f"T12M taxable supplies AED {t12m:,.0f} EXCEED the mandatory VAT registration "
            f"threshold (AED {VAT_MANDATORY_THRESHOLD_AED:,}). Client must be VAT-registered."
        )
    elif t12m >= VAT_MANDATORY_THRESHOLD_AED * (1 - THRESHOLD_WARNING_PCT):
        warnings.append(
            f"T12M taxable supplies AED {t12m:,.0f} are within 20% of the mandatory "
            f"VAT registration threshold (AED {VAT_MANDATORY_THRESHOLD_AED:,}). Monitor closely."
        )
    elif t12m >= VAT_VOLUNTARY_THRESHOLD_AED:
        warnings.append(
            f"T12M taxable supplies AED {t12m:,.0f} exceed the voluntary VAT registration "
            f"threshold (AED {VAT_VOLUNTARY_THRESHOLD_AED:,}). Voluntary registration may be beneficial."
        )
    return warnings


def estimate_ct_liability(net_profit: float, is_free_zone: bool = False) -> dict:
    """
    Indicative CT liability based on net profit.
    PRE-ADJUSTMENT only — does not account for disallowable expenses,
    exempt income, related-party adjustments, or QFZP qualifying income.
    Requires practitioner review before use.
    """
    if net_profit <= 0:
        return {
            "net_profit_aed": net_profit,
            "indicative_taxable_income_aed": 0,
            "ct_liability_aed": 0,
            "zero_rate_applied_aed": 0,
            "nine_pct_applied_aed": 0,
            "small_business_relief_note": "",
            "free_zone_note": "Free zone: QFZP determination required by practitioner." if is_free_zone else "",
            "caveat": "Pre-adjustment estimate. Requires practitioner sign-off.",
        }

    taxable_income = net_profit  # indicative only
    zero_band = min(taxable_income, CT_ZERO_RATE_THRESHOLD_AED)
    standard_band = max(0, taxable_income - CT_ZERO_RATE_THRESHOLD_AED)
    liability = standard_band * CT_STANDARD_RATE

    sbr_note = ""
    annual_revenue_proxy = net_profit * 4  # rough proxy for annual from quarterly
    if annual_revenue_proxy <= SBR_REVENUE_CEILING_AED:
        sbr_note = (
            "Revenue appears ≤ AED 3M — Small Business Relief may apply (for tax periods "
            "ending on or before 31 Dec 2026). Confirm with practitioner."
        )

    return {
        "net_profit_aed": round(net_profit, 2),
        "indicative_taxable_income_aed": round(taxable_income, 2),
        "ct_liability_aed": round(liability, 2),
        "zero_rate_applied_aed": round(zero_band, 2),
        "nine_pct_applied_aed": round(standard_band, 2),
        "small_business_relief_note": sbr_note,
        "free_zone_note": "Free zone: QFZP qualifying income determination required by practitioner." if is_free_zone else "",
        "caveat": "Pre-adjustment estimate. Does not account for disallowable expenses, exempt income, or TP adjustments. Requires practitioner sign-off.",
    }


def detect_vat_anomalies(results: list[PeriodResult]) -> list[str]:
    """Flag unusual VAT patterns for practitioner review."""
    flags = []
    for i, r in enumerate(results):
        if r.output_vat == 0 and r.revenue > 0:
            flags.append(
                f"{r.period_label}: Zero output VAT despite non-zero revenue (AED {r.revenue:,.0f}). "
                "Confirm whether revenue is zero-rated, exempt, or a filing gap exists."
            )
        if r.vat_recovery_pct is not None and r.vat_recovery_pct > 90:
            flags.append(
                f"{r.period_label}: High VAT recovery ratio {r.vat_recovery_pct}% — "
                "client may be in a VAT refund position. Review input VAT claims."
            )
        if i > 0:
            prev = results[i - 1]
            if prev.net_vat_payable > 0:
                jump = (r.net_vat_payable - prev.net_vat_payable) / prev.net_vat_payable * 100
                if jump > 50 and (r.qoq_revenue_growth_pct is None or r.qoq_revenue_growth_pct < 20):
                    flags.append(
                        f"{r.period_label}: Net VAT payable jumped {jump:.0f}% QoQ without a "
                        "proportionate revenue increase. Review for correct coding."
                    )
    return flags


def build_visualization_json(results: list[PeriodResult]) -> str:
    """Build a JSON-ready dict of chart data arrays."""
    data = {
        "periods": [r.period_label for r in results],
        "revenue_aed": [r.revenue for r in results],
        "gross_margin_pct": [r.gross_margin_pct for r in results],
        "net_margin_pct": [r.net_margin_pct for r in results],
        "vat_output_aed": [r.output_vat for r in results],
        "vat_input_aed": [r.input_vat for r in results],
        "vat_net_payable_aed": [r.net_vat_payable for r in results],
        "qoq_revenue_growth_pct": [r.qoq_revenue_growth_pct for r in results],
    }
    return json.dumps(data, indent=2)


# ---------------------------------------------------------------------------
# Report printing helpers
# ---------------------------------------------------------------------------

def fmt_aed(value: float) -> str:
    return f"AED {value:>14,.0f}"


def fmt_pct(value: Optional[float]) -> str:
    return f"{value:>6.1f}%" if value is not None else "    N/A"


def print_section(title: str) -> None:
    print()
    print("═" * 70)
    print(f"  {title}")
    print("═" * 70)


def main() -> None:
    """Run full analysis on synthetic data and print a formatted report."""
    client_id = "CLIENT-DEMO"
    is_free_zone = False

    results = compute_period_metrics(SAMPLE_DATA)

    t12m = t12m_revenue(results)
    last_net_profit = results[-1].net_profit
    ct = estimate_ct_liability(last_net_profit, is_free_zone=is_free_zone)

    revenues = [r.revenue for r in results]
    gm_vals = [r.gross_margin_pct for r in results if r.gross_margin_pct is not None]
    nm_vals = [r.net_margin_pct for r in results if r.net_margin_pct is not None]

    cagr = compute_cagr(results[0].revenue, results[-1].revenue, years=len(results) / 4)
    vat_warnings = check_vat_thresholds(t12m)
    vat_anomalies = detect_vat_anomalies(results)

    # Header
    print()
    print("=" * 70)
    print("  FINANSHELS — CLIENT FINANCIAL ANALYSIS")
    print(f"  Client ID : {client_id}")
    print(f"  Period    : {results[0].period_label} – {results[-1].period_label}")
    print("=" * 70)

    # Revenue trend
    print_section("REVENUE TREND")
    print(f"  {'Period':<10} {'Revenue (AED)':>14}  {'QoQ%':>7}  {'YoY%':>7}")
    print("  " + "─" * 44)
    for r in results:
        qoq = fmt_pct(r.qoq_revenue_growth_pct)
        yoy = fmt_pct(r.yoy_revenue_growth_pct)
        print(f"  {r.period_label:<10} {r.revenue:>14,.0f}  {qoq}  {yoy}")
    print(f"\n  T12M Revenue : {fmt_aed(t12m)}")
    if cagr is not None:
        print(f"  CAGR         : {cagr}% over {len(results)/4:.1f} years")

    # Revenue summary stats
    rev_stats = compute_summary_stats(revenues, "Revenue")
    print(f"\n  Summary — Revenue: mean {fmt_aed(rev_stats['mean'])} | "
          f"median {fmt_aed(rev_stats['median'])} | "
          f"volatility {rev_stats['volatility']} (CV {rev_stats['coefficient_of_variation_pct']}%)")

    # Profitability ratios
    print_section("PROFITABILITY RATIOS")
    print(f"  {'Period':<10} {'Gross Margin':>13} {'OpEx Ratio':>11} {'Net Margin':>11}")
    print("  " + "─" * 50)
    for r in results:
        print(f"  {r.period_label:<10} {fmt_pct(r.gross_margin_pct):>13} "
              f"{fmt_pct(r.opex_ratio_pct):>11} {fmt_pct(r.net_margin_pct):>11}")

    gm_stats = compute_summary_stats(gm_vals, "Gross Margin%")
    nm_stats = compute_summary_stats(nm_vals, "Net Margin%")
    print(f"\n  Gross Margin — mean {gm_stats['mean']:.1f}% | min {gm_stats['min']:.1f}% | max {gm_stats['max']:.1f}%")
    print(f"  Net Margin   — mean {nm_stats['mean']:.1f}% | min {nm_stats['min']:.1f}% | max {nm_stats['max']:.1f}%")

    # VAT pattern
    print_section("VAT INPUT / OUTPUT PATTERN")
    print(f"  {'Period':<10} {'Output VAT':>12} {'Input VAT':>12} {'Net Payable':>12} {'Recovery%':>10}")
    print("  " + "─" * 54)
    for r in results:
        print(f"  {r.period_label:<10} {r.output_vat:>12,.0f} {r.input_vat:>12,.0f} "
              f"{r.net_vat_payable:>12,.0f} {fmt_pct(r.vat_recovery_pct):>10}")
    print(f"\n  T12M Taxable Supplies: {fmt_aed(t12m)}")
    for w in vat_warnings:
        print(f"  ⚑ {w}")
    if vat_anomalies:
        print("\n  VAT Anomalies:")
        for a in vat_anomalies:
            print(f"  ⚑ {a}")

    # CT estimate
    print_section("CORPORATE TAX INDICATIVE ESTIMATE (most recent period)")
    print(f"  Net Profit (most recent period)  : {fmt_aed(ct['net_profit_aed'])}")
    print(f"  Indicative Taxable Income        : {fmt_aed(ct['indicative_taxable_income_aed'])}")
    print(f"  0% tier (≤ AED {CT_ZERO_RATE_THRESHOLD_AED:,})         : {fmt_aed(ct['zero_rate_applied_aed'])}")
    print(f"  9% tier (above AED {CT_ZERO_RATE_THRESHOLD_AED:,})     : {fmt_aed(ct['nine_pct_applied_aed'])}")
    print(f"  Indicative CT Liability          : {fmt_aed(ct['ct_liability_aed'])}")
    if ct["small_business_relief_note"]:
        print(f"\n  ⚑ {ct['small_business_relief_note']}")
    if ct["free_zone_note"]:
        print(f"\n  ⚑ {ct['free_zone_note']}")
    print(f"\n  ⚠ {ct['caveat']}")

    # Visualization JSON
    print_section("VISUALIZATION DATA (JSON-ready)")
    print(build_visualization_json(results))

    print()
    print("═" * 70)
    print("  NOTE: This analysis is a professional internal work product.")
    print("  Review by a qualified Finanshels team member required before")
    print("  sharing with clients. Verify all figures against current FTA guidance.")
    print("═" * 70)
    print()


if __name__ == "__main__":
    main()
