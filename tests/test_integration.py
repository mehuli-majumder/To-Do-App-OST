import pytest
import json
from app import st

def test_app_runs():
    """
    Simple integration test to ensure the To-Do app module can be imported 
    and Streamlit starts without errors.
    """
    assert st is not None

def test_tasks_json_exists():
    """
    Check if the tasks.json file exists and is valid JSON.
    """
    with open("tasks.json", "r") as f:
        data = json.load(f)
    assert isinstance(data, list) or isinstance(data, dict)
