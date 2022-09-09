from playwright.sync_api import Page
import pytest
from pages.main_page import MainBankPage
from pages.credit_cards_page import CreditCardsPage


@pytest.fixture()
def start_page(page: Page):
    main_page = MainBankPage(page)
    main_page.go_to_page(main_page.url)
    return main_page


@pytest.fixture()
def cards_page(page: Page):
    cr_cards_page = CreditCardsPage(page)
    return cr_cards_page


