import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))
import streamlit as st
from todo import Task 

# Set the page title and icon
st.set_page_config(page_title="To-Do App", page_icon="✅")

# --- App Title ---
st.title("Streamlit To-Do App")
st.write("A simple and interactive app to manage your daily tasks.")

# --- Initialize Session State ---
# 'st.session_state' is a dictionary-like object that persists across reruns.
# We initialize the 'tasks' list here if it doesn't already exist.
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

# --- Functions to Interact with State ---
# These functions modify the list of tasks stored in the session state.

def add_task_to_state(description):
    """Adds a new task object to the session state list."""
    if description:  # Ensure the description is not empty
        st.session_state.tasks.append(Task(description))
        st.toast("✨ Task added!", icon="🎉")

def delete_task_from_state(index):
    """Deletes a task from the session state list by its index."""
    if 0 <= index < len(st.session_state.tasks):
        st.session_state.tasks.pop(index)
        st.toast("Task deleted!", icon="🗑️")

def mark_task_done_in_state(index):
    """Marks a task in the session state as done."""
    if 0 <= index < len(st.session_state.tasks):
        st.session_state.tasks[index].mark_done()
        st.toast("Great job!", icon="👍")


# --- Task Input Form ---
st.header("Add a New Task", divider="rainbow")
with st.form("new_task_form", clear_on_submit=True):
    new_task_description = st.text_input("Task Description", placeholder="e.g., Buy groceries")
    submit_button = st.form_submit_button("Add Task")

    if submit_button:
        add_task_to_state(new_task_description)


# --- Display Tasks ---
st.header("Your Tasks", divider="rainbow")

if not st.session_state.tasks:
    st.info("You have no pending tasks. Add one above! 🚀")
else:
    # Create columns for a cleaner layout
    col1, col2, col3 = st.columns([0.6, 0.2, 0.2]) # Ratio of column widths

    with col1:
        st.write("**Task**")
    with col2:
        st.write("**Mark Done**")
    with col3:
        st.write("**Delete**")
        
    st.markdown("---") # Visual separator

    # Loop through tasks and display them with buttons
    for i, task in enumerate(st.session_state.tasks):
        col1, col2, col3 = st.columns([0.6, 0.2, 0.2])
        
        with col1:
            # Display the task with its status icon
            status_icon = "✅" if task.done else "⏳"
            st.markdown(f"**{i+1}.** {status_icon} {task.description}")

        with col2:
            # The 'disabled' param prevents marking a completed task again
            if st.button("Done", key=f"done_{i}", disabled=task.done, use_container_width=True):
                mark_task_done_in_state(i)
                st.rerun() # Rerun the script to immediately reflect the change

        with col3:
            if st.button("Delete", key=f"delete_{i}", type="primary", use_container_width=True):
                delete_task_from_state(i)
                st.rerun() # Rerun to update the list
