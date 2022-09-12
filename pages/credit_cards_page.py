from abc import ABC
from pages.web_page import WebPage
from pages.main_page import MainBankPage
from playwright.sync_api import Page, expect
from hooks.generator_random_data import GenerateRandomData
from time import sleep


class ApplicationFormCard:

    def __init__(self, page: Page):
        self.page = page
        self.fio = GenerateRandomData.get_random_fio()
        self.mobile = GenerateRandomData.get_random_mobile()
        self.email = GenerateRandomData.get_random_email()
        self.gender = GenerateRandomData.get_random_gender()

    def fill_in_app_form(self):
        self.page.locator('//input[@data-test-id= "input" and @name="fullName"]').scroll_into_view_if_needed()
        self.page.locator('//input[@data-test-id= "input" and @name="fullName"]').click()
        self.page.keyboard.insert_text(self.fio)

        self.page.locator('//input[@data-test-id= "phoneInput"]').click()
        self.page.locator('//input[@data-test-id= "phoneInput"]').scroll_into_view_if_needed()
        self.page.keyboard.insert_text(self.mobile)

        self.page.locator('//input[@data-test-id= "email-input"]').click()
        self.page.keyboard.insert_text(self.email)

        self.page.locator(f'//button[@data-test-id="sex-{self.gender}"]').click()

        self.page.locator('(//div[@class="e1jwl"])[2]').set_checked(checked=True)

    def check_email_validation(self):

        self.page.locator('//input[@data-test-id= "email-input"]').click()
        rus_word = 'майл'
        eng_transform = 'vfqk'
        self.page.keyboard.insert_text(rus_word)
        if self.page.locator(f'//input[@data-test-id= "email-input" and @value = "{eng_transform}"]').is_visible():
            return True
        else:
            return False


class CreditCardsPage(MainBankPage, WebPage, ABC):

    def __init__(self, page: Page):
        super().__init__(page)
        self.url = 'https://alfabank.ru/get-money/credit-cards/'
        self.app_form = ApplicationFormCard(page)

    def get_email_validation(self):

        self.page.locator('//button[@data-test-id="button" and @text = "Получить карту"]').click()
        if "#anketa" not in self.page.url:
            raise Exception('Button of get credit card was not clicked!', self.page.url)
        return self.app_form.check_email_validation()

    def get_100_days_card(self):

        self.app_form.fill_in_app_form()
        self.page.locator('//button[@data-test-id="button" and @type="submit"]').click()

    def get_header_of_the_tab(self):

        self.new_page = self.page.context.new_page()
        self.new_page.goto(self.url, wait_until="commit")
        titles = []
        for i in range(5):
            titles.append(self.page.title())
            sleep(0.5)

        for title in titles:
            if titles[0] != title:
                return False
            else:
                return True
        self.new_page.close()






