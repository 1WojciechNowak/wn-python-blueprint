# 🐍 {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## 📋 Prerequisites

- [pyenv](https://github.com/pyenv/pyenv) - Python version management
- [Poetry](https://python-poetry.org/) - Dependency management

Both can be installed via `brew install pyenv poetry` or see links above.

## 🚀 Setup

```bash
pyenv install {{ cookiecutter.python_version }}  # if not already installed
make install
```

## ▶️ Running the Project

```bash
poetry run {{ cookiecutter.project_slug.replace('_', '-') }}
```

## 🔧 Troubleshooting

To start fresh (remove virtual environment and reinstall):

```bash
make clean
make install
```

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for development guidelines.
