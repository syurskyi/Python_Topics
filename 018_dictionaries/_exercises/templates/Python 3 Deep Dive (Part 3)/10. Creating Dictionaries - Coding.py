a = {'k1': 100, 'k2': 200}
print(a)

print(hash((1, 2, 3)))

# hash([1, 2, 3]) TypeError: unhashable type: 'list'

print('#' * 52 + ' So we can create dictionaries that look like this: ')

a = {('a', 100): ['a', 'b', 'c'], 'key2': {'a': 100, 'b': 200}}
print(a)

print('#' * 52 + ' Interestingly, functions are hashable: ')

def my_func(a, b, c):
    print(a, b, c)

print(hash(my_func))

print('#' * 52 + ' Which means we can use functions as keys in dictionaries: ')
d = {my_func: [10, 20, 30]}
print(d)

print('#' * 52 + ' A simple application of this might be to store the argument values we want to use to call the '
                 'function at a later time: ')

def fn_add(a, b):
    return a + b

def fn_inv(a):
    return 1/a

def fn_mult(a, b):
    return a * b

funcs = {fn_add: (10, 20), fn_inv: (2,), fn_mult: (2, 8)}
print(funcs)

print('#' * 52 + ' Remember that when we iterate through a dictionary we are actually iterating through the keys: ')

for f in funcs:
    print(f)

for f in funcs:
    result = f(*funcs[f])
    print(result)

print('#' * 52 + ' We can also iterate through the items (as tuples) in a dictionary as follows: ')

for f, args in funcs.items():
    print(f, args)

for f, args in funcs.items():
    result = f(*args)
    print(result)

print('#' * 52 + ' #### Using the class constructor ')

d = dict(a=100, b=200)
print(d)

print('#' * 52 + ' We can also build a dictionary by passing it an iterable containing the keys and the values: ')

d = dict([('a', 100), ('b', 200)])
print(d)

print('#' * 52 + ' The restriction here is that the elements of the iterable must themselves be iterables with exactly'
                 ' two elements.  ')

d = dict([('a', 100), ['b', 200]])
print(d)

print('#' * 52 + ' Of course we can also pass a dictionary as well:  ')

d = {'a': 100, 'b': 200, 'c': {'d': 1, 'e': 2}}

print(id(d))

print('#' * 52 + '  And lets create a dictionary: ')

new_dict = dict(d)
print(new_dict)
print(id(new_dict))

print('#' * 52 + '  As you can see, we have a new object - however, what about the nested dictionary? ')

print(id(d['c']), id(new_dict['c']))

print('#' * 52 + '  #### Using Comprehensions ')

keys = ['a', 'b', 'c']
values = (1, 2, 3)

print('#' * 52 + '  We can then easily create a dictionary this way - the non-Pythonic way! ')

d = {}  # creates an empty dictionary
for k, v in zip(keys, values):
    d[k] = v

print(d)

print('#' * 52 + ' But it is much simpler to use a dictionary comprehension:  ')

d = {k: v for k, v in zip(keys, values)}
print(d)

print('#' * 52 + '  Dictionary comprehensions support the same syntax as list comprehensions - you can have'
                 '  nested loops, `if` statements, etc. ')

keys = ['a', 'b', 'c', 'd']
values = (1, 2, 3, 4)

d = {k: v for k, v in zip(keys, values) if v % 2 == 0}
print(d)

print('#' * 52 + '  ')

x_coords = (-2, -1, 0, 1, 2)
y_coords = (-2, -1, 0, 1, 2)

grid = [(x, y)
         for x in x_coords
         for y in y_coords]
print(grid)

print('#' * 52 + ' We can use the `math` modules `hypot` function to do calculate these distances ')

import math
print(math.hypot(1, 1))

grid_extended = [(x, y, math.hypot(x, y)) for x, y in grid]
print(grid_extended)

print('#' * 52 + ' We can now easily tweak this to make a dictionary, where the coordinate pairs are the key, '
                 ' and the distance the value: ')

grid_extended = {(x, y): math.hypot(x, y) for x, y in grid}
print(grid_extended)

print('#' * 52 + '  #### Using `fromkeys` ')
print('#' * 52 + ' The `dict` class also provides the `fromkeys` method that we can use to create dictionaries.'
                 ' This class method is used to create a dictionary from an iterable containing the keys, and'
                 ' a **single** value used to assign to each key. ')

counters = dict.fromkeys(['a', 'b', 'c'], 0)
print(counters)

print('#' * 52 + ' If we do not specify a value, then `None` is used:  ')

d = dict.fromkeys('abc')
print(d)

print('#' * 52 + ' Notice how I used the fact that strings are iterables to specify the three single character '
                 'keys for this dictionary!  ')
print('#' * 52 + ' `fromkeys` method will insert the keys in the order in which they are retrieved from the iterable: ')

d = dict.fromkeys('python')
print(d)
print((d))




