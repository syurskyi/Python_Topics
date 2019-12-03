# -*- coding: utf-8 -*-

# User-defined exception
#
# # Raise an instance
class Bad(Exception):
    pass

def doomed():
    raise Bad()

# User-defined exception
# Catch class name
class Bad(Exception):
    pass

def doomed():
    raise Bad()

try:
    doomed()
except Bad:                           # Catch class name
    print('got Bad')