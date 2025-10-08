# To-Do App (CLI & Web UI)

![To-Do App Banner](https://placehold.co/1200x300/6366f1/FFFFFF?text=To-Do%20App&font=lato)

A versatile and feature-rich To-Do application that runs both as a command-line interface (CLI) and as an interactive web application using Streamlit. This project demonstrates core Python principles, project structuring, testing, and a full development workflow.

## Features

- **Dual Interfaces**: Run the app in your terminal or in your browser.
- **Task Persistence**: Tasks are automatically saved to a \`tasks.json\` file, so you never lose your data.
- **Task Properties**: Add tasks with descriptions, priority levels (High, Medium, Low), and optional due dates.
- **Full CRUD Functionality**: Create, view, mark as done, and delete tasks.
- **Advanced Management**:
  - **Search**: Quickly find tasks by keyword.
  - **Bulk Delete**: Clear all completed tasks with a single command.
  - **Smart Sorting**: Tasks are automatically sorted by priority and then by due date.
- **Ready for Collaboration**: Includes clear contribution guidelines.
- **Automated Setup**: A \`setup.py\` script creates a virtual environment and installs all dependencies for you.
- **Tested**: Unit tests are included to ensure core logic is reliable.

## Project Structure

\`\`\`
To-Do-App-OST/
│
├── .gitignore
├── app.py                  # Streamlit Web App entry point
├── CONTRIBUTING.md         # Guidelines for contributors
├── README.md               # This file
├── requirements.txt        # Project dependencies
├── setup.py                # Automated setup script
├── tasks.json              # Database file for storing tasks
│
├── src/
│   ├── main.py             # CLI App entry point
│   └── todo.py             # Core application logic and Task class
│
└── tests/
    └── test_todo.py        # Unit tests for the core logic
\`\`\`

## Installation & Setup

This project includes a setup script to automate the entire installation process.

1.  **Clone the repository:**
    \`\`\`bash
    git clone https://github.com/mehuli-majumder/To-Do-App-OST.git
    cd To-To-App-OST
    \`\`\`

2.  **Run the setup script:**
    This will create a virtual environment, install all required packages from \`requirements.txt\`, and run tests to verify the installation.
    \`\`\`bash
    python setup.py
    \`\`\`

## Usage

After running the setup script, you must first activate the virtual environment.

- **On Windows:**
  \`\`\`cmd
  .venv\\Scripts\\activate
  \`\`\`
- **On macOS/Linux:**
  \`\`\`bash
  source .venv/bin/activate
  \`\`\`

Once the environment is active, you can run either the Web App or the CLI.

### Running the Web App

To launch the interactive Streamlit interface, run:
\`\`\`bash
streamlit run app.py
\`\`\`
Your browser will automatically open with the application.

### Running the Command-Line Interface (CLI)

To use the app directly in your terminal, run:
\`\`\`bash
python src/main.py
\`\`\`

## Running Tests

To run the unit tests manually, activate the virtual environment and run \`pytest\`:
\`\`\`bash
pytest
\`\`\`

## Contributing

Contributions are welcome! Please read the [CONTRIBUTING.md](CONTRIBUTING.md) file for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License.
