"""
benchmark-queries.py
--------------------
Finanshels — Benchmark Analyzer (Tax & Finance)

Compares client or firm metrics against sector benchmark ranges and prints
a gap analysis report. Benchmark data is Finanshels internal reference data
— indicative only, not published FTA statistics.

Metrics covered:
  - Gross margin %
  - Net margin %
  - Operating expense ratio %
  - VAT recovery ratio % (input / output)
  - Effective CT rate % (indicative, pre-adjustment)

For `firm` subjects, covers compliance KPIs:
  - On-Time Filing Rate (OTFR)
  - Registration Completion Rate (RCR)
  - Return Accuracy Rate (RAR)
  - Deadline Miss Rate (DMR)
  - Portfolio Coverage Rate (PCR)

Runs standalone with synthetic subject data.

Usage:
    python3 benchmark-queries.py

stdlib only — no pip dependencies.
"""

from dataclasses import dataclass
from typing import Optional


# ---------------------------------------------------------------------------
# Data models
# ---------------------------------------------------------------------------

@dataclass
class BenchmarkRange:
    """Q1, median, Q3 reference range for one metric."""
    metric: str
    unit: str          # "%" or "ratio"
    q1: float
    median: float
    q3: float
    lower_is_better: bool = False  # True for expense ratios, CT rate, DMR


@dataclass
class SubjectMetric:
    """Actual value for one metric from the subject being benchmarked."""
    metric: str
    value: float


@dataclass
class GapResult:
    """Computed gap analysis for one metric."""
    metric: str
    unit: str
    subject_value: float
    q1: float
    median: float
    q3: float
    position: str          # ABOVE | WITHIN | BELOW
    gap_to_median: float
    upside_to_q3: float
    lower_is_better: bool


# ---------------------------------------------------------------------------
# Benchmark reference data
# Finanshels internal reference ranges — indicative only.
# Verify against authoritative sector data before client use.
# ---------------------------------------------------------------------------

FINANCIAL_BENCHMARKS: dict[str, list[BenchmarkRange]] = {
    "professional_services": [
        BenchmarkRange("Gross Margin %",      "%",  50.0, 62.0, 75.0),
        BenchmarkRange("Net Margin %",         "%",  12.0, 18.0, 28.0),
        BenchmarkRange("OpEx Ratio %",         "%",  30.0, 38.0, 48.0, lower_is_better=True),
        BenchmarkRange("VAT Recovery %",       "%",  20.0, 32.0, 50.0),
        BenchmarkRange("Effective CT Rate %",  "%",   3.0,  6.0,  9.0, lower_is_better=True),
    ],
    "trading_retail": [
        BenchmarkRange("Gross Margin %",      "%",  18.0, 28.0, 40.0),
        BenchmarkRange("Net Margin %",         "%",   3.0,  7.0, 14.0),
        BenchmarkRange("OpEx Ratio %",         "%",  15.0, 20.0, 28.0, lower_is_better=True),
        BenchmarkRange("VAT Recovery %",       "%",  55.0, 68.0, 80.0),
        BenchmarkRange("Effective CT Rate %",  "%",   2.0,  4.0,  8.0, lower_is_better=True),
    ],
    "technology": [
        BenchmarkRange("Gross Margin %",      "%",  55.0, 68.0, 80.0),
        BenchmarkRange("Net Margin %",         "%",   8.0, 15.0, 25.0),
        BenchmarkRange("OpEx Ratio %",         "%",  40.0, 50.0, 62.0, lower_is_better=True),
        BenchmarkRange("VAT Recovery %",       "%",  25.0, 40.0, 60.0),
        BenchmarkRange("Effective CT Rate %",  "%",   2.0,  5.0,  9.0, lower_is_better=True),
    ],
    "hospitality_food": [
        BenchmarkRange("Gross Margin %",      "%",  55.0, 65.0, 75.0),
        BenchmarkRange("Net Margin %",         "%",   5.0, 10.0, 18.0),
        BenchmarkRange("OpEx Ratio %",         "%",  45.0, 54.0, 65.0, lower_is_better=True),
        BenchmarkRange("VAT Recovery %",       "%",  30.0, 45.0, 60.0),
        BenchmarkRange("Effective CT Rate %",  "%",   2.0,  5.0,  8.0, lower_is_better=True),
    ],
    "construction_contracting": [
        BenchmarkRange("Gross Margin %",      "%",  12.0, 20.0, 32.0),
        BenchmarkRange("Net Margin %",         "%",   3.0,  8.0, 15.0),
        BenchmarkRange("OpEx Ratio %",         "%",  10.0, 14.0, 20.0, lower_is_better=True),
        BenchmarkRange("VAT Recovery %",       "%",  50.0, 65.0, 80.0),
        BenchmarkRange("Effective CT Rate %",  "%",   2.0,  5.0,  8.0, lower_is_better=True),
    ],
    "general": [
        BenchmarkRange("Gross Margin %",      "%",  20.0, 40.0, 60.0),
        BenchmarkRange("Net Margin %",         "%",   4.0, 10.0, 20.0),
        BenchmarkRange("OpEx Ratio %",         "%",  15.0, 30.0, 50.0, lower_is_better=True),
        BenchmarkRange("VAT Recovery %",       "%",  25.0, 45.0, 65.0),
        BenchmarkRange("Effective CT Rate %",  "%",   2.0,  5.0,  9.0, lower_is_better=True),
    ],
}

