import pytest
from playwright.async_api import Page
from pages.main_page import MainBankPage


@pytest.mark.asyncio_cooperative
@pytest.fixture()
async def start_page(page: Page):
    main_page = MainBankPage(page)
    await main_page.go_to_page(main_page.url)
    return main_page


