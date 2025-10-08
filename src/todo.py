import json
from datetime import datetime

# --- Constants ---
FILE_PATH = "tasks.json"
PRIORITY_ORDER = {"High": 0, "Medium": 1, "Low": 2}

# --- Task Class ---
class Task:
    def __init__(self, description, priority="Medium", due_date=None, done=False):
        self.description = description
        self.done = done
        self.priority = priority

        # MODIFIED: Ensure due_date is always a `date` object for consistent comparison
        if isinstance(due_date, datetime):
            # If it's a datetime object (from strptime), convert it to a date object
            self.due_date = due_date.date()
        else:
            # It's either already a date object (from streamlit) or None
            self.due_date = due_date

    def mark_done(self):
        self.done = True

    def __str__(self):
        status = "✔️" if self.done else "❌"
        priority_map = {"High": "H", "Medium": "M", "Low": "L"}
        p_str = f"[{priority_map.get(self.priority, 'M')}]"
        d_str = f"(Due: {self.due_date.strftime('%Y-%m-%d')})" if self.due_date else ""
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
        due_date_str = data.get("due_date")
        due_date = datetime.strptime(due_date_str, "%Y-%m-%d") if due_date_str else None
        return cls(
            description=data.get("description"),
            priority=data.get("priority", "Medium"),
            due_date=due_date,
            done=data.get("done", False)
        )

# --- Helper Functions ---
def _get_sorted_tasks():
    """Returns a new list of tasks sorted by priority and due date."""
    # The `or datetime.max` ensures tasks without due dates are last
    return sorted(
        tasks,
        key=lambda t: (PRIORITY_ORDER.get(t.priority, 1), t.due_date or datetime.max.date())
    )

# --- Persistence Functions ---
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

# --- Global Task List ---
tasks = load_tasks()

# --- Core Functions ---
def add_task(description, priority="Medium", due_date=None):
    task = Task(description, priority, due_date)
    tasks.append(task)
    save_tasks()
    return task

def view_tasks():
    if not tasks:
        return "No tasks available."
    sorted_tasks = _get_sorted_tasks()
    return "\n".join([f"{i+1}. {task}" for i, task in enumerate(sorted_tasks)])

def mark_done(index):
    sorted_tasks = _get_sorted_tasks()
    if 0 <= index < len(sorted_tasks):
        # Find the original task object in the unsorted list and mark it done
        task_to_mark = sorted_tasks[index]
        task_to_mark.mark_done()
        save_tasks()
        return True
    return False

def delete_task(index):
    sorted_tasks = _get_sorted_tasks()
    if 0 <= index < len(sorted_tasks):
        task_to_delete = sorted_tasks[index]
        tasks.remove(task_to_delete)
        save_tasks()
        return True
    return False
