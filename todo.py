tasks = []

def add_task():
    name = input("Enter task name: ")
    deadline = input("Enter deadline (YYYY-MM-DD): ")
    priority = input("Enter priority (High/Medium/Low): ")
    category = input("Enter category (Study/Work/Personal): ")

    task = {
        "name": name,
        "deadline": deadline,
        "priority": priority,
        "category": category,
        "completed": False
    }

    tasks.append(task)
    print("Task added successfully!\n")


def view_tasks():
    if len(tasks) == 0:
        print("No tasks available.\n")
        return

    for i, task in enumerate(tasks):
        status = "Done" if task["completed"] else "Pending"
        print(f"{i+1}. {task['name']} | Deadline: {task['deadline']} | Priority: {task['priority']} | Category: {task['category']} | Status: {status}")
    print()
def mark_completed():
    view_tasks()
    num = int(input("Enter task number to mark as completed: "))
    if 1 <= num <= len(tasks):
        tasks[num-1]["completed"] = True
        print("Task marked as completed.\n")
    else:
        print("Invalid task number.\n")


def delete_task():
    view_tasks()
    num = int(input("Enter task number to delete: "))
    if 1 <= num <= len(tasks):
        tasks.pop(num-1)
        print("Task deleted successfully.\n")
    else:
        print("Invalid task number.\n")


def filter_category():
    cat = input("Enter category to filter: ")
    found = False

    for task in tasks:
        if task["category"].lower() == cat.lower():
            status = "Done" if task["completed"] else "Pending"
            print(f"{task['name']} | Deadline: {task['deadline']} | Priority: {task['priority']} | Status: {status}")
            found = True

    if not found:
        print("No tasks found in this category.\n")
    print()


if __name__ == "__main__":
    while True:
        print("===== TO-DO LIST MANAGER =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Filter by Category")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_completed()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            filter_category()
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.\n")