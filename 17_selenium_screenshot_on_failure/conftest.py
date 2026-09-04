from pathlib import Path

import pytest


SCREENSHOT_DIR = Path("screenshots")
SCREENSHOT_DIR.mkdir(exist_ok=True)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")

        if driver:
            screenshot_path = SCREENSHOT_DIR / f"{item.name}.png"
            driver.save_screenshot(str(screenshot_path))
