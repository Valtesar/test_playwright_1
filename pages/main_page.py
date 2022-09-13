from abc import ABC
from pages.web_page import WebPage
from playwright.sync_api import Page, expect
from random import randrange
import pytest
from time import sleep

index = randrange(4)
current_index = index


class RandomIndexGenerator:
    def __init__(self):
        self.index = self.generate_random_index(4)

    @staticmethod
    def generate_random_index(index_range):
        index = randrange(index_range)
        return index


class MainBankPage(WebPage, ABC):
    """Класс для работы с главной страницей банка и его экземплярами"""

    def __init__(self, page: Page):
        super().__init__(page)
        self.url = 'https://alfabank.ru/'
        self.animation_block = AnimationBlock(page)
        self.banner_block = BannerBlock(page)

    def pick_middle_menu_block(self):
        """Метод нажимает на случайную кнопку меню"""

        self.page.locator(f'//*[contains(@class, "a3sPfj") and @tabindex = {current_index}]').click()

    def pick_upper_menu_block(self, first_button=None, second_button=None):
        """Метод наводит на нужную кнопку меню вверху экрана, и затем нажимает нужную кнопку в выпадающем меню"""

        if (first_button and second_button) is not None:
            pos = self.page.locator(f'//a[@class="a2_r6X g2_r6X e2_r6X d1B_-k" and @title = "{first_button}"]')\
                .bounding_box()
            self.page.mouse.move(pos['x'], pos['y'])
            self.page.locator(f'//a[@class="a2_r6X g2_r6X e2_r6X d1B_-k" and @title= "{second_button}"]').click()
        else:
            raise Exception('Missing name of the button!')


class AnimationBlock:
    """Класс для работы с экземплярами раздела блока анимации (блок кнопок)"""

    def __init__(self, page: Page):
        self.page = page
        self._animation_block_visibility = None
        self._animation_block_turnover = None
        self._animation_block_header_text = None
        self._animation_block_body_text = None

    def get_animation_status(self, visible):
        """Метод проверяет, что анимация заполнения шкалы в карусели видна на странице"""

        locator = self.page.locator('//div[@class= "h3L1Y9"]')

        if visible:
            expect(locator).to_be_visible(timeout=3000)
            self._animation_block_visibility = True

            return self._animation_block_visibility

        if not visible:
            expect(locator).not_to_be_visible(timeout=3000)
            self._animation_block_visibility = True

            return self._animation_block_visibility
        else:
            self._animation_block_visibility = False

            return self._animation_block_visibility

    def get_animation_turnover(self):
        """Метод проверяет, что  в анимации при заполнении шкалы происходит переключение на другую кнопку.
           Возвращает --> True если кнопка переключилась, --> False если кнопка осталася прежней"""

        attribute_before = self.page.locator('//div[@class= "e3L1Y9"]').get_attribute('style')

        with self.page.expect_request('https://mc.yandex.ru/watch/**'):
            pass

        attribute_after = self.page.locator('//div[@class= "e3L1Y9"]').get_attribute('style')

        return attribute_before != attribute_after

    def get_animation_block_text(self):
        """Метод получает текст из кнопок анимации, проверяет, что бы кол-во заголовков кнопок соответствовало
           кол-ву тел кнопок. В случае соответствия --> возвращает True, иначе --> возвращает False.
           Создает словарь где ключ - это текст заголовка кнопки, а значение - это текст тела кнопки."""

        self._animation_block_header_text = self.page.locator('//p[contains(@class, "a1zii3 h1zii3")]')\
            .all_text_contents()
        self._animation_block_body_text = self.page.locator('//p[contains(@class, "a1zii3 gG2mwi")]')\
            .all_text_contents()

        if len(self._animation_block_header_text) == len(self._animation_block_body_text):

            self._animation_block_header_text = [w.replace(u'\xa0', u' ') for w in self._animation_block_header_text]
            self._animation_block_body_text = [w.replace(u'\xa0', u' ') for w in self._animation_block_body_text]

            print(dict(zip(self._animation_block_header_text, self._animation_block_body_text)))
            return True
        else:
            return False


class BannerBlock:
    """Класс для работы с экземплярами раздела баннеров"""

    def __init__(self, page: Page):
        self.page = page
        self._banner_block_visibility = None
        self._banner_block_turnover = None
        self._banner_block_header_text = None
        self._banner_block_body_text = None

    def get_banner_status(self):
        """Метод проверяет, что текущий баннер связанный с индексом кнопки отображается корректно"""

        attribute_hidden = self.page.locator(f'(//div[contains(@class, "c2XhKl b2XhKl")][{current_index + 1}])')\
            .get_attribute('aria-hidden')

        if attribute_hidden == 'false':
            self._banner_block_visibility = True
            return self._banner_block_visibility

        elif attribute_hidden == 'true':
            self._banner_block_visibility = False
            return self._banner_block_visibility

        else:
            raise Exception('Something wrong with locator or object not located on page!')



