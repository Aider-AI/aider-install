#!/bin/bash
set -e

# Clean previous builds and venv
rm -rf build/ dist/ *.egg-info .venv/

# Create fresh virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Build the package
python3 -m pip install --upgrade build
python3 -m build

# Upload to PyPI
python3 -m pip install --upgrade twine
python3 -m twine upload dist/*

deactivate
