# 🐍 {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## 📋 Prerequisites

- [pyenv](https://github.com/pyenv/pyenv) - Python version management
- [Poetry](https://python-poetry.org/) - Dependency management

## 🚀 Setup

```bash
make install
```

## 📦 Project Structure

```
src/
└── {{ cookiecutter.project_slug }}/
    ├── __init__.py
    └── main.py
tests/
├── __init__.py
└── test_main.py
{%- if cookiecutter.include_jupyter == 'yes' %}
notebooks/
└── hello_world.ipynb
{%- endif %}
```

## ▶️ Running the Project

```bash
poetry run {{ cookiecutter.project_slug.replace('_', '-') }}
```

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for development setup and guidelines.
