"""
metrics-framework.py
--------------------
Finanshels — Tax Compliance Metrics Dashboard

Computes firm-wide tax-compliance KPIs from engagement data:
  - On-Time Filing Rate (OTFR)
  - Registration Completion Rate (RCR)
  - Return Accuracy Rate (RAR)
  - Deadline Miss Count / Deadline Miss Rate (DMC/DMR)
  - Portfolio Coverage Rate (PCR)

Runs standalone with synthetic data. Swap SAMPLE_ENGAGEMENTS and
SAMPLE_CLIENTS for real data at runtime.

Usage:
    python3 metrics-framework.py

stdlib only — no pip dependencies.
"""

import csv
import io
from datetime import date, datetime
from typing import NamedTuple, Optional


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------

class Engagement(NamedTuple):
    client_id: str
    engagement_type: str       # VAT_RETURN | CT_RETURN | REGISTRATION
    due_date: date
    submitted_date: Optional[date]  # None if not yet submitted
    status: str                # submitted | pending | overdue | cancelled
    practitioner: str
    had_amendment: bool        # True if FTA queried / amendment filed within 30 days


# ---------------------------------------------------------------------------
# Synthetic sample data — replace with real CSV load in production
# ---------------------------------------------------------------------------

SAMPLE_ENGAGEMENTS_CSV = """\
client_id,engagement_type,due_date,submitted_date,status,practitioner,had_amendment
C001,VAT_RETURN,2024-10-28,2024-10-25,submitted,Layla,False
C002,VAT_RETURN,2024-10-28,2024-10-28,submitted,Layla,False
C003,VAT_RETURN,2024-10-28,2024-11-02,submitted,Ahmed,False
C004,VAT_RETURN,2024-10-28,,overdue,Ahmed,False
C005,CT_RETURN,2024-09-30,2024-09-29,submitted,Sara,True
C006,CT_RETURN,2024-09-30,2024-10-05,submitted,Sara,False
C007,CT_RETURN,2024-09-30,2024-09-28,submitted,Ahmed,False
C008,REGISTRATION,2024-08-15,2024-08-14,submitted,Layla,False
C009,REGISTRATION,2024-08-15,2024-08-20,submitted,Layla,False
C010,REGISTRATION,2024-08-15,2024-08-13,submitted,Sara,False
C011,VAT_RETURN,2024-10-28,2024-10-27,submitted,Sara,True
C012,VAT_RETURN,2024-10-28,2024-10-30,submitted,Ahmed,False
C013,CT_RETURN,2024-09-30,,overdue,Ahmed,False
C014,VAT_RETURN,2024-10-28,2024-10-28,submitted,Layla,False
C015,REGISTRATION,2024-08-15,2024-08-15,submitted,Ahmed,False
C016,VAT_RETURN,2024-10-28,,cancelled,Layla,False
C017,CT_RETURN,2024-09-30,2024-09-25,submitted,Sara,False
C018,VAT_RETURN,2024-10-28,2024-10-28,submitted,Ahmed,False
"""

# All active clients — used for Portfolio Coverage Rate
ALL_ACTIVE_CLIENTS = {
    "C001", "C002", "C003", "C004", "C005", "C006", "C007", "C008",
    "C009", "C010", "C011", "C012", "C013", "C014", "C015", "C016",
    "C017", "C018",
}

# KPI targets
TARGETS = {
    "OTFR": 95.0,       # %
    "RCR": 98.0,        # %
    "RAR": 97.0,        # %
    "DMR": 2.0,         # %
    "PCR": 100.0,       # %
}


# ---------------------------------------------------------------------------
# Parsing
# ---------------------------------------------------------------------------

def parse_date(value: str) -> Optional[date]:
    """Parse ISO date string; return None for empty strings."""
    value = value.strip()
    if not value:
        return None
    return datetime.strptime(value, "%Y-%m-%d").date()


