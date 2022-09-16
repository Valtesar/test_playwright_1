from pages.main_page import AnimationBlockMain
from pages.small_business_page import AnimationBlockSmallBusiness


class TimeComparison:
    """Класс для работы с объектами времени работы анимации на страницах сайта"""

    def __init__(self, val1, val2):
        """val1 - main_page_time
           val2 - small_business_page_time"""

        self._main_page_time = val1
        self._small_business_page_time = val2

    def comparison_main_and_business_page(self):
        """Метод сверяет два значения типа float и возвращает форматированную строку с разницей двух значений"""

        if self._main_page_time < self._small_business_page_time:
            dif1 = self._small_business_page_time - self._main_page_time
            print(f'Значение времени на странице малого бизнесса и ИП больше на {dif1}, чем на главной странице.')

        elif self._main_page_time > self._small_business_page_time:
            dif2 = self._main_page_time - self._small_business_page_time
            print(f'Значение времени на главной странице больше на {dif2}, чем на странице малого бизнесса и ИП')

        else:
            print('Значения времени на главной странице и странице малого бизнесса и ИП равно или неверно.')

    @staticmethod
    def output_time_comparison():
        small_business_animation_time = AnimationBlockSmallBusiness.animation_time
        main_animation_time = AnimationBlockMain.animation_time
        time = TimeComparison(main_animation_time, small_business_animation_time)
        time.comparison_main_and_business_page()
