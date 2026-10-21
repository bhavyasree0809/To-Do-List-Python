
from datetime import datetime

tasks = []

print("===== TO-DO LIST PRO =====")

while True:
    print("\n--- MENU ---")
    print("1. Add Task")
    print("2. View / Filter Tasks")
    print("3. Delete Task")
    print("4. Search Tasks")
    print("5. Complete a Task")
    print("6. Exit")

    choice = input("Enter your choice: ").strip()

    # 1. ADD TASK
    if choice == "1":
        title = input("Enter task name: ").strip()

        if not title:
            print("Error: Task name cannot be empty!")
            continue

        priority = input(
            "Enter priority (High, Medium, Low) [Default: Medium]: "
        ).strip().capitalize()

        if priority not in ["High", "Medium", "Low"]:
            priority = "Medium"

        due_date = input(
            "Enter due date (YYYY-MM-DD) or press Enter to skip: "
        ).strip()

        if due_date:
            try:
                datetime.strptime(due_date, "%Y-%m-%d")
            except ValueError:
                print("Invalid date! Due date set to None.")
                due_date = "None"
        else:
            due_date = "None"

        tasks.append({
            "title": title,
            "priority": priority,
            "due_date": due_date,
            "completed": False
        })

        print("Task added successfully!")

    # 2. VIEW / FILTER TASKS
    elif choice == "2":
        if not tasks:
            print("No tasks yet.")
            continue

        print("\nFilter Options: All, Pending, Completed")
        filter_choice = input(
            "Choose filter [Default: All]: "
        ).strip().capitalize()

        if filter_choice not in ["All", "Pending", "Completed"]:
            filter_choice = "All"

        print("\n===== YOUR TASKS =====")
        displayed_count = 0

        for i, task in enumerate(tasks, start=1):
            if filter_choice == "Pending" and task["completed"]:
                continue

            if filter_choice == "Completed" and not task["completed"]:
                continue

            status = "Completed" if task["completed"] else "Pending"

            print(
                f"{i}. [{status}] {task['title']} | "
                f"Priority: {task['priority']} | "
                f"Due: {task['due_date']}"
            )

            displayed_count += 1

        if displayed_count == 0:
            print("No tasks match this filter.")

    # 3. DELETE TASK
    elif choice == "3":
        if not tasks:
            print("No tasks available to delete.")
            continue

        for i, task in enumerate(tasks, start=1):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{i}. {task['title']} ({status})")

        try:
            number = int(input("Enter task number to delete: "))

            if 1 <= number <= len(tasks):
                removed = tasks.pop(number - 1)
                print("Task deleted:", removed["title"])
            else:
                print("Invalid task number!")

        except ValueError:
            print("Please enter a valid number.")

    # 4. SEARCH TASKS
    elif choice == "4":
        if not tasks:
            print("No tasks available to search.")
            continue

        query = input("Enter keyword to search: ").strip().lower()

        if not query:
            print("Please enter a search keyword.")
            continue

        print("\n===== SEARCH RESULTS =====")
        found = False

        for i, task in enumerate(tasks, start=1):
            if query in task["title"].lower():
                status = "Completed" if task["completed"] else "Pending"

                print(
                    f"{i}. [{status}] {task['title']} | "
                    f"Priority: {task['priority']} | "
                    f"Due: {task['due_date']}"
                )

                found = True

        if not found:
            print("No matching tasks found.")

    # 5. COMPLETE A TASK
    elif choice == "5":
        pending = [
            (i, task)
            for i, task in enumerate(tasks, start=1)
            if not task["completed"]
        ]

        if not pending:
            print("No pending tasks available!")
            continue

        print("\n===== PENDING TASKS =====")

        for i, task in pending:
            print(f"{i}. {task['title']} | Priority: {task['priority']}")

        try:
            number = int(
                input("Enter task number to complete: ")
            )

            if 1 <= number <= len(tasks):
                if not tasks[number - 1]["completed"]:
                    tasks[number - 1]["completed"] = True
                    print(
                        "Task completed:",
                        tasks[number - 1]["title"]
                    )
                else:
                    print("This task is already completed.")
            else:
                print("Invalid task number!")

        except ValueError:
            print("Please enter a valid number.")

    # 6. EXIT
    elif choice == "6":
        print("Thank you for using TO-DO LIST PRO!")
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Please select 1 to 6.")
