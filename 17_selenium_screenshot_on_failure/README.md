# Selenium Screenshot on Test Failure

Automatically captures a screenshot whenever a Selenium test fails using a **Pytest hook**.

## Project Overview

This project demonstrates how to implement automatic screenshot capture for failed Selenium tests.

When a test fails during the execution phase, the Pytest hook detects the failure and captures the current browser state as a PNG image.

## Tech Stack

* Python
* Selenium WebDriver
* Pytest
* Google Chrome

## How It Works

The `pytest_runtest_makereport` hook is used to inspect the result of every test.

When the test fails:

1. Pytest detects the failed test.
2. The Selenium `driver` fixture is retrieved.
3. A screenshot is captured using:

   ```python
   driver.save_screenshot()
   ```
4. The screenshot is saved inside the `screenshots` directory.
5. The filename is generated from the test name.

## Screenshot Directory

The project automatically creates the directory if it doesn't already exist:

```python
SCREENSHOT_DIR = Path("screenshots")
SCREENSHOT_DIR.mkdir(exist_ok=True)
```

Example:

```text
screenshots/
└── test_login.png
```

## Pytest Hook

The implementation belongs in `conftest.py`:

```python
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")

        if driver:
            screenshot_path = SCREENSHOT_DIR / f"{item.name}.png"
            driver.save_screenshot(str(screenshot_path))
```

## Project Structure

```text
15_selenium_screenshot_on_failure/
│
├── conftest.py
├── screenshots/
├── requirements.txt
└── test_*.py
```

## Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Run Tests

Run all tests:

```bash
pytest -v
```

To demonstrate the screenshot functionality, run a test that intentionally fails.

After the failure, check:

```text
screenshots/
```

A screenshot corresponding to the failed test should be generated.

## Key Features

* Automatic screenshot capture on test failure
* Pytest `pytest_runtest_makereport` hook
* Selenium WebDriver integration
* Automatic screenshot directory creation
* Test-specific screenshot filenames
* No screenshot generated for successful tests
* Reusable across multiple Selenium test cases

## Expected Result

For a failed Selenium test:

```text
FAILED test_example.py::test_example
```

A screenshot should be automatically created:

```text
screenshots/test_example.png
```

This provides a useful failure artifact for debugging UI automation failures.
