"""Tests for the {{ cookiecutter.module_name }} module."""


import {{ cookiecutter.module_name }}


def test_version():
    """Test the `__version__` exists."""
    assert hasattr({{ cookiecutter.module_name }}, "__version__")
    assert {{ cookiecutter.module_name }}.__version__


def test_imports():
    """Test the submodules all import."""
    # FIXME: Actually add the test
