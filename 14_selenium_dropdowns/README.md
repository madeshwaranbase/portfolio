# Selenium Dropdown Automation Test

Automated dropdown selection test using **Python, Selenium WebDriver, and Pytest**.

## Project Overview

This project automates the dropdown functionality of **The Internet** web application.

**URL:** `https://the-internet.herokuapp.com/dropdown`

The test selects **Option 2** from the dropdown and verifies that the correct option has been selected.

## Tech Stack

* Python
* Selenium WebDriver
* Pytest
* Google Chrome

## Test Scenario

### Dropdown Selection

1. Launch the Chrome browser.
2. Navigate to the Dropdown page.
3. Locate the dropdown using its ID.
4. Create a Selenium `Select` object.
5. Select **Option 2** using visible text.
6. Verify that **Option 2** is selected.
7. Close the browser after test execution.

## Expected Result

The dropdown should contain **Option 2**, and after selection:

```text
Option 2
```

should be displayed as the selected option.

## Project Structure

```text
12_selenium_dropdown_test/
│
├── README.md
├── requirements.txt
└── test_dropdown.py
```

## Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Run the Test

Run the test with:

```bash
pytest -v
```

Or run the specific test:

```bash
pytest -v test_dropdown.py
```

## Automation Features

* Pytest fixture for WebDriver setup and teardown
* Chrome WebDriver automation
* Selenium `Select` class for dropdown handling
* Selection by visible text
* Assertion-based validation
* Automatic browser cleanup

## Expected Test Result

```text
1 passed
```

The test passes when **Option 2** is successfully selected and verified.
