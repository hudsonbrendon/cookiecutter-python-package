from {{cookiecutter.pkg_name}} import {{cookiecutter.pkg_name|capitalize}}


class Test{{cookiecutter.pkg_name|capitalize}}:
    def test_{{cookiecutter.pkg_name}}(self):
        instance = {{cookiecutter.pkg_name|capitalize}}()

        assert isinstance(instance, {{cookiecutter.pkg_name|capitalize}})
    
