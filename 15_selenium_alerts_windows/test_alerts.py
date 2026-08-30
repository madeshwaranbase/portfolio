from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def test_javascript_alert():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()

    alert = WebDriverWait(driver, 5).until(lambda d: d.switch_to.alert)
    assert alert.text == "I am a JS Alert"

    alert.accept()
    driver.quit()
