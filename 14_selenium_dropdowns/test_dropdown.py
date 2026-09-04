import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_dropdown(driver):
    driver.get("https://the-internet.herokuapp.com/dropdown")

    dropdown = Select(driver.find_element(By.ID, "dropdown"))

    dropdown.select_by_visible_text("Option 2")

    assert dropdown.first_selected_option.text == "Option 2"
