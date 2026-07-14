import json
import os
from datetime import datetime

DATA_FILE = os.path.join(os.path.dirname(__file__), "tasks.json")


# Loads all tasks from the JSON file and returns them as a list
def _load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)


# Saves the list of tasks to the JSON file
def _save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


# Returns all tasks, sorted so incomplete tasks come first, then by creation date
def fetch_tasks():
    tasks = _load_tasks()
    # Sort by is_done first (False < True, so incomplete tasks appear first),
    # then by created_at so older tasks come before newer ones
    tasks.sort(key=lambda t: (t["is_done"], t["created_at"]))
    return tasks


# Adds a new task with the given title and saves it to the file
def add_task(title):
    tasks = _load_tasks()
    next_id = max((t["id"] for t in tasks), default=0) + 1
    task = {
        "id": next_id,
        "title": title,
        "is_done": False,
        "created_at": datetime.now().isoformat(),
    }
    tasks.append(task)
    _save_tasks(tasks)
    return task


# Toggles a task between done and not done, then saves the change
def toggle_task(task_id):
    tasks = _load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["is_done"] = not task["is_done"]
            break
    _save_tasks(tasks)


# Removes a task by its ID and saves the updated list
def delete_task(task_id):
    tasks = _load_tasks()
    tasks = [t for t in tasks if t["id"] != task_id]
    _save_tasks(tasks)
