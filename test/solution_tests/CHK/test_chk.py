from unittest.mock import patch

from solutions.CHK import checkout_solution
from solutions.CHK.sku_data import SkuData, sku_data

test_data = """+------+-------+------------------------+
| Item | Price | Special offers                  |
+------+-------+---------------------------------+
| A    | 50    | 3A for 130, 5A for 200          |
| B    | 30    | 2B for 45                       |
| C    | 20    |                                 |
| D    | 15    |                                 |
| E    | 40    | 2E get one B free               |
| F    | 10    | 2F get one F free               |
| H    | 10    | 5H for 45, 10H for 80           |
| Q    | 30    | 3Q for 80                       |
| U    | 40    | 3U get one U free               |
| S    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
| T    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
| X    | 17    | buy any 3 of (S,T,X,Y,Z) for 45 |
| Y    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
| Z    | 21    | buy any 3 of (S,T,X,Y,Z) for 45 |
+------+-------+---------------------------------+"""
test_sku_data = SkuData(test_data)


class TestSum:
    @patch("solutions.CHK.checkout_solution.sku_data", test_sku_data)
    def test_checkout_illegal_input(self):
        assert checkout_solution.checkout("A1") == -1
        assert checkout_solution.checkout("AB!") == -1

    @patch("solutions.CHK.checkout_solution.sku_data", test_sku_data)
    def test_checkout_empty(self):
        assert checkout_solution.checkout("") == 0

    @patch("solutions.CHK.checkout_solution.sku_data", test_sku_data)
    def test_checkout_one_item(self):
        assert checkout_solution.checkout("A") == 50
        assert checkout_solution.checkout("C") == 20

    @patch("solutions.CHK.checkout_solution.sku_data", test_sku_data)
    def test_checkout_multiple_items_no_offer(self):
        assert checkout_solution.checkout("AC") == 70
        assert checkout_solution.checkout("ABCD") == 115

    @patch("solutions.CHK.checkout_solution.sku_data", test_sku_data)
    def test_checkout_multiple_items_one_offer(self):
        assert checkout_solution.checkout("AA") == 100

    @patch("solutions.CHK.checkout_solution.sku_data", test_sku_data)
    def test_checkout_multiple_items_multiple_offer(self):
        assert checkout_solution.checkout("AAABBC") == 195

    @patch("solutions.CHK.checkout_solution.sku_data", test_sku_data)
    def test_checkout_multiple_items_repeat_offer(self):
        assert checkout_solution.checkout("BBBBD") == 105

    @patch("solutions.CHK.checkout_solution.sku_data", test_sku_data)
    def test_checkout_prioritises_best_offer(self):
        assert checkout_solution.checkout("AAAAAA") == 250

    @patch("solutions.CHK.checkout_solution.sku_data", test_sku_data)
    def test_checkout_different_offers_for_same_item(self):
        # 200(5) + 130(3) + 50(1)
        assert checkout_solution.checkout("AAAAAAAAA") == 380

    @patch("solutions.CHK.checkout_solution.sku_data", test_sku_data)
    def test_checkout_accounts_for_free_item_when_available(self):
        assert checkout_solution.checkout("BEE") == 80

    @patch("solutions.CHK.checkout_solution.sku_data", test_sku_data)
    def test_checkout_accounts_for_multiple_free_items_when_available(self):
        assert checkout_solution.checkout("BBEEEE") == 160

    @patch("solutions.CHK.checkout_solution.sku_data", test_sku_data)
    def test_checkout_ignores_free_item_when_not_in_basket(self):
        assert checkout_solution.checkout("AEE") == 130
        assert checkout_solution.checkout("ABEEEE") == 210

    @patch("solutions.CHK.checkout_solution.sku_data", test_sku_data)
    def test_checkout_buy_x_get_x_free_offer(self):
        assert checkout_solution.checkout("FF") == 20
        assert checkout_solution.checkout("FFF") == 20
        assert checkout_solution.checkout("FFFF") == 30
        assert checkout_solution.checkout("FFFFFF") == 40

    @patch("solutions.CHK.checkout_solution.sku_data", test_sku_data)
    def test_checkout_complex_order(self):
        # Z  + T  + 4Q + Q  + 10H + 5H + C  + 2F + 4U (1 free)
        # 21 + 20 + 80 + 30 + 80  + 45 + 20 + 20 + 120
        assert checkout_solution.checkout("ZTQQQQHHHHHHHHHHHHHHHCFFUUUU") == 436

    @patch("solutions.CHK.checkout_solution.sku_data", test_sku_data)
    def test_checkout_multi_selection_offer(self):
        assert checkout_solution.checkout("SXZ") == 45


