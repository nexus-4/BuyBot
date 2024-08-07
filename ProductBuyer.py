
class ProductBuyer:
    def __init__(self, driver):
        self.driver = driver

    def click_buy_now_button(self):
        buy_now_button = self.driver.find_element_by_xpath("//button[@class='buy-now']")
        buy_now_button.click()

    def complete_checkout(self):
        # Add checkout logic here
        pass