FIRM_KPI_BENCHMARKS: list[BenchmarkRange] = [
    BenchmarkRange("OTFR %",  "%", 90.0, 95.0,  98.0),
    BenchmarkRange("RCR %",   "%", 92.0, 97.0,  99.0),
    BenchmarkRange("RAR %",   "%", 92.0, 96.0,  99.0),
    BenchmarkRange("DMR %",   "%",  0.5,  2.0,   4.0, lower_is_better=True),
    BenchmarkRange("PCR %",   "%", 95.0, 99.0, 100.0),
]


# ---------------------------------------------------------------------------
# Gap analysis engine
# ---------------------------------------------------------------------------

def classify_position(
    value: float,
    q1: float,
    q3: float,
    lower_is_better: bool,
) -> str:
    """Return ABOVE / WITHIN / BELOW relative to the benchmark band."""
    if lower_is_better:
        if value < q1:
            return "ABOVE"   # better than Q1 (low side is good)
        elif value <= q3:
            return "WITHIN"
        else:
            return "BELOW"   # worse than Q3 (too high)
    else:
        if value > q3:
            return "ABOVE"
        elif value >= q1:
            return "WITHIN"
        else:
            return "BELOW"


def compute_gap(
    subject: SubjectMetric,
    benchmark: BenchmarkRange,
) -> GapResult:
    """Compute gap analysis for one metric."""
    position = classify_position(
        subject.value, benchmark.q1, benchmark.q3, benchmark.lower_is_better
    )
    gap_to_median = round(subject.value - benchmark.median, 1)
    upside_to_q3 = round(benchmark.q3 - subject.value, 1)

    return GapResult(
        metric=subject.metric,
        unit=benchmark.unit,
        subject_value=subject.value,
        q1=benchmark.q1,
        median=benchmark.median,
        q3=benchmark.q3,
        position=position,
        gap_to_median=gap_to_median,
        upside_to_q3=upside_to_q3,
        lower_is_better=benchmark.lower_is_better,
    )


def run_gap_analysis(
    subject_metrics: list[SubjectMetric],
    benchmarks: list[BenchmarkRange],
) -> list[GapResult]:
    """Match subject metrics to benchmarks and compute all gaps."""
    bench_map = {b.metric: b for b in benchmarks}
    results = []
    for sm in subject_metrics:
        if sm.metric in bench_map:
            results.append(compute_gap(sm, bench_map[sm.metric]))
        else:
            print(f"  [WARN] No benchmark found for metric: {sm.metric}")
    return results


def compute_overall_score(gaps: list[GapResult]) -> tuple[float, str]:
    """Score overall performance; return (score_pct, grade)."""
    if not gaps:
        return 0.0, "Underperforming"
    points = sum(2 if g.position == "ABOVE" else (1 if g.position == "WITHIN" else 0) for g in gaps)
    max_points = 2 * len(gaps)
    score = round(points / max_points * 100, 1)
    if score >= 80:
        grade = "Strong"
    elif score >= 60:
        grade = "Satisfactory"
    elif score >= 40:
        grade = "Needs Attention"
    else:
        grade = "Underperforming"
    return score, grade


def build_recommendations(gaps: list[GapResult]) -> tuple[list[str], list[str]]:
    """
    Return (strengths, recommendations).
    ABOVE metrics → strengths list.
    BELOW metrics → ranked recommendations (compliance/CT first).
    """
    strengths = []
    rec_candidates = []

    compliance_metrics = {"OTFR %", "RCR %", "RAR %", "DMR %", "PCR %", "Effective CT Rate %"}

    for g in gaps:
        if g.position == "ABOVE":
            direction = "below" if g.lower_is_better else "above"
            strengths.append(
                f"{g.metric}: {g.subject_value}{g.unit} is {direction} the top-quartile "
                f"benchmark ({g.q3}{g.unit}). Strong performance — maintain."
            )
        elif g.position == "BELOW":
            gap_abs = abs(g.gap_to_median)
            priority = 0 if g.metric in compliance_metrics else 1
            rec_candidates.append((priority, g, gap_abs))

    rec_candidates.sort(key=lambda x: (x[0], -x[2]))
    recommendations = []
    for _, g, gap_abs in rec_candidates[:5]:
        if g.lower_is_better:
            rec = (
                f"{g.metric} is {g.subject_value}{g.unit}, which is above the Q3 benchmark "
                f"({g.q3}{g.unit}) — {gap_abs:.1f}pp worse than median. "
                f"Review underlying drivers and target a reduction toward {g.median}{g.unit}."
            )
        else:
            rec = (
                f"{g.metric} is {g.subject_value}{g.unit}, which is below the Q1 benchmark "
                f"({g.q1}{g.unit}) — {gap_abs:.1f}pp below median. "
                f"Identify improvement levers to close the gap toward {g.median}{g.unit}."
            )
        recommendations.append(rec)

    return strengths, recommendations


