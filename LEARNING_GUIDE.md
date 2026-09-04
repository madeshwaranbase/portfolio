# LEARNING GUIDE — Python & Selenium SDET Portfolio

This learning guide covers all **20 projects** in the portfolio, from Python fundamentals to a production-style Selenium automation framework.

The projects are intentionally arranged as a progression:

```text
Python Fundamentals
        ↓
Python Automation & Utilities
        ↓
API / CLI Testing Concepts
        ↓
Selenium Fundamentals
        ↓
Advanced Selenium + Pytest
        ↓
Automation Framework Design
        ↓
SDET-Level Practices
```

---

# Portfolio Roadmap

| #  | Project                        | Primary Skills                             |
| -- | ------------------------------ | ------------------------------------------ |
| 01 | Python Calculator              | Functions, conditions, input handling      |
| 02 | Number Guessing Game           | Loops, conditions, randomization           |
| 03 | Expense Tracker                | CRUD, lists/dictionaries, file handling    |
| 04 | Password Generator             | Randomization, security concepts           |
| 05 | File Organizer                 | File system automation, `pathlib`          |
| 06 | Employee CSV Manager           | CSV, data processing, CRUD                 |
| 07 | Log File Analyzer              | Log parsing, regex, reporting              |
| 08 | API Data Checker               | API testing, `requests`, JSON              |
| 09 | CLI Todo App                   | CLI design, persistence, application logic |
| 10 | Test Result Reporter           | Test reporting, data aggregation           |
| 11 | Selenium Login Test            | Selenium fundamentals                      |
| 12 | Selenium Form Automation       | Forms, input controls                      |
| 13 | Selenium Web Tables            | Dynamic table handling                     |
| 14 | Selenium Dropdowns             | `Select` class                             |
| 15 | Selenium Alerts & Windows      | Alerts, browser windows                    |
| 16 | Selenium File Upload/Download  | File handling + Selenium                   |
| 17 | Selenium Screenshot on Failure | Pytest hooks, debugging                    |
| 18 | Selenium Data-Driven Testing   | Parameterization                           |
| 19 | Selenium Parallel Testing      | Parallel execution                         |
| 20 | Selenium Automation Framework  | Framework architecture + SDET practices    |

---

# 01 — Python Calculator

## Objective

Build a command-line calculator that performs basic arithmetic operations.

## Concepts

Learn:

* Variables
* Data types
* Functions
* `if / elif / else`
* User input
* Exception handling
* Arithmetic operators

## Example

```python
def add(a, b):
    return a + b
```

## SDET Relevance

This project establishes the programming fundamentals required to write automation frameworks.

### Interview Topics

Be able to explain:

* Functions
* Return values
* Exception handling
* Type conversion
* Input validation

---

# 02 — Number Guessing Game

## Objective

Build a game where the user attempts to guess a randomly generated number.

## Concepts

Learn:

* `random`
* `while` loops
* Conditional logic
* Counters
* Input validation

## Core Flow

```text
Generate number
      ↓
Get user input
      ↓
Compare values
      ↓
Too high / Too low / Correct
      ↓
Repeat
```

## SDET Relevance

Develops understanding of:

* Control flow
* Boundary conditions
* Repeated execution
* Validation logic

These concepts are directly applicable to test-case design.

---

# 03 — Expense Tracker

## Objective

Create an application that allows users to add, view, update, and delete expenses.

## Concepts

Learn:

* Lists
* Dictionaries
* Functions
* CRUD operations
* File persistence
* Data validation

## CRUD

```text
Create
Read
Update
Delete
```

## SDET Relevance

CRUD concepts appear everywhere in testing.

You should understand how to test:

* Valid data
* Missing data
* Invalid data
* Duplicate data
* Boundary values

---

# 04 — Password Generator

## Objective

Create a password generator with configurable password length and character types.

## Concepts

Learn:

* `random`
* `string`
* Character sets
* Functions
* Validation

Example character groups:

```text
Lowercase
Uppercase
Numbers
Special characters
```

## SDET Relevance

Learn to think about:

* Security
* Input boundaries
* Random data
* Validation
* Negative scenarios

---

# 05 — File Organizer

## Objective

Automatically organize files into folders based on their extensions.

Example:

```text
Downloads/
├── Images/
├── Documents/
├── Videos/
└── Others/
```

## Concepts

Learn:

* `pathlib`
* File operations
* Directory creation
* File moving
* Extensions

## SDET Relevance

This introduces **filesystem automation**, which is useful for:

* Test data management
* Reports
* Screenshots
* Downloads
* Test artifacts

---

# 06 — Employee CSV Manager