def load_engagements(csv_text: str) -> list[Engagement]:
    """Parse CSV text into a list of Engagement records."""
    reader = csv.DictReader(io.StringIO(csv_text.strip()))
    engagements = []
    for row in reader:
        engagements.append(
            Engagement(
                client_id=row["client_id"].strip(),
                engagement_type=row["engagement_type"].strip().upper(),
                due_date=parse_date(row["due_date"]),
                submitted_date=parse_date(row.get("submitted_date", "")),
                status=row["status"].strip().lower(),
                practitioner=row.get("practitioner", "Unknown").strip(),
                had_amendment=row.get("had_amendment", "False").strip().lower() == "true",
            )
        )
    return engagements


# ---------------------------------------------------------------------------
# KPI computation
# ---------------------------------------------------------------------------

def compute_otfr(engagements: list[Engagement]) -> dict:
    """
    On-Time Filing Rate: percentage of submitted engagements filed on or before due date.
    Excludes cancelled engagements.
    Returns overall and per-type breakdown.
    """
    types = ["VAT_RETURN", "CT_RETURN", "REGISTRATION"]
    results = {}

    active = [e for e in engagements if e.status != "cancelled"]
    submitted = [e for e in active if e.submitted_date is not None]
    on_time = [e for e in submitted if e.submitted_date <= e.due_date]

    results["overall"] = {
        "total_due": len(active),
        "submitted": len(submitted),
        "on_time": len(on_time),
        "rate": round(len(on_time) / len(submitted) * 100, 1) if submitted else 0.0,
    }

    for etype in types:
        sub_t = [e for e in submitted if e.engagement_type == etype]
        ot_t = [e for e in sub_t if e.submitted_date <= e.due_date]
        results[etype] = {
            "submitted": len(sub_t),
            "on_time": len(ot_t),
            "rate": round(len(ot_t) / len(sub_t) * 100, 1) if sub_t else None,
        }

    return results


def compute_rcr(engagements: list[Engagement]) -> dict:
    """
    Registration Completion Rate: percentage of REGISTRATION engagements
    completed (submitted) on or before due date.
    """
    regs = [e for e in engagements if e.engagement_type == "REGISTRATION" and e.status != "cancelled"]
    completed_on_time = [e for e in regs if e.submitted_date is not None and e.submitted_date <= e.due_date]

    return {
        "total_registrations": len(regs),
        "completed_on_time": len(completed_on_time),
        "rate": round(len(completed_on_time) / len(regs) * 100, 1) if regs else 0.0,
    }


def compute_rar(engagements: list[Engagement]) -> dict:
    """
    Return Accuracy Rate: percentage of submitted returns accepted without
    amendment or FTA query within 30 days.
    """
    submitted = [
        e for e in engagements
        if e.status != "cancelled" and e.submitted_date is not None
        and e.engagement_type in ("VAT_RETURN", "CT_RETURN")
    ]
    clean = [e for e in submitted if not e.had_amendment]

    return {
        "total_submitted": len(submitted),
        "clean": len(clean),
        "amended": len(submitted) - len(clean),
        "rate": round(len(clean) / len(submitted) * 100, 1) if submitted else 0.0,
    }


def compute_dmc(engagements: list[Engagement], report_date: date) -> dict:
    """
    Deadline Miss Count: engagements where submitted_date > due_date
    OR status is overdue at end of reporting period.
    """
    active = [e for e in engagements if e.status != "cancelled"]
    missed = []
    for e in active:
        if e.status == "overdue":
            missed.append(e)
        elif e.submitted_date is not None and e.submitted_date > e.due_date:
            missed.append(e)

    # Days overdue for each miss
    details = []
    for e in missed:
        if e.submitted_date is not None:
            days_overdue = (e.submitted_date - e.due_date).days
        else:
            days_overdue = (report_date - e.due_date).days
        details.append({
            "client_id": e.client_id,
            "type": e.engagement_type,
            "due_date": e.due_date.strftime("%d/%m/%Y"),
            "days_overdue": days_overdue,
            "practitioner": e.practitioner,
        })

    details.sort(key=lambda x: x["days_overdue"], reverse=True)

    rate = round(len(missed) / len(active) * 100, 1) if active else 0.0
    return {
        "count": len(missed),
        "rate": rate,
        "top_overdue": details[:5],
    }


