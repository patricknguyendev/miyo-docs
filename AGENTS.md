# Miyo documentation instructions

## Audience and purpose

This repository is the customer-facing Miyo Help Center. Help a customer finish a task, understand a money concept, protect their privacy, or recover from a problem.

## Source of truth

- Confirm behavior against the current `main` branch of `patricknguyendev/MiyoWeb`.
- Prefer user-visible labels and states from the product UI over internal planning documents.
- If a capability is behind a feature flag, entitlement, private beta, or provider approval, say so clearly or omit it.
- Never document an unmerged plan as available product behavior.

## Terminology

- Use **Miyo**, not Imperium.
- Use **household** for the shared space and **partner** for the other household member.
- Use **linked account** for an account connected through Plaid.
- Use **manual account** for an account maintained by the customer.
- Use **monthly budget** for category planning and **savings goal** for longer-term saving.

## Writing style

- Use active voice and second person.
- Lead with the outcome, then give the shortest reliable path.
- Use sentence case for headings.
- Bold exact UI labels, such as **Connect Bank**.
- Put prerequisites before steps and expected results after them.
- Explain financial calculations with a concrete example.
- Avoid marketing language, implementation details, and generic conclusions.

## Content boundaries

- Do not publish admin workflows, secrets, internal endpoints, launch controls, or incident procedures.
- Do not present Miyo as a bank, adviser, lender, broker, or money-movement service.
- Do not promise that balances or transactions are always current; tell customers to verify important information with their financial institution.
- Direct privacy, security, and legal questions to the official Miyo pages and contact addresses.

## Mintlify conventions

- Every page needs `title` and `description` frontmatter.
- Use root-relative internal links without file extensions.
- Add every customer-discoverable page to `docs.json`.
- Use built-in Mintlify components where they improve scanning.
- Run `mint validate`, `mint broken-links`, and `mint a11y` before publishing.
