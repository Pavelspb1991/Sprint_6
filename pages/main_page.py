from pages.base_page import BasePage
from components.components import WebElement
from urls import Urls


class MainPage(BasePage):
    def __init__(self, driver):
        self.base_url = Urls.BASE_URL
        super().__init__(driver, self.base_url)
        self.main_page_header = WebElement(driver, '//div[@class="Home_Header__iJKdX"]', 'xpath')
        self.question_list = WebElement(driver, '//div[contains(@class, "Home_FAQ")]', 'xpath')
        self.order_button = WebElement(driver, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]', 'xpath')
        self.header_order_button = WebElement(driver, '//button[@class = "Button_Button__ra12g"]', 'xpath')
        self.header_logo_button = WebElement(driver, '//a[@class="Header_LogoScooter__3lsAR"]', 'xpath')
        self.header_yandex_button = WebElement(driver, '//a[@class="Header_LogoYandex__3TSOI"]', 'xpath')
        self.yandex_dzen_logo = WebElement(driver, '//a[@aria-label="Логотип Бренда"]', 'xpath')
        self.cookie_button = WebElement(driver, '//button[@class="App_CookieButton__3cvqF"]', 'xpath')
        self.questions_items = {
            1: WebElement(driver, '//div[@id="accordion__heading-0"]', 'xpath'),
            2: WebElement(driver, '//div[@id="accordion__heading-1"]', 'xpath'),
            3: WebElement(driver, '//div[@id="accordion__heading-2"]', 'xpath'),
            4: WebElement(driver, '//div[@id="accordion__heading-3"]', 'xpath'),
            5: WebElement(driver, '//div[@id="accordion__heading-4"]', 'xpath'),
            6: WebElement(driver, '//div[@id="accordion__heading-5"]', 'xpath'),
            7: WebElement(driver, '//div[@id="accordion__heading-6"]', 'xpath'),
            8: WebElement(driver, '//div[@id="accordion__heading-7"]', 'xpath')
        }
        self.answers_items = {
            1: WebElement(driver, '//div[@id="accordion__panel-0"]', 'xpath'),
            2: WebElement(driver, '//div[@id="accordion__panel-1"]', 'xpath'),
            3: WebElement(driver, '//div[@id="accordion__panel-2"]', 'xpath'),
            4: WebElement(driver, '//div[@id="accordion__panel-3"]', 'xpath'),
            5: WebElement(driver, '//div[@id="accordion__panel-4"]', 'xpath'),
            6: WebElement(driver, '//div[@id="accordion__panel-5"]', 'xpath'),
            7: WebElement(driver, '//div[@id="accordion__panel-6"]', 'xpath'),
            8: WebElement(driver, '//div[@id="accordion__panel-7"]', 'xpath')
        }

    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

