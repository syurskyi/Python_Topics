import os


def create_module_file(module_name, **kwargs):
    '''Create a module file named <module_name>.py.
    Module has a single function (print_values) that will print
    out the supplied (stringified) kwargs.
    '''

    module_file_name = f'{module_name}.py'
    module_rel_file_path = module_file_name
    module_abs_file_path = os.path.abspath(module_rel_file_path)

    with open(module_abs_file_path, 'w') as f:
        f.write(f'# {module_name}.py\n\n')
        f.write(f"print('running {module_file_name}...')\n\n")
        f.write(f'def print_values():\n')
        for key, value in kwargs.items():
            f.write(f"\tprint('{str(key)}', '{str(value)}')\n")

create_module_file('test', k1=10, k2='python')

import test

print(test)
print(test.print_values())

###########################################################################
print('#' * 52 + ' change test module')

create_module_file('test', k1=10, k2='python', k3='cheese')
print(test.print_values())

###########################################################################
print('#' * 52 + ' import module again')

import test
print(test.print_values())

print(id(test))

import sys
del sys.modules['test']

###########################################################################
print('#' * 52 + ' import module again')

import test

print(test.print_values())

print(id(test))
print(id(test))

###########################################################################
print('#' * 52 + ' create module file')

create_module_file('test', k1=10, k2='python',
                   k3='cheese', k4='parrots')

import importlib
print(importlib.reload(test))
print(id(test))

print(test.print_values())

create_module_file('test2', k1='python')

###########################################################################
print('#' * 52 + ' from test2 import module again')

from test2 import print_values

print_values()

print(id(print_values()))

create_module_file('test2', k1='python', k2='cheese')

# importlib.reload(test2)

# ---------------------------------------------------------------------------
# NameError                                 Traceback (most recent call last)
# <ipython-input-26-7b4c6fe87427> in <module>()
# ----> 1 importlib.reload(test2)
#
# NameError: name 'test2' is not defined


###########################################################################
print('#' * 52 + ' import test2')

import test2

print(test2.print_values())
print(id(test2.print_values))
print(id(print_values))

print(importlib.reload(test2))
print(test2.print_values())
print(print_values())
print(id(test2.print_values))
print(id(print_values))