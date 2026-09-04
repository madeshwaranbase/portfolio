from selenium import webdriver


def create_driver(browser="chrome", headless=False):
    browser = browser.lower()

    if browser == "chrome":
        options = webdriver.ChromeOptions()

        if headless:
            options.add_argument("--headless=new")

        options.add_argument("--start-maximized")

        return webdriver.Chrome(options=options)

    elif browser == "firefox":
        options = webdriver.FirefoxOptions()

        if headless:
            options.add_argument("--headless")

        return webdriver.Firefox(options=options)

    elif browser == "edge":
        options = webdriver.EdgeOptions()

        if headless:
            options.add_argument("--headless")

        return webdriver.Edge(options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser}")
