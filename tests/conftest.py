from playwright.sync_api import Page
import pytest
from pages.main_page import MainBankPage


@pytest.fixture()
def start_page(page: Page):
    main_page = MainBankPage(page)
    main_page.go_to_page(main_page.url)
    return main_page


