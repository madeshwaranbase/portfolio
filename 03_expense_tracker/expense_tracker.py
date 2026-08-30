import csv
from pathlib import Path

FILE_NAME = Path("expenses.csv")


def load_expenses():
    if not FILE_NAME.exists():
        return []

    with FILE_NAME.open(newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def save_expenses(expenses):
    with FILE_NAME.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["category", "amount", "note"])
        writer.writeheader()
        writer.writerows(expenses)


def add_expense(expenses):
    category = input("Category: ").strip()
    note = input("Note: ").strip()

    try:
        amount = float(input("Amount: "))
    except ValueError:
        print("Amount must be a number.")
        return

    expenses.append({
        "category": category,
        "amount": str(amount),
        "note": note
    })
    save_expenses(expenses)
    print("Expense added.")


def show_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return

    total = 0
    print("\nExpenses")
    print("-" * 40)

    for item in expenses:
        amount = float(item["amount"])
        total += amount
        print(f'{item["category"]:<15} {amount:>8.2f}  {item["note"]}')

    print("-" * 40)
    print(f"Total: {total:.2f}")


def main():
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
