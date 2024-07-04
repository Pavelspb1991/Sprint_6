from conftest import driver
import pytest
import allure
from pages.order_page import OrderPage
from pages.main_page import MainPage
from parametrize_values import ParametrizeValues


@allure.title("Проверка позитивного сценария оформления заказа")
@allure.description("Флоу позитивного сценария с двумя наборами данных. "
                    "Две точки входа в сценарий: кнопка «Заказать» вверху страницы и внизу.")
@pytest.mark.parametrize('button_name, user_values', [
    ('order_button', ParametrizeValues.values_order_1),
    ('header_order_button', ParametrizeValues.values_order_2)
])
def test_order(driver, button_name, user_values):
    main_page = MainPage(driver)
    main_page.visit()
    with allure.step("Ожидание загрузки кнопки куки и нажатие на нее"):
        main_page.cookie_button.wait_for_element_visible()
        main_page.cookie_button.click()
    with allure.step("Получаем атрибут(селектор)  button_name из класса MainPage"):
        button = getattr(main_page, button_name)
        button.click()
    order_page = OrderPage(driver)
    with allure.step("Ожидание загрузки формы Для кого самокат"):
        order_page.input_name.wait_for_element_visible()
    with allure.step("Заполняем форму Для кого самокат данными из user_values"):
        order_page.input_order_form_1(user_values)
    with allure.step("Ожидание загрузки формы Про аренду"):
        order_page.input_date.wait_for_element_visible()
    with allure.step("Заполняем форму Про аренду данными из user_values"):
        order_page.input_order_form_2(user_values)
    with allure.step('Ожидание загрузки сообщения об успешном оформлении'):
        order_page.success_message.wait_for_element_visible()
    with allure.step('Проверка сообщения об успешном оформлении'):
        message = order_page.success_message.get_text()
        assert 'Заказ оформлен' in message


