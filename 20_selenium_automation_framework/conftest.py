import pytest

from utils.config_reader import ConfigReader
from utils.driver_factory import create_driver


config = ConfigReader()


@pytest.fixture
def driver():
    browser = config.get("browser", "browser")
    headless = config.get_boolean("browser", "headless")

    driver = create_driver(
        browser=browser,
        headless=headless
    )

    implicit_wait = config.get_int(
        "timeouts",
        "implicit_wait"
    )

    driver.implicitly_wait(implicit_wait)

    yield driver

    driver.quit()
