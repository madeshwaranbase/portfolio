"""
Unit tests for expense_tracker.py
Run: pytest test_expense_tracker.py -v
"""
import pytest
from expense_tracker import (
    build_expense,
    calculate_total,
    format_expense_line,
    load_expenses,
    save_expenses,
)


class TestBuildExpense:
    def test_build_expense_valid(self):
        expense = build_expense("Food", "Lunch", "12.50")
        assert expense == {"category": "Food", "amount": "12.5", "note": "Lunch"}

    def test_build_expense_strips_whitespace(self):
        expense = build_expense("  Travel  ", "  Taxi  ", "20")
        assert expense["category"] == "Travel"
        assert expense["note"] == "Taxi"

    def test_build_expense_invalid_amount_raises(self):
        with pytest.raises(ValueError):
            build_expense("Food", "Lunch", "not-a-number")


class TestCalculateTotal:
    def test_calculate_total_multiple_items(self):
        expenses = [{"amount": "10"}, {"amount": "20.5"}, {"amount": "5"}]
        assert calculate_total(expenses) == 35.5

    def test_calculate_total_empty_list(self):
        assert calculate_total([]) == 0

    def test_calculate_total_single_item(self):
        assert calculate_total([{"amount": "100"}]) == 100.0


class TestFormatExpenseLine:
    def test_format_expense_line_contains_category_and_note(self):
        line = format_expense_line({"category": "Food", "amount": "12.5", "note": "Lunch"})
        assert "Food" in line
        assert "Lunch" in line
        assert "12.50" in line


class TestFileRoundTrip:
    def test_save_and_load_round_trip(self, tmp_path):
        file_path = tmp_path / "expenses.csv"
        expenses = [
            {"category": "Food", "amount": "12.5", "note": "Lunch"},
            {"category": "Travel", "amount": "20.0", "note": "Taxi"},
        ]
        save_expenses(expenses, file_path)
        loaded = load_expenses(file_path)
        assert loaded == expenses

    def test_load_expenses_missing_file_returns_empty_list(self, tmp_path):
        file_path = tmp_path / "does_not_exist.csv"
        assert load_expenses(file_path) == []

    def test_save_expenses_overwrites_existing_file(self, tmp_path):
        file_path = tmp_path / "expenses.csv"
        save_expenses([{"category": "A", "amount": "1", "note": "x"}], file_path)
        save_expenses([{"category": "B", "amount": "2", "note": "y"}], file_path)
        loaded = load_expenses(file_path)
        assert len(loaded) == 1
        assert loaded[0]["category"] == "B"
