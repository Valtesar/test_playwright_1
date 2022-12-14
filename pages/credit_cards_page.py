from abc import ABC
from pages.web_page import WebPage
from pages.main_page import MainBankPage
from playwright.sync_api import Page, expect
from hooks.generator_random_data import GenerateRandomData as GRD
from time import sleep


class ApplicationFormCard:
    """Класс реализации объекта анкеты заявки на кредитную карту."""

    EN = "qwertyuiop[]asdfghjkl;'zxcvbnm,."
    RUS = "йцукенгшщзхъфывапролджэячсмитьбю"

    def __init__(self, page: Page):
        self.page = page
        self.fio = GRD.get_random_fio()
        self.mobile = GRD.get_random_mobile()
        self.email = GRD.get_random_email()
        self.gender = GRD.get_random_gender()
        self.passport_series = GRD.get_random_passport_series()
        self.passport_number = GRD.get_random_passport_number()

    def fill_in_app_form(self):
        """Метод класса для заполнения полей анкеты случайными данными сгенерированными в инициализаторе класса"""

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

    def fill_in_app_form_passport(self):
        """Метод заполнения полей анкеты с паспортными данными сгенерированными в инициализаторе класса"""

        self.page.locator('//input[@class ="input__control" and @name="passportSeries"]').click()
        self.page.keyboard.insert_text(self.passport_series)

        self.page.locator('//input[@class ="input__control" and @name="passportNumber"]').click()
        self.page.keyboard.insert_text(self.passport_number)

    def check_email_validation(self):
        """"Метож проверки поля email на валидацию в виде ввода русских букв и сраненнием текста в текстбоксе
            с корректным преводом на английские символы"""

        self.page.locator('//input[@data-test-id= "email-input"]').click()
        rus_word = 'майл'
        eng_transform = 'vfqk'
        self.page.keyboard.insert_text(rus_word)
        if self.page.locator(f'//input[@data-test-id= "email-input" and @value = "{eng_transform}"]').is_visible():
            return True
        else:
            return False

    def check_appeal_by_name(self):
        """Метод проверки поп-апа с обращением к клиенту по имени отчеству на наличие корректного обращения"""

        message = ''.join(self.page.locator('//p[contains(@class, "paragraph continue")]').all_text_contents())
        fio_ru = self.fio.translate(str.maketrans(ApplicationFormCard.EN, ApplicationFormCard.RUS))
        name_patronymic_ru = ' '.join(fio_ru.title().split()[1:])
        if name_patronymic_ru in message:
            return True
        else:
            return False


class MainCreditCardsPage(MainBankPage, WebPage, ABC):
    """Класс реализации объекта страницы кредитных карт сайта"""

    def __init__(self, page: Page):
        super().__init__(page)
        self.url = 'https://alfabank.ru/get-money/credit-cards/'
        self.app_form = ApplicationFormCard(page)

    def get_email_validation(self):
        """Метод нажимает на кнопку <Получить карту> и проверяет, что url изменился"""

        self.page.locator('//button[@data-test-id="button" and @text = "Получить карту"]').click()
        if "#anketa" not in self.page.url:
            raise Exception('Button of get credit card was not clicked!', self.page.url)
        return self.app_form.check_email_validation()

    def get_100_days_card(self):
        """Метож вызывает функцию заполнения формы получения карты и нажимает на кнопку продолжить."""

        self.app_form.fill_in_app_form()
        self.page.locator('//button[@data-test-id="button" and @type="submit"]').click()

    def get_header_of_the_tab(self):
        """Метод открывает новую вкладку и собирает названия заголовков предыдущей вкладки с интервалом в 0.5 секунд,
            формирует спиисок из заголовков. Проверяет, что бы все заголовки в списке были одинаковые."""

        new_page = self.page.context.new_page()
        new_page.goto(self.url, wait_until="commit")
        titles = []
        for i in range(5):
            titles.append(self.page.title())
            sleep(0.5)

        for title in titles:
            if titles[0] != title:
                return False
            else:
                new_page.close()
                return True

    def set_passport_values(self):
        """Метод вызывает функцию заполнения паспортным данных, затем обновляет страницу и проверяет,
           что поп-ап отображается"""

        self.app_form.fill_in_app_form_passport()
        self.page.reload()
        return self.page.locator('//div[contains(@class, "modal continue")]').is_visible()

    def get_popup_info(self):
        """Метод вызывает функцию проверки обращения по имени отчеству в поп-апе"""

        return self.app_form.check_appeal_by_name()

    def get_fields_from_page(self):
        """Метож нажимает на кнопку заполнения анкеты с начала, и проверяет, что бы на странице отсутствовали поля
           серии и номера паспорта"""

        self.page.locator('(//span[@class="link__text"])[3]').click()
        expect(self.page.locator('//input[@class="input__control" and @name="passportSeries"]')).not_to_be_visible()
        expect(self.page.locator('//input[@class="input__control" and @name="passportNumber"]')).not_to_be_visible()
        self.page.close()

        return True


