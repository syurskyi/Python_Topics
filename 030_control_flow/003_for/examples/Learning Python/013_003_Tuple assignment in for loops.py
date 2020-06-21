__author__ = 'sergejyurskyj'


print('#' * 52 + ' Tuple assignment at work')
T = [(1, 2), (3, 4), (5, 6)]
for (a, b) in T:                   # Tuple assignment at work
    print(a, b)

print('#' * 52 + ' Use dict keys iterator and index')
D = {'a': 1, 'b': 2, 'c': 3}
for key in D:
   print(key, '=>', D[key])             # Use dict keys iterator and index

list(D.items())

print('#' * 52 + ' Iterate over both keys and values')
for (key, value) in D.items():
   print(key, '=>', value)              # Iterate over both keys and values

print(T)


print('#' * 52 + ' Manual assignment equivalent')
for both in T:
    a, b = both                         # Manual assignment equivalent
    print(a, b)

print('#' * 52 + ' Nested sequences work too')
((a, b), c) = ((1, 2), 3)               # Nested sequences work too
print(a, b, c)


for ((a, b), c) in [((1, 2), 3), ((4, 5), 6)]: print(a, b, c)

for ((a, b), c) in [([1, 2], 3), ['XY', 6]]: print(a, b, c)
