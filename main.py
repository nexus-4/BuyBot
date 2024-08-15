from WebScraper import WebScraper
from ProductExtractor import ProductExtractor


def main():
    url = "https://www.adidas.com.br/yeezy-boost-700/FV5304.html"
    scraper = WebScraper(url)
    scraper.navigate_to_url()
    page_source = scraper.get_page_source()

    extractor = ProductExtractor(page_source)
    product_name = extractor.extract_product_name()
    product_price = extractor.extract_product_price()
    product_promo_price = extractor.extract_product_promo_price()

    print(f"Product Name: {product_name}")
    print(f"Product Price: {product_price}")
    print(f"Product Promo price: {product_promo_price}")

    scraper.close_driver()


if __name__ == "__main__":
    main()