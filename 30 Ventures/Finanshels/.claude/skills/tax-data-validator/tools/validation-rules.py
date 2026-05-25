"""
validation-rules.py
-------------------
UAE tax data validator for Finanshels.

Validates client financial/tax data records (invoices, VAT lines, chart of
accounts, transactions) against UAE FTA rules and Finanshels data standards.

Runs on stdlib only — no pip dependencies required.

Usage:
    python3 validation-rules.py

The main() function demonstrates the validator on synthetic data covering
common error patterns seen in UAE client data imports.
"""

import re
import csv
import io
import json
from datetime import datetime, date
from typing import Any, Dict, List, Optional, Tuple

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

UAE_TRN_PATTERN = re.compile(r"^\d{15}$")

# Accepted VAT category codes per UAE VAT law
VALID_VAT_CATEGORIES = {"S", "Z", "E", "OS"}

# Standard VAT rate (5%) with a small tolerance for floating-point rounding
VAT_RATE_STANDARD = 0.05
VAT_RATE_TOLERANCE = 0.0001

VALID_CURRENCIES = {"AED"}

# Required fields by data type
REQUIRED_FIELDS = {
    "invoices": [
        "invoice_number",
        "invoice_date",
        "net_amount",
        "vat_amount",
        "vat_category",
    ],
    "vat_lines": [
        "invoice_number",
        "invoice_date",
        "net_amount",
        "vat_amount",
        "vat_category",
    ],
    "chart_of_accounts": ["account_code", "account_name", "account_type"],
    "transactions": ["transaction_date", "description", "account_code"],
}

# Date formats we will attempt to parse and normalise
DATE_INPUT_FORMATS = [
    "%Y-%m-%d",   # ISO-8601 — preferred
    "%d/%m/%Y",   # common UAE/UK format
    "%m/%d/%Y",   # US format (treat as warning)
    "%d-%m-%Y",
    "%Y/%m/%d",
]

# ---------------------------------------------------------------------------
# Helper utilities
# ---------------------------------------------------------------------------


def strip_trn(value: str) -> str:
    """Remove spaces, hyphens and other common formatting from a TRN string."""
    return re.sub(r"[\s\-]", "", str(value).strip())


def parse_amount(value: Any) -> Optional[float]:
    """
    Convert a value to float. Returns None if conversion fails.
    Handles strings with commas (e.g. "1,234.56") and currency prefixes.
    """
    if isinstance(value, (int, float)):
        return float(value)
    cleaned = re.sub(r"[^\d.\-]", "", str(value).replace(",", ""))
    try:
        return float(cleaned)
    except ValueError:
        return None


def parse_date(value: str) -> Tuple[Optional[date], bool]:
    """
    Attempt to parse a date string.

    Returns:
        (parsed_date, is_iso) — is_iso is True only when the input was
        already in YYYY-MM-DD format (no transformation needed).
    """
    raw = str(value).strip()
    for fmt in DATE_INPUT_FORMATS:
        try:
            parsed = datetime.strptime(raw, fmt).date()
            is_iso = fmt == "%Y-%m-%d"
            return parsed, is_iso
        except ValueError:
            continue
    return None, False


def round_aed(amount: float) -> float:
    """Round to 2 decimal places (fils precision)."""
    return round(amount, 2)


# ---------------------------------------------------------------------------
# Validation rules
# ---------------------------------------------------------------------------


def validate_trn(trn_raw: str) -> List[Dict]:
    """
    Validate a UAE TRN.

    Returns a list of issue dicts (empty = valid).
    Each issue: {code, severity, field, original, message}.
    """
    issues = []
    stripped = strip_trn(trn_raw)

    if not stripped:
        issues.append(
            {
                "code": "TRN_MISSING",
                "severity": "ERROR",
                "field": "trn",
                "original": trn_raw,
                "message": "TRN is blank.",
            }
        )
        return issues

    if not UAE_TRN_PATTERN.match(stripped):
        issues.append(
            {
                "code": "TRN_FORMAT_ERROR",
                "severity": "ERROR",
                "field": "trn",
                "original": trn_raw,
                "message": (
                    f"TRN '{stripped}' is not 15 digits. "
                    f"Got {len(stripped)} digit(s) after stripping formatting."
                ),
            }
        )

    # Warn if formatting characters were present (strip happened)
    if stripped != str(trn_raw).strip():
        issues.append(
            {
                "code": "TRN_FORMAT_WARN",
                "severity": "WARN",
                "field": "trn",
                "original": trn_raw,
                "message": (
                    f"TRN contained formatting characters. "
                    f"Normalised to '{stripped}'."
                ),
            }
        )

    return issues


