import logging
from pprint import pprint
from sys import stdout as STDOUT


# Example 2
class Meta(type):
    def __new__(meta, name, bases, class_dict):
        print(meta, name, bases, class_dict)
        return type.__new__(meta, name, bases, class_dict)

class MyClassInPython2(object):
    __metaclass__ = Meta
    stuff = 123

    def foo(self):
        pass
