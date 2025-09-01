'''
3. To-Do List Manager Concepts: File handling, functions, CRUD operations, menus
'''

# Step 1: Create a file (tasks.txt) to store tasks
#   - Each task will have: ID, description, status (pending/completed)

# Step 2: Define functions for CRUD operations
#   - add_task()
#   - edit_task()
#   - delete_task()
#   - view_tasks()
#   - mark_task_complete()
tasks = []

# Step 3: Load tasks from file
def load_tasks():
    try:
        with open(r"tasks.txt", "r") as file:
            for line in file:
                tid, desc, status = line.strip().split(",")
                tasks.append([int(tid), desc, status])
    except FileNotFoundError:
        pass  # First run, file may not exist

# Step 4: Save tasks to file
def save_tasks():
    with open(r"C:\Users\Neeraj Bhardwaj\Desktop\Python Projects\Projects\Python\3. To-Do List Manager\tasks.txt", "w") as file:
        for task in tasks:
            file.write(f"{task[0]},{task[1]},{task[2]}\n")

# Step 5: Add task
def add_task():
    desc = input("Enter Task Description: ")
    tid = len(tasks) + 1
    tasks.append([tid, desc, "Pending"])
    print("✅ Task added!")

# Step 6: Edit task
def edit_task():
    try:
        tid = int(input("Enter Task ID to edit: "))
        for task in tasks:
            if task[0] == tid:
                task[1] = input("Enter new description: ")
                task[2] = input("Enter new status (Pending/Completed): ")
                print("✏️ Task updated!")
                return
        print("❌ Task not found.")
    except ValueError:
        print("Invalid ID.")

# Step 7: Delete task
def delete_task():
    try:
        tid = int(input("Enter Task ID to delete: "))
        for task in tasks:
            if task[0] == tid:
                tasks.remove(task)
                print("🗑️ Task deleted!")
                return
        print("❌ Task not found.")
    except ValueError:
        print("Invalid ID.")

# Step 8: View tasks
def view_tasks():
    if tasks:
        print("\nID  Description         Status")
        print("--  -----------------   --------")
        for task in tasks:
            print(f"{task[0]:<3} {task[1]:<18} {task[2]:<10}")
    else:
        print("📭 No tasks available.")

# Step 9: Mark task complete
def mark_task_complete():
    try:
        tid = int(input("Enter Task ID to mark complete: "))
        for task in tasks:
            if task[0] == tid:
                task[2] = "Completed"
                print("✅ Task marked as completed!")
                return
        print("❌ Task not found.")
    except ValueError:
        print("Invalid ID.")

# Step 10: Menu loop
def main():
    load_tasks()
    while True:
        print("\n" + "="*25)
        print("       TO-DO LIST       ")
        print("="*25)
        print("1. Add Task")
        print("2. Edit Task")
        print("3. Delete Task")
        print("4. View Tasks")
        print("5. Mark Task Complete")
        print("6. Exit")
        print("="*25)

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("❌ Invalid input, enter a number 1-6.")
            continue

        if choice == 1:
            add_task()
        elif choice == 2:
            edit_task()
        elif choice == 3:
            delete_task()
        elif choice == 4:
            view_tasks()
        elif choice == 5:
            mark_task_complete()
        elif choice == 6:
            save_tasks()
            print("👋 Goodbye!")
            break
        else:
            print("Enter a number between 1-6.")

        save_tasks()  # Save after each operation

# Run program
if __name__ == "__main__":
    main()