def compute_pcr(engagements: list[Engagement], all_clients: set) -> dict:
    """
    Portfolio Coverage Rate: percentage of all active clients that appear
    in at least one engagement record for the period.
    """
    clients_with_engagement = {e.client_id for e in engagements if e.status != "cancelled"}
    missing = all_clients - clients_with_engagement

    return {
        "total_active_clients": len(all_clients),
        "clients_with_engagement": len(clients_with_engagement),
        "missing_clients": sorted(missing),
        "rate": round(len(clients_with_engagement) / len(all_clients) * 100, 1) if all_clients else 0.0,
    }


# ---------------------------------------------------------------------------
# RAG status
# ---------------------------------------------------------------------------

def rag_status(value: float, target: float, amber_band: float = 3.0, lower_is_better: bool = False) -> str:
    """Return GREEN / AMBER / RED based on proximity to target."""
    if lower_is_better:
        if value <= target:
            return "GREEN"
        elif value <= target + amber_band:
            return "AMBER"
        return "RED"
    else:
        if value >= target:
            return "GREEN"
        elif value >= target - amber_band:
            return "AMBER"
        return "RED"


# ---------------------------------------------------------------------------
# Report printing
# ---------------------------------------------------------------------------

def print_separator(char: str = "═", width: int = 70) -> None:
    print(char * width)


def print_kpi_row(label: str, value: str, target: str, status: str) -> None:
    print(f"  {label:<38} {value:>7}  {target:>8}  {status}")


def print_dashboard(
    period: str,
    report_date: date,
    otfr: dict,
    rcr: dict,
    rar: dict,
    dmc: dict,
    pcr: dict,
) -> None:
    """Render the KPI dashboard to stdout."""
    print()
    print_separator()
    print("  FINANSHELS — TAX COMPLIANCE METRICS DASHBOARD")
    print(f"  Reporting Period : {period}")
    print(f"  Generated        : {report_date.strftime('%d/%m/%Y')}")
    print_separator()

    print()
    print("  KPI SCORECARD")
    print_separator("─")
    print(f"  {'KPI':<38} {'Value':>7}  {'Target':>8}  Status")
    print_separator("─")

    # OTFR overall
    otfr_status = rag_status(otfr["overall"]["rate"], TARGETS["OTFR"])
    print_kpi_row(
        "On-Time Filing Rate (OTFR)",
        f"{otfr['overall']['rate']}%",
        f"≥{TARGETS['OTFR']}%",
        otfr_status,
    )
    for etype, label in [("VAT_RETURN", "VAT returns"), ("CT_RETURN", "CT returns"), ("REGISTRATION", "Registrations")]:
        val = otfr[etype]["rate"]
        val_str = f"{val}%" if val is not None else "N/A"
        print(f"    {'— ' + label:<36} {val_str:>7}")

    # RCR
    rcr_status = rag_status(rcr["rate"], TARGETS["RCR"])
    print_kpi_row(
        "Registration Completion Rate (RCR)",
        f"{rcr['rate']}%",
        f"≥{TARGETS['RCR']}%",
        rcr_status,
    )

    # RAR
    rar_status = rag_status(rar["rate"], TARGETS["RAR"])
    print_kpi_row(
        "Return Accuracy Rate (RAR)",
        f"{rar['rate']}%",
        f"≥{TARGETS['RAR']}%",
        rar_status,
    )

    # DMC / DMR
    dmc_status = rag_status(dmc["rate"], TARGETS["DMR"], lower_is_better=True)
    print_kpi_row(
        "Deadline Miss Count (DMC)",
        str(dmc["count"]),
        "",
        "",
    )
    print_kpi_row(
        "  Deadline Miss Rate (DMR)",
        f"{dmc['rate']}%",
        f"≤{TARGETS['DMR']}%",
        dmc_status,
    )

    # PCR
    pcr_status = rag_status(pcr["rate"], TARGETS["PCR"])
    print_kpi_row(
        "Portfolio Coverage Rate (PCR)",
        f"{pcr['rate']}%",
        f"={TARGETS['PCR']}%",
        pcr_status,
    )

    print_separator("─")

    # Overdue list
    print()
    print("  TOP OVERDUE ENGAGEMENTS")
    print_separator("─")
    if dmc["top_overdue"]:
        print(f"  {'Client ID':<12} {'Type':<15} {'Due Date':<12} {'Days Overdue':>12}  Practitioner")
        print_separator("─")
        for row in dmc["top_overdue"]:
            print(f"  {row['client_id']:<12} {row['type']:<15} {row['due_date']:<12} {row['days_overdue']:>12}  {row['practitioner']}")
    else:
        print("  No overdue engagements — all submissions on time.")
    print_separator("─")

    # Missing clients
    if pcr["missing_clients"]:
        print()
        print("  CLIENTS WITH NO ENGAGEMENT RECORD THIS PERIOD")
        print_separator("─")
        print("  " + ", ".join(pcr["missing_clients"]))
        print_separator("─")

    # Recommendations
    print()
    print("  RECOMMENDATIONS")
    print_separator("─")
    recommendations = build_recommendations(otfr, rcr, rar, dmc, pcr)
    if recommendations:
        for i, rec in enumerate(recommendations, 1):
            print(f"  {i}. {rec}")
    else:
        print("  All KPIs on target. No immediate action required.")
    print_separator("─")
    print()
    print("  NOTE: Review all outputs against current FTA guidance before")
    print("  sharing externally. This is an internal work product.")
    print()
    print_separator()


