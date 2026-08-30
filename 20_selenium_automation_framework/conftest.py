import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils.config_reader import get_config


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default=None,
        help="Browser name. Currently supports chrome."
    )
    parser.addoption(
        "--headless",
        action="store_true",
        help="Run Chrome in headless mode."
    )


@pytest.fixture
def driver(request):
    config = get_config()
    browser = request.config.getoption("--browser") or config["browser"]["name"]
    headless = request.config.getoption("--headless")

    if browser.lower() != "chrome":
        raise ValueError("This example framework currently supports Chrome.")

    options = Options()

    if headless:
        options.add_argument("--headless=new")

    options.add_argument("--window-size=1440,900")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(3)

    yield driver

    driver.quit()
