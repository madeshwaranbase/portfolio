from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_file_upload(tmp_path):
    file_path = tmp_path / "sample.txt"
    file_path.write_text("Selenium upload test", encoding="utf-8")

    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/upload")

    driver.find_element(By.ID, "file-upload").send_keys(str(file_path))
    driver.find_element(By.ID, "file-submit").click()

    uploaded_name = driver.find_element(By.ID, "uploaded-files").text
    assert uploaded_name == "sample.txt"

    driver.quit()
