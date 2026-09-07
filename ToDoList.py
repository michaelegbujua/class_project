class ToDoList:
    #the self function (oop)
    def __init__(self):
        """Initialize the to-do list with empty tasks and menu items"""
        self.tasks = []
        self.menu_items = [
            "\n --- To Do List Manager ---",
            "1. Add task",
            "2. View tasks",
            "3. Remove task",
            "4. Exit"
        ]

    #allows user to add new tasks 
    def add_task(self):
        """Add a new task to the list"""
        task = input('Enter task to add: ')
        self.tasks.append(task)
        print(f"Task '{task}' added!")

    #allows user view currently added tasks
    def view_tasks(self):
        """Display all current tasks"""
        if not self.tasks:
            print("Your to-do list is empty")
        else:
            print("\n-- Current Tasks ---")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")

    #allow user remove tasks (either by index or name text)
    def remove_task(self):
        """Remove a task by index or name"""
        if not self.tasks:
            print("Your to-do list is empty!")
            return

        #show current tasks first
        self.view_tasks()
        task_to_remove = input("Enter task number to remove:")

        #remove by index if input is a number
        if task_to_remove.isdigit():
            index = int(task_to_remove) - 1
            if 0 <= index < len(self.tasks):
                removed = self.tasks.pop(index)
                print(f"Removed: '{removed}'")
            else:
                print(f"Alert: Task number {task_to_remove} doesn't exist!")
            return

        #when user enters text as  input
        if task_to_remove in self.tasks:
            self.tasks.remove(task_to_remove)
            print(f"Task '{task_to_remove}' does not exist !")


    #allow user display menu
    def display_menu(self):
        """Display the menu options"""
        for item in self.menu_items:
            print(item)

    
    #to run the program
    def run(self):
        """Main program loop to handle user input"""
        while True:
            self.display_menu()
            choice = input("\nEnter your Choice (1-4): ")

            #conditional logic for choice
            if choice  == "1":
                self.add_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.remove_task()
            elif choice == "4":
                print("Goodbye !!")
                break
            else:
                print("Invalid Choice. Try Again!!")

           

#create and run the app
if __name__ == "__main__":
    app = ToDoList()
    app.run()

            






        