"""
Unit tests for password_generator.py
Run: pytest test_password_generator.py -v
"""
import pytest
from password_generator import validate_length, generate_password, CHARACTERS, MIN_LENGTH


class TestValidateLength:
    def test_valid_length(self):
        assert validate_length("12") == 12

    def test_non_numeric_raises(self):
        with pytest.raises(ValueError, match="whole number"):
            validate_length("abc")

    def test_below_minimum_raises(self):
        with pytest.raises(ValueError, match="at least"):
            validate_length("3")

    def test_exact_minimum_is_valid(self):
        assert validate_length(str(MIN_LENGTH)) == MIN_LENGTH

    def test_negative_number_raises(self):
        with pytest.raises(ValueError):
            validate_length("-5")


class TestGeneratePassword:
    def test_generated_length_matches_request(self):
        assert len(generate_password(16)) == 16

    def test_generated_password_uses_allowed_characters_only(self):
        password = generate_password(50)
        assert all(char in CHARACTERS for char in password)

    def test_minimum_length_password(self):
        assert len(generate_password(MIN_LENGTH)) == MIN_LENGTH

    def test_passwords_are_randomized(self):
        passwords = {generate_password(20) for _ in range(20)}
        assert len(passwords) == 20  # vanishingly unlikely to collide

    def test_custom_character_set(self):
        password = generate_password(10, characters="ab")
        assert all(char in "ab" for char in password)
        assert len(password) == 10