def build_recommendations(otfr: dict, rcr: dict, rar: dict, dmc: dict, pcr: dict) -> list[str]:
    """Generate concrete recommendations for any KPI below target."""
    recs = []

    if otfr["CT_RETURN"]["rate"] is not None and otfr["CT_RETURN"]["rate"] < TARGETS["OTFR"]:
        recs.append(
            f"CT Return OTFR is {otfr['CT_RETURN']['rate']}% (target ≥{TARGETS['OTFR']}%). "
            "Review CT deadline tracker and assign a senior practitioner to outstanding files."
        )

    if otfr["VAT_RETURN"]["rate"] is not None and otfr["VAT_RETURN"]["rate"] < TARGETS["OTFR"]:
        recs.append(
            f"VAT Return OTFR is {otfr['VAT_RETURN']['rate']}% (target ≥{TARGETS['OTFR']}%). "
            "Confirm EmaraTax submission confirmations are being logged on the day of filing."
        )

    if rcr["rate"] < TARGETS["RCR"]:
        recs.append(
            f"Registration Completion Rate is {rcr['rate']}% (target ≥{TARGETS['RCR']}%). "
            "Identify delayed registrations and check for pending client document submissions or EmaraTax portal issues."
        )

    if rar["rate"] < TARGETS["RAR"]:
        recs.append(
            f"Return Accuracy Rate is {rar['rate']}% (target ≥{TARGETS['RAR']}%). "
            f"{rar['amended']} return(s) required amendment. Review amendment log for common error patterns "
            "(e.g., incorrect VAT codes, missing related-party disclosures) and update the pre-submission checklist."
        )

    if dmc["rate"] > TARGETS["DMR"]:
        recs.append(
            f"Deadline Miss Rate is {dmc['rate']}% (target ≤{TARGETS['DMR']}%). "
            f"{dmc['count']} engagement(s) missed deadline. Escalate top overdue items to practice manager."
        )

    if pcr["rate"] < TARGETS["PCR"]:
        missing = ", ".join(pcr["missing_clients"])
        recs.append(
            f"Portfolio Coverage Rate is {pcr['rate']}% — clients {missing} have no engagement record. "
            "Confirm whether engagements are correctly created in the practice management system."
        )

    return recs


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    """Run KPI computation on synthetic engagement data and print dashboard."""
    period = "Q4 2024"
    report_date = date(2024, 12, 31)

    engagements = load_engagements(SAMPLE_ENGAGEMENTS_CSV)

    otfr = compute_otfr(engagements)
    rcr = compute_rcr(engagements)
    rar = compute_rar(engagements)
    dmc = compute_dmc(engagements, report_date)
    pcr = compute_pcr(engagements, ALL_ACTIVE_CLIENTS)

    print_dashboard(period, report_date, otfr, rcr, rar, dmc, pcr)


if __name__ == "__main__":
    main()
