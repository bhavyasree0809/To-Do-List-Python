tasks = []
print("TO-DO LIST PRO")

while True:
    print("\n--- MENU ---")
    print("1. Add Task")
    print("2. View / Filter Tasks")
    print("3. Delete Task")
    print("4. Search Tasks")
    print("5. Complete a Task")
    print("6. Exit")
    
    choice = input("Enter your choice: ").strip()
    
    # 1. ADD TASK (With Priority and Due Date)
    if choice == "1":
        title = input("Enter task name: ").strip()
        if not title:
            print("Error: Task name cannot be empty!")
            continue
            
        priority = input("Enter priority (High, Medium, Low) [Default: Medium]: ").strip().capitalize()
        if priority not in ["High", "Medium", "Low"]:
            priority = "Medium"
            
        due_date = input("Enter due date (YYYY-MM-DD) or press Enter to skip: ").strip()
        if due_date:
            try:
                # Validate date format
                datetime.strptime(due_date, "%Y-%m-%d")
            except ValueError:
                print("Error: Invalid date format! Setting due date to 'None'.")
                due_date = "None"
        else:
            due_date = "None"
            
        tasks.append({
            "title": title,
            "priority": priority,
            "due_date": due_date,
            "completed": False
        })
        print("Success: Task added successfully!")
        
    # 2. VIEW AND FILTER TASKS
    elif choice == "2":
        if not tasks:
            print("No tasks yet.")
            continue
            
        print("\nFilter Options:")
        print("All | Pending | Completed")
        filter_choice = input("Choose a filter [Default: All]: ").strip().capitalize()
        
        print(f"\n--- Your Tasks ({filter_choice if filter_choice in ['Pending', 'Completed'] else 'All'}) ---")
        
        displayed_count = 0
        for i, t in enumerate(tasks, 1):
            # Apply filters
            if filter_choice == "Pending" and t["completed"]:
                continue
            if filter_choice == "Completed" and not t["completed"]:
                continue
                
            status = "Completed" if t["completed"] else "Pending"
            print(f"{i}. [{status}] {t['title']} | Priority: {t['priority']} | Due: {t['due_date']}")
            displayed_count += 1
            
        if displayed_count == 0:
            print("No tasks match this filter.")
            
    # 3. DELETE TASK
    elif choice == "3":
        if not tasks:
            print("Error: No tasks to delete.")
            continue
            
        for i, t in enumerate(tasks, 1):
            status = "Completed" if t["completed"] else "Pending"
            print(f"{i}. {t['title']} ({status})")
            
        try:
            number = int(input("Enter task number to delete: "))
            if 1 <= number <= len(tasks):
                removed = tasks.pop(number - 1)
                print(f"Task deleted: {removed['title']}")
            else:
                print("Error: Invalid task number! Out of range.")
        except ValueError:
            print("Error: Invalid input! Please enter a valid number.")
            
    # 4. SEARCH TASKS
    elif choice == "4":
        if not tasks:
            print("Error: No tasks available to search.")
            continue
            
        query = input("Enter keyword to search for: ").strip().lower()
        print(f"\n--- Search Results for '{query}' ---")
        
        found = False
        for i, t in enumerate(tasks, 1):
            if query in t["title"].lower():
                status = "Completed" if t["completed"] else "Pending"
                print(f"{i}. [{status}] {t['title']} | Priority: {t['priority']} | Due: {t['due_date']}")
                found = True
                
        if not found:
            print("No matching tasks found.")
            
    # 5. COMPLETE A TASK
    elif choice == "5":
        pending_tasks = [t for t in tasks if not t["completed"]]
        if not pending_tasks:
            print("All tasks are already completed!")
            continue
            
        for i, t in enumerate(tasks, 1):
            if not t["completed"]:
                print(f"{i}. {t['title']} | Priority: {t['priority']}")
                
        try:
            number = int(input("Enter task number to mark as completed: "))
            if 1 <= number <= len(tasks):
                if not tasks[number - 1]["completed"]:
                    tasks[number - 1]["completed"] = True
                    print(f"Task status updated: {tasks[number - 1]['title']} is now Completed!")
                else:
                    print("Notice: This task is already completed.")
            else:
                print("Error: Invalid task number!")
        except ValueError:
            print("Error: Invalid input! Please enter a valid number.")
            
    # 6. EXIT
    elif choice == "6":
        print("Goodbye!")
        break
        
    else:
        print("Error: Invalid choice! Please select an option from 1 to 6.")
