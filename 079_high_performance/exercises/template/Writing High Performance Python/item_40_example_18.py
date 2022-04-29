import logging
from pprint import pprint
from sys import stdout as STDOUT


# Example 18
def delegated():
    yield 1
    yield 2

def composed():
    yield 'A'
    for value in delegated():  # yield from in Python 3
        yield value
    yield 'B'

print list(composed())
