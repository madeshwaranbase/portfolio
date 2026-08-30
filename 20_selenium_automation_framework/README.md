# Project 20 - Selenium Python Automation Framework

This is the final project in the portfolio. It combines the earlier Selenium skills into a small, maintainable automation framework.

## Architecture

```text
tests
  |
  v
page objects
  |
  v
selenium webdriver
  |
  v
browser
```

Supporting layers:

```text
conftest.py       -> fixtures and browser setup
config/           -> environment settings
utils/            -> configuration reader and logging
pages/            -> page objects
tests/            -> test cases
reports/          -> HTML test reports
logs/             -> execution logs
```

## Features

- Pytest
- Selenium WebDriver
- Page Object Model
- Fixtures
- Configuration file
- Logging
- HTML reports
- Command-line browser/headless options
- Parallel execution support

## Install

From this project directory:

```bash
pip install -r requirements.txt
```

## Run all tests

```bash
pytest
```

## Run headless

```bash
pytest --headless
```

## Run using 3 workers

```bash
pytest -n 3
```

## Run one test

```bash
pytest tests/test_login.py -v
```

## Reports

After execution:

```text
reports/report.html
```

## Logs

Execution logs are written to:

```text
logs/automation.log
```

## Why Page Object Model?

Locators and page-specific actions stay inside page classes. Test cases then describe business actions instead of being filled with Selenium implementation details.

For example:

```python
page.login("tomsmith", "SuperSecretPassword!")
```

instead of putting username/password locators directly in every test.

## Next Improvements

Possible future additions:

- Firefox support
- Environment-specific configuration
- Explicit wait helper
- Screenshot-on-failure fixture
- Allure reporting
- API helper layer
- CI matrix for multiple browsers
- Docker execution
