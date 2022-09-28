from time import sleep


class TestTariffsAndDocuments:
    """Класс для тестирования раздела тарифы и документация"""

    def test_files(self, start_page, docs_and_tariffs_page):
        """Тест проверки наличия файлов тарифов и документации на странице, а так же получение их размеров"""

        start_page.pick_lower_menu_block('Тарифы и документы')
        sleep(3)
        assert docs_and_tariffs_page.get_active_button() == "Комплексное банковское обслуживание"
        sleep(2)
        docs_and_tariffs_page.get_files_sizes()
        docs_and_tariffs_page.pick_the_biggest_file()
        assert docs_and_tariffs_page.try_open_file()
        docs_and_tariffs_page.switch_active_button('Комплексное банковское обслуживание')
        sleep(2)
        docs_and_tariffs_page.output_information()
        sleep(5)

