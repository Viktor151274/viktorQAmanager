from selenium.webdriver.common.by import By
from modules.ui.page_objects.base_page import BasePage

class ResultPage(BasePage):
    def __init__(self):
        super().__init__()

    SUCCESS_MESSAGE = (By.CLASS_NAME, "header__status-text")
    ERROR_MESSAGE = (By.CLASS_NAME, "tracking__error-text")

    def is_success_message_displayed(self):
        return len(self.driver.find_elements(*self.SUCCESS_MESSAGE)) > 0

    def is_error_message_displayed(self):
        return len(self.driver.find_elements(*self.ERROR_MESSAGE)) > 0