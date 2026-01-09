# WN Python Blueprint

A [cookiecutter](https://github.com/cookiecutter/cookiecutter) template for Python projects with modern tooling.

## Features

- **Poetry** - Dependency management
- **Ruff** - Linting and formatting
- **Mypy** - Static type checking
- **Pytest** - Testing with coverage
- **Pre-commit** - Git hooks for automated checks
- **Jupyter** - Optional notebook support

## Usage

### Prerequisites

Install cookiecutter:
```bash
pip install cookiecutter
# or
pipx install cookiecutter
```

### Create a New Project

From GitHub:
```bash
cookiecutter gh:wojciechnowak/wn-python-blueprint
```

From local clone:
```bash
cookiecutter path/to/wn-python-blueprint
```

### Prompts

| Variable | Description | Default |
|----------|-------------|---------|
| `project_name` | Human-readable project name | My Project |
| `project_slug` | Python package name (auto-generated) | my_project |
| `project_description` | Short project description | Python project with modern tooling |
| `author_name` | Your name | Your Name |
| `python_version` | Python version | 3.12 |
| `include_jupyter` | Include Jupyter support | yes |

### After Generation

```bash
cd your_project_slug
make install        # Install dependencies
make pre-commit     # Install git hooks
make check          # Run all checks
```

## What's Included

```
your_project/
├── src/
│   └── your_project/
│       ├── __init__.py
│       └── main.py
├── tests/
│   └── test_main.py
├── .gitignore
├── .pre-commit-config.yaml
├── .python-version
├── CONTRIBUTING.md
├── Makefile
├── README.md
├── poetry.toml
└── pyproject.toml
```

## License

MIT
