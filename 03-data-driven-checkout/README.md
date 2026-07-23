# Data-Driven Checkout — Playwright/JS

POM-based checkout automation against saucedemo.com, driven entirely off `data/checkoutData.json`. Add a scenario to the JSON, it runs as a test — no spec changes needed.

## Structure
```
data-driven-checkout/
├─ pages/
│  ├─ LoginPage.js
│  ├─ InventoryPage.js
│  ├─ CartPage.js
│  └─ CheckoutPage.js
├─ data/
│  └─ checkoutData.json      # test cases: user, product, buyer info, expected outcome
├─ utils/
│  └─ testDataReader.js      # JSON loader
├─ tests/
│  └─ checkout.spec.js       # loops over checkoutData.json
├─ .github/workflows/playwright.yml
├─ playwright.config.js
└─ package.json
```

## Run
```bash
npm install
npx playwright install
npm test                 # all
npm run test:checkout    # checkout suite only
npm run test:headed      # watch it run
npm run report           # open HTML report
```

## Add a new case
Append an object to `data/checkoutData.json`:
```json
{
  "scenario": "your_case_name",
  "username": "standard_user",
  "password": "secret_sauce",
  "product": "Sauce Labs Backpack",
  "firstName": "X",
  "lastName": "Y",
  "postalCode": "641001",
  "expected": "success"
}
```
Set `expected` to `"error"` to assert a validation-error path instead of order completion.

## Notes
- `InventoryPage.productAddButton()` derives the `data-test` selector from the product name — no hardcoded per-product locators.
- Swap `baseURL` in `playwright.config.js` to point this at your own app; the POM structure and data-driven pattern carry over unchanged.
