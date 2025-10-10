# Makefile for To-Do-App-OST
# Shortcuts: make install, make test, make run
# Usage examples:
#   make install
#   make test
#   make run
#   make run ENTRY=src/todo.py

ENTRY ?= src/main.py
REQS ?= requirements.txt

.PHONY: help venv install test run clean

help:
	@echo "Usage:"
	@echo "  make install        Creates .venv (if missing) and installs dependencies"
	@echo "  make test           Runs pytest"
	@echo "  make run            Runs your application (override ENTRY if needed)"
	@echo ""
	@echo "Examples:" 
	@echo "  make run ENTRY=src/todo.py"

venv:
	@echo "Creating virtualenv (.venv) if missing..."
	@python -m venv .venv || python3 -m venv .venv || (echo "Failed to create venv with 'python' or 'python3'"; exit 1)
	@echo "Virtualenv ready (.venv)"

install: venv
	@PY=$$( [ -f .venv/bin/python ] && echo .venv/bin/python || ( [ -f .venv/Scripts/python.exe ] && echo .venv/Scripts/python.exe || echo python ) ); \
	echo "Using $$PY to install dependencies"; \
	$$PY -m pip install --upgrade pip setuptools wheel; \
	if [ -f $(REQS) ]; then $$PY -m pip install -r $(REQS); else echo "No $(REQS) found — skipping"; fi

test:
	@PY=$$( [ -f .venv/bin/python ] && echo .venv/bin/python || ( [ -f .venv/Scripts/python.exe ] && echo .venv/Scripts/python.exe || echo python ) ); \
	echo "Using $$PY to run tests"; \
	$$PY -m pytest -q

run:
	@PY=$$( [ -f .venv/bin/python ] && echo .venv/bin/python || ( [ -f .venv/Scripts/python.exe ] && echo .venv/Scripts/python.exe || echo python ) ); \
	if [ -f $(ENTRY) ]; then echo "Running $(ENTRY) with $$PY"; $$PY $(ENTRY); else echo "Entry $(ENTRY) not found. Override with 'make run ENTRY=src/todo.py'"; false; fi

clean:
	@echo "Cleaning up __pycache__ and .pyc files..."; \
	find . -name "__pycache__" -type d -exec rm -rf {} + || true; \
	find . -name "*.pyc" -delete || true; \
	rm -rf .venv || true
