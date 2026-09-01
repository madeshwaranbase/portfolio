"""
Unit tests for game.py
Run: pytest test_game.py -v
"""
import pytest
from game import check_guess, get_random_number


class TestCheckGuess:
    def test_guess_too_low(self):
        assert check_guess(10, 50) == "low"

    def test_guess_too_high(self):
        assert check_guess(90, 50) == "high"

    def test_guess_correct(self):
        assert check_guess(50, 50) == "correct"

    def test_guess_at_lower_boundary(self):
        assert check_guess(1, 1) == "correct"

    def test_guess_at_upper_boundary(self):
        assert check_guess(100, 100) == "correct"

    @pytest.mark.parametrize("guess,secret,expected", [
        (1, 100, "low"),
        (100, 1, "high"),
        (55, 55, "correct"),
    ])
    def test_check_guess_parametrized(self, guess, secret, expected):
        assert check_guess(guess, secret) == expected


class TestGetRandomNumber:
    def test_default_range(self):
        for _ in range(100):
            n = get_random_number()
            assert 1 <= n <= 100

    def test_custom_range(self):
        for _ in range(100):
            n = get_random_number(10, 20)
            assert 10 <= n <= 20

    def test_single_value_range(self):
        assert get_random_number(5, 5) == 5
