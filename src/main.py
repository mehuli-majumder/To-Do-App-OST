from todo import add_task, view_tasks, mark_done, delete_task, delete_completed_tasks

def menu():
    while True:
        print("\n--- TO-DO APP ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Delete All Completed Tasks")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            desc = input("Enter task description: ")
            add_task(desc)
            print("✅ Task added!")

        elif choice == "2":
            print("\nTasks:")
            print(view_tasks())

        elif choice == "3":
            idx = int(input("Enter task number to mark as done: ")) - 1
            if mark_done(idx):
                print("✅ Task marked as done!")
            else:
                print("⚠️ Invalid task number.")

        elif choice == "4":
            idx = int(input("Enter task number to delete: ")) - 1
            if delete_task(idx):
                print("🗑 Task deleted!")
            else:
                print("⚠️ Invalid task number.")

        elif choice == "5":
            delete_completed_tasks()

        elif choice == "6":
            print("👋 Goodbye!")
            break

        else:
            print("⚠️ Invalid choice, try again.")


if __name__ == "__main__":
    menu()
