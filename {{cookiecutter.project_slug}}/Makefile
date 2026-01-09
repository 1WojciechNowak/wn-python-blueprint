# Use TAB characters for indentation (not spaces)!
.PHONY: help install clean check fix test pre-commit{% if cookiecutter.include_jupyter == 'yes' %} kernel jupyter{% endif %}

help:
	@echo "Available commands:"
	@echo ""
	@echo "Setup"
	@echo "  make install   - Install dependencies"
	@echo "  make clean     - Remove virtual environment"
	@echo ""
	@echo "Quality"
	@echo "  make check     - Run all checks (lint + types + test)"
	@echo "  make fix       - Auto-fix and format code"
	@echo "  make test      - Run tests only"
	@echo ""
	@echo "Git Hooks"
	@echo "  make pre-commit - Install pre-commit hooks"
{% if cookiecutter.include_jupyter == 'yes' %}
	@echo ""
	@echo "Jupyter"
	@echo "  make kernel    - Register Jupyter kernel"
	@echo "  make jupyter   - Launch Jupyter Notebook"
{% endif %}

# -----------------------------------------
# Setup
# -----------------------------------------

install:
	poetry install

clean:
	poetry env remove python || true

# -----------------------------------------
# Quality
# -----------------------------------------

check:
	poetry run ruff check .
	poetry run mypy .
	poetry run pytest

fix:
	poetry run ruff check . --fix
	poetry run ruff format .

test:
	poetry run pytest

# -----------------------------------------
# Git Hooks
# -----------------------------------------

pre-commit:
	poetry run pre-commit install
{% if cookiecutter.include_jupyter == 'yes' %}

# -----------------------------------------
# Jupyter
# -----------------------------------------

kernel:
	poetry run python -m ipykernel install --user --name={{ cookiecutter.project_slug }} --display-name "Python ({{ cookiecutter.project_slug }})"

jupyter:
	poetry run jupyter notebook
{% endif %}
