from solutions.CHK import checkout_solution

# +------+-------+------------------------+
# | Item | Price | Special offers         |
# +------+-------+------------------------+
# | A    | 50    | 3A for 130, 5A for 200 |
# | B    | 30    | 2B for 45              |
# | C    | 20    |                        |
# | D    | 15    |                        |
# | E    | 40    | 2E get one B free      |
# | F    | 10    | 2F get one F free      |
# | G    | 20    |                        |
# | H    | 10    | 5H for 45, 10H for 80  |
# | I    | 35    |                        |
# | J    | 60    |                        |
# | K    | 80    | 2K for 150             |
# | L    | 90    |                        |
# | M    | 15    |                        |
# | N    | 40    | 3N get one M free      |
# | O    | 10    |                        |
# | P    | 50    | 5P for 200             |
# | Q    | 30    | 3Q for 80              |
# | R    | 50    | 3R get one Q free      |
# | S    | 30    |                        |
# | T    | 20    |                        |
# | U    | 40    | 3U get one U free      |
# | V    | 50    | 2V for 90, 3V for 130  |
# | W    | 20    |                        |
# | X    | 90    |                        |
# | Y    | 10    |                        |
# | Z    | 50    |                        |
# +------+-------+------------------------+

class TestSum:
    def test_checkout_illegal_input(self):
        assert checkout_solution.checkout("A1") == -1
        assert checkout_solution.checkout("AB!") == -1

    def test_checkout_empty(self):
        assert checkout_solution.checkout("") == 0

    def test_checkout_one_item(self):
        assert checkout_solution.checkout("A") == 50
        assert checkout_solution.checkout("C") == 20

    def test_checkout_multiple_items_no_offer(self):
        assert checkout_solution.checkout("AC") == 70
        assert checkout_solution.checkout("ABCD") == 115

    def test_checkout_multiple_items_one_offer(self):
        assert checkout_solution.checkout("AA") == 100

    def test_checkout_multiple_items_multiple_offer(self):
        assert checkout_solution.checkout("AAABBC") == 195

    def test_checkout_multiple_items_repeat_offer(self):
        assert checkout_solution.checkout("BBBBD") == 105

    def test_checkout_prioritises_best_offer(self):
        assert checkout_solution.checkout("AAAAAA") == 250

    def test_checkout_different_offers_for_same_item(self):
        # 200(5) + 130(3) + 50(1)
        assert checkout_solution.checkout("AAAAAAAAA") == 380

    def test_checkout_accounts_for_free_item_when_available(self):
        assert checkout_solution.checkout("BEE") == 80

    def test_checkout_accounts_for_multiple_free_items_when_available(self):
        assert checkout_solution.checkout("BBEEEE") == 160

    def test_checkout_ignores_free_item_when_not_in_basket(self):
        assert checkout_solution.checkout("AEE") == 130
        assert checkout_solution.checkout("ABEEEE") == 210

    def test_checkout_buy_x_get_x_free_offer(self):
        assert checkout_solution.checkout("FF") == 20
        assert checkout_solution.checkout("FFF") == 20
        assert checkout_solution.checkout("FFFF") == 30
        assert checkout_solution.checkout("FFFFFF") == 40

    def test_checkout_complex_order(self):
        # Z  + T  + 4Q + Q  + 10H + 5H + 2F + 4U (1 free)
        # 50 + 20 + 80 + 30 + 80  + 45 + 20 + 120
        ZTQQQQHHHHHHHHHHHHHHHCFFUUUU
        assert checkout_solution.checkout("ZTQQQQHHHHHHHHHHHHHHHCFFUUUU") == 445