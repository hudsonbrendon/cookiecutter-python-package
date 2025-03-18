# Cookiecutter Python Package Template

```bash
cookiecutter https://github.com/hudsonbrendon/cookiecutter-python-package.git
```

## Installing uv

We use uv to manage dependencies and virtual environments due to its speed and efficiency. To install uv, run:

```bash
# MacOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows PowerShell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

With uv installed, create and activate a virtual environment:

```bash
# Create a virtual environment
uv venv

# Activate the virtual environment
# On macOS/Linux:
source .venv/bin/activate
# On Windows:
.venv\Scripts\activate
```

Install the project and its dependencies:

```bash
uv pip install -e ".[dev]"
```

# Pre-commit

With the virtual environment activated, run the command below:

```bash
pre-commit install
```

[pre-commit](https://pre-commit.com/) is a hook manager for git that applies numerous validations during commit. Python, yml and json file formatting validations are present in this project.

# Adding dependencies

To add a dependency we can run:

```bash
# Add a regular dependency
uv pip install package-name

# Add a development dependency
uv pip install package-name --dev
```

To update dependencies:

```bash
uv pip sync
```

## Tests

To run the tests directly in the environment, run:

```bash
pytest -n auto
```

If you want to run a specific test, run:

```bash
pytest -k "<test-name>"
```

# Coverage

To run coverage on the project, run:

```bash
pytest -n auto --cov=. --cov-report=html
```

A directory called **htmlcov** will be generated with all the content of the coverage result, inside it execute:

```bash
python3 -m http.server
```

And then access [http://localhost:8000](http://localhost:8000) to view the content.

# Build and publish

To build the application, run:

```bash
python -m build
```

And to publish to PyPI, run:

```bash
twine upload dist/*
```

# Documentation

Creating clear and structured documentation is essential for any Python package, and MkDocs is a great tool for this purpose. With its Markdown-based approach and easy deployment options, MkDocs simplifies the process of generating and maintaining project documentation.

For a Python package template, integrating MkDocs allows developers to:

- Provide well-organized API documentation.
- Maintain a consistent structure for guides and tutorials.
- Easily host documentation on GitHub Pages or similar platforms.

By combining MkDocs with plugins like mkdocstrings, you can automatically generate documentation from docstrings, ensuring that your package remains well-documented and easy to use.

Would you like a more detailed guide on setting it up? Access [https://www.mkdocs.org/](https://www.mkdocs.org/)


## Branch and commit patterns

To create branches, we use the Git Flow pattern, read more about it at:

[https://danielkummer.github.io/git-flow-cheatsheet/](https://danielkummer.github.io/git-flow-cheatsheet/)

And for commits we follow the Conventional Commits conventions, read more about it at:

[https://www.conventionalcommits.org/en/v1.0.0/](https://www.conventionalcommits.org/en/v1.0.0/)

# Contribute 🚀
