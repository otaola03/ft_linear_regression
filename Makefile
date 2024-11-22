# Variables
VENV_DIR = .venv
PYTHON = $(VENV_DIR)/bin/python
PIP = $(VENV_DIR)/bin/pip
REQ_FILE = requirements.txt

# Comandos
all: help

# Crear el entorno virtual
$(VENV_DIR):
	python3 -m venv $(VENV_DIR)
	@echo "Entorno virtual creado en $(VENV_DIR)"

# Crear el entorno virtual
create: $(VENV_DIR)
	@echo "Entorno virtual creado."

# Eliminar el entorno virtual
delete:
	rm -rf $(VENV_DIR)
	@echo "Entorno virtual eliminado."

# Instalar dependencias desde requirements.txt
install: $(VENV_DIR)
	$(PIP) install --upgrade pip
	$(PIP) install -r $(REQ_FILE)
	@echo "Dependencias instaladas."

# Guardar las dependencias actuales en requirements.txt
freeze: $(VENV_DIR)
	$(PIP) freeze > $(REQ_FILE)
	@echo "Dependencias guardadas en $(REQ_FILE)."

# Ejecutar tu aplicación (modifica app.py según tu archivo principal)
run: $(VENV_DIR)
	$(PYTHON) app.py

# Limpiar archivos generados por Python y borrar el entorno virtual
clean:
	rm -rf $(VENV_DIR)
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -exec rm -rf {} +
	@echo "Archivos temporales y entorno virtual eliminados."

# Mostrar ayuda
help:
	@echo "Comandos disponibles:"
	@echo "  make          - Mostrar esta ayuda."
	@echo "  make create   - Crear el entorno virtual."
	@echo "  make delete   - Eliminar el entorno virtual."
	@echo "  make install  - Crear el entorno virtual e instalar dependencias."
	@echo "  make freeze   - Guardar dependencias en requirements.txt."
	@echo "  make run      - Ejecutar la aplicación."
	@echo "  make clean    - Eliminar el entorno virtual y archivos temporales."

