# Python & Selenium Automation Portfolio

A structured SDET automation portfolio containing **20 progressively designed projects**, covering Python programming, API testing, Selenium WebDriver, Pytest, test automation practices, and framework engineering.

The portfolio starts with Python fundamentals and gradually evolves into a **maintainable Selenium + Pytest automation framework** following real-world SDET practices.

---

## Projects

### Python & Automation Fundamentals

| # | Project | Key Skills |
|---|---|---|
| 01 | [CLI Calculator](01_python_calculator/) | Functions, conditions, input validation |
| 02 | [Number Guessing Game](02_number_guessing_game/) | Loops, conditions, randomization |
| 03 | [Expense Tracker](03_expense_tracker/) | CRUD, collections, file handling |
| 04 | [Password Generator](04_password_generator/) | Randomization, validation, string handling |
| 05 | [File Organizer](05_file_organizer/) | `pathlib`, filesystem automation |
| 06 | [Employee CSV Manager](06_employee_csv_manager/) | CSV processing, CRUD, data handling |
| 07 | [Log File Analyzer](07_log_file_analyzer/) | Log parsing, regex, data analysis |
| 08 | [API Data Checker](08_api_data_checker/) | REST API, HTTP, JSON, assertions |
| 09 | [CLI Todo App](09_cli_todo_app/) | CLI development, persistence, application logic |
| 10 | [Test Result Reporter](10_test_result_reporter/) | Test result processing, reporting, statistics |

---

### Selenium + Python

| # | Project | Key Skills |
|---|---|---|
| 11 | [Selenium Login Test](11_selenium_login_test/) | WebDriver, locators, assertions |
| 12 | [Selenium Form Automation](12_selenium_form_automation/) | Forms, inputs, checkboxes, radio buttons |
| 13 | [Selenium Web Table](13_selenium_web_table/) | Tables, rows, columns, data extraction |
| 14 | [Selenium Dropdowns](14_selenium_dropdowns/) | `Select`, dropdown automation |
| 15 | [Selenium Alerts & Windows](15_selenium_alerts_windows/) | Alerts, popups, browser windows |
| 16 | [Selenium File Upload & Download](16_selenium_file_upload_download/) | File handling, upload/download validation |
| 17 | [Screenshot on Failure](17_selenium_screenshot_on_failure/) | Pytest hooks, failure diagnostics |
| 18 | [Data-Driven Selenium](18_selenium_data_driven_testing/) | Parameterization, test data |
| 19 | [Parallel Selenium](19_selenium_parallel_testing/) | `pytest-xdist`, parallel execution |
| 20 | [Selenium Automation Framework](20_selenium_automation_framework/) | POM, fixtures, configuration, logging, reporting |

---

# Technology Stack

### Programming

- Python 3.10+
- Object-Oriented Programming
- File handling
- JSON
- CSV
- Regular Expressions

### Testing

- Pytest
- Pytest Fixtures
- Pytest Parameterization
- Pytest Markers
- Pytest Hooks
- Assertions
- HTML Reporting
- Parallel Test Execution

### UI Automation

- Selenium WebDriver
- Chrome
- Firefox
- Edge
- Page Object Model
- Explicit Waits
- Browser Windows
- JavaScript Alerts
- Dropdowns
- Tables
- File Upload / Download
- Screenshots

### API Automation

- REST APIs
- HTTP methods
- Status codes
- JSON response validation
- `requests`

### DevOps

- Git
- GitHub
- GitHub Actions
- CI/CD
- Test artifacts

---

# Learning Progression

The portfolio follows a deliberate progression rather than introducing a complex framework from the beginning.

```text
Python Fundamentals
        ↓
Python Automation
        ↓
File & Data Processing
        ↓
API Testing
        ↓
Testing Concepts
        ↓
Selenium Fundamentals
        ↓
Advanced Selenium
        ↓
Pytest
        ↓
Data-Driven Testing
        ↓
Parallel Execution
        ↓
Automation Framework Design
        ↓
CI/CD
````

Each project introduces new concepts while building on skills from previous projects.

---

# Project 20 — Automation Framework

Project 20 is the flagship project of the portfolio.

It combines the concepts learned throughout the previous projects into a reusable Selenium automation framework.

### Framework Architecture

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
                  WebDriver Layer
                        │
                        ▼
                  Web Application


       ┌─────────────────────────────────┐
       │          Framework Utils        │
       │                                 │
       │ Config Reader   Driver Factory  │
       │ Logger          Wait Utilities  │
       │ Screenshots     Test Data       │
       └─────────────────────────────────┘
```

