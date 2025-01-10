
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from modules.ui.page_objects.base_page import BasePage


class MainPage(BasePage):

    SEARCH_BAR = (By.NAME, "search")

    def search_product(self, product_name):
        search_bar = self.driver.find_element(*self.SEARCH_BAR)
        search_bar.send_keys(product_name + Keys.RETURN)