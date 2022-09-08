import pytest
from time import sleep


class TestMenuAndBanner:
    def test_menu_and_banner(self, start_page):
        assert start_page.animation_block.get_animation_turnover()
        start_page.pick_menu_block()
        assert not start_page.animation_block.get_animation_status()
        assert start_page.banner_block.get_banner_status()
        start_page.reload()
        sleep(3)
        assert start_page.animation_block.get_animation_status()
        assert start_page.animation_block.get_animation_block_text()


