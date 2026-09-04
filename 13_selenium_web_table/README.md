### Requirement — Selenium Web Table Automation

Automate the **Web Tables** functionality of The Internet application using **Python and Selenium WebDriver**.

**URL:** `https://the-internet.herokuapp.com/tables`

#### Test Scenario

1. Launch the Chrome browser.
2. Navigate to the Web Tables page.
3. Locate all rows from **Table 1**.
4. Read the cells from each row.
5. Extract the **Last Name** column from each row.
6. Store the extracted names in a list.
7. Verify that **"Smith"** is present in the table.
8. Close the browser after test execution.

#### Technical Requirements

* Use Selenium WebDriver.
* Use `find_elements()` to locate table rows.
* Use CSS Selector:

  ```css
  #table1 tbody tr
  ```
* Use `find_elements(By.TAG_NAME, "td")` to locate table cells.
* Use `.text` to retrieve cell values.
* Use a Python list to store the extracted names.
* Use a Pytest assertion to validate the expected data.
* Ensure the browser is closed after execution.

#### Expected Result

The table should contain **Smith** in the Last Name column, and the test should pass.
