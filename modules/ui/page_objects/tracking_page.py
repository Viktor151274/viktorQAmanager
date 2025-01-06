from selenium.webdriver.common.by import By
from modules.ui.page_objects.base_page import BasePage


class TrackingPage(BasePage):
    # Локатори
    TRACKING_INPUT = (By.ID, "cargo_number")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "input")
    RESULT_MESSAGE = (By.CLASS_NAME, "input")
    ERROR_MESSAGE = (By.CLASS_NAME, "error-message-class")

    def open(self, base_url):
        """Відкриває сторінку Нової Пошти."""
        self.open_url(base_url)

    def enter_tracking_number(self, number):
        """Вводить номер накладної."""
        tracking_input = self.wait_for_element(self.TRACKING_INPUT)
        tracking_input.clear()
        tracking_input.send_keys(number)

    def click_search(self):
        """Натискає кнопку пошуку."""
        search_button = self.wait_for_element(self.SEARCH_BUTTON)
        search_button.click()

    def get_result_message(self):
        """Повертає текст результату відстеження."""
        result_message = self.wait_for_element(self.RESULT_MESSAGE)
        return result_message.text

    def get_error_message(self):
        """Повертає текст повідомлення про помилку."""
        error_message = self.wait_for_element(self.ERROR_MESSAGE)
        return error_message.text