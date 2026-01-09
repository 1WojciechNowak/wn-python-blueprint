.PHONY: help install clean check fix test typecheck{% if cookiecutter.include_jupyter == 'yes' %} kernel jupyter{% endif %}

help:
	@echo "Available commands:"
	@echo ""
	@echo "Setup"
	@echo "  make install   - Install dependencies"
	@echo "  make clean     - Remove virtual environment"
	@echo ""
	@echo "Quality"
	@echo "  make check     - Run all (fix + typecheck + test)"
	@echo "  make fix       - Auto-fix and format code"
	@echo "  make test      - Run tests"
	@echo "  make typecheck - Run type checking (mypy)"
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

check: fix typecheck test

typecheck:
	poetry run mypy .

fix:
	poetry run ruff check . --fix
	poetry run ruff format .

test:
	poetry run pytest

{% if cookiecutter.include_jupyter == 'yes' %}

# -----------------------------------------
# Jupyter
# -----------------------------------------

kernel:
	poetry run python -m ipykernel install --user --name={{ cookiecutter.project_slug }} --display-name "Python ({{ cookiecutter.project_slug }})"

jupyter:
	poetry run jupyter notebook
{% endif %}