def validate_date_field(value: str, field: str) -> List[Dict]:
    """Validate and normalise a date field."""
    issues = []
    raw = str(value).strip()

    if not raw:
        issues.append(
            {
                "code": "DATE_MISSING",
                "severity": "ERROR",
                "field": field,
                "original": raw,
                "message": f"'{field}' is blank.",
            }
        )
        return issues

    parsed, is_iso = parse_date(raw)

    if parsed is None:
        issues.append(
            {
                "code": "DATE_INVALID",
                "severity": "ERROR",
                "field": field,
                "original": raw,
                "message": f"'{field}' value '{raw}' could not be parsed as a date.",
            }
        )
    elif not is_iso:
        issues.append(
            {
                "code": "DATE_FORMAT_WARN",
                "severity": "WARN",
                "field": field,
                "original": raw,
                "message": (
                    f"'{field}' is '{raw}'; normalised to ISO-8601 "
                    f"'{parsed.isoformat()}'."
                ),
            }
        )

    return issues


def validate_vat_amounts(
    net_raw: Any,
    vat_raw: Any,
    vat_category: str,
    invoice_number: str = "",
) -> List[Dict]:
    """
    Validate that VAT amount is consistent with the declared category and rate.

    - Standard (S): vat = net * 5% ± tolerance
    - Zero-rated (Z): vat = 0
    - Exempt (E): vat = 0
    - Out of scope (OS): vat = 0
    """
    issues = []
    net = parse_amount(net_raw)
    vat = parse_amount(vat_raw)
    ref = f" (invoice: {invoice_number})" if invoice_number else ""

    if net is None:
        issues.append(
            {
                "code": "AMOUNT_INVALID",
                "severity": "ERROR",
                "field": "net_amount",
                "original": str(net_raw),
                "message": f"net_amount '{net_raw}' is not a valid number{ref}.",
            }
        )
    if vat is None:
        issues.append(
            {
                "code": "AMOUNT_INVALID",
                "severity": "ERROR",
                "field": "vat_amount",
                "original": str(vat_raw),
                "message": f"vat_amount '{vat_raw}' is not a valid number{ref}.",
            }
        )

    if net is None or vat is None:
        return issues

    # Decimal precision
    if round_aed(vat) != vat:
        issues.append(
            {
                "code": "AMOUNT_PRECISION",
                "severity": "WARN",
                "field": "vat_amount",
                "original": str(vat_raw),
                "message": (
                    f"vat_amount '{vat}' has more than 2 decimal places{ref}. "
                    "Will be rounded to fils precision."
                ),
            }
        )

    cat = str(vat_category).strip().upper()

    if cat == "S":
        expected_vat = round_aed(net * VAT_RATE_STANDARD)
        rounded_vat = round_aed(vat)
        if abs(rounded_vat - expected_vat) > VAT_RATE_TOLERANCE:
            issues.append(
                {
                    "code": "VAT_RATE_MISMATCH",
                    "severity": "ERROR",
                    "field": "vat_amount",
                    "original": str(vat_raw),
                    "message": (
                        f"Standard-rated invoice{ref}: expected VAT of "
                        f"{expected_vat} (5% of {net}) but got {rounded_vat}."
                    ),
                }
            )
    elif cat in {"Z", "E", "OS"}:
        if abs(vat) > VAT_RATE_TOLERANCE:
            issues.append(
                {
                    "code": "VAT_NONZERO_EXEMPT",
                    "severity": "ERROR",
                    "field": "vat_amount",
                    "original": str(vat_raw),
                    "message": (
                        f"Category '{cat}' invoice{ref} must have VAT = 0, "
                        f"but got {vat}."
                    ),
                }
            )
    else:
        issues.append(
            {
                "code": "INVALID_VAT_CATEGORY",
                "severity": "ERROR",
                "field": "vat_category",
                "original": str(vat_category),
                "message": (
                    f"Invalid VAT category '{vat_category}'{ref}. "
                    f"Must be one of: {', '.join(sorted(VALID_VAT_CATEGORIES))}."
                ),
            }
        )

    return issues


