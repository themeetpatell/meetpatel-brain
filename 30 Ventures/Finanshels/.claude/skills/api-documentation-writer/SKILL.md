---
name: api-documentation-writer
description: Use when you need to document an internal or third-party tax and accounting API for the Finanshels team — including EmaraTax integration endpoints, accounting platform APIs (Xero, QuickBooks, Zoho Books), internal microservices, or webhook schemas that handle UAE VAT or Corporate Tax data. Triggers on phrases like "write API docs", "document this endpoint", "create an API spec", "document the EmaraTax integration", "write usage examples for this webhook", or when a developer shares an undocumented route, OpenAPI stub, or integration script. Produces a complete API spec with endpoint descriptions, request/response schemas, UAE tax field notes, error codes, and runnable usage examples.
---

# API Documentation Writer

Documents internal and third-party tax and accounting APIs for the Finanshels team, producing a consistent, team-ready API spec with field-level UAE tax annotations and usage examples.

## When to use

- A new internal endpoint is built for VAT return aggregation, CT calculation, or EmaraTax data prep.
- A third-party API integration (Xero, QuickBooks, Zoho Books, SAP B1) needs team-facing docs.
- An existing API was changed (new field, new error code, schema version bump) and docs are stale.
- A webhook schema (e.g. accounting platform push events) needs documenting so other services can consume it safely.
- Onboarding a new engineer who needs to understand how the EmaraTax pipeline works.
- Producing a spec alongside a PR for a compliance-critical integration.

## Inputs needed

**Required**
- API source — one of: OpenAPI/Swagger YAML or JSON, code (route handlers, controllers, service files), cURL examples, Postman collection, or a plain-English description of what the API does.
- API name and purpose (e.g. "VAT Return Submission Service — prepares and posts VAT returns to EmaraTax").

**Optional**
- Base URL and environment info (dev / staging / production).
- Authentication method (API key, OAuth2, JWT, mTLS).
- Known edge cases or error conditions to document.
- Target audience: internal engineers, partner integrators, or both.
- Existing partial docs to extend (rather than start from scratch).

## Workflow

1. **Parse the source**
   - Extract all endpoints (HTTP method + path), or all functions/methods if it is an SDK.
   - Identify request parameters (path, query, header, body) and response shapes.
   - Note any UAE-specific fields: TRN, tax period dates, AED amounts, VAT category codes, EmaraTax reference numbers.

2. **Annotate UAE tax fields**
   - For any field that carries a UAE tax meaning, add a `tax-note` annotation explaining:
     - What the field represents (e.g. "supplier TRN — 15-digit UAE tax registration number").
     - Validation rules (format, allowed values, mandatory conditions).
     - Which FTA concept it maps to (e.g. Box 1 of the VAT return).

3. **Write endpoint documentation**
   - Follow the template in `templates/api-spec-template.md`.
   - One section per endpoint (or per SDK method).
   - Include: summary, description, authentication, path/query/header params, request body schema, response schema, error codes, and at least one usage example.

4. **Write usage examples**
   - Provide a cURL example for every endpoint (use placeholder values, never real credentials).
   - Where the API is consumed in Python or TypeScript by Finanshels tooling, provide a code snippet.
   - For EmaraTax integrations, show the complete request-response cycle including how to handle a submission reference number.

5. **Document error codes**
   - List all HTTP status codes the API returns with a plain-English meaning.
   - For 4xx errors, explain what the caller must fix.
   - For 5xx errors, explain the retry strategy.
   - Include any FTA-specific error codes returned in the response body.

6. **Review for completeness**
   - Run through the quality checklist below.
   - Flag any fields where the purpose is unclear — mark them `[NEEDS CLARIFICATION]` rather than guessing.

7. **Output the spec** using the template structure.

## Output format

The output follows `templates/api-spec-template.md`. At minimum:

```
# API Name
> Version · Base URL · Auth method

## Overview
[2–4 sentences: what this API does, who uses it, UAE tax context]

## Authentication
[How to authenticate, where to get credentials, token lifetime]

## Endpoints

### POST /vat/returns
**Summary:** Submit a VAT return to EmaraTax.
**Auth:** Bearer token (OAuth2)

#### Request
[parameter table + JSON body schema with tax-notes]

#### Response
[JSON schema + field descriptions]

#### Errors
| Code | Meaning | Action |
|------|---------|--------|
| 400 | Invalid TRN format | Validate TRN is 15 digits before calling |
| 422 | Tax period already filed | Check EmaraTax portal; do not resubmit |

#### Example
[cURL + response]

---

## Changelog
[Version history if available]
```

## Quality checklist

- [ ] Every endpoint has a one-line summary and a 1–3 sentence description
- [ ] All required vs optional fields distinguished in every schema
- [ ] Every UAE tax-specific field has a `tax-note` annotation
- [ ] TRN field documented as 15 digits, no special characters
- [ ] AED amount fields documented with 2 d.p. (fils) precision requirement
- [ ] VAT category codes listed with UAE meanings (S / Z / E / OS)
- [ ] At least one cURL example per endpoint
- [ ] All documented error codes include a plain-English action for the caller
- [ ] Authentication section explains how to obtain and rotate credentials
- [ ] No real credentials, real TRNs, or real client data in any example
- [ ] `[NEEDS CLARIFICATION]` markers used rather than guessing unknown fields
- [ ] Changelog section present if this is an update to existing docs

## Examples

- "Write API docs for our internal `/vat/return/prepare` endpoint that takes a Xero organisation ID and returns a structured VAT return payload."
- "Document the EmaraTax VAT return submission API so the engineering team can integrate it without having to read the FTA portal every time."
- "Create a spec for the Zoho Books webhook that fires when an invoice is created — we need to know all the fields so we can map them to our VAT lines."

## Guardrails

- UAE jurisdiction only. Do not document non-UAE tax fields or reference IRS, HMRC, or GSTN concepts.
- Outputs are internal professional documentation. A qualified Finanshels team member must verify tax field annotations before the spec is used in a production integration.
- Never include real API keys, tokens, TRNs, or client financial data in examples. Use clearly fake placeholders like `YOUR_API_KEY`, `100000000000001`, `AED 1,000.00`.
- If the source code or API behaviour is ambiguous on a UAE tax point (e.g. which rounding rule applies), flag it explicitly — do not assume.
- EmaraTax schema versions change when the FTA updates the portal. Note the schema version and tell the reader to verify against current FTA developer documentation.

## Reference

See ../_shared/finanshels-context.md for UAE tax facts, rates, and deadlines.
