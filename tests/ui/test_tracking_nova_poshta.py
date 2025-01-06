def test_valid_tracking_number(driver, base_url):
    """
    Тестує пошук з валідним номером накладної.
    """
    from modules.ui.page_objects.tracking_page import TrackingPage

    tracking_page = TrackingPage()
    tracking_page.open(base_url)
    tracking_page.enter_tracking_number("12345678901234")  # Замінити на реальний номер
    tracking_page.click_search()
    result_message = tracking_page.get_result_message()
    assert "Інформація про відправлення" in result_message, "Валідний номер не повертає правильний результат"


def test_invalid_tracking_number(driver, base_url):
    """
    Тестує пошук з невалідним номером накладної.
    """
    from modules.ui.page_objects.tracking_page import TrackingPage

    tracking_page = TrackingPage()
    tracking_page.open(base_url)
    tracking_page.enter_tracking_number("00000000000000")  # Некоректний номер
    tracking_page.click_search()
    result_message = tracking_page.get_result_message()
    assert "Накладна не знайдена" in result_message, "Некоректний номер повертає неправильний результат"


def test_empty_tracking_number(driver, base_url):
    """
    Тестує пошук з порожнім полем для введення номера.
    """
    from modules.ui.page_objects.tracking_page import TrackingPage

    tracking_page = TrackingPage()
    tracking_page.open(base_url)
    tracking_page.click_search()
    error_message = tracking_page.get_error_message()
    assert "Введіть номер накладної" in error_message, "Повідомлення про порожнє поле не з'являється"