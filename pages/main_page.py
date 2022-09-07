from abc import ABC

from pages.web_page import WebPage
from playwright.sync_api import Page
import pytest


class MainBankPage(WebPage, ABC):

    def __init__(self, page: Page):
        super().__init__(page)
        self.url = 'https://alfabank.ru/'

    def pick_menu_block(self, index: int):
        self.page.locator(f'//*[contains(@class, "a3sPfj") and @tabindex = {index}]').click()

    def animation_block(self):
        return self.page.locator('//div[@class= "h3L1Y9"]').is_visible()

    def get_block_info(self):
        pass

    def get_banner_info(self):
        pass


class AnimationBlock(MainBankPage):
    def __init__(self, page: Page):
        super().__init__(page)
        pass

