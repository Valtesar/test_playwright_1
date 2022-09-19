from time import sleep


class TestTariffsAndDocuments:
    def test_files(self, start_page, docs_and_tariffs_page):
        start_page.pick_lower_menu_block('Тарифы и документы')
        sleep(3)
        pass
