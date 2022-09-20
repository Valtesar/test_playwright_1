from playwright.sync_api import Page, expect
from hooks.file_size_transformation import FileSizeTransformation


class DocsPage:
    def __init__(self, page: Page):
        self.page = page
        self.file_sizes = []

    def get_active_button(self):
        """Метод проверяет нахождения активной кнопки на странице,
         возвращает -> str название текущей активной кнопки."""

        expect(self.page.locator('//p[contains(@class, "d28gXp g28gXp")]'))\
            .to_be_visible()
        return ''.join(self.page.locator('//p[contains(@class, "d28gXp g28gXp")]').all_text_contents())

    def get_files_sizes(self):
        """Метод собирает значения размера файлов на странице в список"""
        self.file_sizes = self.page.locator('//p[@class="aqMVUC bqMVUC hqMVUC DqMVUC cqMVUC eG2mwi RG2mwi"]')\
            .all_text_contents()
        self.file_sizes = FileSizeTransformation.from_kb_to_mb(self.file_sizes)

    def pick_the_biggest_file(self):
        """Выбирает самый большой файл из списка"""
        print('Самый большой файл находящийся на странице имеет размер:', max(self.file_sizes))
        pass

    def try_download_file(self):
        """Метод скачивает файл со страницы"""
        pass
