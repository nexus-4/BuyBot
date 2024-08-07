from bs4 import BeautifulSoup

class ProductExtractor:
    def __init__(self, page_source):
        self.page_source = page_source
        self.soup = BeautifulSoup(self.page_source, 'html.parser')

    def extract_product_name(self):
        return self.soup.find("h1", {"class": "name___120FN"}).text.strip()

    def extract_product_price(self):
        return self.soup.find("span", {"class": "product-price__2Mip5"}).text.strip()