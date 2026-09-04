import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

LOGIN_URL = "https://the-internet.herokuapp.com/login"


@pytest.fixture
def driver():
    drv = webdriver.Chrome()
    drv.implicitly_wait(2)
    yield drv
    drv.quit()  # always runs, even if the test body fails/asserts


def test_login(driver):
    driver.get(LOGIN_URL)
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button.radius").click()

    flash = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "flash"))
    )

    assert "You logged into a secure area!" in flash.text
