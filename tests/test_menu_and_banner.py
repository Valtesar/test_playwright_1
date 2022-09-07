import pytest
import logging
from time import sleep
from random import randrange

logger = logging.getLogger('tests')


class TestMenuAndBanner:
    def test_menu_and_banner(self, start_page):
        sleep(5)
        assert start_page.animation_block.get_animation_turnover()
        start_page.pick_menu_block()
        assert not start_page.animation_block.get_animation_status()
        sleep(2)
        assert start_page.banner_block.get_banner_status()
        sleep(2)
        start_page.reload()
        sleep(3)
        assert start_page.animation_block.get_animation_status()
        sleep(2)
        assert start_page.animation_block.get_animation_block_text()
        sleep(2)

