import pytest
from modules.ui.page_objects.rozetka.main_page import MainPage
from modules.ui.page_objects.rozetka.product_page import ProductPage
from modules.ui.page_objects.rozetka.cart_page import CartPage

@pytest.mark.ui
@pytest.mark.rozetka
def test_add_product_to_cart(driver):
    # Передаємо driver в конструктори сторінок
    main_page = MainPage(driver)
    product_page = ProductPage(driver)
    cart_page = CartPage(driver)

    # Step 1: Open Rozetka main page
    main_page.open_url("https://rozetka.com.ua/")

    # Step 2: Search for "ноутбук"
    main_page.search_product("ноутбук")

    # Step 3: Add the first product to the cart
    product_page.add_to_cart()

    # Step 4: Go to the cart page
    driver.get("https://rozetka.com.ua/cart/")

    # Step 5: Verify the product is in the cart
    assert cart_page.is_product_in_cart("ноутбук"), "Product not found in the cart!"