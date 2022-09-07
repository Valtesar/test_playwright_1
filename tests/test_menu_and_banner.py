import pytest
import logging
from time import sleep
from random import randrange

logger = logging.getLogger('tests')


class TestMenuAndBanner:
    def test_menu_and_banner(self, start_page):
        sleep(5)
        assert start_page.animation_block.get_animation_turnover()
        start_page.pick_menu_block(randrange(4))
        assert not start_page.animation_block.get_animation_status()
        sleep(2)

