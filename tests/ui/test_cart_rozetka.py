import pytest
from modules.ui.page_objects.home_page import HomePage
from modules.ui.page_objects.cart_page import CartPage

@pytest.mark.usefixtures("driver", "base_url")
class TestCart:

    def test_add_item_to_cart(self, driver, base_url):
        # 1. Відкрити головну сторінку
        home_page = HomePage()
        home_page.driver.get(base_url)

        # 2. Виконати пошук товару
        home_page.search_for_item("Телефон")

        # 3. Додати товар до кошика
        cart_page = CartPage()
        cart_page.driver = home_page.driver  # Спільний драйвер
        cart_page.add_item_to_cart()

        # 4. Перейти до кошика
        cart_page.go_to_cart()

        # 5. Перевірити наявність товару у кошику
        assert cart_page.is_item_in_cart("Телефон"), "Товар не додано до кошика!"