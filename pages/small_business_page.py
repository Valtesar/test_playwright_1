from pages.web_page import WebPage
from pages.main_page import MainBankPage
from playwright.sync_api import Page, expect


class MainSmallBusinessPage:

    def __init__(self, page: Page):
        self.page = page
        self.animation_block_sb = AnimationBlockSmallBusiness(page)



