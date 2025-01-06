from selenium.webdriver.common.by import By
from modules.ui.page_objects.base_page import BasePage

class HomePage(BasePage):
    SEARCH_INPUT = (By.NAME, "search")
    SEARCH_BUTTON = (By.CLASS_NAME, "button_color_green")

    def search_for_item(self, item_name):
        # пошук товару
        search_input = self.driver.find_element(*self.SEARCH_INPUT)
        search_input.clear()
        search_input.send_keys(item_name)

        search_button = self.driver.find_element(*self.SEARCH_BUTTON)
        search_button.click()