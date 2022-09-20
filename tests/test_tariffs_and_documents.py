from time import sleep


class TestTariffsAndDocuments:
    def test_files(self, start_page, docs_and_tariffs_page):
        start_page.pick_lower_menu_block('Тарифы и документы')
        sleep(3)
        assert docs_and_tariffs_page.get_active_button() == "Комплексное банковское обслуживание"
        sleep(2)
        docs_and_tariffs_page.get_files_sizes()
        docs_and_tariffs_page.pick_the_biggest_file()
        pass
