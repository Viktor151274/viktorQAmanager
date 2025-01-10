from selenium.webdriver.common.by import By
from modules.ui.page_objects.base_page import BasePage

class ProductPage(BasePage):

    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "buy-button")  # Update selector as per Rozetka's DOM structure
    
    def add_to_cart(self):
        add_button = self.driver.find_element(*self.ADD_TO_CART_BUTTON)
        add_button.click()