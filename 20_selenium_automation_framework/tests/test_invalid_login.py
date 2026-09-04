import pytest

from pages.login_page import LoginPage


@pytest.mark.parametrize(
    "username,password,expected_message",
    [
        (
            "tomsmith",
            "wrong-password",
            "Your password is invalid!"
        ),
        (
            "wrong-user",
            "SuperSecretPassword!",
            "Your username is invalid!"
        ),
    ],
)
def test_invalid_login(
    driver,
    username,
    password,
    expected_message
):
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login(username, password)

    assert expected_message in login_page.get_flash_message()
