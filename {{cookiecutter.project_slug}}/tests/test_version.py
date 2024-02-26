from {{cookiecutter.pkg_name}} import __version__


def test_version() -> None:
    assert __version__ == "{{cookiecutter.project_version}}"
