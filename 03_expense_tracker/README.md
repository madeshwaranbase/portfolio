# Expense Tracker (CLI)

A CLI expense tracker that persists entries to CSV, with core logic separated from I/O and file handling for full test coverage.

## Why this project

Project 03 of a 20-project Python/Selenium portfolio. Demonstrates testing code that touches the filesystem — using pytest's `tmp_path` fixture for isolated, no-side-effect file I/O tests, a pattern directly transferable to test automation frameworks that read/write fixtures or reports.

## Features

- File path injected as a parameter (not hardcoded) — enables isolated testing
- `build_expense()` separates validation/parsing from user input collection
- Clean CSV persistence (load/save) with `csv.DictReader`/`DictWriter`
- 10 unit tests (pytest) covering parsing, totals, formatting, and file round-trips via `tmp_path`

## Tech stack

- Python 3.12
- pytest

## Project structure

```
03_expense_tracker/
├── expense_tracker.py         # core logic + CLI loop
├── test_expense_tracker.py    # pytest suite
└── README.md
```

## How to run

```bash
# Run the tracker
python3 expense_tracker.py

# Run the tests
pip install pytest
pytest test_expense_tracker.py -v
```

## Sample run

```
1. Add expense
2. View expenses
3. Exit
Choose: 1
Category: Food
Note: Lunch
Amount: 12.50
Expense added.

Expenses
----------------------------------------
Food                12.50  Lunch
----------------------------------------
Total: 12.50
```

## Test results

```
10 passed in 0.03s
```
