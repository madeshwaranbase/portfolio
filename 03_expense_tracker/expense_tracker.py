"""
Expense Tracker (CLI)

Author: Madeshwaran
"""
import csv
from pathlib import Path
from typing import Optional

DEFAULT_FILE = Path("expenses.csv")
FIELDNAMES = ["category", "amount", "note"]


def load_expenses(file_path: Path = DEFAULT_FILE) -> list[dict]:
    """Load expenses from a CSV file. Returns an empty list if the file doesn't exist."""
    if not file_path.exists():
        return []
    with file_path.open(newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def save_expenses(expenses: list[dict], file_path: Path = DEFAULT_FILE) -> None:
    """Write expenses to a CSV file, overwriting any existing content."""
    with file_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(expenses)


def build_expense(category: str, note: str, amount_str: str) -> dict:
    """
    Build an expense record from raw string input.
    Raises ValueError if amount_str is not a valid number.
    """
    amount = float(amount_str)  # raises ValueError on bad input
    return {
        "category": category.strip(),
        "amount": str(amount),
        "note": note.strip(),
    }


def calculate_total(expenses: list[dict]) -> float:
    """Return the sum of all expense amounts."""
    return sum(float(item["amount"]) for item in expenses)


def format_expense_line(item: dict) -> str:
    """Format a single expense as a display line."""
    amount = float(item["amount"])
    return f'{item["category"]:<15} {amount:>8.2f}  {item["note"]}'


def add_expense(expenses: list[dict], file_path: Path = DEFAULT_FILE) -> None:
    category = input("Category: ")
    note = input("Note: ")
    amount_str = input("Amount: ")
    try:
        expense = build_expense(category, note, amount_str)
    except ValueError:
        print("Amount must be a number.")
        return
    expenses.append(expense)
    save_expenses(expenses, file_path)
    print("Expense added.")


def show_expenses(expenses: list[dict]) -> None:
    if not expenses:
        print("No expenses found.")
        return
    print("\nExpenses")
    print("-" * 40)
    for item in expenses:
        print(format_expense_line(item))
    print("-" * 40)
    print(f"Total: {calculate_total(expenses):.2f}")


def main() -> None:
    expenses = load_expenses()
    while True:
        print("\n1. Add expense")
        print("2. View expenses")
        print("3. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            show_expenses(expenses)
        elif choice == "3":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
