

class TestMenuAndBanner:
    def test_menu_and_banner(self, start_page):
        assert start_page.animation_block.get_animation_turnover()
        start_page.pick_middle_menu_block()
        assert start_page.animation_block.get_animation_status(False)
        assert start_page.banner_block.get_banner_status()
        start_page.reload()
        assert start_page.animation_block.get_animation_status(True)
        assert start_page.animation_block.get_animation_block_text()
        start_page.close_page()

    def test_banners_time(self, start_page):
        # assert start_page.animation_block.get_animation_visible_time()
        start_page.pick_top_menu_block('Малому бизнесу и ИП')

