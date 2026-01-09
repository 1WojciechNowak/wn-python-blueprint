.PHONY: help install clean check fix typecheck{% if cookiecutter.include_tests == 'yes' %} test{% endif %}{% if cookiecutter.include_jupyter == 'yes' %} kernel jupyter{% endif %}

help:
	@echo "Available commands:"
	@echo ""
	@echo "Setup"
	@echo "  make install   - Install dependencies"
	@echo "  make clean     - Remove virtual environment"
	@echo ""
	@echo "Quality"
{% if cookiecutter.include_tests == 'yes' %}
	@echo "  make check     - Run all (fix + typecheck + test)"
{% else %}
	@echo "  make check     - Run all (fix + typecheck)"
{% endif %}
	@echo "  make fix       - Auto-fix and format code"
{% if cookiecutter.include_tests == 'yes' %}
	@echo "  make test      - Run tests"
{% endif %}
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

{% if cookiecutter.include_tests == 'yes' %}
check: fix typecheck test
{% else %}
check: fix typecheck
{% endif %}

typecheck:
	poetry run mypy .

fix:
	poetry run ruff check . --fix
	poetry run ruff format .
{% if cookiecutter.include_tests == 'yes' %}

test:
	poetry run pytest
{% endif %}

{% if cookiecutter.include_jupyter == 'yes' %}

# -----------------------------------------
# Jupyter
# -----------------------------------------

kernel:
	poetry run python -m ipykernel install --user --name={{ cookiecutter.project_slug }} --display-name "Python ({{ cookiecutter.project_slug }})"

jupyter:
	poetry run jupyter notebook
{% endif %}
