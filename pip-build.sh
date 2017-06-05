#!/usr/bin/env sh
echo Cleaning...
rm -Rf dist
rm -Rf build
echo "Creating source dist..."
python setup.py build sdist
echo "Creating binary dist"
python setup.py build bdist_wheel --universal
sudo pip install -e .
