from functools import singledispatch


@singledispatch
def add(a, b):
    raise NotImplementedError('Unsupported type')


@add.register(int)
def _(a, b):
    print("First argument is of type ", type(a))
    print(a + b)


@add.register(str)
def _(a, b):
    print("First argument is of type ", type(a))
    print(a + b)


@add.register(list)
def _(a, b):
    print("First argument is of type ", type(a))
    print(a + b)


if __name__ == '__main__':
    add(1, 2)
    add('Python', 'Programming')
    add([1, 2, 3], [5, 6, 7])

# First argument is of type <class 'int'>
# 3
#
# First argument is of type <class 'str'>
# PythonProgramming
#
# First argument is of type <class 'list'>
# [1, 2, 3, 5, 6, 7]
#
# Traceback (most recent call last):
#     File "overloads.py", line 30, in <module>
#         add({}, 1)
#     File "/usr/local/lib/python3.5/functools.py", line 743, in wrapper
#         return dispatch(args[0].__class__)(*args, **kw)
#     File "overloads.py", line 5, in add
#         raise NotImplementedError('Unsupported type')
# NotImplementedError: Unsupported type