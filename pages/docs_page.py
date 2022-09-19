from playwright.sync_api import Page, expect


class DocsPage:
    def __init__(self, page: Page):
        self.page = page


