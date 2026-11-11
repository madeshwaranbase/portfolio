# 03 Data Driven Checkout

Data-driven form validation, ticket quantity boundaries and non-mutating checkout checks.

## Application under test
- UI: https://eventhub.rahulshettyacademy.com/login
- API docs: https://api.eventhub.rahulshettyacademy.com/api/docs/

## Install and configure
```bash
npm install
npx playwright install
cp .env.example .env
```
Set your own EventHub sandbox account credentials in `.env`. Never commit secrets.

## Run
```bash
npm test
npm run typecheck
npm run report
```

## Architecture
- `src/pages`: page objects and UI interactions
- `src/fixtures`: reusable test fixtures
- `src/api`: API client and OpenAPI contract helpers
- `tests`: focused UI/API test specifications
- `.github/workflows`: CI workflow

## API contract integrity
The Swagger UI did not expose readable operation definitions in the documentation retrieval environment. This project loads the actual OpenAPI JSON at runtime. Set `OPENAPI_SPEC_URL` to the exact JSON URL shown by Swagger. API routes and payloads must be selected from that document; this framework does not invent EventHub routes or schemas.

## Safety and data
Booking creation is disabled by default. Set `RUN_MUTATING_TESTS=true` only when using a dedicated practice account and you intentionally want to create bookings. Never clear shared bookings automatically.

## Validation status
Source code is generated against the provided EventHub page captures and known UI selectors. Live execution and API contract validation remain environment-dependent and must be run before claiming passing results.
