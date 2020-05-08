#/usr/bin/env python3


from random import randint


def foobar(arg=None):
    return True


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def divide(a, b):
    return a / float(b)


def multiply(a, b):
    return a * b


def reverse_string(arg):
    return arg[::-1]


def print_something(arg):
    print(arg)


def rand_int(max):
    return randint(0, max)
