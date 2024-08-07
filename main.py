import os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

class ProductExtractor:
    def __init__(self, page_source):
        self.page_source = page_source
        self.soup = BeautifulSoup(self.page_source, 'html.parser')

    def extract_product_name(self):
        return self.soup.find("h1", {"class": "product-name"}).text.strip()

    def extract_product_price(self):
        return self.soup.find("span", {"class": "product-price"}).text.strip()

class ProductBuyer:
    def __init__(self, driver):
        self.driver = driver

    def click_buy_now_button(self):
        buy_now_button = self.driver.find_element_by_xpath("//button[@class='buy-now']")
        buy_now_button.click()

    def complete_checkout(self):
        # Add checkout logic here
        pass

def main():
    url = "https://www.example.com/product"
    scraper = WebScraper(url)
    scraper.navigate_to_url()
    page_source = scraper.get_page_source()

    extractor = ProductExtractor(page_source)
    product_name = extractor.extract_product_name()
    product_price = extractor.extract_product_price()

    buyer = ProductBuyer(scraper.driver)
    buyer.click_buy_now_button()
    buyer.complete_checkout()

    scraper.close_driver()

if __name__ == "__main__":
    main()