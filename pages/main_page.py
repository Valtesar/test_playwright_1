from abc import ABC
from pages.web_page import WebPage
from playwright.sync_api import Page
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

    def __init__(self, page: Page):
        super().__init__(page)
        self.url = 'https://alfabank.ru/'
        self.animation_block = AnimationBlock(page)
        self.banner_block = BannerBlock(page)

    def pick_menu_block(self):
        self.page.locator(f'//*[contains(@class, "a3sPfj") and @tabindex = {current_index}]').click()

    def get_block_info(self):
        pass

    def get_banner_info(self):
        pass


class AnimationBlock:
    def __init__(self, page: Page):
        self.page = page
        self._animation_block_visibility = None
        self._animation_block_turnover = None
        self._animation_block_header_text = None
        self._animation_block_body_text = None

    def get_animation_status(self):
        self._animation_block_visibility = self.page.locator('//div[@class= "h3L1Y9"]').is_visible()
        return self._animation_block_visibility

    def get_animation_turnover(self):
        attribute_before = self.page.locator('//div[@class= "e3L1Y9"]').get_attribute('style')
        with self.page.expect_request('https://mc.yandex.ru/watch/**'):
            pass
        attribute_after = self.page.locator('//div[@class= "e3L1Y9"]').get_attribute('style')
        return attribute_before != attribute_after

    def get_block_text(self):
        pass


class BannerBlock:
    def __init__(self, page: Page):
        self.page = page
        self._banner_block_visibility = None
        self._banner_block_turnover = None
        self._banner_block_header_text = None
        self._banner_block_body_text = None

    def get_banner_status(self):
        attribute_hidden = self.page.locator(f'(//div[contains(@class, "c2XhKl b2XhKl")][{current_index + 1}])')\
            .get_attribute('aria-hidden')

        if attribute_hidden == 'false':
            self._banner_block_visibility = True
            return self._banner_block_visibility

        elif attribute_hidden == 'true':
            self._banner_block_visibility = False
            return False
        else:
            raise Exception('Something wrong with locator or object not located on page!')



