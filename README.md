# Miyo Help Center

Customer-facing product documentation for [Miyo](https://joinmiyo.com), built with Mintlify.

## Local development

Use a current Node.js release, then start the preview from this repository root:

```powershell
npx mint dev
```

The preview is available at `http://localhost:3000` by default.

## Validation

Run these checks before publishing:

```powershell
npx mint validate
npx mint broken-links
npx mint a11y
```

## Content rules

- Write for Miyo customers, not internal operators or developers.
- Confirm product behavior against the current MiyoWeb `main` branch.
- Use second person, active voice, and the exact labels customers see in the app.
- Do not document unshipped or flag-gated behavior as generally available.
- Mark uncertain behavior with an MDX TODO comment.
- Never include real financial data, credentials, tokens, or customer information.
- Update the relevant help page when a product change alters a customer workflow.

## Publishing

Mintlify deploys previews from pull requests and publishes changes from the connected default branch.
