tasks = []


def add_task():
    title = input("Task: ").strip()

    if not title:
        print("Task title cannot be empty.")
        return

    tasks.append({
        "title": title,
        "done": False
    })

    print("Task added.")


def show_tasks():
    if not tasks:
        print("No tasks found.")
        return

    for index, task in enumerate(tasks, start=1):
        status = "✓" if task["done"] else " "
        print(f"{index}. [{status}] {task['title']}")


def mark_task_done():
    show_tasks()

    if not tasks:
        return

    task_number = int(input("Task number: "))

    if not is_valid_task_number(task_number):
        print("Invalid task number.")
        return

    tasks[task_number - 1]["done"] = True
    print("Task marked as done.")


def remove_task():
    show_tasks()

    if not tasks:
        return

    task_number = int(input("Task number: "))

    if not is_valid_task_number(task_number):
        print("Invalid task number.")
        return

    removed_task = tasks.pop(task_number - 1)
    print(f"Removed: {removed_task['title']}")


def is_valid_task_number(task_number):
    return 1 <= task_number <= len(tasks)


def display_menu():
    print("\nTASK MANAGER")
    print("1. Add task")
    print("2. Show tasks")
    print("3. Mark task as done")
    print("4. Remove task")
    print("5. Exit")


while True:
    display_menu()

    choice = input("Choose: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        show_tasks()

    elif choice == "3":
        mark_task_done()

    elif choice == "4":
        remove_task()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")