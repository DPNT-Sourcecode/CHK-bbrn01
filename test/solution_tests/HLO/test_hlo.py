from solutions.HLO import hello_solution


class TestSum:
    def test_hello(self):
        assert hello_solution.hello(1, 2) == 3
