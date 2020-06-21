import sys

print(sys.exec_prefix)

import importlib

print(importlib.__file__)

print(importlib)

###########################################################################

print(importlib.import_module('fractions'))

# f = fractions.Fraction(2, 3)

# ---------------------------------------------------------------------------
# NameError                                 Traceback (most recent call last)
# <ipython-input-7-92ac4b49f1a5> in <module>()
# ----> 1 f = fractions.Fraction(2, 3)
#
# NameError: name 'fractions' is not defined

fractions = importlib.import_module('fractions')

f = fractions.Fraction(2, 3)

print(f)

print(fractions)

import math


print(math)

print(fractions.__spec__)

# import foo

print('#' * 52 + ' print sys.meta_path')

print(sys.meta_path)

print(importlib.util.find_spec('math'))
print(importlib.util.find_spec('fractions'))

print('#' * 52 + ' with open')

with open('module1.py', 'w') as code_file:
    code_file.write("print('running module1.py...')\n")
    code_file.write('a = 100\n')

print(importlib.util.find_spec('module1'))

###########################################################################
print('#' * 52 + ' import module1')
import module1

print(module1.a)


###########################################################################
print('#' * 52 + ' import os')

import os

# you can use this for Mac/Linux:
# ext_module_path = os.environ['HOME']

# you can use this in Windows 10
#ext_module_path = os.environ['HOMEPATH']

# or you can just hard code some path
# ext_module_path = 'c:\\temp'

ext_module_path = os.environ.get('HOME', os.environ['HOMEPATH'])

print(ext_module_path)

###########################################################################
print('#' * 52 + ' create module2')

file_abs_path = os.path.join(ext_module_path, 'module2.py')
with open(file_abs_path, 'w') as code_file:
    code_file.write("print('running module2.py...')\n")
    code_file.write("x = 'python'\n")

print(importlib.util.find_spec('module2'))

# import module2

# ---------------------------------------------------------------------------
# ModuleNotFoundError                       Traceback (most recent call last)
# <ipython-input-27-4fbab195dd19> in <module>()
# ----> 1 import module2
#
# ModuleNotFoundError: No module named 'module2'

try:
    import module2
except ModuleNotFoundError:
    # could not find module
    # maybe import an alternative module instead??
    # e.g. import module1 as module2
    # but please do not just silence the exception!
    # if you're importing the module most likely you are
    # using it somewhere in your code - so raise an
    # exception at the precise location where the root cause
    # occurred!
    # so the following is BAD!!
    print('Module was not found.')

print(ext_module_path in sys.path)
sys.path.append(ext_module_path)
print(importlib.util.find_spec('module2'))

import module2
print(module2.x)