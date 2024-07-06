from pages.main_page import MainPage
from conftest import driver
import pytest
import allure
from parametrize_values import ParametrizeValues


class TestFaqDropdown:
    @allure.title('Проверка раздела "Вопросы о важном"')
    @allure.description("Проверка появления корректного текста при нажатии на нужный пункт раздела")
    @pytest.mark.parametrize('question_number, values', ParametrizeValues.values)
    def test_faq_dropdown_displays_correct_answer(self, driver, question_number, values):
        main_page = MainPage(driver)
        main_page.visit()
        with allure.step("ожидание загрузки страницы"):
            main_page.main_page_header.wait_for_element_visible()
        with allure.step("Нажатие на кнопку куки"):
            main_page.cookie_button.wait_for_element_visible()
            main_page.cookie_button.click()
        with allure.step("Прокрутка страницы до Вопросы и ответы"):
            main_page.question_list.wait_for_element_visible()
            main_page.question_list.scroll_to_element()
            # Тут мы получаем данные из словаря questions_items, в котором хранится xpath нужного нам пункта
            # И кликаем на него
        with allure.step(f"Нажатие на пункт {question_number}"):
            question = main_page.questions_items[question_number]
            question.wait_for_element_clickable()
            question.click_force()
            # В этом шаге идет проверка текста, данные для селекторов взяты из словаря answers_items
        with allure.step(f"Проверка текста для пункта {question_number}"):
            answer = main_page.answers_items[question_number]
            answer.wait_for_element_visible()
            actual_text = answer.find_element().text
            assert actual_text == values
