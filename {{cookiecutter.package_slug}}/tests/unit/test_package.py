"""Tests for the {{ cookiecutter.module_name }} module."""


import importlib
import pkgutil

import {{ cookiecutter.module_name }}


def test_version():
    """Test the `__version__` exists."""
    assert hasattr({{ cookiecutter.module_name }}, "__version__")
    assert {{ cookiecutter.module_name }}.__version__


def test_imports():
    """Test the submodules all import."""
    package = {{ cookiecutter.module_name }}
    prefix = package.__name__ + "."
    for _, modname, _ in pkgutil.walk_packages(package.__path__, prefix):
        importlib.import_module(modname)

