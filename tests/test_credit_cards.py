class TestCreditCardsPage:
    def test_credit_card_order(self, start_page):
        start_page.pick_upper_menu_block('Карты', 'Целый год без %')
