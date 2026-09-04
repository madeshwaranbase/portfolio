### Requirement — Parameterized Selenium Login Test

Automate the login functionality of **The Internet** application using **Python, Selenium WebDriver, and Pytest parameterization**.

**URL:** `https://the-internet.herokuapp.com/login`

### Test Scenario

Validate login behavior using multiple sets of credentials.

| Username     | Password               | Expected Result |
| ------------ | ---------------------- | --------------- |
| `tomsmith`   | `SuperSecretPassword!` | Success         |
| `tomsmith`   | `wrong-password`       | Failure         |
| `wrong-user` | `SuperSecretPassword!` | Failure         |

### Requirements

1. Launch Chrome for each test case.
2. Navigate to the login page.
3. Enter the username and password provided by the test data.
4. Click the **Login** button.
5. Read the message displayed in the `flash` element.
6. For a successful login, verify:

   ```text
   You logged into a secure area!
   ```
7. For an unsuccessful login, verify either:

   ```text
   Your username is invalid!
   ```

   or:

   ```text
   Your password is invalid!
   ```
8. Close the browser after each test execution.
9. Use `pytest.mark.parametrize` to execute the same test with multiple credential combinations.

### Expected Result

All **3 parameterized test cases** should pass:

```text
3 passed
```

