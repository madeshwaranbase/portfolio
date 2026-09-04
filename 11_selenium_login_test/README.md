# Selenium Login Automation Test

Automated login test using **Python, Selenium WebDriver, and Pytest**.

## Project Overview

This project automates the login functionality of [The Internet](https://the-internet.herokuapp.com/login) application.

The test verifies that a user can successfully log in with valid credentials and that the expected success message is displayed.

## Tech Stack

* **Python**
* **Selenium WebDriver**
* **Pytest**
* **Google Chrome**

## Test Scenario

### Successful Login

1. Open the login page.
2. Enter the valid username.
3. Enter the valid password.
4. Click the **Login** button.
5. Wait for the success message.
6. Verify that the message contains:

```text
You logged into a secure area!
```

7. Close the browser after test execution.

## Test Credentials

| Field    | Value                  |
| -------- | ---------------------- |
| Username | `tomsmith`             |
| Password | `SuperSecretPassword!` |

## Project Structure

```text
11_selenium_login_test/
│
├── README.md
├── requirements.txt
└── test_login.py
```

## Installation

Clone the repository and navigate to the project:

```bash
cd 11_selenium_login_test
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Run the Test

Execute the test using:

```bash
pytest test_login.py
```

For more detailed output:

```bash
pytest -v test_login.py
```

## Automation Features

* Pytest fixture for WebDriver setup and teardown
* Chrome WebDriver automation
* Implicit wait configuration
* Explicit wait using `WebDriverWait`
* Expected Conditions using `visibility_of_element_located`
* Selenium locators using `ID` and `CSS_SELECTOR`
* Assertion-based validation
* Automatic browser cleanup using fixture teardown

## Expected Result

The test should pass when the valid credentials successfully log the user into the secure area and the following message is displayed:

```text
You logged into a secure area!
```

## Author

**Madeshwaran**
Python & Selenium Automation Portfolio
