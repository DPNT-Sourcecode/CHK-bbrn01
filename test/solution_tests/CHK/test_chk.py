from solutions.CHK import checkout_solution


# Our price table and offers: 
# +------+-------+----------------+
# | Item | Price | Special offers |
# +------+-------+----------------+
# | A    | 50    | 3A for 130     |
# | B    | 30    | 2B for 45      |
# | C    | 20    |                |
# | D    | 15    |                |
# +------+-------+----------------+


class TestSum:
    def test_checkout_one_item(self):
        assert checkout_solution.checkout("A") == 50
        assert checkout_solution.checkout("C") == 15

    def test_checkout_multiple_items_no_offer(self):
        assert checkout_solution.checkout("AC") == 70
        assert checkout_solution.checkout("ABCD") == 115
    
    def test_checkout_multiple_items_one_offer(self):
        assert checkout_solution.checkout("AA") == 70

    def test_checkout_multiple_items_multiple_offer(self):
        assert checkout_solution.checkout("AC") == 70

    def test_checkout_multiple_items_repeat_offer(self):

    def test_checkout_illegal_input(self):

