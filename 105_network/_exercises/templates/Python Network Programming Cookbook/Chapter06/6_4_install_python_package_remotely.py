#!/usr/bin/env python
# Python Network Programming Cookbook, Second Edition -- Chapter - 6
# This program is optimized for Python 2.7.12 and Python 3.5.2.
# It may run on any other version with/without modifications.

____ getpass ______ getpass
____ fabric.api ______ settings, run, env, prompt


___ remote_server
    env.hosts _ ['127.0.0.1']
    env.user _ prompt('Enter user name: ')
    env.password _ getpass('Enter password: ')
    
___ install_package
    run("pip install yolk")
