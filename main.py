import json
import os
from db import connect
import psycopg2

def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            return json.load(file)
    return []


def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks,file, indent=4)



def add_task():
    task = input("Enter a new task: ")
    tasks = load_tasks()
    tasks.append(task)
    print("Task added!")
    save_tasks(tasks)
    print("Task saved to file")
    


def view_task():
    conn = connect()
    tasks = load_tasks()
    try:
        with conn.cursor() as cur:
            cur.execute("select tsk.id, tsk.task_desc from tasks tsk ORDER BY tsk.id asc")
            tasks = cur.fetchall()
            if tasks:
                print("Your Tasks: ")
                for task in task:
                    print(task)
                    # status = "✔" if task[2] else "✘"
                    print(f"{task[0]}. {task[1]}")
                    # print(f"{task[0]}. {task[1]} [{status}]")
            
            else:
                print("No tasks found.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error retrieving tasks: {error}")   
    finally:
        conn.close()
    
    # if not tasks:
    #     print("No tasks found.")
    # else:
    #     print("Your tasks: ")
    #     for idx, task in enumerate(tasks, 1):
    #         print(f"{idx}. {task}")


def remove_task():
    tasks = load_tasks()
    view_task()
    try: 
        task_num = int(input("Enter the task number to remove: ")) - 1
        if 0 <=  task_num <= len(tasks):
            removed_task = tasks.pop(task_num)
            save_tasks(tasks)
            print(f"Removed task: {removed_task}")
        else: 
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def update_task():
    tasks = load_tasks()
    view_task()

    task_num = int(input("Which task would you like to update: "))
    if 0 <= task_num - 1 <= len(tasks):
        new_task = input("Enter new Task: ")
        tasks[task_num - 1] = new_task
        print(f'Task {task_num} is updated to "{new_task}"')
        save_tasks(tasks)



def main():
    while True:
        print("\nTo-do List Menu:")
        print("1. View Tasks")
        print("2. Add Tasks")
        print("3. Remove Tasks")
        print("4. Update Tasks")
        print("5. Exit")

        choice = int(input("Choose an option: "))

        match choice:
            case 1:
                view_task()
            case 2:
                add_task()
            case 3:
                remove_task()
            case 4:
                update_task()
                # print("update task")
            case 5: 
                print("Goodbye!")
                break
            case _:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

