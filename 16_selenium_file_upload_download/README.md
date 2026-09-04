# Selenium File Upload Automation Test

Automated file upload test using **Python, Selenium WebDriver, and Pytest**.

## Project Overview

This project automates the **File Upload** functionality of **The Internet** web application.

**URL:** `https://the-internet.herokuapp.com/upload`

The test creates a temporary text file, uploads it through the application, and verifies that the correct filename is displayed after upload.

## Tech Stack

* Python
* Selenium WebDriver
* Pytest
* Google Chrome

## Test Scenario

### File Upload

1. Launch the Chrome browser.
2. Create a temporary file named `sample.txt`.
3. Write the following content to the file:

   ```text
   Selenium upload test
   ```
4. Navigate to the File Upload page.
5. Locate the file upload field.
6. Upload the file using Selenium `send_keys()`.
7. Click the **Upload** button.
8. Retrieve the uploaded filename.
9. Verify that the filename is:

   ```text
   sample.txt
   ```
10. Close the browser after test execution.

## Technical Implementation

The test uses Pytest's `tmp_path` fixture to create a temporary file:

```python
file_path = tmp_path / "sample.txt"
file_path.write_text("Selenium upload test", encoding="utf-8")
```

The file is uploaded directly through the HTML file input:

```python
driver.find_element(
    By.ID, "file-upload"
).send_keys(str(file_path))
```

This approach avoids interacting with the operating system's file picker.

## Project Structure

```text
14_selenium_file_upload_test/
│
├── README.md
├── requirements.txt
└── test_file_upload.py
```

## Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Run the Test

Run all tests:

```bash
pytest -v
```

Or run this specific test:

```bash
pytest -v test_file_upload.py
```

## Automation Features

* Pytest fixture for WebDriver setup and teardown
* Temporary file creation using `tmp_path`
* Selenium file upload using `send_keys()`
* Element identification using `By.ID`
* Uploaded filename validation
* Assertion-based verification
* Automatic browser cleanup

## Expected Result

After uploading the file, the application should display:

```text
sample.txt
```

The test passes when the uploaded filename matches the expected filename.

### Expected Test Result

```text
1 passed
```
