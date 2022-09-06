from pages.web_page import WebPage
from playwright.async_api import Page
import pytest


@pytest.mark.asyncio_cooperative
class MainBankPage(WebPage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.url = 'https://alfabank.ru/'

    async def pick_menu_block(self, index: int):
        await self.page.locator(f'//*[contains(@class, "a3sPfj") and @tabindex = {index}]').click()

    async def get_block_status(self):
        pass

    async def get_banner_status(self):
        pass
