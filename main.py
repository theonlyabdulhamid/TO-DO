tasks = []


def create_task():
    while True:
        task_name = input("Task name: ").strip().capitalize()
        if len(task_name)<1:
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
    if len(tasks)==0:
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
                 status="Completed"
            else:
                 status="Pending"
                 
            print(f"{task['id']:<4}{task['task_name']:<22}{task['priority']:<12}{task['date']:<13}{status:<11}")
def complete_task():
    if tasks:
        while True: 
            view_tasks()
            try:
                task_id=int(input("Please input task id: "))
                if task_id<1 or task_id>len(tasks):
                 print('Please input a valid id number')
                else:
                    tasks[task_id-1]['completed']=True
                    print(f'Task "{tasks[task_id-1]["task_name"]}" marked as completed')
                    break
            except ValueError:
                print('Please input a valid id number')
    else:
        print("No tasks found.")
def delete_task():
    if tasks:
        while True:
            view_tasks()
            try:
                task_id= int(input("Please input the tax id you want to delete: "))
            except ValueError:
                print("Please enter a valid tax id")
create_task()
create_task()
complete_task()
view_tasks()