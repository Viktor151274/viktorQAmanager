from selenium.webdriver.common.by import By
from modules.ui.page_objects.base_page import BasePage

class CartPage(BasePage):
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "buy-button")
    CART_ICON = (By.CSS_SELECTOR, ".header-actions__button_type_cart")
    ITEM_IN_CART = (By.CLASS_NAME, "cart-product__title")

    def add_item_to_cart(self):
        #Додаємо товар у кошик
        add_button = self.driver.find_element(*self.ADD_TO_CART_BUTTON)
        add_button.click()

    def go_to_cart(self):
        #Переходить до кошика
        cart_icon = self.driver.find_element(*self.CART_ICON)
        cart_icon.click()

    def is_item_in_cart(self, item_name):
        #Перевірка наявність товару у кошику
        item = self.driver.find_element(*self.ITEM_IN_CART)
        return item_name in item.text