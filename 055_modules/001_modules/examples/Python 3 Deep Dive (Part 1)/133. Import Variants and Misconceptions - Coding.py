import sys
for key in sorted(sys.modules.keys()):
    print(key)
###########################################################################
print('#' * 52 + ' cmath')

print('cmath' in sys.modules)

from cmath import exp

print('cmath' in globals())

print('exp' in globals())

print(sys.modules['cmath'])

cmath = sys.modules['cmath']

print(cmath)

print(exp(2+3j))

print(cmath.sqrt(1+1j))

###########################################################################
print('#' * 52 + ' print globals')

print(globals())

from cmath import *

print(globals())

###########################################################################
print('#' * 52 + ' cmath')

print(sqrt(2+2j))
print(pi)
print(sin(2-3j))
print(sqrt)

###########################################################################
print('#' * 52 + ' from math import *')

from math import *

print(sqrt)

from cmath import sqrt
from math import sqrt

import cmath
import math

print(math.sqrt(2))
print(cmath.sqrt(2+2j))

import math as r_math
import cmath as c_math

print(r_math)
print(c_math)

print(r_math.sqrt(2))
print(c_math.sqrt(2))

###########################################################################
print('#' * 52 + ' import importlib')
import importlib

r_math = importlib.import_module('math')
c_math = importlib.import_module('cmath')

print(r_math)
print(c_math)

###########################################################################
print('#' * 52 + ' from math import')

from math import sqrt as r_sqrt
from cmath import sqrt as c_sqrt

print(r_sqrt)
print(c_sqrt)

###########################################################################
print('#' * 52 + ' importlib.import_module')

r_sqrt = importlib.import_module('math').sqrt
c_sqrt = importlib.import_module('cmath').sqrt

print(r_sqrt)
print(c_sqrt)

###########################################################################
print('#' * 52 + ' nested import')

def my_func(a):
    import math
    return math.sqrt(a)

from time import perf_counter

from collections import namedtuple

Timings = namedtuple('Timing', 'timing_1 timing_2 abs_diff rel_diff_perc')

def compare_timings(timing1, timing2):
    rel_diff = (timing2 - timing1)/timing1 * 100

    timings = Timings(round(timing1, 1),
                      round(timing2, 1),
                      round(timing2 - timing1, 2),
                      round(rel_diff, 2))
    return timings

test_repeats = 10_000_000

import math

start = perf_counter()

for _ in range(test_repeats):
    math.sqrt(2)
end = perf_counter()
elapsed_fully_qualified = end - start
print(f'Elapsed: {elapsed_fully_qualified}')

from math import sqrt

start = perf_counter()
for _ in range(test_repeats):
    sqrt(2)
end = perf_counter()
elapsed_direct_symbol = end - start
print(f'Elapsed: {elapsed_direct_symbol}')

print(compare_timings(elapsed_fully_qualified, elapsed_direct_symbol))

import math


def func():
    math.sqrt(2)


start = perf_counter()
for _ in range(test_repeats):
    func()
end = perf_counter()
elapsed_func_fully_qualified = end - start
print(f'Elapsed: {elapsed_func_fully_qualified}')

print(compare_timings(elapsed_fully_qualified, elapsed_func_fully_qualified))

from math import sqrt


def func():
    sqrt(2)


start = perf_counter()
for _ in range(test_repeats):
    func()
end = perf_counter()
elapsed_func_direct_symbol = end - start
print(f'Elapsed: {elapsed_func_direct_symbol}')

print(compare_timings(elapsed_func_fully_qualified, elapsed_func_direct_symbol))


def func():
    import math
    math.sqrt(2)


start = perf_counter()
for _ in range(test_repeats):
    func()
end = perf_counter()
elapsed_nested_fully_qualified = end - start
print(f'Elapsed: {elapsed_nested_fully_qualified}')

compare_timings(elapsed_func_fully_qualified, elapsed_nested_fully_qualified)


def func():
    from math import sqrt
    sqrt(2)


start = perf_counter()
for _ in range(test_repeats):
    func()
end = perf_counter()
elapsed_nested_direct_symbol = end - start
print(f'Elapsed: {elapsed_nested_direct_symbol}')

compare_timings(elapsed_nested_fully_qualified, elapsed_nested_direct_symbol)