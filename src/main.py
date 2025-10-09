# This version includes all necessary imports
from datetime import datetime
from todo import add_task, view_tasks, mark_done, delete_task, delete_completed_tasks, search_tasks

def menu():
    while True:
        print("\n--- TO-DO APP ---")
        # This is the full menu with all features
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Delete All Completed Tasks")
        print("6. Search Tasks")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            desc = input("Enter task description: ")
            priority = input("Enter priority (High, Medium, Low) [Medium]: ") or "Medium"
            due_date_str = input("Enter due date (YYYY-MM-DD) [Optional]: ")
            due_date = None
            if due_date_str:
                try:
                    due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
                except ValueError:
                    print("⚠️ Invalid date format. Task added without a due date.")
            
            add_task(desc, priority, due_date)
            print("✅ Task added!")

        elif choice == "2":
            print("\n--- Your Tasks ---")
            print(view_tasks())
            print("--------------------")

        elif choice == "3":
            try:
                idx = int(input("Enter task number to mark as done: ")) - 1
                if mark_done(idx):
                    print("✅ Task marked as done!")
                else:
                    print("⚠️ Invalid task number.")
            except ValueError:
                print("⚠️ Please enter a valid number.")

        elif choice == "4":
            try:
                idx = int(input("Enter task number to delete: ")) - 1
                if delete_task(idx):
                    print("🗑️ Task deleted!")
                else:
                    print("⚠️ Invalid task number.")
            except ValueError:
                print("⚠️ Please enter a valid number.")
        
        elif choice == "5":
            delete_completed_tasks()
            print("🧹 All completed tasks have been deleted!")
        
        # This is the "Search" feature from the incoming changes
        elif choice == "6":
            keyword = input("Enter keyword to search: ")
            print("\nMatching Tasks:")
            print(search_tasks(keyword))
        
        # This is the "Exit" option, correctly numbered, from the incoming changes
        elif choice == "7":
            print("👋 Goodbye!")
            break

        else:
            print("⚠️ Invalid choice, try again.")


if __name__ == "__main__":
    menu()