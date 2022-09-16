from playwright.sync_api import Page, expect
import time
import numpy as np


class MainSmallBusinessPage:
    """Класс для работы со страницей <малого бизнеса и ИП> и его экземплярами"""

    def __init__(self, page: Page):
        """Инициализируем свойства объекта из полученного атрибута page, и объекта класса блока анимации"""

        self.page = page
        self.animation_block_sb = AnimationBlockSmallBusiness(page)


class AnimationBlockSmallBusiness:
    """Класс для работы с блоком анимации на странице <малого бизнеса и ИП> и его экземплярами"""
    animation_block_time = []

    def __init__(self, page: Page):
        self.page = page

    def get_animation_visible_time_sb(self):
        """Метод измеряет время отображения анимации на каждом блоке и в случае расхождения времени возвращает -> False,
           если время примерно равно, то возвращает -> True."""

        blocks = [1, 2, 3, 0]
        times = []

        if not self.page.locator('//div[contains(@class, "i3sPf")]').is_visible():
            return False

        for i in blocks:
            while not self.page.locator(f'//div[contains(@class, "i3sPf") and @tabindex="{i}"]').is_visible():
                pass
            else:
                n = time.process_time()
                while self.page.locator(f'//div[contains(@class, "i3sPf") and @tabindex="{i}"]').is_visible():
                    pass
                else:
                    elapsed_time = time.process_time() - n
                    times.append(elapsed_time)
        print('Animation change time on the small business main page:', times)

        AnimationBlockSmallBusiness.animation_block_time = times
        diff = np.diff(times)
        for t in diff:
            if t >= 1:
                return False
        return True

    @property
    def animation_time(self):
        return AnimationBlockSmallBusiness.animation_block_time
