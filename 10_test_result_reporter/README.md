# 10 — Test Result Reporter

A CLI tool that reads test results from a CSV file and generates a pass/fail summary report, both printed and saved to disk. Demonstrates CSV parsing, `collections.Counter`, and structuring reporting logic so it's testable independent of file I/O and `print`.

## What it does

- Auto-generates a sample `test_results.csv` if one doesn't exist
- Reads `test_name,status` rows
- Computes total/passed/failed counts and pass rate
- Lists all failed test names (or "None" if all passed)
- Writes the report to `test_report.txt` and prints it to stdout

## Why this project

The original script ran everything — file creation, CSV parsing, counting, report formatting, writing, and printing — at module scope in one linear block. Refactored into `ensure_sample_input()`, `load_results()`, `build_report()`, and `save_report()`, with `build_report()` as a pure function that takes parsed rows and returns a report string with no I/O. This mirrors how a real CI test-report generator should be built: the reporting logic needs to be verifiable against fixed input without re-running an actual test suite or touching the filesystem.

## Run it

```bash
python test_result_reporter.py
```

## Run the tests

```bash
pip install pytest --break-system-packages
pytest test_test_result_reporter.py -v
```

## Tech

Python 3, `csv`, `collections.Counter`, `pathlib`, `pytest`.
