# Contributing

## Prerequisites

- [pyenv](https://github.com/pyenv/pyenv) - Python version management
- [Poetry](https://python-poetry.org/) - Dependency management

## Setup

1. Install the required Python version:
   ```bash
   pyenv install {{ cookiecutter.python_version }}
   ```

2. Install dependencies:
   ```bash
   make install
   ```

## Development Workflow

1. Write code
2. Auto-fix and format:
   ```bash
   make fix
   ```
3. Run all checks before committing:
   ```bash
   make check
   ```

Start fresh (remove virtual environment):
```bash
make clean
make install
```

## Tools

This project uses the following development tools (configured in `pyproject.toml`):

| Tool | Purpose | Command |
|------|---------|---------|
| **Ruff** | Linting and code formatting | `make fix` |
| **Mypy** | Static type checking | `make check` |
| **Pytest** | Testing with coverage | `make test` |

Run all checks at once:
```bash
make check    # Runs: ruff + mypy + pytest
```

Run individually:
```bash
poetry run ruff check .      # Lint only
poetry run ruff format .     # Format only
poetry run mypy .            # Type check only
```
{% if cookiecutter.include_jupyter == 'yes' %}

## Jupyter Notebooks

### What is a kernel?

Jupyter notebooks need a **kernel** - the Python interpreter that runs your code. By default, Jupyter uses its own Python, which doesn't have access to your project's dependencies.

To use your Poetry virtual environment in Jupyter, you need to register it as a kernel.

### Setup (one time)

After `make install`, register the kernel:

```bash
make kernel
```

This creates a kernel named "Python ({{ cookiecutter.project_slug }})" that uses your Poetry environment.

### Usage

Launch Jupyter:

```bash
make jupyter
```

In Jupyter, select the kernel:
1. Open or create a notebook
2. Click "Kernel" → "Change Kernel"
3. Select "Python ({{ cookiecutter.project_slug }})"

Now your notebook has access to all project dependencies.
{% endif %}
