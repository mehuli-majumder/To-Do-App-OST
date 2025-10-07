import unittest
from src.todo import add_task, view_tasks, mark_done, delete_task, tasks

class TestTodoApp(unittest.TestCase):

    def setUp(self):
        tasks.clear()

    def test_add_task(self):
        add_task("Test task")
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].description, "Test task")

    def test_mark_done(self):
        add_task("Task 1")
        result = mark_done(0)
        self.assertTrue(result)
        self.assertTrue(tasks[0].done)

    def test_delete_task(self):
        add_task("Task 1")
        result = delete_task(0)
        self.assertTrue(result)
        self.assertEqual(len(tasks), 0)

    def test_view_tasks_empty(self):
        self.assertEqual(view_tasks(), "No tasks available.")

if __name__ == "__main__":
    unittest.main()