## Objective

Build a system for managing employee records using CSV files.

## Concepts

Learn:

* CSV files
* Reading/writing data
* Dictionaries
* Searching
* Updating records
* Deleting records

## SDET Relevance

CSV is commonly used for:

* Test data
* Parameterized tests
* Bulk test execution
* Data-driven testing

---

# 07 — Log File Analyzer

## Objective

Read an application log and identify important events.

Example:

```text
INFO
WARNING
ERROR
```

## Concepts

Learn:

* File reading
* String processing
* Regular expressions
* Counting
* Report generation

Example output:

```text
INFO: 120
WARNING: 15
ERROR: 7
```

## SDET Relevance

Log analysis is an important debugging skill.

When a UI test fails, an SDET should be able to correlate:

```text
Test failure
     ↓
Application logs
     ↓
Root cause
```

---

# 08 — API Data Checker

## Objective

Validate API responses using Python.

## Concepts

Learn:

* HTTP
* GET requests
* Status codes
* JSON
* Response validation
* Assertions

Example:

```python
response = requests.get(url)

assert response.status_code == 200
```

## Important HTTP Concepts

Understand:

```text
GET
POST
PUT
PATCH
DELETE
```

And:

```text
200
201
400
401
403
404
500
```

## SDET Relevance

This is the transition from general Python development toward **test automation engineering**.

---

# 09 — CLI Todo App

## Objective

Build a command-line Todo application.

## Concepts

Learn:

* Application structure
* CRUD
* Persistence
* CLI menus
* Input validation
* Modular programming

## SDET Relevance

Before automating an application, understand the application's behavior.

Think in terms of:

```text
Requirement
   ↓
Expected behavior
   ↓
Test scenario
   ↓
Validation
```

---

# 10 — Test Result Reporter

## Objective

Build a utility that processes test results and generates a summary report.

Example:

```text
Total:   100
Passed:   82
Failed:   12
Skipped:   6
Pass Rate: 82%
```

## Concepts

Learn:

* Data aggregation
* File parsing
* Reporting
* Statistics
* Automation artifacts

## SDET Relevance

This introduces the concept of **test observability**.

A test suite should not simply say:

```text
FAILED
```

It should help answer:

```text
What failed?
Where?
When?
Why?
How many?
```

---

# 11 — Selenium Login Test

## Objective

Automate a successful login.

## Concepts

Learn:

* Selenium WebDriver
* Locators
* `send_keys()`
* `click()`
* Assertions
* Browser lifecycle

Example:

```python
driver.find_element(By.ID, "username").send_keys("tomsmith")
```

## SDET Skills

Understand:

* ID locator
* CSS selector
* XPath
* Browser automation
* Assertions

This is your entry point into **UI automation**.

---

# 12 — Selenium Form Automation

## Objective

Automate form fields and validate submitted information.

## Concepts

Learn:

* Text fields
* Checkboxes
* Radio buttons
* Buttons
* Form submission
* Element state

## Important Selenium APIs

```python
send_keys()
click()
is_selected()
is_enabled()
is_displayed()
```

## SDET Relevance

Learn how to design tests around UI controls rather than individual clicks.

---

# 13 — Selenium Web Tables

## Objective

Read and validate information from a dynamic HTML table.

## Concepts

Learn:

* Rows
* Columns
* Nested element searches
* Loops
* Data extraction
* Assertions

Example:

```python
rows = driver.find_elements(
    By.CSS_SELECTOR,
    "#table1 tbody tr"
)
```

## SDET Relevance

Real applications frequently contain:

* Tables
* Grids
* Search results
* Pagination
* Dynamic data

You should be comfortable extracting and validating structured UI data.

---

# 14 — Selenium Dropdowns

## Objective

Automate HTML `<select>` dropdowns.

## Concepts

Learn Selenium's:

```python
from selenium.webdriver.support.ui import Select
```

Example:

```python
dropdown.select_by_visible_text("Option 2")
```

Also learn:

```python
select_by_index()
select_by_value()
```

## SDET Relevance

Understand the difference between:

* Native HTML dropdowns
* Custom JavaScript dropdowns

They require different automation strategies.

---

# 15 — Selenium Alerts & Windows

## Objective

Automate JavaScript alerts and browser window interactions.

## Concepts

Learn:

```python
driver.switch_to.alert
```

Alert operations:

```text
accept()
dismiss()
send_keys()
text
```

Also learn:

```python
driver.window_handles
driver.switch_to.window()
```

## SDET Relevance

Modern applications frequently use:

* Alerts
* New tabs
* Popups
* Authentication windows
* Multiple browser contexts

