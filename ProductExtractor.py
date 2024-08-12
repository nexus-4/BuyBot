from bs4 import BeautifulSoup


class ProductExtractor:
    def __init__(self, page_source: str):
        self.page_source = page_source
        self.soup = BeautifulSoup(self.page_source, 'html.parser')

    def _extract_element_text(self, tag: str, class_name: str) -> str:
        element = self.soup.find(tag, {"class": class_name})
        if element:
            return element.text.strip()
        else:
            return " "

    def extract_product_name(self) -> str:
        return self._extract_element_text("h1", "name___120FN")

    def extract_product_price(self) -> str:
        return self._extract_element_text("div", "gl-price-item")

