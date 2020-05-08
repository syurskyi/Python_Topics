#!/usr/bin/env python
"""
  Don't install this, just here for demo of a real module
   https://github.com/lathama/python-testing-example
"""

from setuptools import setup, find_packages
from sys import version_info, exit
import testingdemo

setup(
    name='Testingdemo',
    version=testingdemo.__version__,
    description='Python Testing Demonstration',
    url='',
    license='',
    packages=find_packages(),
    install_requires=[''],
    entry_points={
        'console_scripts': ['testingdemo=testingdemo.AnExample:report_something']
    }
)
