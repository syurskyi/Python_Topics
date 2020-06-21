#!/usr/bin/env python
"""
  Don't install this, just here for demo of a real module
   https://github.com/lathama/python-testing-example
"""

____ setuptools ______ setup, find_packages
____ ___ ______ version_info, exit
______ testingdemo

setup(
    name_'Testingdemo',
    version_testingdemo.__version__,
    description_'Python Testing Demonstration',
    url_'',
    license_'',
    packages_find_packages(),
    install_requires_[''],
    entry_points_{
        'console_scripts': ['testingdemo=testingdemo.AnExample:report_something']
    }
)
