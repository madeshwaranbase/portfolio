import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


def test_home_page(driver):
    driver.get("https://the-internet.herokuapp.com/")
    assert "The Internet" in driver.title


def test_login_page(driver):
    driver.get("https://the-internet.herokuapp.com/login")
    assert "Login Page" in driver.title


def test_checkbox_page(driver):
    driver.get("https://the-internet.herokuapp.com/checkboxes")
    assert "Checkboxes" in driver.title
