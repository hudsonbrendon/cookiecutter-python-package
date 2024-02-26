# Cookiecutter Python Package Template

```bash
cookiecutter https://github.com/hudsonbrendon/cookiecutter-python-package.git
```

## Installing Poetry

We will use poetry to manage the virtual environment and our dependencies, to do this run:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

With poetry installed, run:

```bash
poetry install --with dev
```

Then activate the virtual environment with:

```bash
poetry shell
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
poetry add <dependence>
```

If your dependency is at a development level (such as testing packages), don't forget to use the --dev flag:

```bash
poetry add <dependency> --group dev
```

To remove a dependency, use:

```bash
poetry removes <dependency>
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
poetry build
```

And to publish to the register, run:

```bash
poetry publish
```

## Branch and commit patterns

To create branches, we use the Git Flow pattern, read more about it at:

[https://danielkummer.github.io/git-flow-cheatsheet/](https://danielkummer.github.io/git-flow-cheatsheet/)

And for commits we follow the Conventional Commits conventions, read more about it at:

[https://www.conventionalcommits.org/en/v1.0.0/](https://www.conventionalcommits.org/en/v1.0.0/)

# Contribute 🚀
