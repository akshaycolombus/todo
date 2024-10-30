import json
import os

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
    save_tasks(tasks)
    print("Task added!")


def view_task():
    tasks = load_tasks
    if not tasks:
        print("No tasks found.")
    else:
        print("Your tasks: ")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

