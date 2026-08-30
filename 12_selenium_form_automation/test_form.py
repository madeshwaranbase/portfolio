from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/checkboxes")

    checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")

    if not checkboxes[0].is_selected():
        checkboxes[0].click()

    assert checkboxes[0].is_selected()

    if checkboxes[1].is_selected():
        checkboxes[1].click()

    assert not checkboxes[1].is_selected()

    driver.quit()
