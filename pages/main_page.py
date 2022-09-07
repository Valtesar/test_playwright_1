from abc import ABC
from pages.web_page import WebPage
from playwright.sync_api import Page
import pytest
from time import sleep


class MainBankPage(WebPage, ABC):

    def __init__(self, page: Page):
        super().__init__(page)
        self.url = 'https://alfabank.ru/'
        self.animation_block = AnimationBlock(page)

    def pick_menu_block(self, index: int):
        self.page.locator(f'//*[contains(@class, "a3sPfj") and @tabindex = {index}]').click()

    def get_block_info(self):
        pass

    def get_banner_info(self):
        pass


class AnimationBlock:
    def __init__(self, page: Page):
        self.page = page
        self._block_visibility = None
        self._block_turnover = None
        self._block_header_text = None
        self._block_body_text = None

    def get_animation_status(self):
        self._block_visibility = self.page.locator('//div[@class= "h3L1Y9"]').is_visible()
        return self._block_visibility

    def get_animation_turnover(self):
        attribute_before = self.page.locator('//div[@class= "e3L1Y9"]').get_attribute('style')
        with self.page.expect_request('https://mc.yandex.ru/watch/**'):
            pass
        attribute_after = self.page.locator('//div[@class= "e3L1Y9"]').get_attribute('style')
        return attribute_before != attribute_after

    def get_block_text(self):
        pass


class BannerBlock(AnimationBlock):
    def get_block_text2(self):
        pass
