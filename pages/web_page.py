from playwright.async_api import Page
import pytest
from abc import abstractmethod


class WebPage(object):
    """Класс для работы с объектами веб страниц."""

    def __init__(self, page: Page, height: int = 1600, width: int = 900):
        self.page = page
        self.height = height
        self.width = width

    def reload(self):
        self.page.reload(wait_until='load')

    def close_page(self):
        self.page.close()

    def go_to_page(self, url):
        self.page.goto(url, wait_until='load')

    def change_tab(self, function):
        with self.page.context.expect_page(function) as new_page:
            function()
        new_page = new_page.value
        return new_page

    @abstractmethod
    def get_title_of_the_tab(self):
        pass
