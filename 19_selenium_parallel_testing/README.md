# Project 19 - Parallel Selenium Testing

Uses pytest-xdist to run independent Selenium tests in parallel.

## Install

```bash
pip install -r requirements.txt
```

## Run normally

```bash
pytest -v
```

## Run with 3 workers

```bash
pytest -n 3 -v
```

Parallel execution is useful when a suite becomes large and tests are independent.
