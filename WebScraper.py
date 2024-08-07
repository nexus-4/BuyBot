from selenium import webdriver

class WebScraper:
    def __init__(self, url, browser="Safari"):
        self.url = url
        self.browser = browser
        self.driver = self.get_driver()

    def get_driver(self):
        if self.browser == "Safari":
            return webdriver.Safari()
        elif self.browser == "Firefox":
            return webdriver.Firefox()
        elif self.browser == "Edge":
            return webdriver.Edge()
        elif self.browser == "Chrome":
            return webdriver.Chrome()
        else:
            raise ValueError("Unsupported browser")

    def navigate_to_url(self):
        self.driver.get(self.url)

    def get_page_source(self):
        return self.driver.page_source

    def close_driver(self):
        self.driver.quit()