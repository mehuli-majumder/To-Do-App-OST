class Task:
    def __init__(self, description):
        self.description = description
        self.done = False

    def mark_done(self):
        self.done = True

    def __str__(self):
        status = "✓" if self.done else "✗"
        return f"[{status}] {self.description}"


tasks = []

def add_task(description):
    task = Task(description)
    tasks.append(task)
    return task

def view_tasks():
    if not tasks:
        return "No tasks available."
    return "\n".join([f"{i+1}. {task}" for i, task in enumerate(tasks)])

def mark_done(index):
    if 0 <= index < len(tasks):
        tasks[index].mark_done()
        return True
    return False

def delete_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
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
