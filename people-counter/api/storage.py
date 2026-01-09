import json
import threading
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_FILE = os.path.join(BASE_DIR, "..", "tasks.json")

lock = threading.Lock()


def load():
    try:
        with open(DB_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=2)


def save_task(task_id, **kwargs):
    with lock:
        data = load()
        data[task_id] = kwargs
        save(data)


def update_task(task_id, **kwargs):
    with lock:
        data = load()
        if task_id in data:
            data[task_id].update(kwargs)
            save(data)


def get_task(task_id):
    return load().get(task_id)
