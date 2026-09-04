import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_table_contains_expected_person(driver):
    driver.get("https://the-internet.herokuapp.com/tables")

    rows = driver.find_elements(By.CSS_SELECTOR, "#table1 tbody tr")

    names = []

    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        names.append(cells[1].text)

    assert "Smith" in names
