from datetime import datetime as dt
import json

tasks = []


def main():
    menu = """
========================================
            MY TO-DO LIST
========================================

1. Add task
2. View pending tasks
3. View completed tasks
4. Mark tasks
5. View all tasks
6. Edit task
7. Delete task
8. Save tasks
9. Exit
"""
    while True:
        print(menu)
        try:
            option = int(input("Choose an option: "))
            if option == 1:
                create_task()
            elif option == 2:
                view_pending()
            elif option == 3:
                view_completed()
            elif option == 4:
                mark_task(tasks)
            elif option == 5:
                view_tasks(tasks)
            elif option == 6:
                edit_task()
            elif option == 7:
                delete_task()
            elif option == 8:
                save_task()
            elif option == 9:
                print("Goodbye!")
                break
            else:
                print("Enter a valid option")

        except ValueError:
            print("Enter a valid option")


def create_task():
    while True:
        task_name = input("Task name: ").strip().capitalize()
        if len(task_name) < 1:
            print("Task name cannot be empty")
        else:
            break
    while True:
        priority = input("Priority:").strip().capitalize()
        if priority.lower() in ["high", "medium", "low"]:
            break
        print("Priority should be High, Medium or Low")
    while True:
        date = input("Enter Due Date in this format DD-MM-YYYY: ")

        try:
            dt.strptime(date, "%d-%m-%Y")
            break
        except ValueError:
            print("Date should be in this format DD-MM-YYYY")

    task = {
        "id": len(tasks) + 1,
        "task_name": task_name,
        "priority": priority,
        "date": date,
        "completed": False,
    }
    tasks.append(task)


def view_tasks(tasks_list):
    if len(tasks_list) == 0:
        print("No tasks found.")
    else:
        print("""
        ========================================
                    MY TO-DO LIST
        ========================================
        """)
        print(f"{'ID':<4}{'TASK':<22}{'PRIORITY':<12}{'DUE DATE':<13}{'STATUS':<11}")
        print("------------------------------------------------------------")
        for task in tasks_list:
            if task["completed"]:
                status = "Completed"
            else:
                status = "Pending"

            print(
                f"{task['id']:<4}{task['task_name']:<22}{task['priority']:<12}{task['date']:<13}{status:<11}"
            )


def complete_task(tasks):
    if tasks:
        while True:
            view_tasks(tasks)
            try:
                task_id = int(input("Please input task id: "))
                if task_id < 1 or task_id > len(tasks):
                    print("Please input a valid task ID.")
                else:
                    tasks[task_id - 1]["completed"] = True
                    print(f'Task "{tasks[task_id-1]["task_name"]}" marked as completed')
                    break
            except ValueError:
                print("Please input a valid task ID.")
    else:
        print("No tasks found.")


def delete_task():
    if tasks:
        while True:
            view_tasks(tasks)
            try:
                task_id = int(input("Please input the task ID you want to delete: "))
                if task_id < 1 or task_id > len(tasks):
                    print("Enter a valid task ID")
                else:
                    tasks.pop(task_id - 1)
                    print(f"Task deleted")
                    for index, task in enumerate(tasks, 1):
                        task["id"] = index
                    break
            except ValueError:
                print("Please input a valid task ID.")


def pending_task(tasks):
    if tasks:
        while True:
            view_tasks(tasks)
            try:
                task_id = int(input("Enter task ID: "))
                if task_id < 1 or task_id > len(tasks):
                    print("Please input a valid task ID.")
                else:
                    tasks[task_id - 1]["completed"] = False
                    print(f'Task "{tasks[task_id-1]["task_name"].capitalize()}" marked as pending')
                    break
            except ValueError:
                print("Enter a valid task ID.")
    else:
        print("No tasks found.")


def mark_task(tasks):
    print("1. Mark as completed\n2. Mark as pending")
    while True:
        try:
            choice = int(input("Choose option: "))
            if choice== 1:
                complete_task(tasks)
                break
            elif choice== 2:
                pending_task(tasks)
                break
            else:
                print("Please Enter option 1 or 2")
        except ValueError:
            print("Please Enter option 1 or 2")


def edit_task():
    print("Enter task ID to edit: ")
    view_tasks(tasks)
    while True:
        try:
            task_id = int(input("please enter task id to edit"))
            if task_id >= 1 and task_id <= len(tasks):
                break
            else:
                print("Please input a valid task ID.")
        except ValueError:
            print("Please input a valid task ID.")
    while True:
        print("""
                    Input 1 to change task name.
                    Input 2 to change its priority.
                    Input 3 to change its due date.""")
        try:
            option = int(input("Choose option: "))
            if option == 1:
                while True:
                    y = input("update task name: ").strip().capitalize()
                    if len(y) >= 1:
                        tasks[task_id - 1]["task_name"] = y
                        print("Task name updated successfully!")
                        break
                    else:
                        print("task name cannot be empty")
                break
            elif option == 2:
                while True:
                    x = input("Update task priority: ").strip().capitalize()
                    if x.lower() in ["low", "high", "medium"]:
                        tasks[task_id - 1]["priority"] = x
                        print("Priority updated successfully!")
                        break
                    else:
                        print("Priority must be low,medium or high")

                break
            elif option == 3:
                x = input("Enter Due Date in this format DD-MM-YYYY: ")

                try:
                    dt.strptime(x, "%d-%m-%Y")
                    tasks[task_id - 1]["date"] = x
                    print("Date updated successfully!")

                    break
                except ValueError:
                    print("Date should be in this format DD-MM-YYYY")
            else:
                print("Please input a valid task ID.")
        except ValueError:
            print("Please input a valid task ID.")


def view_pending():
    pending = []
    if len(tasks) > 0:
        for task in tasks:
            if task["completed"] == False:
                pending.append(task)
        if len(pending) > 0:
            view_tasks(pending)
        else:
            print("You dont have any pending tasks!")
    else:
        print("please add a task first")


def view_completed():
    completed = []
    if len(tasks) > 0:
        for task in tasks:
            if task["completed"] == True:
                completed.append(task)
        if len(completed) > 0:
            view_tasks(completed)
        else:
            print("You dont have any completed tasks!")
    else:
        print("Please add a task first")


def save_task():
    try:
        with open("tasks.json", "w") as file:
            json.dump(tasks, file)
            print("Saved successfully")
    except FileNotFoundError:
        print("File 'tasks.json'not found")
    load_task()


def load_task():
    try:
        with open("tasks.json", "r") as file:
            tasks.clear()
            tasks.extend(json.load(file))
    except FileNotFoundError:
        tasks.clear()


load_task()
main()
