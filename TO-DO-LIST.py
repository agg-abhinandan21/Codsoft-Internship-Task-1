import json
import os

FILE_NAME = "todo_list.json"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)

def show_tasks(tasks):
    if not tasks:
        print("No tasks found!")
    for i, task in enumerate(tasks):
        status = "✓" if task["done"] else "✗"
        print(f"{i + 1}. [{status}] {task['task']}")

def add_task(tasks):
    task_name = input("Enter task: ")
    tasks.append({"task": task_name, "done": False})

def complete_task(tasks):
    show_tasks(tasks)
    task_no = int(input("Enter task number to mark complete: ")) - 1
    if 0 <= task_no < len(tasks):
        tasks[task_no]["done"] = True

def delete_task(tasks):
    show_tasks(tasks)
    task_no = int(input("Enter task number to delete: ")) - 1
    if 0 <= task_no < len(tasks):
        tasks.pop(task_no)

def main():
    tasks = load_tasks()
    while True:
        print("\n--- TO-DO LIST ---")
        print("1. View Tasks\n2. Add Task\n3. Complete Task\n4. Delete Task\n5. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
