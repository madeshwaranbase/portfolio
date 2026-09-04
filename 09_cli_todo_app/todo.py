import json
from pathlib import Path

FILE_NAME = Path("tasks.json")


def load_tasks():
    if not FILE_NAME.exists():
        return []
    try:
        return json.loads(FILE_NAME.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []


def save_tasks(tasks):
    FILE_NAME.write_text(
        json.dumps(tasks, indent=2),
        encoding="utf-8"
    )


def show_tasks(tasks):
    if not tasks:
        print("No tasks.")
        return
    for index, task in enumerate(tasks, start=1):
        mark = "x" if task["done"] else " "
        print(f"{index}. [{mark}] {task['title']}")


def add_task(tasks):
    title = input("Task: ").strip()
    if not title:
        print("Task cannot be empty.")
        return
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("Task added.")


def complete_task(tasks):
    show_tasks(tasks)
    try:
        number = int(input("Task number: "))
        if not 1 <= number <= len(tasks):
            raise IndexError
        tasks[number - 1]["done"] = True
        save_tasks(tasks)
        print("Task completed.")
    except (ValueError, IndexError):
        print("Invalid task number.")


def delete_task(tasks):
    show_tasks(tasks)
    try:
        number = int(input("Task number: "))
        if not 1 <= number <= len(tasks):
            raise IndexError
        removed = tasks.pop(number - 1)
        save_tasks(tasks)
        print(f"Deleted: {removed['title']}")
    except (ValueError, IndexError):
        print("Invalid task number.")


def main():
    tasks = load_tasks()
    while True:
        print("\n1. Add task")
        print("2. List tasks")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
