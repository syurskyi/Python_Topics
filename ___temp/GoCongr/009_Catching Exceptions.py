# -*- coding: utf-8 -*-

# Catching Exceptions
def fetcher(obj, index):
    return obj[index]

x = 'spam'

try:
    fetcher(x, 4)
except IndexError:                    # Catch and recover
    print('got exception')

print()


def catcher():
    try:
        fetcher(x, 4)
    except IndexError:
        print('got exception')
    print('continuing')
catcher()