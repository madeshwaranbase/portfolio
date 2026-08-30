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

    if any(e["id"] == employee_id for e in employees):
        print("Employee ID already exists.")
        return

    name = input("Name: ").strip()
    department = input("Department: ").strip()
    salary = input("Salary: ").strip()

    employees.append({
        "id": employee_id,
        "name": name,
        "department": department,
        "salary": salary
    })
    save_employees(employees)
    print("Employee added.")


def search_employee(employees):
    search = input("Enter ID or name: ").strip().lower()

    results = [
        e for e in employees
        if search in e["id"].lower() or search in e["name"].lower()
    ]

    if not results:
        print("No employee found.")
        return

    for employee in results:
        print(employee)


def delete_employee(employees):
    employee_id = input("Employee ID to delete: ").strip()
    original_count = len(employees)

    employees[:] = [e for e in employees if e["id"] != employee_id]

    if len(employees) == original_count:
        print("Employee not found.")
    else:
        save_employees(employees)
        print("Employee deleted.")


def main():
    employees = load_employees()

    while True:
        print("\n1. Add employee")
        print("2. Search employee")
        print("3. Delete employee")
        print("4. Show all")
        print("5. Exit")

        choice = input("Choose: ").strip()

        if choice == "1":
            add_employee(employees)
        elif choice == "2":
            search_employee(employees)
        elif choice == "3":
            delete_employee(employees)
        elif choice == "4":
            for employee in employees:
                print(employee)
        elif choice == "5":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
