# Selenium Multiple Page Title Validation

Automated page title validation tests using **Python, Selenium WebDriver, and Pytest**.

## Project Overview

This project demonstrates how to validate the page titles of multiple pages in **The Internet** web application.

The test suite verifies:

* Home page title
* Login page title
* Checkboxes page title

A reusable **Pytest WebDriver fixture** is used for browser setup and cleanup.

## Tech Stack

* Python
* Selenium WebDriver
* Pytest
* Google Chrome

## Test Scenarios

### 1. Home Page

**URL:** `https://the-internet.herokuapp.com/`

Expected title:

```text
The Internet
```

### 2. Login Page

**URL:** `https://the-internet.herokuapp.com/login`

Expected title:

```text
Login Page
```

### 3. Checkboxes Page

**URL:** `https://the-internet.herokuapp.com/checkboxes`

Expected title:

```text
Checkboxes
```

## Technical Implementation

A Pytest fixture manages the Selenium WebDriver:

```python
@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()
```

This ensures the browser is closed after every test, including when a test fails.

## Project Structure

```text
16_selenium_multiple_page_validation/
│
├── README.md
├── requirements.txt
└── test_page_titles.py
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

Run the specific test file:

```bash
pytest -v test_page_titles.py
```

## Automation Features

* Pytest test framework
* Reusable WebDriver fixture
* Chrome browser automation
* Multiple independent test cases
* Page title validation
* Automatic browser cleanup
* Assertion-based verification

## Expected Result

All three tests should pass:

```text
test_home_page PASSED
test_login_page PASSED
test_checkbox_page PASSED

3 passed
```

This test suite demonstrates a clean foundation for building a reusable Selenium + Pytest automation framework.
