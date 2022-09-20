from playwright.sync_api import Page, expect


class DocsPage:
    def __init__(self, page: Page):
        self.page = page

    def get_active_button(self):
        """Возвращает название текущей нажатой кнопки"""
        expect(self.page.locator('//p[contains(@class, "d28gXp g28gXp")]'))\
            .to_be_visible()
        return ''.join(self.page.locator('//p[contains(@class, "d28gXp g28gXp")]').all_text_contents())

    def get_files_sizes(self):
        """Метод собирает значения размера файлов на странице в список"""
        pass

    def pick_biggest_file(self):
        """Выбирает самый большой файл из списка"""
        pass

    def try_download_file(self):
        """Метод скачивает файл со страницы"""
        pass
