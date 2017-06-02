#!/usr/bin/env sh
rm -Rf dist
rm -Rf build
python setup.py build sdist bdist_wheel --universal
sudo pip install -e .
