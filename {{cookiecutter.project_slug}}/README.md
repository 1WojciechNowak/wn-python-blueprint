# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Prerequisites

- [pyenv](https://github.com/pyenv/pyenv) - Python version management
- [Poetry](https://python-poetry.org/) - Dependency management

## Setup

```bash
make install      # Install dependencies
make pre-commit   # Install git hooks
make check        # Run all checks
```

## Project Structure

```
src/
└── {{ cookiecutter.project_slug }}/
    ├── __init__.py
    └── main.py
tests/
└── test_main.py
```

## Running the Project

```bash
poetry run {{ cookiecutter.project_slug.replace('_', '-') }}
```

Or as a module:
```bash
poetry run python -m {{ cookiecutter.project_slug }}.main
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for development setup and guidelines.