---

# 16 — Selenium File Upload & Download

## Objective

Automate uploading and validating downloaded files.

## Upload

Use:

```python
file_input.send_keys(file_path)
```

No OS-level file picker automation is required for a standard HTML file input.

## Concepts

Learn:

* File paths
* Temporary files
* Selenium file upload
* Download validation
* Filesystem verification

## SDET Relevance

File automation is common in:

* Banking
* HR applications
* Reporting systems
* Document management
* Data import/export workflows

---

# 17 — Selenium Screenshot on Failure

## Objective

Automatically capture screenshots when Selenium tests fail.

## Concepts

Learn:

* Pytest hooks
* `pytest_runtest_makereport`
* Test lifecycle
* Selenium screenshots
* Failure diagnostics

Example:

```python
driver.save_screenshot("screenshots/test_login.png")
```

## SDET Relevance

This is an important **debugging capability**.

The failure becomes:

```text
Test Failure
     ↓
Screenshot
     ↓
HTML Report
     ↓
Log
     ↓
Root Cause Analysis
```

---

# 18 — Selenium Data-Driven Testing

## Objective

Execute the same Selenium test with multiple sets of data.

## Concepts

Learn:

```python
@pytest.mark.parametrize()
```

Example:

```python
@pytest.mark.parametrize(
    "username,password",
    [
        ("tomsmith", "SuperSecretPassword!"),
        ("tomsmith", "wrong-password"),
        ("wrong-user", "SuperSecretPassword!"),
    ]
)
```

## Benefits

* Less duplicated code
* Higher test coverage
* Easy maintenance
* Better negative testing

## SDET Relevance

This is a core automation-framework skill.

You should understand how to separate:

```text
Test Logic
     +
Test Data
```

---

# 19 — Selenium Parallel Testing

## Objective

Run multiple Selenium tests concurrently to reduce execution time.

## Concepts

Learn:

* `pytest-xdist`
* Parallel execution
* Worker processes
* Test isolation
* Thread/process safety

Example:

```bash
pytest -n auto
```

Conceptually:

```text
              Test Suite
                  │
        ┌─────────┼─────────┐
        ↓         ↓         ↓
     Worker 1  Worker 2  Worker 3
        ↓         ↓         ↓
      Tests     Tests     Tests
```

## SDET Relevance

Parallel execution becomes important when a regression suite grows from:

```text
20 tests
```

to:

```text
500+ tests
```

The objective is to reduce feedback time.

---

# 20 — Selenium Python Automation Framework

## Objective

Combine everything learned into a **maintainable, scalable SDET automation framework**.

This is the flagship project in the portfolio.

---

# Project 20 Architecture

```text
                        TEST CASES
                            │
                            ▼
                      PAGE OBJECTS
                            │
                            ▼
                        BASE PAGE
                            │
                            ▼
                     SELENIUM DRIVER
                            │
                            ▼
                       APPLICATION


      ┌─────────────────────────────────────┐
      │             Framework               │
      │                                     │
      │ Config       Driver Factory         │
      │ Logger       Wait Utilities         │
      │ Reporting    Screenshots             │
      │ Test Data    API Utilities           │
      └─────────────────────────────────────┘
```

---

# Page Object Model

Pages contain:

```text
Locators
Actions
Page-specific behavior
```

Tests contain:

```text
Business validation
Assertions
Test scenarios
```

Example:

```python
login_page.login(username, password)
```

rather than:

```python
driver.find_element(...)
driver.find_element(...)
driver.click()
```

---

# Base Page

Centralize common operations:

```text
click()
enter_text()
get_text()
wait_for_element()
is_visible()
get_title()
```

This reduces duplicated Selenium code.

---

# Configuration

Use:

```text
config/config.ini
```

For:

```text
Base URL
Browser
Headless mode
Timeouts
Environment settings
```

The test code should not contain environment-specific values wherever practical.

---

# Driver Factory

Centralize browser creation.

Support:

```text
Chrome
Firefox
Edge
```

and:

```text
Headed
Headless
```

Example concept:

```text
Test
 ↓
conftest.py
 ↓
Driver Factory
 ↓
Browser
```

---

# Fixtures

`conftest.py` manages:

* WebDriver creation
* Configuration
* Setup
* Teardown
* Future framework-level fixtures

Tests should simply request:

```python
def test_login(driver):
```

---

# Logging

Centralized logging should record useful events:

```text
Test started
Page opened
Element interaction
Important validation
Test completed
Failure
```

Avoid excessive logging such as recording every insignificant Selenium operation.

---

# Wait Strategy

Prefer explicit waits:

