import pytest
from modules.ui.page_objects.main_page import MainPage
from modules.ui.page_objects.result_page import ResultPage


@pytest.mark.ui
def test_search_valid_tracking_number(base_page):
    main_page = MainPage()
    result_page = ResultPage()

    # Step 1: Open tracking page
    main_page.open_url("https://novaposhta.ua")

    # Step 2: Search for a valid tracking number
    main_page.search_tracking_number("20451061760965")

    # Step 3: Assert success message is displayed
    assert result_page.is_success_message_displayed(), "Valid tracking number did not show success message!"

def test_search_invalid_tracking_number(base_page):
    main_page = MainPage()
    result_page = ResultPage()

    # Step 1: Open tracking page
    main_page.open_url("https://novaposhta.ua")

    # Step 2: Search for an invalid tracking number
    main_page.search_tracking_number("invalid123456")

    # Step 3: Assert error message is displayed
    assert result_page.is_error_message_displayed(), "Invalid tracking number did not show error message!"