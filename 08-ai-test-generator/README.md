# EventHub OpenAPI Test Design Generator

Creates a human-reviewable test-design document from the actual EventHub OpenAPI JSON file. Optional LLM enrichment suggests additional scenarios but does not invent undocumented requirements.

## Setup
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
## Generate
```bash
python generate_tests.py --spec openapi.json --output proposed-test-cases.md
```
Optional AI enrichment:
```bash
export AI_API_KEY=...
python generate_tests.py --spec openapi.json --ai
```
Export the real OpenAPI JSON from https://api.eventhub.rahulshettyacademy.com/api/docs/ before running.
