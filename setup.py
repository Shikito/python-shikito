#!/usr/bin/env python
import sys

from setuptools import setup, find_packages

if sys.version_info < (3, 5):
    sys.exit('Sorry, Python < 3.5 is not supported')

with open('README.md') as f:
    README = f.read()

setup(
    name='shikito',
    version='0.0.0',
    packages=find_packages(),
)
