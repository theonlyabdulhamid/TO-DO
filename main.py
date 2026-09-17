tasks = []
def main():
    menu="""
========================================
            MY TO-DO LIST
========================================

1. Add task
2. View pending tasks
3. View completed tasks
4. Complete task
5. Edit task
6. Delete task
7. Save tasks
8. Exit
"""
    while True:
        print(menu)
        option= int(input("Choose an option: "))
         



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
    date = input("Enter Due Date: ")

    task = {
        "id": len(tasks) + 1,
        "task_name": task_name,
        "priority": priority,
        "date": date,
        "completed": False,
    }
    tasks.append(task)


def view_tasks():
    if len(tasks) == 0:
        print("No tasks found.")
    else:
        print("""
        ========================================
                    MY TO-DO LIST
        ========================================
        """)
        print(f"{'ID':<4}{'TASK':<22}{'PRIORITY':<12}{'DUE DATE':<13}{'STATUS':<11}")
        print("------------------------------------------------------------")
        for task in tasks:
            if task["completed"]:
                status = "Completed"
            else:
                status = "Pending"

            print(
                f"{task['id']:<4}{task['task_name']:<22}{task['priority']:<12}{task['date']:<13}{status:<11}"
            )


def complete_task():
    if tasks:
        while True:
            view_tasks()
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
            view_tasks()
            try:
                task_id = int(input("Please input the tax id you want to delete: "))
                if task_id < 1 or task_id > len(tasks):
                    print("Enter a valid tax id")
                else:
                    tasks.pop(task_id - 1)
                    print(f"Task deleted")
                    for index, task in enumerate(tasks, 1):
                        task["id"] = index
                    break
            except ValueError:
                print("Please input a valid task ID.")


def edit_task():
    print("Enter task id to edit: ")
    view_tasks()
    while True:
        try:
            task_id = int(input("please enter tax id to edit"))
            if task_id >= 1 and task_id <= len(tasks):
                break
            else:
                print(
                    "Please input a valid task ID."
                )
        except ValueError:
            print(
                "Please input a valid task ID."
            )
    while True:
        print("""
                    Input 1 to change task name.
                    Input 2 to change its priority.
                    Input 3 to change its due date.""")
        try:
            option = int(input("Choose option: "))
            if option == 1:
                while True:
                    y= input("update task name: "). strip().capitalize()
                    if len(y)>=1:
                        tasks[task_id - 1]["task_name"] =y
                        break
                    else:
                        print("task name cannot be empty")
                break
            elif option == 2:
                while True:
                    x= input("update task priority: ").strip().capitalize()
                    if x.lower() in ["low","high","medium"]:
                        tasks[task_id - 1]["priority"] =x
                        break
                    else:
                        print("priority must be low,medium or high")

                break
            elif option == 3:
                tasks[task_id - 1]["date"] = input("update task date")
                break
            else:
                print(
                    "Please input a valid task ID."
                )
        except ValueError:
            print(
                "Please input a valid task ID."
            )