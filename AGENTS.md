# Miyo documentation instructions

## Audience and purpose

This repository is the customer-facing Miyo Help Center built on Mintlify. Help a customer finish a task, understand a money concept, protect their privacy, or recover from a problem.

## Source of truth

- Confirm behavior against the current `main` branch of `patricknguyendev/MiyoWeb`.
- Prefer user-visible labels and states from the product UI over internal planning documents.
- If a capability is behind a feature flag, entitlement, private beta, or provider approval, say so clearly or omit it.
- Never document an unmerged plan as available product behavior.
- Use the Mintlify skill and current Mintlify documentation for platform behavior.

## Terminology

- Use **Miyo**, not Imperium, in customer-facing content.
- Use **household member** when the behavior is not limited to a romantic partner.
- Use **partner** only when the product behavior is specifically limited to Miyo's two-person household.
- Use **account** for a financial account and **Miyo account** for a user's login identity.
- Use **linked account** for an account connected through Plaid.
- Use **manual account** for an account maintained by the customer.
- Use **Budget** and **Privacy** when referring to those named navigation areas.
- Use **Simple** and **Advanced** for the two budget modes.
- Use **monthly budget** for category planning and **savings goal** for longer-term saving.

## Writing style

- Use active voice and second person.
- Lead with the outcome, then give the shortest reliable path.
- Keep sentences concise and use sentence case for headings.
- Bold exact UI labels, such as **Accounts** or **Create goal**.
- Put prerequisites before steps and expected results after them.
- Explain financial calculations with a concrete example.
- Avoid marketing superlatives, implementation details, generic conclusions, and financial advice.
- Use root-relative links without file extensions for internal pages.
- Mark uncertain behavior with an MDX TODO comment.

## Content boundaries

- Document customer-visible, generally available behavior.
- Do not expose internal admin, diagnostics, feature flags, security controls, vendor costs, internal endpoints, launch controls, or incident procedures.
- Do not present Miyo as a bank, adviser, lender, broker, or money-movement service.
- Do not promise that balances, transactions, projections, or detected recurring charges are complete or current.
- Never include real customer financial data, credentials, access tokens, verification codes, or secrets.
- Distinguish product organization and projections from financial, tax, investment, legal, or credit advice.
- Direct privacy, security, and legal questions to the official Miyo pages and contact addresses.

## Mintlify conventions

- Every page needs `title` and `description` frontmatter.
- Add every customer-discoverable page to `docs.json`.
- Use built-in Mintlify components where they improve scanning.

Before publishing, run:

```powershell
npx mint validate
npx mint broken-links
npx mint a11y
```
