#! python3.8
# -*- coding: utf-8 -*-

# File name:    setup.py
# Author:       Tobias Rosskopf
# Email:        tobirosskopf@gmail.com
# Created:      27.11.2019
# Modified:     27.11.2019


"""
Setup docstring
    USE:
    $ python setup.py register
    $ python setup.py upload
"""

# Standard imports
from setuptools import setup

# Constants
PACKAGE_NAME = 'gigfinder'
PACKAGE_LIST = [
    'gigfinder',
    'geocoder.py',
    'shpwriter.py',
    ]

with open("README.md", 'r') as f:
    long_description = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    # Metadata
    name = PACKAGE_NAME,
    version = '1.0',
    description = 'Write description!',
    long_description = long_description,
    license = 'MIT',
    author = 'Tobias Rosskopf',
    author_email = 'tobirosskopf@gmail.com',
    url = '',

    # Package info
    python_requires = '>=3.8',
    packages = [PACKAGE_NAME] + PACKAGE_LIST,
    install_requires = requirements,
    keywords = '',
)
