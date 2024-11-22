# Variables
PACKAGE_NAME := mm_py_api

# Commands
.PHONY: clean build upload

# Clean up old build artefacts
clean:
	rm -rf dist/ build/ *.egg-info

# Build source and wheel distributions
build: clean
	python -m build

# Upload to PyPI
upload: build
	twine upload dist/*
