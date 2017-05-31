#!/usr/bin/env sh
python setup.py build sdist bdist_wheel --universal
sudo pip install -e .