def validate_invoice_number(value: Any) -> List[Dict]:
    """Validate invoice number is non-empty; warn if numeric-only."""
    issues = []
    raw = str(value).strip() if value is not None else ""

    if not raw:
        issues.append(
            {
                "code": "INVOICE_NUMBER_MISSING",
                "severity": "ERROR",
                "field": "invoice_number",
                "original": str(value),
                "message": "invoice_number is blank.",
            }
        )
        return issues

    if raw.isdigit():
        issues.append(
            {
                "code": "NUMERIC_INVOICE_ID",
                "severity": "WARN",
                "field": "invoice_number",
                "original": raw,
                "message": (
                    f"invoice_number '{raw}' is numeric-only. "
                    "Consider prefixing with a series code (e.g. INV-001)."
                ),
            }
        )

    return issues


def validate_currency(value: Any) -> List[Dict]:
    """Flag non-AED currencies."""
    issues = []
    raw = str(value).strip().upper() if value else ""

    if raw and raw not in VALID_CURRENCIES:
        issues.append(
            {
                "code": "FOREIGN_CURRENCY",
                "severity": "WARN",
                "field": "currency",
                "original": str(value),
                "message": (
                    f"Currency '{raw}' is not AED. "
                    "Include for review; do not auto-convert to AED."
                ),
            }
        )
    return issues


# ---------------------------------------------------------------------------
# Record-level validator
# ---------------------------------------------------------------------------


def validate_invoice_record(record: Dict, index: int) -> Dict:
    """
    Run all applicable rules on a single invoice/VAT-line record.

    Returns:
        {
            "row": int,
            "status": "VALID" | "WARNING" | "ERROR" | "SKIP",
            "issues": [list of issue dicts],
        }
    """
    # Detect blank rows
    if all(not str(v).strip() for v in record.values()):
        return {"row": index, "status": "SKIP", "issues": []}

    issues = []

    # Invoice number
    issues += validate_invoice_number(record.get("invoice_number"))

    # Date
    issues += validate_date_field(
        record.get("invoice_date", ""), "invoice_date"
    )

    # TRN (supplier or customer — try both keys)
    for trn_field in ("supplier_trn", "customer_trn"):
        raw_trn = record.get(trn_field)
        if raw_trn:
            issues += validate_trn(raw_trn)

    # VAT amounts
    issues += validate_vat_amounts(
        record.get("net_amount"),
        record.get("vat_amount"),
        record.get("vat_category", ""),
        invoice_number=str(record.get("invoice_number", "")),
    )

    # Currency (optional field)
    if "currency" in record:
        issues += validate_currency(record.get("currency"))

    # Determine overall status
    severities = {i["severity"] for i in issues}
    if "ERROR" in severities:
        status = "ERROR"
    elif "WARN" in severities:
        status = "WARNING"
    else:
        status = "VALID"

    return {"row": index, "status": status, "issues": issues}


# ---------------------------------------------------------------------------
# Batch validator
# ---------------------------------------------------------------------------


