from playwright.sync_api import Page, expect
from hooks.file_size_transformation import FileSizeTransformation


class DocsPage:
    def __init__(self, page: Page):
        self.page = page
        self.file_sizes = []
        self.file_names = []
        self.files_and_names = []

    def get_active_button(self):
        """Метод проверяет нахождения активной кнопки на странице,
         возвращает -> str название текущей активной кнопки."""

        expect(self.page.locator('//p[contains(@class, "d28gXp g28gXp")]'))\
            .to_be_visible()
        return ''.join(self.page.locator('//p[contains(@class, "d28gXp g28gXp")]').all_text_contents())

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

        print('\nСамый большой файл находящийся на странице:\n{}\nИмеет размер:\n{} Мб'
              .format(max(self.files_and_names.items(), key=lambda x: x[1])[0],
                      max(self.files_and_names.items(), key=lambda x: x[1])[1]))

    def try_download_file(self):
        """Метод скачивает указанный файл со страницы"""
        pass

    def check_downloaded_file(self):
        """Метод проверяет скачанный файл на соответствие требованиям"""
        pass
