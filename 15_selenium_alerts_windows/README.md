# Selenium JavaScript Alert Automation Test

Automated JavaScript alert handling test using **Python, Selenium WebDriver, and Pytest**.

## Project Overview

This project automates JavaScript alert handling on **The Internet** web application.

**URL:** `https://the-internet.herokuapp.com/javascript_alerts`

The test triggers a JavaScript alert, verifies its message, and accepts the alert.

## Tech Stack

* Python
* Selenium WebDriver
* Pytest
* Google Chrome

## Test Scenario

### JavaScript Alert

1. Launch the Chrome browser.
2. Navigate to the JavaScript Alerts page.
3. Click **Click for JS Alert**.
4. Wait for the JavaScript alert to appear.
5. Retrieve and verify the alert text.
6. Verify that the message is:

   ```text
   I am a JS Alert
   ```
7. Accept the alert.
8. Close the browser after test execution.

## Technical Implementation

The test uses Selenium's:

```python
driver.switch_to.alert
```

to switch the browser context from the webpage to the JavaScript alert.

An explicit wait is used to wait for the alert:

```python
WebDriverWait(driver, 5).until(
    lambda d: d.switch_to.alert
)
```

## Project Structure

```text
13_selenium_javascript_alert_test/
│
├── README.md
├── requirements.txt
└── test_javascript_alert.py
```

## Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Run the Test

Run the test using:

```bash
pytest -v
```

Or run the specific test:

```bash
pytest -v test_javascript_alert.py
```

## Automation Features

* Pytest fixture for WebDriver setup and teardown
* Chrome WebDriver automation
* Explicit wait for JavaScript alert
* Alert text validation
* `switch_to.alert` implementation
* Alert acceptance using `accept()`
* Assertion-based validation
* Automatic browser cleanup

## Expected Result

The JavaScript alert should display:

```text
I am a JS Alert
```

The alert should be accepted successfully and the test should pass.

### Expected Test Result

```text
1 passed
```
