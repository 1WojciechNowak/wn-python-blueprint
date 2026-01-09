# 🤝 Contributing

## 🛠️ Development

Before committing your changes:

```bash
{%- if cookiecutter.include_tests == 'yes' %}
make check    # Run all: fix + typecheck + test
{%- else %}
make check    # Run all: fix + typecheck
{%- endif %}
```

### Tools

This project uses the following development tools:

| Tool | Purpose | Command |
|------|---------|---------|
| **Ruff** | Linting and formatting | `make fix` |
| **Mypy** | Static type checking | `make typecheck` |
{%- if cookiecutter.include_tests == 'yes' %}
| **Pytest** | Testing with coverage | `make test` |
{%- endif %}
{% if cookiecutter.include_jupyter == 'yes' %}

## 📓 Jupyter Notebooks

Register the kernel to access project dependencies in notebooks:

```bash
make kernel   # Register kernel (one time)
make jupyter  # Launch Jupyter
```

Select kernel "Python ({{ cookiecutter.project_slug }})" in your notebook.
{% endif %}