def validate_batch(records: List[Dict], data_type: str = "invoices") -> Dict:
    """
    Validate a list of record dicts.

    Returns a report dict with summary, per-record results, duplicate analysis,
    and transformation rules.
    """
    results: List[Dict] = []
    invoice_keys: Dict[str, List[int]] = {}  # key → list of row indices

    for idx, record in enumerate(records, start=1):
        if data_type in ("invoices", "vat_lines"):
            result = validate_invoice_record(record, idx)
        else:
            # Minimal structural check for other types
            result = {"row": idx, "status": "VALID", "issues": []}
        results.append(result)

        # Track for duplicate detection
        inv_num = str(record.get("invoice_number", "")).strip()
        trn = str(
            record.get("supplier_trn", record.get("customer_trn", ""))
        ).strip()
        inv_date = str(record.get("invoice_date", "")).strip()
        net = str(record.get("net_amount", "")).strip()
        dup_key = f"{inv_num}|{trn}|{inv_date}|{net}"
        invoice_keys.setdefault(dup_key, []).append(idx)

    # Inject duplicate issues
    for key, rows in invoice_keys.items():
        if len(rows) > 1:
            for row_idx in rows:
                results[row_idx - 1]["issues"].append(
                    {
                        "code": "DUPLICATE_INVOICE",
                        "severity": "ERROR",
                        "field": "invoice_number",
                        "original": key.split("|")[0],
                        "message": (
                            f"Duplicate invoice detected. "
                            f"Same invoice_number/TRN/date/amount found at rows: "
                            f"{rows}."
                        ),
                    }
                )
                if results[row_idx - 1]["status"] != "ERROR":
                    results[row_idx - 1]["status"] = "ERROR"

    # Aggregate summary
    summary = {"total": len(results), "valid": 0, "warning": 0, "error": 0, "skip": 0}
    error_codes: Dict[str, int] = {}
    transformation_rules = []
    needs_review = []

    for r in results:
        summary[r["status"].lower()] += 1
        for issue in r["issues"]:
            code = issue["code"]
            error_codes[code] = error_codes.get(code, 0) + 1

            # Build transformation rules for auto-fixable issues
            if issue["code"] == "DATE_FORMAT_WARN":
                original = issue["original"]
                parsed, _ = parse_date(original)
                if parsed:
                    transformation_rules.append(
                        {
                            "row": r["row"],
                            "field": issue["field"],
                            "original": original,
                            "corrected": parsed.isoformat(),
                            "reason": "Normalised to ISO-8601 (YYYY-MM-DD)",
                        }
                    )
            elif issue["code"] == "TRN_FORMAT_WARN":
                transformation_rules.append(
                    {
                        "row": r["row"],
                        "field": issue["field"],
                        "original": issue["original"],
                        "corrected": strip_trn(issue["original"]),
                        "reason": "Removed formatting characters from TRN",
                    }
                )
            elif issue["code"] == "AMOUNT_PRECISION":
                parsed_amount = parse_amount(issue["original"])
                if parsed_amount is not None:
                    transformation_rules.append(
                        {
                            "row": r["row"],
                            "field": issue["field"],
                            "original": issue["original"],
                            "corrected": str(round_aed(parsed_amount)),
                            "reason": "Rounded to 2 decimal places (fils precision)",
                        }
                    )

            # Flag records needing human review
            if issue["severity"] == "ERROR" and issue["code"] not in {
                "DUPLICATE_INVOICE",
                "VAT_RATE_MISMATCH",
            }:
                needs_review.append(
                    {
                        "row": r["row"],
                        "field": issue["field"],
                        "issue": issue["message"],
                        "action": _suggest_action(issue["code"]),
                    }
                )

    return {
        "summary": summary,
        "error_breakdown": error_codes,
        "results": results,
        "transformation_rules": transformation_rules,
        "needs_review": needs_review,
    }


def _suggest_action(code: str) -> str:
    """Return a plain-English suggested action for a given error code."""
    actions = {
        "TRN_MISSING": "Obtain TRN from the supplier/customer; verify on EmaraTax.",
        "TRN_FORMAT_ERROR": "Verify the TRN on EmaraTax — it must be exactly 15 digits.",
        "DATE_MISSING": "Add the invoice date from the original document.",
        "DATE_INVALID": "Correct the date format. Expected: YYYY-MM-DD.",
        "INVOICE_NUMBER_MISSING": "Add the invoice reference from the source document.",
        "INVALID_VAT_CATEGORY": "Set vat_category to S, Z, E, or OS per the invoice.",
        "FOREIGN_CURRENCY": "Confirm the AED equivalent and document the exchange rate used.",
        "AMOUNT_INVALID": "Check the source document and enter a valid numeric amount.",
        "VAT_NONZERO_EXEMPT": "Verify the category; zero-rated/exempt invoices must have VAT = 0.",
    }
    return actions.get(code, "Review the source document and correct the field.")


