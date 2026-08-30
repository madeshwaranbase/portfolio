import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


def test_example(driver):
    driver.get("https://the-internet.herokuapp.com/")
    assert "The Internet" in driver.title
