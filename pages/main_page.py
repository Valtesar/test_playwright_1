from pages.web_page import WebPage
from playwright.async_api import Page


class MainBankPage(WebPage):

    def __init__(self, url: str, page: Page):
        super().__init__(page)
        self.url = url

    def change_menu_block(self):
        pass

    def get_block_status(self):
        pass

    def get_banner_status(self):
        pass
