# {{cookiecutter.project_name}}

{{cookiecutter.project_description}}

## Installation

This package requires Python 3.11+. You can install it using pip:

```bash
pip install {{cookiecutter.pkg_name}}
```

## Development Setup

We use [uv](https://github.com/astral-sh/uv) for dependency management and virtual environments.

### Install uv

```bash
# MacOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows PowerShell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Create and activate virtual environment

```bash
# Create a virtual environment
uv venv

# Activate the virtual environment
# On macOS/Linux:
source .venv/bin/activate
# On Windows:
.venv\Scripts\activate
```

### Install dependencies

```bash
# Install the project in development mode with all dependencies
uv sync
```

## Testing

Run tests with pytest:

```bash
pytest
```

For test coverage:

```bash
pytest --cov={{cookiecutter.pkg_name}} --cov-report=html
```

## Documentation

Build the documentation:

```bash
mkdocs build
```

Serve the documentation locally:

```bash
mkdocs serve
```