```python
WebDriverWait(driver, 10).until(...)
```

Avoid unnecessary:

```python
time.sleep(5)
```

A mature framework should synchronize with **application state**, not arbitrary time delays.

---

# Test Organization

Recommended structure:

```text
tests/
├── smoke/
├── regression/
└── negative/
```

Example:

```python
@pytest.mark.smoke
def test_valid_login():
    ...
```

Run:

```bash
pytest -m smoke
```

---

# Test Data

Separate test data from test implementation.

Example:

```text
test_data/
├── login_data.json
└── users.json
```

This makes data-driven testing easier to maintain.

---

# Reporting

Generate HTML reports:

```text
reports/
└── report.html
```

Reports should provide:

* Test status
* Execution duration
* Failure details
* Test names
* Useful artifacts

---

# Screenshot on Failure

When a UI test fails:

```text
Failure
   ↓
Pytest Hook
   ↓
Screenshot
   ↓
screenshots/
```

This is particularly valuable in CI environments where you cannot directly watch the browser.

---

# Parallel Execution

Support:

```bash
pytest -n auto
```

The framework must ensure tests are independent enough to run concurrently.

Avoid shared mutable state between tests.

---

# API + UI Testing

A strong SDET framework can eventually combine API and UI validation.

Example:

```text
API
 ↓
Create test data
 ↓
UI
 ↓
Validate data
 ↓
API
 ↓
Verify backend state
```

This demonstrates understanding beyond pure UI automation.

---

# CI/CD

Integrate the framework with GitHub Actions.

Target workflow:

```text
Developer Push
      ↓
GitHub
      ↓
GitHub Actions
      ↓
Install Dependencies
      ↓
Run Tests
      ↓
Generate Report
      ↓
Upload Artifacts
      ↓
Pass / Fail
```

This is a major SDET portfolio feature.

---

# Final Framework Structure

The final Project 20 should evolve toward:

```text
20_selenium_automation_framework/
│
├── config/
│   ├── config.ini
│   └── environments/
│
├── pages/
│   ├── __init__.py
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
│   ├── __init__.py
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
├── README.md
└── LEARNING_GUIDE.md
```

---

# SDET Skills Developed Across the 20 Projects

## Python

By the end, you should understand:

```text
Variables
Data Types
Functions
Conditions
Loops
Collections
Files
Exceptions
Modules
Packages
OOP
JSON
CSV
Regex
CLI applications
```

---

## Testing

You should understand:

```text
Test Cases
Assertions
Positive Testing
Negative Testing
Boundary Testing
Data-Driven Testing
Smoke Testing
Regression Testing
Test Isolation
Test Reporting
Failure Analysis
```

---

## Selenium

You should understand:

```text
WebDriver
Locators
XPath
CSS Selectors
Web Elements
Waits
Forms
Tables
Dropdowns
Alerts
Windows
File Upload
Downloads
Screenshots
```

---

## Pytest

You should understand:

```text
Fixtures
conftest.py
Parameterization
Markers
Hooks
Assertions
Test Discovery
Plugins
HTML Reports
Parallel Execution
```

---

## Framework Engineering

You should understand:

```text
Page Object Model
Base Page
Driver Factory
Configuration Management
Logging
Test Data Management
Reusable Utilities
Reporting
Failure Artifacts
CI/CD
```

---

# Interview Preparation

For each project, don't just memorize the code.

Be able to answer:

### 1. What problem does the project solve?

### 2. Why did you choose this implementation?

### 3. What happens when invalid input is provided?

### 4. How would you test it?

### 5. How would you improve it?

### 6. What edge cases would you cover?

### 7. How would you make it scalable?

This changes your portfolio from:

> "I followed Selenium tutorials."

to:

> "I understand how to design, implement, validate, and maintain automation systems."

---

# Recommended Interview Story

The strongest way to present the portfolio is as a progression:

```text
Projects 1–5
     ↓
Python Programming Foundation

Projects 6–10
     ↓
Automation, Data & Testing Utilities

Projects 11–16
     ↓
Selenium UI Automation

Projects 17–19
     ↓
Advanced Pytest & Selenium

Project 20
     ↓
Complete SDET Automation Framework
```

## Final Goal

By Project 20, you should be able to explain an end-to-end automation architecture:

```text
Requirement
    ↓
Test Scenario
    ↓
Test Data
    ↓
Pytest
    ↓
Fixture
    ↓
Driver Factory
    ↓
Page Object
    ↓
Base Page
    ↓
Selenium
    ↓
Application
    ↓
Assertion
    ↓
Logging
    ↓
Screenshot / Report
    ↓
CI/CD

