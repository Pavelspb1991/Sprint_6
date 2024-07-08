from pages.main_page import MainPage
from conftest import driver
import allure
from urls import Urls


class TestLogoRedirect:
    @allure.title("Проверка перехода на главную страницу самоката при клике на лого")
    def test_logo_redirect(self, driver):  # Добавить "self" в аргументы
        main_page = MainPage(driver)
        main_page.visit()
        with allure.step("Ожидание загрузки страницы"):
            assert main_page.header_order_button.wait_for_element_visible()
        with allure.step("Переход на страницу заказа"):
            main_page.header_order_button.click()
        with allure.step("Ожидание загрузки главной страницы"):
            assert main_page.header_order_button.wait_for_element_visible()
        with allure.step("Проверка перехода по клику на лого"):
            main_page.header_logo_button.click()
        with allure.step("Ожидание загрузки страницы"):
            assert main_page.main_page_header.wait_for_element_visible()
        with allure.step("Проверка соответствия адреса страницы"):
            assert main_page.get_url() == Urls.BASE_URL

    @allure.title("Проверка перехода на страницу Дзена при клике на логотип Яндекс")
    def test_yandex_logo_redirect(self, driver):  # Добавить "self" в аргументы
        main_page = MainPage(driver)
        main_page.visit()
        with allure.step("ожидание загрузки страницы"):
            assert main_page.header_yandex_button.wait_for_element_visible()
        with allure.step("Клик на логотип яндекса"):
            main_page.header_yandex_button.click()
        with allure.step("Переключение вкладки и ожидание загрузки страницы"):
            main_page.switch_to_new_window()
            main_page.yandex_dzen_logo.wait_for_element_visible()
        with allure.step("Проверка адреса страницы Яндекс Дзена"):
            assert main_page.get_url() == Urls.YANDEX_DZEN_URL
