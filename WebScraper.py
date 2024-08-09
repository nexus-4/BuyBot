from selenium import webdriver
from selenium.common.exceptions import WebDriverException


class WebScraper:
    supported_browsers = {
        "Safari": webdriver.Safari,
        "Firefox": webdriver.Firefox,
        "Edge": webdriver.Edge,
        "Chrome": webdriver.Chrome
    }

    def __init__(self, url, browser="Chrome", headless=False, implicitly_wait=10):
        if browser not in self.supported_browsers:
            raise ValueError(f"Unsupported browser: {browser}")

        self.url = url
        self.browser = browser
        self.headless = headless
        self.implicitly_wait = implicitly_wait
        self.driver = self.get_driver()

    def get_driver(self):
        try:
            options = None

            if self.browser in ["Chrome", "Firefox"]:
                options_class = webdriver.ChromeOptions if self.browser == "Chrome" else webdriver.FirefoxOptions
                options = options_class()

                if self.headless:
                    options.add_argument("--headless")

            driver = self.supported_browsers[self.browser](options=options)
            driver.implicitly_wait(self.implicitly_wait)
            return driver

        except WebDriverException as e:
            raise Exception(f"Failed to initialize {self.browser} driver: {str(e)}")

    def navigate_to_url(self):
        try:
            self.driver.get(self.url)
        except WebDriverException as e:
            raise Exception(f"Failed to navigate to {self.url}: {str(e)}")

    def get_page_source(self):
        try:
            return self.driver.page_source
        except WebDriverException as e:
            raise Exception(f"Failed to get page source: {str(e)}")

    def close_driver(self):
        try:
            if self.driver:
                self.driver.quit()
        except WebDriverException as e:
            raise Exception(f"Failed to close driver: {str(e)}")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close_driver()

