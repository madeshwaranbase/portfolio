from selenium.webdriver.common.by import By


class LoginPage:
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.radius")
    FLASH_MESSAGE = (By.ID, "flash")

    def __init__(self, driver):
        self.driver = driver

    def open(self, base_url):
        self.driver.get(f"{base_url}/login")

    def login(self, username, password):
        self.driver.find_element(*self.USERNAME).send_keys(username)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def get_message(self):
        return self.driver.find_element(*self.FLASH_MESSAGE).text
