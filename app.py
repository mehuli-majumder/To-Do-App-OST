import streamlit as st
from datetime import datetime
from src.todo import mark_done, delete_task, load_tasks, save_tasks

# Set page config at the very top
st.set_page_config(page_title="To-Do App", page_icon="✅")

# --- App Title ---
st.title("✅ To-Do App")
st.write("Manage your tasks with priorities and due dates!")

# --- Initialize State ---
# Load tasks from the file into the session state once on first run
if 'tasks' not in st.session_state:
    st.session_state.tasks = load_tasks()

# --- Callback Functions for Buttons ---
# Using callbacks is the recommended way to handle state with buttons in Streamlit
def handle_mark_done(task_index):
    """Callback to mark a task as done."""
    if mark_done(task_index):
        # Reload tasks from the file to refresh the state
        st.session_state.tasks = load_tasks()
    else:
        st.error("Could not mark task as done.")

def handle_delete_task(task_index):
    """Callback to delete a task."""
    if delete_task(task_index):
        st.session_state.tasks = load_tasks()
    else:
        st.error("Could not delete task.")

def handle_add_task():
    """Callback to add a new task from the form."""
    # Read values from the form widgets stored in session state
    desc = st.session_state.new_task_desc
    priority = st.session_state.new_task_priority
    due_date = st.session_state.new_task_due_date
    
    if desc:
        from src.todo import add_task # Import here to avoid circular dependency issues
        add_task(desc, priority, due_date)
        st.session_state.tasks = load_tasks()
        st.toast("✨ Task added!", icon="🎉")
        # Clear the input widgets
        st.session_state.new_task_desc = ""
        st.session_state.new_task_due_date = None


# --- Task Input Form ---
st.header("Add a New Task", divider="rainbow")
with st.form("new_task_form"):
    st.text_input("Task Description", placeholder="e.g., Finish PBL project", key="new_task_desc")
    
    col1, col2 = st.columns(2)
    with col1:
        st.selectbox("Priority", ["High", "Medium", "Low"], key="new_task_priority")
    with col2:
        st.date_input("Due Date (Optional)", value=None, key="new_task_due_date")
    
    # When this button is pressed, the form is submitted and the callback runs
    st.form_submit_button("Add Task", on_click=handle_add_task)


# --- Display Tasks ---
st.header("Your Tasks", divider="rainbow")

# MODIFIED: Get the sorted list of task objects to display
priority_order = {"High": 0, "Medium": 1, "Low": 2}
# Use the task list from the session state
sorted_tasks = sorted(
    st.session_state.tasks,
    key=lambda t: (priority_order.get(t.priority, 1), t.due_date or datetime.max.date())
)

if not sorted_tasks:
    st.info("You have no pending tasks. Add one above! 🚀")
else:
    # MODIFIED: Iterate through the sorted tasks and display them with interactive buttons
    for i, task in enumerate(sorted_tasks):
        col1, col2, col3 = st.columns([0.7, 0.15, 0.15])
        
        with col1:
            # NEW: Use the desired emojis for status
            status_emoji = "✔️" if task.done else "❌"
            priority_map = {"High": "[H]", "Medium": "[M]", "Low": "[L]"}
            p_str = priority_map.get(task.priority, "[M]")
            d_str = f"(Due: {task.due_date.strftime('%Y-%m-%d')})" if task.due_date else ""
            
            # Display the task using markdown for a nice look
            st.markdown(f"**{i+1}. {status_emoji} {p_str}** {task.description} *{d_str}*")

        with col2:
            st.button(
                "Done",
                key=f"done_{i}",
                on_click=handle_mark_done,
                args=(i,), # Pass the sorted index to the callback
                disabled=task.done,
                use_container_width=True
            )

        with col3:
            st.button(
                "Delete",
                key=f"delete_{i}",
                on_click=handle_delete_task,
                args=(i,), # Pass the sorted index to the callback
                type="primary",
                use_container_width=True
            )