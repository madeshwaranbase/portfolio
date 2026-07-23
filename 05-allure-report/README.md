# Allure Reporting — Playwright + TypeScript

Playwright Test suite instrumented for rich Allure reports: named steps, severity/epic/feature labels, environment info, and failure categorization — not just pass/fail counts.

## Structure
```
05-allure-report/
├─ pages/
│  ├─ LoginPage.ts       # allure.step()-wrapped actions
│  └─ InventoryPage.ts
├─ tests/
│  ├─ login.spec.ts      # epic/feature/severity labels per test
│  └─ inventory.spec.ts
├─ categories.json        # buckets failures: product defect vs test defect vs timeout
├─ playwright.config.ts   # allure-playwright reporter + environment info
└─ .github/workflows/allure.yml
```

## Run
```bash
npm install
npx playwright install
npm test              # runs suite, writes raw results to allure-results/
npm run report         # generates the HTML report and opens it
```

`npm run report` requires the Allure commandline, which is installed as a dev dependency — no separate global install needed.

## What makes the report useful (not just green/red)
- **Steps**: every page-object action is wrapped in `allure.step(...)`, so a failure shows exactly which UI action broke, not just which test.
- **Severity/epic/feature labels**: each test tags itself (`allure.severity('critical')`, `allure.epic('Authentication')`) so the report can be filtered by business area or by how bad a failure is.
- **Categories**: `categories.json` reclassifies raw failures into "likely product defect" vs "test/script defect" vs "timeout" based on the error message — useful when triaging a long red run.
- **Environment info**: `playwright.config.ts` attaches framework, target site, OS, and Node version to every run, so an old report is still self-describing months later.
- **Auto screenshots/video/trace on failure**: configured once in `playwright.config.ts`, no per-test code needed.

## Extending
- New page objects: wrap actions in `allure.step()` the same way `LoginPage`/`InventoryPage` do — that's what makes steps show up nested in the report instead of one flat test name.
- New failure categories: add a rule to `categories.json` (matched by status + a message regex).
