from components.components import WebElement
from pages.base_page import BasePage


class OrderPage(BasePage):
    def __init__(self, driver):
        self.base_url = "https://qa-scooter.praktikum-services.ru/"
        super().__init__(driver, self.base_url)
        # Селекторы для формы "Для кого самокат"
        self.input_name = WebElement(driver, "//input[@placeholder= '* Имя']", 'xpath')
        self.input_surname = WebElement(driver, "//input[@placeholder= '* Фамилия']", 'xpath')
        self.input_address = WebElement(driver, "//input[@placeholder='* Адрес: куда привезти заказ']", 'xpath')
        self.input_metro = WebElement(driver, "//input[@placeholder= '* Станция метро']", 'xpath')
        self.select_metro = WebElement(driver,"//li[@class='select-search__row']", 'xpath')
        self.input_phone = WebElement(driver, "//input[@placeholder= '* Телефон: на него позвонит курьер']", 'xpath')
        self.next_button = WebElement(driver, "//button[text()='Далее']", 'xpath')

        # Селекторы для формы "Про аренду"
        self.input_date = WebElement(driver, "//input[@placeholder='* Когда привезти самокат']", 'xpath')
        self.calendar = WebElement(driver, "//div[contains(text(), '11')]", 'xpath')
        self.input_days_rent = WebElement(driver, "//div[contains(text(), 'Срок аренды')]", 'xpath')
        self.input_num_days_rent = WebElement(driver, "//div[@class = 'Dropdown-menu']/div[text() ='трое суток']", 'xpath')
        self.grey_scooter_checkbox = WebElement(driver, "//input[@id='grey']", 'xpath')
        self.input_comment = WebElement(driver, "//input[@placeholder= 'Комментарий для курьера']", 'xpath')
        self.order_button_form_2 = WebElement(driver, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']", 'xpath')
        self.confirm_button = WebElement(driver, "//button[text()='Да']", 'xpath')
        self.success_message = WebElement(driver, "//div[contains(text(), 'Заказ оформлен')]", 'xpath')

    def input_order_form_1(self, user_values):
        self.input_name.send_keys(user_values[0])
        self.input_surname.send_keys(user_values[1])
        self.input_address.send_keys(user_values[2])
        self.input_metro.send_keys(user_values[3])
        self.select_metro.click()
        self.input_phone.send_keys(user_values[4])
        self.next_button.click()

    def input_order_form_2(self, user_values):
        self.input_date.click()
        self.calendar.click()
        self.input_days_rent.click()
        self.input_num_days_rent.click()
        self.grey_scooter_checkbox.click()
        self.input_comment.send_keys(user_values[5])
        self.order_button_form_2.click()
        self.confirm_button.wait_for_element_visible()
        self.confirm_button.click()








