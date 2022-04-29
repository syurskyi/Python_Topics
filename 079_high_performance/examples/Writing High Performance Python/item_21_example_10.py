import logging
from pprint import pprint
from sys import stdout as STDOUT


# Example 10
def print_args(*args, **kwargs):
    print 'Positional:', args
    print 'Keyword:   ', kwargs

print_args(1, 2, foo='bar', stuff='meep')
