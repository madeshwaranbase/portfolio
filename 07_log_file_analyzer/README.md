# 06 — Employee CSV Manager

A command-line employee record manager that persists data to a CSV file. Built to demonstrate file I/O, input validation, and CRUD logic — the same patterns that show up in test data setup/teardown for automation frameworks.

## What it does

- Add, search, list, and delete employee records (`id`, `name`, `department`, `salary`)
- Persists to `employees.csv` after every write (no explicit "save" step required)
- Validates input: rejects empty required fields, duplicate IDs, and non-numeric/negative salaries
- Case-insensitive search by ID or partial name match
- Delete requires explicit `y` confirmation to avoid accidental data loss

## Why this project

Shows I can reason about state and persistence correctly — the original version of this script had a bug where new records were held in memory but never written to disk. Fixing it (and writing tests that would have caught it) is the point: it's the same category of bug that causes flaky or silently-wrong automated tests.

## Run it

```bash
python employee_manager.py
```

Follow the on-screen menu (Add / Search / Delete / List / Exit).

## Run the tests

```bash
pip install pytest --break-system-packages
pytest test_employee_manager.py -v
```

15 tests, fully isolated from your real `employees.csv` via a `tmp_path` fixture:

| Area | Coverage |
|---|---|
| Load/Save | missing file, roundtrip, header integrity |
| Add | success + persistence, duplicate ID, empty ID/name, invalid salary, negative salary |
| Search | by ID, partial case-insensitive name, no match |
| Delete | confirmed, declined, not found |

## Tech

Python 3, `csv`, `pathlib`, `pytest`, `monkeypatch` for input mocking.
