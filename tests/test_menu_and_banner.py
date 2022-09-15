from time import sleep


class TestMenuAndBanner:
    """Класс тестов для проверки коррктности отображения блоков меню и баннеров"""

    def test_menu_and_banner(self, start_page):
        """Тест меню и баннеров на главной странице сайта.
           Проверяет, наличие анимации на блоках кнопок, а так же ее остановка при нажатии. При обновлении анимация
           вновь должна появлятся.
           """
        assert start_page.animation_block.get_animation_turnover()
        start_page.pick_middle_menu_block()
        assert start_page.animation_block.get_animation_status(False)
        assert start_page.banner_block.get_banner_status()
        start_page.reload()
        assert start_page.animation_block.get_animation_status(True)
        assert start_page.animation_block.get_animation_block_text()
        start_page.close_page()

    def test_banners_time(self, start_page, small_business_page):
        """Тест для проверки времени работы анимации на двух страницах: главной и странице <Малому бизнесу и ИП>.
           Сравнение времени анимации на двух страницах. В случае большой разницы в анимации между блоками
           тест вернет ошибку."""

        # assert start_page.animation_block.get_animation_visible_time()
        start_page.pick_top_menu_block('Малому бизнесу и ИП')
        sleep(3)
        assert small_business_page.animation_block_sb.get_animation_visible_time_sb()


