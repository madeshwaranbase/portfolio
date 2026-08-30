from selenium import webdriver
from selenium.webdriver.common.by import By


def test_table_contains_expected_person():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/tables")

    rows = driver.find_elements(By.CSS_SELECTOR, "#table1 tbody tr")

    names = []
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        names.append(cells[1].text)

    assert "John Smith" in names

    driver.quit()
