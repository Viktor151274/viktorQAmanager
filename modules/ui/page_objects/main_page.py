from selenium.webdriver.common.by import By
from modules.ui.page_objects.base_page import BasePage

class MainPage(BasePage):
    def __init__(self):
        super().__init__()
    
    SEARCH_BAR = (By.ID, "cargo_number")
    SEARCH_BUTTON = (By.CLASS_NAME, "submit")

    def search_tracking_number(self, tracking_number):
        search_bar = self.driver.find_element(*self.SEARCH_BAR)
        search_bar.clear()
        search_bar.send_keys(tracking_number)
        search_button = self.driver.find_element(*self.SEARCH_BUTTON)
        search_button.click()
