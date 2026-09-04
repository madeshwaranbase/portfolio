# 07 — Log File Analyzer

A CLI tool that parses a log file and reports counts per log level plus the most frequent error message. Demonstrates text parsing, `collections.Counter`, and structuring a script so its core logic is unit-testable in isolation from I/O and `print`.

## What it does

- Auto-generates a sample `sample.log` if one doesn't exist
- Counts log lines by level (`INFO`, `ERROR`, `WARNING`, etc.)
- Tracks the frequency of each distinct `ERROR` message
- Prints a summary with the level breakdown and the single most common error

## Why this project

The original version ran everything at module scope — no functions, so there was nothing to call from a test without subprocessing the whole script. Refactored it into `parse_log()` and `format_summary()` as pure functions returning data/strings instead of printing directly, which is the same separation-of-concerns pattern needed to make any CLI or reporting tool testable.

## Run it

```bash
python log_file_analyzer.py
```

## Run the tests

```bash
pip install pytest --break-system-packages
pytest test_log_file_analyzer.py -v
```

13 tests:

| Area | Coverage |
|---|---|
| `ensure_sample_log` | creates file when missing, doesn't overwrite existing |
| `parse_log` | level counts, error message counts, blank lines skipped, level with no message, non-ERROR levels excluded from messages, empty file |
| `format_summary` | header present, level lines formatted, most-common-error shown/omitted |
| `main` | end-to-end run in an isolated temp cwd |

## Tech

Python 3, `collections.Counter`, `pathlib`, `pytest`, `monkeypatch`.
