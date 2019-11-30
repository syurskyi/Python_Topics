# # -*- coding: utf-8 -*-

# Во время отладки, в трассировочную информацию выводится __name__ функции.
def foo():
    print("foo")


print(foo.__name__)


# выведет: foo

# Однако, декораторы мешают нормальному ходу дел:
def bar(func):
    def wrapper():
        print
        "bar"
        return func()

    return wrapper


@bar
def foo():
    print
    "foo"


print(foo.__name__)
# выведет: wrapper

# "functools" может нам с этим помочь

import functools


def bar(func):
    # Объявляем "wrapper" оборачивающим "func"
    # и запускаем магию:
    @functools.wraps(func)
    def wrapper():
        print("bar")
        return func()

    return wrapper


@bar
def foo():
    print("foo")


print(foo.__name__)
# выведет: foo