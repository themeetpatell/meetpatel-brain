# [API Name]

> **Version:** 1.0.0 · **Base URL:** `https://api.example.finanshels.com/v1` · **Auth:** Bearer (OAuth2)

---

## Overview

[2–4 sentences describing what this API does, who the consumers are (internal services,
EmaraTax pipeline, accounting integrations), and which UAE tax obligations it supports
(VAT return preparation, CT data aggregation, TRN validation, etc.).]

**UAE tax context:** [Which FTA process does this API feed into? E.g. "Prepares Box 1–14
figures for the quarterly VAT return submitted via EmaraTax."]

---

## Authentication

| Property | Value |
|----------|-------|
| Method | OAuth2 client credentials |
| Token endpoint | `POST /auth/token` |
| Token lifetime | 3600 seconds (1 hour) |
| Scopes | `vat:read`, `vat:write`, `ct:read`, `ct:write` |

**Obtaining credentials:** [Where to get `client_id` and `client_secret` — e.g. "Request
from the Finanshels DevOps team via the internal secrets portal. Never hardcode these."]

**Rotating credentials:** [Rotation policy — e.g. "Rotate every 90 days. Old secret
remains valid for 24 hours after rotation to allow zero-downtime rollover."]

```bash
# Obtain a token
curl -X POST https://api.example.finanshels.com/auth/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=client_credentials&client_id=YOUR_CLIENT_ID&client_secret=YOUR_CLIENT_SECRET"

# Response
{
  "access_token": "eyJhbGci...",
  "token_type": "Bearer",
  "expires_in": 3600
}
```

---

## Endpoints

---

### [METHOD] [/path/to/endpoint]

**Summary:** [One sentence — what does this endpoint do?]

**Auth required:** Yes / No · Scope: `[scope]`

**Rate limit:** [e.g. 100 requests/minute per client]

#### Path parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `taxPeriodId` | string | Yes | Unique identifier for the tax period. Format: `YYYY-QN` (e.g. `2024-Q1`). |

#### Query parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `includeAdjustments` | boolean | No | `false` | Include manual adjustment lines in the response. |

#### Request headers

| Header | Required | Description |
|--------|----------|-------------|
| `Authorization` | Yes | `Bearer <access_token>` |
| `X-Client-Version` | No | Caller's app version — used for debugging. |

#### Request body

**Content-Type:** `application/json`

```json
{
  "trn": "100000000000001",
  "taxPeriodStart": "2024-01-01",
  "taxPeriodEnd": "2024-03-31",
  "currency": "AED",
  "vatLines": [
    {
      "invoiceNumber": "INV-001",
      "invoiceDate": "2024-01-15",
      "supplierTrn": "100000000000002",
      "netAmount": 10000.00,
      "vatAmount": 500.00,
      "vatCategory": "S"
    }
  ]
}
```

**Field reference:**

| Field | Type | Required | Tax note |
|-------|------|----------|----------|
| `trn` | string | Yes | UAE Tax Registration Number. Must be exactly 15 digits. No spaces or hyphens. Verify on EmaraTax before submission. |
| `taxPeriodStart` | string (ISO-8601) | Yes | Start date of the VAT tax period. Must align with the period registered with the FTA. |
| `taxPeriodEnd` | string (ISO-8601) | Yes | End date of the VAT tax period. |
| `currency` | string | Yes | Must be `AED`. Foreign-currency invoices must be converted to AED at the rate on the invoice date before submission. |
| `vatLines[].netAmount` | number | Yes | Net (ex-VAT) invoice amount in AED. 2 decimal places (fils). |
| `vatLines[].vatAmount` | number | Yes | VAT amount in AED. For standard-rated (`S`) lines: must equal `round(netAmount × 0.05, 2)`. For `Z`, `E`, `OS`: must be `0.00`. |
| `vatLines[].vatCategory` | string | Yes | `S` = standard 5%, `Z` = zero-rated, `E` = exempt, `OS` = out of scope. |

#### Response

**Status:** `200 OK`

**Content-Type:** `application/json`

```json
{
  "submissionId": "SUB-20240401-00123",
  "status": "ACCEPTED",
  "taxPeriod": "2024-Q1",
  "totals": {
    "standardRatedSupplies": 10000.00,
    "vatOnStandardRated": 500.00,
    "zeroRatedSupplies": 0.00,
    "exemptSupplies": 0.00,
    "netVatPayable": 500.00
  },
  "processedAt": "2024-04-01T09:00:00Z"
}
```

**Response field reference:**

| Field | Type | Description |
|-------|------|-------------|
| `submissionId` | string | Unique reference for this submission. Store this for audit purposes (7-year retention requirement). |
| `status` | string | `ACCEPTED`, `PENDING`, or `REJECTED`. |
| `totals.netVatPayable` | number | Amount payable to the FTA. Verify this matches your internal VAT return before filing. |
| `processedAt` | string (ISO-8601) | Timestamp of processing. |

#### Error codes

| HTTP Status | Code | Meaning | Action for caller |
|-------------|------|---------|-------------------|
| 400 | `INVALID_TRN` | TRN is not 15 digits or contains non-numeric characters. | Validate TRN format before calling. Strip spaces and hyphens. |
| 400 | `INVALID_TAX_PERIOD` | Tax period dates are missing, in the wrong format, or the period does not match FTA records. | Verify the period against the client's registered tax period on EmaraTax. |
| 400 | `VAT_MISMATCH` | A VAT line's `vatAmount` does not reconcile with `netAmount × vatCategory rate`. | Recalculate VAT amounts and resubmit. |
| 401 | `UNAUTHORIZED` | Access token is missing, expired, or invalid. | Re-authenticate and retry. |
| 409 | `PERIOD_ALREADY_FILED` | A return for this tax period has already been submitted and accepted. | Check EmaraTax portal. Do not resubmit. Contact the FTA if an amendment is needed. |
| 422 | `VALIDATION_ERROR` | One or more VAT lines failed field-level validation. See `errors[]` in the response body. | Fix each item in `errors[]` and resubmit. |
| 429 | `RATE_LIMITED` | Request rate exceeded. | Back off exponentially. Retry after the `Retry-After` header value. |
| 500 | `INTERNAL_ERROR` | Server-side error. | Log the `X-Request-ID` response header and report to the Finanshels engineering team. Do not resubmit automatically. |

#### Full example

```bash
curl -X POST https://api.example.finanshels.com/v1/vat/returns \
  -H "Authorization: Bearer eyJhbGci..." \
  -H "Content-Type: application/json" \
  -d '{
    "trn": "100000000000001",
    "taxPeriodStart": "2024-01-01",
    "taxPeriodEnd": "2024-03-31",
    "currency": "AED",
    "vatLines": [
      {
        "invoiceNumber": "INV-001",
        "invoiceDate": "2024-01-15",
        "supplierTrn": "100000000000002",
        "netAmount": 10000.00,
        "vatAmount": 500.00,
        "vatCategory": "S"
      }
    ]
  }'
```

```json
{
  "submissionId": "SUB-20240401-00123",
  "status": "ACCEPTED",
  "taxPeriod": "2024-Q1",
  "totals": {
    "standardRatedSupplies": 10000.00,
    "vatOnStandardRated": 500.00,
    "zeroRatedSupplies": 0.00,
    "exemptSupplies": 0.00,
    "netVatPayable": 500.00
  },
  "processedAt": "2024-04-01T09:00:00Z"
}
```

---

### [Add more endpoints below using the same structure]

---

## Webhooks (if applicable)

### [Event name] — `[event.type]`

**Trigger:** [When is this event fired?]

**Payload:**

```json
{
  "event": "invoice.created",
  "occurredAt": "2024-01-15T12:00:00Z",
  "data": {
    "[NEEDS CLARIFICATION — document payload fields here]"
  }
}
```

**Retry policy:** [How many times is the webhook retried? Back-off strategy?]

**Idempotency:** [How should receivers handle duplicate deliveries?]

---

## Common UAE tax field reference

| Field name (canonical) | Type | Format | Tax note |
|------------------------|------|--------|----------|
| `trn` | string | 15 digits | UAE Tax Registration Number. Issued by FTA via EmaraTax. |
| `taxPeriodStart` / `taxPeriodEnd` | string | ISO-8601 (`YYYY-MM-DD`) | Must match the period on the FTA's records. |
| `vatCategory` | string | `S`, `Z`, `E`, `OS` | Per UAE VAT law: Standard 5%, Zero-rated, Exempt, Out of scope. |
| `netAmount` | number | AED, 2 d.p. | Excludes VAT. In AED or converted to AED at invoice-date exchange rate. |
| `vatAmount` | number | AED, 2 d.p. | Must be `round(netAmount × 0.05, 2)` for `S`; must be `0.00` for `Z`, `E`, `OS`. |
| `currency` | string | ISO-4217 | `AED` required for FTA submissions. Flag any other value. |

---

## SDK / Client library usage (if applicable)

```python
# Python example (Finanshels internal SDK)
from finanshels_sdk import VatClient

client = VatClient(client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET")

result = client.vat.submit_return(
    trn="100000000000001",
    tax_period_start="2024-01-01",
    tax_period_end="2024-03-31",
    vat_lines=[
        {
            "invoice_number": "INV-001",
            "invoice_date": "2024-01-15",
            "supplier_trn": "100000000000002",
            "net_amount": "10000.00",
            "vat_amount": "500.00",
            "vat_category": "S",
        }
    ],
)
print(result.submission_id)  # SUB-20240401-00123
```

---

## Changelog

| Version | Date | Change |
|---------|------|--------|
| 1.0.0 | 2024-01-01 | Initial release |
| [NEEDS CLARIFICATION] | | |

---

## Support & escalation

- **Engineering issues:** Raise a ticket in [internal issue tracker].
- **EmaraTax API issues:** Contact FTA support via the EmaraTax portal.
- **Tax interpretation questions:** Escalate to the Finanshels Tax team before making assumptions in code.
