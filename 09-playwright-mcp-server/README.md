# EventHub Playwright MCP Server

Local stdio MCP server with an allow-listed browser surface. It intentionally avoids arbitrary JavaScript evaluation and restricts navigation to the configured EventHub origin.

## Install
```bash
npm install
npx playwright install chromium
cp .env.example .env
npm run build
npm start
```
## Tools
- `open_eventhub`: open `/`, `/login`, `/events` or `/bookings`.
- `inspect_page`: report URL, title and visible headings.
- `click_test_id`: click an element by validated `data-testid`.
- `fill_label`: fill a field by accessible label.
- `screenshot`: save a local screenshot with a safe filename.

Use only as a local developer tool. Do not expose the stdio process as a public service.
