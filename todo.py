tasks = []

print("📝 TO-DO LIST")

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks yet.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, 1):
                print(i, ".", task)

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            for i, task in enumerate(tasks, 1):
                print(i, ".", task)

            number = int(input("Enter task number to delete: "))
            tasks.pop(number - 1)
            print("Task deleted!")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
