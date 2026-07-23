# API + UI Hybrid Testing Framework

Playwright + Cucumber (BDD) + TypeScript. Creates a real user account through automationexercise.com's public API, then proves that account works by logging in through the actual UI — the API and UI steps are correlated, not two independent checks against unrelated data.

## Structure
```
04-api-ui-hybrid/
├─ features/
│  └─ account-hybrid.feature      # Gherkin scenarios
├─ step-definitions/
│  └─ account.steps.ts            # step implementations
├─ pages/
│  └─ LoginPage.ts                 # POM for the UI side
├─ api/
│  ├─ accountApiClient.ts          # createAccount / deleteAccount HTTP calls
│  └─ userFactory.ts               # generates unique user payloads
├─ support/
│  ├─ world.ts                     # Cucumber World: shared page + api state
│  └─ hooks.ts                     # browser lifecycle, failure screenshots
├─ .github/workflows/hybrid-tests.yml
├─ cucumber.js
├─ tsconfig.json
└─ package.json
```

## Scenarios
1. **Create via API → verify via UI**: generates a unique user, creates it through `POST /createAccount`, then logs into the live site with those exact credentials and asserts "Logged in as {name}" appears.
2. **Delete via API → verify UI rejects it**: creates an account, deletes it through `DELETE /deleteAccount`, then confirms the same credentials now fail login through the UI.

## Run
```bash
npm install
npx playwright install
npm test                    # runs all features
npm run test:tags "@smoke"  # runs only @smoke-tagged scenarios
npm run report              # opens the HTML report
```

Set `HEADED=true npm test` to watch the browser instead of running headless.

## Why this design
- Each test run generates a timestamped, unique email — reruns never collide with a previous run's leftover account.
- Failure screenshots auto-attach to the Cucumber HTML report via the `After` hook — no manual screenshot code in step definitions.
- `AccountApiClient` and `LoginPage` are the only two places that know about HTTP calls or DOM selectors — step definitions stay readable as plain English-to-code mapping.

## Extending
- Add new scenarios to `account-hybrid.feature`, then add matching steps to `account.steps.ts` — reuse `apiClient` and page objects rather than writing raw `axios`/`page` calls in step files.
- Swap the target site by adding a new API client + page object; `world.ts` and `hooks.ts` need no changes.
