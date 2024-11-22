VENV_DIR = .venv
PYTHON = $(VENV_DIR)/bin/python
PIP = $(VENV_DIR)/bin/pip
REQ_FILE = requirements.txt

# Commands
all: help

# Create the virtual environment
$(VENV_DIR):
	python3 -m venv $(VENV_DIR)
	@echo "\033[1;32m[✔] Virtual environment created in $(VENV_DIR)\033[0m"

# Activate the virtual environment (this prints instructions)
activate: $(VENV_DIR)
	@echo "\033[1;36mTo activate the virtual environment:\033[0m"
	@echo "\033[1;33m  source $(VENV_DIR)/bin/activate\033[0m (Linux/macOS)"
	@echo "\033[1;33m  $(VENV_DIR)\Scripts\\activate\033[0m (Windows)"
	@echo "\033[1;32m[✔] Virtual environment ready to be activated.\033[0m"

# Install dependencies from requirements.txt
install: $(VENV_DIR)
	$(PIP) install --upgrade pip
	$(PIP) install -r $(REQ_FILE)
	@echo "\033[1;34m[✔] Dependencies installed.\033[0m"

# Save the current dependencies to requirements.txt
freeze: $(VENV_DIR)
	$(PIP) freeze > $(REQ_FILE)
	@echo "\033[1;34m[✔] Dependencies saved to $(REQ_FILE).\033[0m"

# Run your application (modify app.py as needed)
run: $(VENV_DIR)
	$(PYTHON) src/app.py
	@echo "\033[1;33m[✔] Application executed.\033[0m"

# Clean Python-generated files and delete the virtual environment
clean:
	rm -rf $(VENV_DIR)
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -exec rm -rf {} +
	@echo "\033[1;31m[✘] Temporary files and virtual environment removed.\033[0m"

# Show help
help:
	@echo "\033[1;36mAvailable commands:\033[0m"
	@echo "\033[1;33m  make\033[0m          - Show this help message."
	@echo "\033[1;33m  make activate\033[0m - Show how to activate the virtual environment."
	@echo "\033[1;33m  make install\033[0m  - Create the virtual environment and install dependencies."
	@echo "\033[1;33m  make freeze\033[0m   - Save dependencies to requirements.txt."
	@echo "\033[1;33m  make run\033[0m      - Run the application."
	@echo "\033[1;33m  make clean\033[0m    - Remove the virtual environment and temporary files."

PHONY: all activate install freeze run clean help
