# To-Do-App-OST

A versatile, feature-rich **To-Do application** that runs both as a **command-line interface (CLI)** and an interactive **web application** using **Streamlit**. This project demonstrates core Python principles, organized project structure, testing, and a thorough development workflow.

***

## Features

- **Dual Interfaces:** Use the app in your terminal or in your browser.
- **Task Persistence:** Tasks are automatically saved to `tasks.json`.
- **Rich Task Properties:** Add descriptions, set priority levels (**High**, **Medium**, **Low**), and optional due dates.
- **Complete Management:** Create, view, mark as done, and delete tasks.
- **Advanced Functionality:**
    - 🔍 **Search** tasks by keyword.
    - 🗑️ **Bulk Delete**: Clear all completed tasks at once.
    - 🧠 **Smart Sorting:** Automatic sort by priority, then due date.
- **Collaboration Ready:** Clear contribution guidelines included.
- **Automated Setup:** `setup.py` creates a virtual environment and installs dependencies.
- **Tested:** Includes unit tests for core logic.

***

## Project Structure

```plaintext
To-Do-App-OST/
│
├── .gitignore
├── app.py                # Streamlit Web App entry point
├── CONTRIBUTING.md       # Guidelines for contributors
├── README.md             # This file
├── requirements.txt      # Project dependencies
├── setup.py              # Automated setup script
├── tasks.json            # Database for storing tasks
│
├── src/
│   ├── main.py           # CLI App entry point
│   └── todo.py           # Core logic and Task class
│
└── tests/
    └── test_todo.py      # Unit tests for core logic
```


***

## Installation \& Setup

This project includes a setup script for automated installation.

### 1. Clone the repository

```bash
git clone https://github.com/mehuli-majumder/To-Do-App-OST.git
cd To-Do-App-OST
```


### 2. Run the setup script

This will create a virtual environment, install all dependencies from `requirements.txt`, and run tests.

```bash
python setup.py
```


***

## Usage

After running the setup script, activate the virtual environment.

### On Windows

```bash
.venv\Scripts\activate
```


### On macOS/Linux

```bash
source .venv/bin/activate
```


### Run the Web App

```bash
streamlit run app.py
```

Your browser will automatically open the application.

### Run the CLI

```bash
python src/main.py
```


***

## Running Tests

```bash
pytest
```


***

## Contributing

Contributions are welcome! 🎉

Please read the [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

***

## License

This project is licensed under the terms specified in the repository.

***

## Languages

- Python 100%

***

## Credits

Maintained by [mehuli-majumder](https://github.com/mehuli-majumder). See repository for all contributors.

---



