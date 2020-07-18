.PHONY: help lint format venv dev doc show-doc test unit integration dist dist-doc clean


SHELL = bash
PROJECT = Test Project
VERSION = $(shell cat VERSION)


help:  ## Describe all available make commands
	# FIXME: Add help
	@echo "Not yet implemented"
	# FIXME: Add implementation

check:  ## Check for any Python lint errors
	# FIXME: Add help
	tox -e lint

lint:  ## Lint the source code and output the results
	LINT=--exit-zero tox -e lint
	# FIXME: Add help

format:  ## Autoformat the source code using Black
	# FIXME: Add help
	DO_FORMAT= tox -e format

venv:  ## Create a virtualenv that includes the package in editable mode
	# FIXME: Add help
	python -m virtualenv .venv
	.venv/bin/pip install -e .

dev: venv  ## Create a virutalenv and enter it
	# FIXME: Add help
	bash --rcfile <(echo 'source ~/.bashrc; source .venv/bin/activate')

doc:  ## Generate the documentation
	# FIXME: Add help
	DO_BUILD= tox -e doc

show-doc:  ## Launch the generated documentation
	# FIXME: Add help
	xdg-open ./docs/_build/index.html

test:  ## Run the package tests
	# FIXME: Add help
	tox

unit:  ## Run the package unit tests
	# FIXME: Add help
	tox -e py37 -- tests/unit

integration:  ## Run the package integration tests
	# FIXME: Add help
	tox -e py37 -- tests/integration

dist:  ## Distribute the package to PyPI
	# FIXME: Add help
	@echo "Not yet implemented"
	# FIXME: Add implementation

dist-doc:  ## Distribute the package to PyPI
	# FIXME: Add help
	@echo "Not yet implemented"
	# FIXME: Add implementation

clean:  ## Remove temporary files
	# FIXME: Add help
	git clean -Xdf
