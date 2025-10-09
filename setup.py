import os
import sys
import subprocess
import venv
from pathlib import Path

# --- Paths ---
ROOT_DIR = Path(__file__).parent.resolve()
SRC_DIR = ROOT_DIR / "src"
TESTS_DIR = ROOT_DIR / "tests"
REQ_FILE = ROOT_DIR / "requirements.txt"
VENV_DIR = ROOT_DIR / ".venv"


def create_virtual_env():
    """Create a virtual environment for isolated setup."""
    if not VENV_DIR.exists():
        print("Creating virtual environment...")
        venv.create(VENV_DIR, with_pip=True)
        print("Virtual environment created.")
    else:
        print("Virtual environment already exists.")


def get_venv_python():
    """Return the path to the venv Python interpreter."""
    if os.name == "nt":  # Windows
        return VENV_DIR / "Scripts" / "python.exe"
    else:
        return VENV_DIR / "bin" / "python"


def create_requirements_file():
    """Create a default requirements.txt if missing."""
    if not REQ_FILE.exists():
        print("Creating default requirements.txt...")
        with open(REQ_FILE, "w") as f:
            f.write("streamlit\n")
            f.write("pytest\n")
        print("requirements.txt created with default dependencies.")
    else:
        print("requirements.txt already exists.")


def install_dependencies(python_exec):
    """Install dependencies inside the virtual environment."""
    print("\nInstalling dependencies...")
    try:
        subprocess.check_call([python_exec, "-m", "pip", "install", "--upgrade", "pip"])
        subprocess.check_call([python_exec, "-m", "pip", "install", "-r", str(REQ_FILE)])
        print("Dependencies installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing dependencies: {e}")
        sys.exit(1)


def verify_structure():
    """Ensure project structure is correct."""
    print("\nVerifying project structure...")
    expected_dirs = ["src", "tests"]
    expected_files = ["app.py"]

    for d in expected_dirs:
        if not (ROOT_DIR / d).exists():
            print(f"Missing folder: {d}")
            sys.exit(1)

    for f in expected_files:
        if not (ROOT_DIR / f).exists():
            print(f"Missing file: {f}")
            sys.exit(1)

    print("Project structure verified.")


def run_tests(python_exec):
    """Run unit tests to verify installation."""
    print("\nRunning unit tests...")
    test_path = TESTS_DIR / "test_todo.py"
    if not test_path.exists():
        print("No test file found. Skipping tests.")
        return
    try:
        subprocess.check_call([python_exec, "-m", "pytest", str(test_path), "-v"])
        print("All tests passed successfully.")
    except subprocess.CalledProcessError:
        print("Some tests failed. Check your code or dependencies.")
        sys.exit(1)


def main():
    print("Starting To-Do App Installer\n")

    verify_structure()
    create_requirements_file()
    create_virtual_env()

    python_exec = get_venv_python()
    install_dependencies(python_exec)
    run_tests(python_exec)

    print("\nSetup Complete.")
    print("Next steps:")
    print("1. Activate the virtual environment:")
    if os.name == "nt":
        print(f"   {VENV_DIR}\\Scripts\\activate")
    else:
        print(f"   source {VENV_DIR}/bin/activate")

    print("\n2. Run the app using Streamlit:")
    print("   streamlit run app.py")

    print("\n3. Or run the CLI app manually:")
    print("   python src/main.py")


if __name__ == "__main__":
    main()