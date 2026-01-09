# 🐍 WN Python Blueprint

A [cookiecutter](https://github.com/cookiecutter/cookiecutter) template for Python projects with modern tooling.

## ✨ Features

- **Project layout** - Modern src/tests/notebooks structure
- **pyenv** - Python version management
- **Poetry** - Dependency management
- **Ruff** - Linting and formatting
- **Mypy** - Static type checking
- **Pytest** - (Optional) Testing with coverage
- **Jupyter** - (Optional) Notebook support

## 🚀 Usage

### Prerequisites

- [cookiecutter](https://cookiecutter.readthedocs.io) - Project templating tool

### Create a New Project

```bash
cookiecutter gh:wojciechnowak/wn-python-blueprint
```

### Template Configuration

| Variable | Description | Default |
|----------|-------------|---------|
| `project_name` | Human-readable project name | My Project |
| `project_slug` | Python package name (auto-generated) | my_project |
| `project_description` | Short project description | Python project with modern tooling |
| `author_name` | Your name | Your Name |
| `python_version` | Python version | 3.12 |
| `include_tests` | Include tests setup | yes |
| `include_jupyter` | Include Jupyter support | yes |

## 📦 What's Included

```
<project_slug>/
├── src/
│   └── <project_slug>/
│       ├── __init__.py
│       └── main.py
├── tests/              # if include_tests: yes
│   └── test_main.py
├── notebooks/          # if include_jupyter: yes
│   └── hello_world.ipynb
├── .gitignore
├── .python-version
├── CONTRIBUTING.md
├── Makefile
├── README.md
├── poetry.toml
└── pyproject.toml
```

## License

[MIT](LICENSE)
