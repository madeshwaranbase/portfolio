# 08 — API Data Checker

A CLI health-check tool that hits a REST API, validates the response shape, and reports pass/fail with an exit code. Demonstrates HTTP testing fundamentals: status code checks, response-time measurement, schema/field validation, and exit codes for CI integration.

## What it does

- GETs `https://jsonplaceholder.typicode.com/users` with a 10s timeout
- Measures response time
- Fails if status code isn't 200, response isn't a JSON list, or any user object is missing `id`, `name`, or `email`
- Prints a PASS/FAIL report and exits `0` (pass) or `1` (fail) — CI-friendly

## Why this project

The original script ran the request, validation, and `SystemExit` calls all inside one `try` block at module scope, which made it impossible to unit test without mocking `sys.exit` and capturing stdout for every branch. Refactored into pure functions — `fetch_users()`, `validate_users()`, `check_api()` — that return data instead of printing or exiting, with all I/O and exit-code logic isolated in `main()`. This is the same shape as an API test in a real automation suite: separate the check from the reporting.

## Run it

```bash
pip install -r requirements.txt --break-system-packages
python api_data_checker.py
```

## Run the tests

```bash
pytest test_api_data_checker.py -v
```

Tests mock `requests.get` (via `responses` or `unittest.mock`) so no real network calls are made — covers 200/non-200, request exceptions, invalid JSON, missing fields, and the pass/fail result shape.

## Tech

Python 3, `requests`, `pytest`, `unittest.mock`.
