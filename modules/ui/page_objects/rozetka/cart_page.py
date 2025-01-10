from selenium.webdriver.common.by import By
from modules.ui.page_objects.base_page import BasePage


class CartPage(BasePage):

    CART_ITEM = (By.CLASS_NAME, "cart-product__title")

    def is_product_in_cart(self, product_name):
        cart_items = self.driver.find_elements(*self.CART_ITEM)
        return any(product_name.lower() in item.text.lower() for item in cart_items)