import math

print('#' * 52 + ' print globals ')
print(globals())


print(globals()['math'])

print(type(math))
print(math)

print('#' * 52 + ' print id(math)  ')
print(id(math))

math = None
print(type(math))
print(id(math))

import math
print(math)
print(id(math))

############################################################################
import sys

print('#' * 52 + ' sys')
print(type(sys.modules))
print(sys.modules['math'])
print(id(sys.modules['math']))

############################################################################

print('#' * 52 + ' math ')

print(math.__name__)

print(math.__dict__)

print(math.sqrt is math.__dict__['sqrt'])

############################################################################
print('#' * 52 + ' fraction')

import fractions

print(fractions.__dict__)
print(fractions.__file__)

############################################################################
print('#' * 52 + ' types')

import types

print(isinstance(fractions, types.ModuleType))

help(types.ModuleType)

mod = types.ModuleType('point', 'A module for handling points.')

print(mod)

help(mod)

from collections import namedtuple
mod.Point = namedtuple('Point', 'x y')

def points_distance(pt1, pt2):
    return math.sqrt((pt1.x - pt2.x) ** 2 + (pt1.y - pt2.y) ** 2)
mod.distance = points_distance

print(mod.__dict__)

p1 = mod.Point(0, 0)
p2 = mod.Point(1, 1)

print(mod.distance(p1, p2))


