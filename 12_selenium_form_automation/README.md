# Requirement — Selenium Checkbox Automation

## Requirement

Automate the checkbox functionality of **The Internet** web application using **Python and Selenium WebDriver**.

**URL:** `https://the-internet.herokuapp.com/checkboxes`

### Test Scenario: Checkbox Selection and Deselection

1. Launch the Chrome browser.
2. Navigate to the Checkboxes page.
3. Locate all available checkboxes using the CSS selector:

   ```css
   input[type='checkbox']
   ```
4. Verify the state of the **first checkbox**.

   * If it is not selected, select it.
   * Verify that the first checkbox is selected.
5. Verify the state of the **second checkbox**.

   * If it is selected, deselect it.
   * Verify that the second checkbox is not selected.
6. Close the browser after test execution.

### Technical Requirements

* Use **Python**.
* Use **Selenium WebDriver**.
* Use **Chrome WebDriver**.
* Use `find_elements()` to locate the checkboxes.
* Use `is_selected()` to verify checkbox state.
* Use `click()` to select/deselect checkboxes.
* Use Pytest assertions to validate the expected states.
* Ensure the browser is closed after test execution.

### Expected Result

* **First checkbox:** Selected.
* **Second checkbox:** Not selected.
* Test should pass when both conditions are satisfied.
