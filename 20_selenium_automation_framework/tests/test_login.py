from pages.login_page import LoginPage
from utils.config_reader import get_config
from utils.logger import get_logger


logger = get_logger(__name__)


def test_valid_login(driver):
    config = get_config()
    page = LoginPage(driver)

    logger.info("Opening login page")
    page.open(config["application"]["base_url"])

    logger.info("Logging in with valid credentials")
    page.login("tomsmith", "SuperSecretPassword!")

    message = page.get_message()

    assert "You logged into a secure area!" in message
    logger.info("Login test passed")
