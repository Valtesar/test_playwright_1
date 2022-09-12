

class TestCreditCardsPage:

    def test_credit_card_order(self, start_page, cards_page):
        start_page.pick_upper_menu_block('Карты', 'Целый год без %')
        assert cards_page.get_email_validation()
        cards_page.get_100_days_card()
        assert cards_page.get_header_of_the_tab()


