from pages.login_page import LoginPage
from utils.config_reader import get_config


def test_invalid_login(driver):
    config = get_config()
    page = LoginPage(driver)

    page.open(config["application"]["base_url"])
    page.login("tomsmith", "wrong-password")

    assert "Your password is invalid!" in page.get_message()
