from selenium import webdriver


def test_home_page():
    driver = webdriver.Chrome()
    try:
        driver.get("https://the-internet.herokuapp.com/")
        assert "The Internet" in driver.title
    finally:
        driver.quit()


def test_login_page():
    driver = webdriver.Chrome()
    try:
        driver.get("https://the-internet.herokuapp.com/login")
        assert "Login Page" in driver.title
    finally:
        driver.quit()


def test_checkbox_page():
    driver = webdriver.Chrome()
    try:
        driver.get("https://the-internet.herokuapp.com/checkboxes")
        assert "Checkboxes" in driver.title
    finally:
        driver.quit()
