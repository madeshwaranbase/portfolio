import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.mark.parametrize(
    "username,password,expected",
    [
        ("tomsmith", "SuperSecretPassword!", "success"),
        ("tomsmith", "wrong-password", "failure"),
        ("wrong-user", "SuperSecretPassword!", "failure"),
    ],
)
def test_login_data(driver, username, password, expected):
    driver.get("https://the-internet.herokuapp.com/login")

    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "button.radius").click()

    message = driver.find_element(By.ID, "flash").text

    if expected == "success":
        assert "You logged into a secure area!" in message
    else:
        assert (
            "Your username is invalid!" in message
            or "Your password is invalid!" in message
        )
