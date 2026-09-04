# Project 20 — Selenium Python Automation Framework

A scalable and maintainable **Selenium + Pytest automation framework** designed to demonstrate real-world SDET automation practices.

## Project Overview

This project is being developed as a production-style UI automation framework rather than a collection of standalone Selenium scripts.

The framework currently demonstrates:

* Page Object Model (POM)
* Reusable Base Page
* Centralized configuration
* Configuration reader utility
* Centralized logging
* Pytest fixtures
* Data-driven login testing
* Positive and negative test scenarios
* Reusable framework components

Additional capabilities such as browser factory, screenshots, reporting, parallel execution, and CI/CD will be integrated as the framework evolves.

---

## Tech Stack

| Technology         | Purpose                  |
| ------------------ | ------------------------ |
| Python             | Programming language     |
| Selenium WebDriver | Browser automation       |
| Pytest             | Test framework           |
| Chrome             | Primary browser          |
| ConfigParser       | Configuration management |
| Python Logging     | Execution logging        |

---

## Application Under Test

The framework currently uses **The Internet** application for UI automation.

Base URL:

```text
https://the-internet.herokuapp.com
```

Primary functionality covered:

* Login
* Invalid login scenarios

---

## Project Structure

```text
20_selenium_automation_framework/
│
├── config/
│   └── config.ini
│
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   └── login_page.py
│
├── tests/
│   ├── test_login.py
│   └── test_invalid_login.py
│
├── utils/
│   ├── __init__.py
│   ├── config_reader.py
│   └── logger.py
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

# Framework Architecture

The framework follows a layered architecture:

```text
                    Test Cases
                        │
                        ▼
                 Page Objects
                        │
                        ▼
                   Base Page
                        │
                        ▼
                Selenium WebDriver
                        │
                        ▼
                  Web Application


       ┌───────────────────────────────┐
       │           Utilities           │
       │                               │
       │  Config Reader    Logger      │
       └───────────────────────────────┘
```

The objective is to keep **test logic separate from Selenium implementation details**.

---

# Page Object Model

The framework uses the **Page Object Model** to improve maintainability and reduce duplicated Selenium code.

### `base_page.py`

Contains reusable browser actions such as:

* Click
* Enter text
* Get text
* Wait for elements
* Check element visibility
* Retrieve page title

### `login_page.py`

Contains login-specific:

* Locators
* Login actions
* Flash message handling

Tests therefore focus on **business behavior** rather than Selenium implementation.

Example:

```python
login_page.login(
    "tomsmith",
    "SuperSecretPassword!"
)
```

instead of repeatedly writing:

```python
driver.find_element(...)
driver.find_element(...)
driver.click()
```

---

# Configuration Management

Configuration is maintained separately from the test code.

### `config/config.ini`

Example:

```ini
[application]
base_url = https://the-internet.herokuapp.com

[browser]
browser = chrome
headless = false

[timeouts]
implicit_wait = 0
explicit_wait = 10
```

The framework reads these values through:

```text
utils/config_reader.py
```

This avoids hardcoding environment and browser configuration throughout the framework.

---

# Configuration Reader

`ConfigReader` provides reusable methods for retrieving configuration values.

Example:

```python
config = ConfigReader()

base_url = config.get(
    "application",
    "base_url"
)

browser = config.get(
    "browser",
    "browser"
)

headless = config.get_boolean(
    "browser",
    "headless"
)
```

This provides a centralized configuration mechanism for the framework.

---

# Logging

The framework includes centralized logging through:

```text
utils/logger.py
```

Logs are written to:

```text
logs/
└── automation.log
```

Example:

```python
logger.info("Opening login page")
logger.info("Entering username")
logger.info("Submitting login form")
```

Example log output:

```text
2026-09-05 00:10:21 | INFO | pages.login_page | Opening login page
2026-09-05 00:10:22 | INFO | pages.login_page | Entering username
2026-09-05 00:10:22 | INFO | pages.login_page | Submitting login form
```

Logging provides useful information for debugging and test execution analysis.

---

# Test Coverage

## Valid Login

Validates successful authentication using:

```text
Username:
tomsmith

Password:
SuperSecretPassword!
```

Expected result:

```text
You logged into a secure area!
```

---

## Invalid Login

Validates negative login scenarios including:

* Invalid username
* Invalid password

The framework verifies the appropriate error message returned by the application.

---

# Installation

Clone the repository:

```bash
git clone <repository-url>
```

Navigate to the project:

```bash
cd 20_selenium_automation_framework
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on macOS/Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Running Tests

Run the complete test suite:

```bash
pytest
```

Run with detailed output:

```bash
pytest -v
```

Run a specific test file:

```bash
pytest -v tests/test_login.py
```

Run invalid login tests:

```bash
pytest -v tests/test_invalid_login.py
```

---

# Framework Design Principles

The framework is designed around the following principles:

### Maintainability

Changes to UI locators should primarily be handled inside Page Objects rather than individual test cases.

### Reusability

Common Selenium operations are implemented once in `BasePage`.

### Separation of Concerns

```text
Tests
  ↓
Business validation

Page Objects
  ↓
UI interaction

Utilities
  ↓
Framework services

Configuration
  ↓
Environment settings
```

### Scalability

The framework structure allows additional pages, tests, utilities, browsers, and environments to be added without restructuring the entire project.

---

# Planned Framework Capabilities

The framework will be expanded to demonstrate additional SDET-level practices:

* [ ] WebDriver factory
* [ ] Chrome / Firefox / Edge support
* [ ] Headless execution
* [ ] Explicit wait utilities
* [ ] Screenshot on failure
* [ ] HTML test reporting
* [ ] Test markers
* [ ] Smoke and regression suites
* [ ] Data-driven testing
* [ ] Parallel execution
* [ ] Environment-specific configuration
* [ ] API + UI testing
* [ ] GitHub Actions CI/CD
* [ ] Test execution artifacts
* [ ] Improved error handling

---

# Target Architecture

The final framework is planned to evolve toward:

```text
20_selenium_automation_framework/
│
├── config/
│   ├── config.ini
│   └── environments/
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── dashboard_page.py
│   └── components/
│
├── tests/
│   ├── smoke/
│   ├── regression/
│   └── negative/
│
├── test_data/
│
├── utils/
│   ├── config_reader.py
│   ├── driver_factory.py
│   ├── logger.py
│   ├── waits.py
│   └── screenshots.py
│
├── reports/
├── screenshots/
├── logs/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

# Objective

The objective of this project is to demonstrate practical **SDET automation engineering skills**, including:

* Framework design
* Selenium WebDriver
* Pytest
* Page Object Model
* Test architecture
* Configuration management
* Logging
* Reusable automation components
* Test maintainability
* CI/CD integration
* Scalable test execution
