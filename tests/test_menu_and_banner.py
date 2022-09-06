import pytest
import logging
from time import sleep


logger = logging.getLogger('tests')

@pytest.mark.asyncio_cooperative
class TestMenuAndBanner:
    @pytest.mark.asyncio_cooperative
    async def test_menu_and_banner(self, start_page):
        await start_page.pick_menu_block(1)
        sleep(5)
