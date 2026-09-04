import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_checkboxes(driver):
    driver.get("https://the-internet.herokuapp.com/checkboxes")

    checkboxes = driver.find_elements(
        By.CSS_SELECTOR, "input[type='checkbox']"
    )

    # First checkbox → Select
    if not checkboxes[0].is_selected():
        checkboxes[0].click()

    assert checkboxes[0].is_selected()

    # Second checkbox → Deselect
    if checkboxes[1].is_selected():
        checkboxes[1].click()

    assert not checkboxes[1].is_selected()
