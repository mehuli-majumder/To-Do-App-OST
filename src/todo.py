import json
from datetime import datetime

FILE_PATH = "tasks.json"

class Task:
    def __init__(self, description, priority="Medium", due_date=None, done=False):
        self.description = description
        self.done = done
        self.priority = priority
        if isinstance(due_date, str):
            self.due_date = datetime.strptime(due_date, "%Y-%m-%d")
        else:
            self.due_date = due_date

    def mark_done(self):
        self.done = True

    def __str__(self):
        # MODIFIED: Use the new emojis for the CLI status
        status = "✔️" if self.done else "❌"
        priority_map = {"High": "H", "Medium": "M", "Low": "L"}
        p_str = f"[{priority_map.get(self.priority, 'M')}]"
        d_str = f"(Due: {self.due_date.strftime('%Y-%m-%d')})" if self.due_date else ""
        # The string now includes the status emoji, priority, description, and due date
        return f"{status} {p_str} {self.description} {d_str}"

    def to_dict(self):
        return {
            "description": self.description,
            "done": self.done,
            "priority": self.priority,
            "due_date": self.due_date.strftime("%Y-%m-%d") if self.due_date else None,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            description=data.get("description"),
            priority=data.get("priority", "Medium"),
            due_date=data.get("due_date"),
            done=data.get("done", False)
        )

def load_tasks():
    try:
        with open(FILE_PATH, 'r') as f:
            tasks_data = json.load(f)
            return [Task.from_dict(data) for data in tasks_data]
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks():
    with open(FILE_PATH, 'w') as f:
        tasks_data = [task.to_dict() for task in tasks]
        json.dump(tasks_data, f, indent=4)

tasks = load_tasks()

def add_task(description, priority="Medium", due_date=None):
    task = Task(description, priority, due_date)
    tasks.append(task)
    save_tasks()
    return task

def view_tasks():
    if not tasks:
        return "No tasks available."
    priority_order = {"High": 0, "Medium": 1, "Low": 2}
    sorted_tasks = sorted(
        tasks,
        key=lambda t: (priority_order.get(t.priority, 1), t.due_date or datetime.max.date())
    )
    # The output will now use the new emoji format from __str__
    return "\n".join([f"{i+1}. {task}" for i, task in enumerate(sorted_tasks)])

def mark_done(index):
    priority_order = {"High": 0, "Medium": 1, "Low": 2}
    sorted_tasks = sorted(
        tasks,
        key=lambda t: (priority_order.get(t.priority, 1), t.due_date or datetime.max.date())
    )
    if 0 <= index < len(sorted_tasks):
        sorted_tasks[index].mark_done()
        save_tasks()
        return True
    return False

def delete_task(index):
    priority_order = {"High": 0, "Medium": 1, "Low": 2}
    sorted_tasks = sorted(
        tasks,
        key=lambda t: (priority_order.get(t.priority, 1), t.due_date or datetime.max.date())
    )
    if 0 <= index < len(sorted_tasks):
        task_to_delete = sorted_tasks[index]
        tasks.remove(task_to_delete)
        save_tasks()
        return True
    return False

def delete_completed_tasks():
    global tasks
    tasks = [task for task in tasks if not task.done]
    return True

def search_tasks(keyword):
    keyword = keyword.lower()
    matching = [task for task in tasks if keyword in task.description.lower()]

    if not matching:
        return "No matching tasks found."

    return "\n".join([f"{i+1}. {task}" for i, task in enumerate(matching)])
