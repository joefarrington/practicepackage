import pytest

from practicepackage.maths import percentage


class TestPercentage:
    def test_one_hundred_percent(self):
        test_numerator = 100
        test_denominator = 100
        actual = percentage(test_numerator, test_denominator)
        expected = 100
        assert actual == expected, f"Expected: {expected}, Actual: {actual}"

    def test_zero_percent(self):
        test_numerator = 0
        test_denominator = 100
        actual = percentage(test_numerator, test_denominator)
        expected = 0
        assert actual == expected, f"Expected: {expected}, Actual: {actual}"

    def test_divide_zero(self):
        test_numerator = 10
        test_denominator = 0
        with pytest.raises(ZeroDivisionError):
            percentage(test_numerator, test_denominator)
