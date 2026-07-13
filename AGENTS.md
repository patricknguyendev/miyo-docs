# Miyo documentation instructions

## About this project

- This repository contains the customer-facing Miyo Help Center built on Mintlify.
- Pages are MDX files with YAML frontmatter.
- Site configuration and navigation live in `docs.json`.
- Use the Mintlify skill and current Mintlify documentation for platform behavior.
- The Miyo application repository is the source of truth for product behavior.

## Terminology

- Use **Miyo**, not Imperium, in customer-facing content.
- Use **household member** when the behavior is not limited to a romantic partner.
- Use **account** for a financial account and **Miyo account** for a user's login identity.
- Use **Budget** and **Privacy** when referring to those named navigation areas.
- Use **Simple** and **Advanced** for the two budget modes.

## Style

- Use active voice and second person.
- Keep sentences concise and use sentence case for headings.
- Bold UI labels, such as **Accounts** or **Create goal**.
- Explain a concept before giving procedural steps.
- Avoid marketing superlatives and financial advice.
- Use root-relative links without file extensions for internal pages.
- Mark uncertain behavior with an MDX TODO comment.

## Content boundaries

- Document customer-visible, generally available behavior.
- Do not expose internal admin, diagnostics, feature-flag, security-control, vendor-cost, or operational details.
- Do not promise that balances, transactions, projections, or detected recurring charges are complete or current.
- Never include real customer financial data, credentials, access tokens, verification codes, or secrets.
- Distinguish product organization and projections from financial, tax, investment, legal, or credit advice.

## Verification

Before publishing, run:

```powershell
mint validate
mint broken-links
mint a11y
```
