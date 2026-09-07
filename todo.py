
def to_do_list():
    tasks = []  # Shared variable for nested functions

    # Nested Functions that handles each task action
    #function to add a new task
    def add_task():
        """Add a task to the shared 'tasks' list."""
        task = input("Enter task to add: ")
        tasks.append(task)  # Directly access 'tasks' from parent
        print(f"Task '{task}' added!")

    #function to view added task
    def view_tasks():
        """Display all tasks from the shared 'tasks' list."""
        if not tasks:
            print("Your to-do list is empty!")
        else:
            print("\n--- Current Tasks ---")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    #function to remove tasks
    def remove_task():
        """Remove a task from the list with proper validation."""
        if not tasks:
            print("Your to-do list is empty!")
            return

        view_tasks()  # Show tasks first
        task_to_remove = input("Enter task number/name to remove: ")

        # Remove by index if input is a number
        if task_to_remove.isdigit():
            index = int(task_to_remove) - 1
            if 0 <= index < len(tasks):
                removed = tasks.pop(index)
                print(f"Removed: '{removed}'")
            else:
                print(f"Alert: Task number {task_to_remove} doesn't exist!")
            return

        # Remove by name if input is text
        if task_to_remove in tasks:
            tasks.remove(task_to_remove)
            print(f"Task '{task_to_remove}' has been removed.")
        else:
            print(f"Alert: Task '{task_to_remove}' does not exist!")

    # ---- Main Menu Loop ----
    menu_items = [
        "\n--- To-Do List Manager ---",
        "1. Add task",
        "2. View tasks",
        "3. Remove task",
        "4. Exit"
    ]

    # Display menu using list and a loop
    while True:
        for i in menu_items:
            print(i)

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_task()  
        elif choice == "2":
            view_tasks()  
        elif choice == "3":
            remove_task()  
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

# Start the program
to_do_list()