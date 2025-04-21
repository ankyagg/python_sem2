# Task Manager Program with User-Specified Priority
tasks = []

def add_task(task_name, priority):
    tasks.append((task_name, priority))
    print(f"Task '{task_name}' with priority '{priority}' added.")

def remove_task(task_name):
    for task in tasks:
        if task[0] == task_name:
            tasks.remove(task)
            print(f"Task '{task_name}' removed.")
            return
    print(f"Task '{task_name}' not found.")

def update_task(task_name, new_priority):
    for task in tasks:
        if task[0] == task_name:
            tasks[tasks.index(task)] = (task_name, new_priority)
            print(f"Task '{task_name}' updated to priority '{new_priority}'.")
            return
    print(f"Task '{task_name}' not found.")

def display_tasks():
    if tasks:
        print("Task List:")
        for task, priority in tasks:
            print(f"- {task}: {priority}")
    else:
        print("No tasks available.")

# Main menu
while True:
    print("\n1. Add Task")
    print("2. Remove Task")
    print("3. Update Task Priority")
    print("4. Display Tasks")
    print("5. Exit")
    
    choice = input("Choose an option: ")
    
    if choice == '1':
        task_name = input("Enter task name: ")
        priority = input("Enter priority (High, Medium, Low): ")
        add_task(task_name, priority)
    elif choice == '2':
        task_name = input("Enter task name to remove: ")
        remove_task(task_name)
    elif choice == '3':
        task_name = input("Enter task name to update: ")
        new_priority = input("Enter new priority (High, Medium, Low): ")
        update_task(task_name, new_priority)
    elif choice == '4':
        display_tasks()
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")
