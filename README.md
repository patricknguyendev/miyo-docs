# Miyo Help Center

Customer-facing documentation for [Miyo](https://joinmiyo.com), a privacy-first household finance app.

## Preview locally

Mintlify's CLI requires a current Node.js release. From this repository:

```powershell
npx mint dev
```

The preview opens at `http://localhost:3000` by default.

## Validate changes

```powershell
npx mint validate
npx mint broken-links
npx mint a11y
```

## Content rules

- Write for Miyo customers, not Miyo engineers.
- Confirm product behavior against the current MiyoWeb `main` branch before documenting it.
- Use the exact labels customers see in the app.
- Do not describe a feature-flagged capability as generally available.
- Keep internal implementation, launch gates, and operational runbooks in MiyoWeb.
- Update the relevant help page in the same product change that alters a customer workflow.

## Publishing

Connect this repository to Mintlify, then configure a custom domain such as `help.joinmiyo.com`. Changes to the default branch deploy through Mintlify after the repository integration is active.
