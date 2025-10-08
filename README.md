<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# Project Structure

[](https://github.com/mehuli-majumder/To-Do-App-OST#project-structure)
To-Do-App-OST/
│
├── .gitignore
├── app.py              \# Streamlit Web App entry point
├── CONTRIBUTING.md     \# Guidelines for contributors
├── README.md           \# This file
├── requirements.txt    \# Project dependencies
├── setup.py            \# Automated setup script
├── tasks.json          \# Database file for storing tasks
│
├── src/
│   ├── main.py         \# CLI App entry point
│   └── todo.py         \# Core application logic and Task class
│
└── tests/
└── test_todo.py    \# Unit tests for the core logic
Installation \& Setup
This project includes a setup script to automate the entire installation process.

1. Clone the repository
bash
Copy code
git clone [https://github.com/mehuli-majumder/To-Do-App-OST.git](https://github.com/mehuli-majumder/To-Do-App-OST.git)
bash
Copy code
cd To-Do-App-OST
2. Run the setup script
This will create a virtual environment, install all required packages from requirements.txt, and run tests to verify the installation.

bash
Copy code
python setup.py
Usage
After running the setup script, you must first activate the virtual environment.

On Windows:

bash
Copy code
.venv\Scripts\activate
On macOS/Linux:

bash
Copy code
source .venv/bin/activate
Once the environment is active, you can run either the Web App or the CLI.

Running the Web App
bash
Copy code
streamlit run app.py
Your browser will automatically open with the application.

Running the Command-Line Interface (CLI)
bash
Copy code
python src/main.py
Running Tests
bash
Copy code
pytest
Contributing
Contributions are welcome! 🎉
Please read the CONTRIBUTING.md file for details on our code of conduct and the process for submitting pull requests.

draft me this readme in such a format that i can copy paste directly and push to github and it is structurally organised with good formatting

Here is a well-organized and ready-to-copy README draft for the To-Do-App-OST project, formatted with clear sections, code blocks, and GitHub-friendly Markdown structure.[^1]

***

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

<div align="center">⁂</div>

[^1]: https://github.com/mehuli-majumder/To-Do-App-OST

