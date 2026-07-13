# Miyo Help Center

Customer-facing product documentation for [Miyo](https://joinmiyo.com), built with Mintlify.

## Local development

Install the Mintlify CLI and run the site from this repository root:

```powershell
npm install --global mint
mint dev
```

The preview is available at `http://localhost:3000` by default.

## Validation

Run these checks before publishing:

```powershell
mint validate
mint broken-links
mint a11y
```

## Publishing

Mintlify deploys from the connected GitHub repository. Pushes to the default branch update the production documentation site.

## Content rules

- Write for Miyo customers, not internal operators or developers.
- Use second person and active voice.
- Keep instructions aligned with the current Miyo interface.
- Do not document unshipped or flag-gated behavior as generally available.
- Mark uncertain behavior with an MDX TODO comment.
- Never include real financial data, credentials, tokens, or customer information.
