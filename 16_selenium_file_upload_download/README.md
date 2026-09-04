Requirement — Selenium File Upload Automation

Automate the File Upload functionality of The Internet web application using Python, Selenium WebDriver, and Pytest.

URL: https://the-internet.herokuapp.com/upload

Test Scenario
Launch the Chrome browser.
Create a temporary file named sample.txt.

Add the content:

Selenium upload test
Navigate to the File Upload page.
Locate the file input field.
Upload sample.txt using Selenium's send_keys().
Click the Upload button.
Retrieve the uploaded filename.

Verify that the uploaded filename is:

sample.txt
Close the browser after test execution.
Technical Requirements
Use Python.
Use Selenium WebDriver.
Use Pytest.
Use the tmp_path fixture to create a temporary test file.
Use Path.write_text() to create the file.
Use send_keys() to upload the file.
Use By.ID to locate the upload elements.
Validate the uploaded filename using an assertion.
Ensure the browser is closed after execution.
