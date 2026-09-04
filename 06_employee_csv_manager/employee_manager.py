import csv
from pathlib import Path

FILE_NAME = Path("employees.csv")
FIELDS = ["id", "name", "department", "salary"]


def load_employees():
    if not FILE_NAME.exists():
        return []

    with FILE_NAME.open(newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def save_employees(employees):
    with FILE_NAME.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(employees)


def add_employee(employees):
    employee_id = input("Employee ID: ").strip()
    if not employee_id:
        print("Employee ID cannot be empty.")
        return

    if any(e["id"] == employee_id for e in employees):
        print("Employee ID already exists.")
        return

    name = input("Name: ").strip()
    department = input("Department: ").strip()
    salary_raw = input("Salary: ").strip()

    if not name or not department:
        print("Name and department cannot be empty.")
        return

    try:
        salary = float(salary_raw)
        if salary < 0:
            raise ValueError
    except ValueError:
        print("Salary must be a non-negative number.")
        return

    employees.append({
        "id": employee_id,
        "name": name,
        "department": department,
        "salary": salary,
    })
    save_employees(employees)
    print(f"Employee {employee_id} added.")


def search_employee(employees):
    query = input("Search by ID or name: ").strip().lower()
    results = [
        e for e in employees
        if query == e["id"].lower() or query in e["name"].lower()
    ]

    if not results:
        print("No matching employees found.")
        return

    for e in results:
        print(f"{e['id']} | {e['name']} | {e['department']} | {e['salary']}")


def delete_employee(employees):
    employee_id = input("Employee ID to delete: ").strip()
    match = next((e for e in employees if e["id"] == employee_id), None)

    if not match:
        print("Employee ID not found.")
        return

    confirm = input(f"Delete {match['name']} ({employee_id})? [y/N]: ").strip().lower()
    if confirm != "y":
        print("Cancelled.")
        return

    employees.remove(match)
    save_employees(employees)
    print(f"Employee {employee_id} deleted.")


def print_menu():
    print("\n1. Add employee")
    print("2. Search employee")
    print("3. Delete employee")
    print("4. List all")
    print("5. Exit")


def main():
    employees = load_employees()

    while True:
        print_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_employee(employees)
        elif choice == "2":
            search_employee(employees)
        elif choice == "3":
            delete_employee(employees)
        elif choice == "4":
            if not employees:
                print("No employees on record.")
            for e in employees:
                print(f"{e['id']} | {e['name']} | {e['department']} | {e['salary']}")
        elif choice == "5":
            print("Goodbye.")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
