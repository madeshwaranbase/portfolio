"""
Unit tests for calculator.py
Run: pytest test_calculator.py -v
"""
import pytest
from calculator import add, subtract, multiply, divide, calculate, DivisionByZeroError


class TestArithmeticOperations:
    def test_add_positive_numbers(self):
        assert add(2, 3) == 5

    def test_add_negative_numbers(self):
        assert add(-2, -3) == -5

    def test_subtract(self):
        assert subtract(10, 4) == 6

    def test_multiply(self):
        assert multiply(3, 4) == 12

    def test_multiply_by_zero(self):
        assert multiply(5, 0) == 0

    def test_divide(self):
        assert divide(10, 2) == 5

    def test_divide_by_zero_raises(self):
        with pytest.raises(DivisionByZeroError):
            divide(10, 0)

    def test_divide_returns_float(self):
        assert divide(7, 2) == 3.5


class TestCalculateDispatch:
    @pytest.mark.parametrize("op,a,b,expected", [
        ("+", 2, 3, 5),
        ("-", 5, 2, 3),
        ("*", 4, 3, 12),
        ("/", 10, 5, 2),
    ])
    def test_calculate_valid_operators(self, op, a, b, expected):
        assert calculate(a, op, b) == expected

    def test_calculate_invalid_operator_raises(self):
        with pytest.raises(ValueError):
            calculate(1, "%", 2)
