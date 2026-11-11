# EventHub Playwright Failure Analyzer

Python CLI for parsing Playwright JSON reports, grouping failures and creating a sanitized Markdown triage report. Optional LLM analysis produces hypotheses, never an asserted root cause.

## Setup
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
## Run
From a Playwright project:
```bash
npx playwright test --reporter=json > playwright-results.json
python analyzer.py --input playwright-results.json --output failure-summary.md
```
Optional AI:
```bash
export AI_API_KEY=...
export AI_BASE_URL=https://api.openai.com/v1
export AI_MODEL=gpt-4.1-mini
python analyzer.py --input playwright-results.json --ai
```
The tool sanitizes common secrets and email addresses before AI submission. Review output before sharing.
