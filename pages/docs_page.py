from playwright.sync_api import Page, expect
from hooks.file_size_transformation import FileSizeTransformation


class DocsPage:
    def __init__(self, page: Page):
        self.page = page
        self.file_sizes = []
        self.file_names = []
        self.files_and_names = {}
        self.the_biggest_file = {}

    def get_active_button(self):
        """Метод проверяет нахождения активной кнопки на странице,
         возвращает -> str название текущей активной кнопки."""

        expect(self.page.locator('//p[contains(@class, "d28gXp g28gXp")]'))\
            .to_be_visible()
        return ''.join(self.page.locator('//p[contains(@class, "d28gXp g28gXp")]').all_text_contents())

    def switch_active_button(self, button):
        """Метод переключается между кнопками на странице. Получает на вход название страницы"""
        pass

    def get_files_sizes(self):
        """Метод собирает названия и размеры файлов на странице,
         соединяет их в словарь в случае одинакового кол-ва пар"""

        self.file_sizes = self.page.locator('//p[@class="aqMVUC bqMVUC hqMVUC DqMVUC cqMVUC eG2mwi RG2mwi"]')\
            .all_text_contents()
        self.file_sizes = FileSizeTransformation.from_kb_to_mb(self.file_sizes)

        self.file_names = self.page.locator('//a[@class="a33ip_ g33ip_ c33ip_"]').all_text_contents()

        if len(self.file_names) == len(self.file_sizes):
            self.files_and_names = dict(zip(self.file_names, self.file_sizes))
        else:
            raise Exception('Missing the filename or file size')

    def pick_the_biggest_file(self):
        """Метод выбирает самый большой находящийся на странице файл и выводит в консоль его назване и размер файла."""

        biggest_file_name = max(self.files_and_names.items(), key=lambda x: x[1])[0].replace(u'\xa0', u' ')
        biggest_file_size = max(self.files_and_names.items(), key=lambda x: x[1])[1]

        self.the_biggest_file = (biggest_file_name, biggest_file_size)

        print('\nСамый большой файл находящийся на странице:\n{}\nИмеет размер:\n{} Мб'
              .format(self.the_biggest_file[0], self.the_biggest_file[1]))

    def try_open_file(self):
        """Метод скачивает указанный файл со страницы"""
        with self.page.context.expect_page(timeout=5000) as new_page_info:
            self.page.locator(f'text={self.the_biggest_file[0]}').click()
        self.new_page = new_page_info.value
        if self.new_page:
            self.new_page.close()
            return True
        else:
            return False
