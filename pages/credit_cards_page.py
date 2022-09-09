from abc import ABC
from pages.web_page import WebPage
from pages.main_page import MainBankPage
from playwright.sync_api import Page, expect
from hooks.generator_random_data import GenerateRandomData
from time import sleep


class CreditCardsPage(MainBankPage, WebPage, ABC):
    def __init__(self, page: Page):
        super().__init__(page)
        self.url = 'https://alfabank.ru/get-money/credit-cards/'

    def get_100_days_card(self):
        self.page.locator('//button[@data-test-id="button" and @text = "Получить карту"]').click()

        if "#anketa" not in self.page.url:
            raise Exception('Button of get credit card was not clicked!', self.page.url)
        self.page.locator('//input[@data-test-id= "input" and @name="fullName"]').scroll_into_view_if_needed()
        self.page.locator('//input[@data-test-id= "input" and @name="fullName"]').type("Hello world")
        sleep(4)