# ---------------------------------------------------------------------------
# Report printing
# ---------------------------------------------------------------------------

def print_separator(char: str = "═", width: int = 100) -> None:
    print(char * width)


def print_report(
    subject_id: str,
    subject_type: str,
    sector: str,
    period: str,
    gaps: list[GapResult],
    score: float,
    grade: str,
    strengths: list[str],
    recommendations: list[str],
) -> None:
    print()
    print_separator()
    print("  FINANSHELS — BENCHMARK ANALYSIS REPORT")
    print(f"  Subject ID   : {subject_id}")
    print(f"  Subject Type : {subject_type.title()}")
    print(f"  Sector       : {sector.replace('_', ' ').title()}")
    print(f"  Period       : {period}")
    print_separator()

    print()
    print_separator("─")
    print("  OVERALL BENCHMARK SCORE")
    print_separator("─")
    print(f"  Score: {score:.1f} / 100    Grade: {grade}")
    print_separator("─")

    print()
    print_separator("─")
    print("  GAP ANALYSIS TABLE")
    print_separator("─")
    hdr = f"  {'Metric':<22} {'Subject':>8} {'Q1':>8} {'Median':>8} {'Q3':>8}  {'Position':<8} {'Gap/Med':>8} {'To Q3':>8}"
    print(hdr)
    print("  " + "─" * 80)
    for g in gaps:
        u = g.unit
        print(
            f"  {g.metric:<22} {g.subject_value:>7.1f}{u} {g.q1:>7.1f}{u} "
            f"{g.median:>7.1f}{u} {g.q3:>7.1f}{u}  {g.position:<8} "
            f"{g.gap_to_median:>+7.1f}{u} {g.upside_to_q3:>+7.1f}{u}"
        )
    print_separator("─")

    if strengths:
        print()
        print_separator("─")
        print("  STRENGTHS")
        print_separator("─")
        for s in strengths:
            print(f"  + {s}")
        print_separator("─")

    print()
    print_separator("─")
    print("  PRIORITISED RECOMMENDATIONS")
    print_separator("─")
    if recommendations:
        for i, rec in enumerate(recommendations, 1):
            print(f"  {i}. {rec}")
    else:
        print("  All metrics within or above benchmark ranges. No immediate action required.")
    print_separator("─")

    print()
    print_separator("─")
    print("  BENCHMARK DATA NOTE")
    print_separator("─")
    print("  Benchmarks are Finanshels internal reference ranges derived from aggregated")
    print("  anonymised client data and sector research. They are indicative only and do")
    print("  not represent published FTA statistics or official survey data.")
    print("  Confirm any material findings against authoritative sources before client use.")
    print("  Effective CT Rate comparisons are based on indicative (pre-adjustment) figures.")
    print_separator("─")
    print()
    print("  NOTE: Review by a qualified Finanshels team member required before sharing")
    print("  this report externally.")
    print()
    print_separator()


# ---------------------------------------------------------------------------
# Synthetic subject data and entry point
# ---------------------------------------------------------------------------

CLIENT_SUBJECT_METRICS = [
    SubjectMetric("Gross Margin %",     43.5),
    SubjectMetric("Net Margin %",       11.2),
    SubjectMetric("OpEx Ratio %",       29.0),
    SubjectMetric("VAT Recovery %",     38.0),
    SubjectMetric("Effective CT Rate %", 5.8),
]

FIRM_SUBJECT_METRICS = [
    SubjectMetric("OTFR %",  96.2),
    SubjectMetric("RCR %",   97.8),
    SubjectMetric("RAR %",   94.1),
    SubjectMetric("DMR %",    1.8),
    SubjectMetric("PCR %",  100.0),
]


def main() -> None:
    """Run benchmark analysis on synthetic data for both a client and the firm."""

    # --- Client benchmark: professional services ---
    sector = "professional_services"
    benchmarks = FINANCIAL_BENCHMARKS[sector]
    gaps = run_gap_analysis(CLIENT_SUBJECT_METRICS, benchmarks)
    score, grade = compute_overall_score(gaps)
    strengths, recommendations = build_recommendations(gaps)

    print_report(
        subject_id="CLIENT-DEMO-01",
        subject_type="client",
        sector=sector,
        period="FY 2024",
        gaps=gaps,
        score=score,
        grade=grade,
        strengths=strengths,
        recommendations=recommendations,
    )

    # --- Firm benchmark: compliance KPIs ---
    gaps_firm = run_gap_analysis(FIRM_SUBJECT_METRICS, FIRM_KPI_BENCHMARKS)
    score_firm, grade_firm = compute_overall_score(gaps_firm)
    strengths_firm, recommendations_firm = build_recommendations(gaps_firm)

    print_report(
        subject_id="FINANSHELS-FIRM",
        subject_type="firm",
        sector="professional_services",
        period="Q4 2024",
        gaps=gaps_firm,
        score=score_firm,
        grade=grade_firm,
        strengths=strengths_firm,
        recommendations=recommendations_firm,
    )


if __name__ == "__main__":
    main()
