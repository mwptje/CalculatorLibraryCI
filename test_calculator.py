'''Test for calculator.py'''

import calculator


class TestCalculator:

    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_subtraction(self):
        assert 0 == calculator.substract(2, 2)