### Framework Capabilities

* Page Object Model
* Reusable Base Page
* Pytest fixtures
* Centralized configuration
* WebDriver factory
* Explicit waits
* Logging
* Data-driven testing
* Screenshot capture on failure
* HTML reporting
* Smoke / regression / negative test categorization
* Parallel execution
* Multiple browser support
* API + UI testing
* GitHub Actions CI/CD

---

# Project 20 Structure

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
│   ├── driver_factory.py
│   └── logger.py
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

The framework will continue to evolve as additional SDET capabilities are implemented.

---

# Design Principles

The projects follow several important automation engineering principles.

### Maintainability

Common functionality is implemented once and reused across tests.

### Reusability

Reusable page methods, fixtures, utilities, and configuration components reduce duplication.

### Separation of Concerns

```text
Tests
  ↓
Business validation

Page Objects
  ↓
UI interaction

Base Page
  ↓
Common Selenium operations

Utilities
  ↓
Framework services

Configuration
  ↓
Execution settings
```

### Test Independence

Tests should be independently executable wherever possible so they can safely run in parallel.

### Debuggability

Failed tests should provide useful artifacts such as:

* Logs
* Screenshots
* HTML reports

---

# Setup

## 1. Clone the Repository

```bash
git clone https://github.com/madeshwaranbase/portfolio.git
```

Navigate to the project:

```bash
cd portfolio
```

---

## 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### macOS / Linux

```bash
source .venv/bin/activate
```

---

## 3. Install Dependencies

Individual projects contain their own `requirements.txt` where dependencies are required.

For example:

```bash
pip install -r 11_selenium_login_test/requirements.txt
```

For the final framework:

```bash
pip install -r 20_selenium_automation_framework/requirements.txt
```

---

# Running Selenium Projects

Navigate to the required project:

```bash
cd 11_selenium_login_test
```

Run the tests:

```bash
pytest -v
```

Each Selenium project contains its own README with project-specific execution instructions.

---

# Running the Automation Framework

Navigate to Project 20:

```bash
cd 20_selenium_automation_framework
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run all tests:

```bash
pytest
```

Run with verbose output:

```bash
pytest -v
```

Run smoke tests:

```bash
pytest -m smoke
```

Run regression tests:

```bash
pytest -m regression
```

Run tests in parallel:

```bash
pytest -n auto
```

Generate an HTML report:

```bash
pytest --html=reports/report.html --self-contained-html
```

---

# What This Portfolio Demonstrates

This portfolio demonstrates progression across three major areas:

### 1. Software Development

```text
Python
 ↓
Functions
 ↓
OOP
 ↓
Files
 ↓
Data Processing
 ↓
CLI Applications
```

### 2. Test Automation

```text
Selenium
 ↓
Pytest
 ↓
Page Objects
 ↓
Fixtures
 ↓
Data-Driven Testing
 ↓
Parallel Execution
```

### 3. SDET Engineering

```text
Framework Design
 ↓
Configuration
 ↓
Logging
 ↓
Reporting
 ↓
Failure Diagnostics
 ↓
API + UI Testing
 ↓
CI/CD
```

---

# Learning Objectives

By completing these projects, the goal is to develop practical understanding of:

* Python programming
* Test automation
* Selenium WebDriver
* Pytest
* Page Object Model
* Test design
* Data-driven testing
* API testing
* Browser automation
* Test reporting
* Logging
* Debugging
* Parallel execution
* Framework architecture
* CI/CD

---

# Author

**Madeshwaran**

Python | Selenium | Pytest | API Testing | SDET Automation

GitHub:
[https://github.com/madeshwaranbase](https://github.com/madeshwaranbase)

They are not useful README content and make the repository look less polished. The version above is cleaner and more appropriate for an **SDET portfolio/recruiter review**.