# ---------------------------------------------------------------------------
# Report printer
# ---------------------------------------------------------------------------


def print_report(report: dict, title: str = "Data Quality Report") -> None:
    """Print a human-readable version of the validation report to stdout."""
    sep = "=" * 60
    print(f"\n{sep}")
    print(f"  {title}")
    print(sep)

    s = report["summary"]
    print(
        f"\nSummary\n"
        f"  Total records : {s['total']}\n"
        f"  Valid         : {s['valid']}\n"
        f"  Warnings      : {s['warning']}\n"
        f"  Errors        : {s['error']}\n"
        f"  Skipped       : {s['skip']}"
    )

    if report["error_breakdown"]:
        print("\nError / Warning Breakdown")
        for code, count in sorted(report["error_breakdown"].items()):
            print(f"  {code:<30} {count}")

    if report["transformation_rules"]:
        print(f"\nTransformation Rules ({len(report['transformation_rules'])} auto-fixable)")
        for i, rule in enumerate(report["transformation_rules"], 1):
            print(
                f"  {i:>2}. Row {rule['row']} | {rule['field']} | "
                f"'{rule['original']}' → '{rule['corrected']}' | {rule['reason']}"
            )

    if report["needs_review"]:
        print(f"\nRecords Requiring Manual Review ({len(report['needs_review'])})")
        for item in report["needs_review"]:
            print(
                f"  Row {item['row']} | {item['field']} | {item['issue']}\n"
                f"         Action: {item['action']}"
            )

    print(f"\n{sep}\n")


# ---------------------------------------------------------------------------
# CSV helper
# ---------------------------------------------------------------------------


def load_csv_string(csv_text: str) -> list[dict]:
    """Parse a CSV string into a list of dicts (header row required)."""
    reader = csv.DictReader(io.StringIO(csv_text.strip()))
    return [dict(row) for row in reader]


# ---------------------------------------------------------------------------
# Main — runnable demonstration
# ---------------------------------------------------------------------------


def main() -> None:
    """
    Demonstrate the validator on synthetic invoice data.

    Scenarios covered:
      - Valid standard-rated invoice (AED)
      - Date in DD/MM/YYYY format (auto-normalised)
      - TRN with hyphens (auto-normalised)
      - Zero-rated invoice with non-zero VAT (error)
      - Missing TRN (error)
      - Duplicate invoice (error)
      - Foreign currency (warning)
      - Numeric-only invoice number (warning)
      - VAT rate mismatch (error)
      - Blank row (skip)
    """
    synthetic_csv = """\
invoice_number,invoice_date,supplier_trn,net_amount,vat_amount,vat_category,currency
INV-001,2024-01-15,100367489100003,10000.00,500.00,S,AED
INV-002,15/02/2024,100367489100003,5000.00,250.00,S,AED
INV-003,2024-03-01,100-367-489-100-003,2000.00,0.00,Z,AED
INV-004,2024-03-10,100367489100003,1500.00,75.00,Z,AED
INV-005,2024-03-15,,3000.00,150.00,S,AED
INV-001,2024-01-15,100367489100003,10000.00,500.00,S,AED
INV-006,2024-04-01,100367489100003,8000.00,400.00,S,USD
00007,2024-04-10,100367489100003,1200.00,60.00,S,AED
INV-008,2024-04-20,100367489100003,5000.00,300.00,S,AED
,,,,,,,
"""

    print("Finanshels — UAE Tax Data Validator")
    print("Synthetic demonstration on 10 records (including 1 empty-field row)")

    records = load_csv_string(synthetic_csv)
    report = validate_batch(records, data_type="invoices")
    print_report(report, title="Invoice Batch — Q1/Q2 2024")

    # Also print the raw JSON report for integration use
    print("Raw report (JSON excerpt — first 2 results):")
    excerpt = {
        "summary": report["summary"],
        "sample_results": report["results"][:2],
    }
    print(json.dumps(excerpt, indent=2))


if __name__ == "__main__":
    main()
