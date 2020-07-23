{{ "#" * cookiecutter.package_name|length }}
{{ cookiecutter.package_name }}
{{ "#" * cookiecutter.package_name|length }}

{{ cookiecutter.description }}

This package is available on `GitHub`_ and `PyPI`_.

The latest documentation for the package can be found here:
`Documentation`_

.. FIXME: Fix doc link
.. _Documentation: https://link_to_docs
.. _GitHub: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.package_slug }}
.. _PyPI: https://pypi.org/{{ cookiecutter.pypi_username }}/{{ cookiecutter.package_slug }}
