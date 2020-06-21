# Generator Functions and Expressions
# Generator expressions versus map
#  Map function on tuple
#  Generator expression
#  Nonfunction case
# Simpler as generator?

print(list(map(abs, (-1, -2, 3, 4))))  # Map function on tuple

print(list(abs(x) for x in (-1, -2, 3, 4)))  # Generator expression

print(list(map(lambda x: x * 2, (1, 2, 3, 4))))  # Nonfunction case

print(list(x * 2 for x in (1, 2, 3, 4)))  # Simpler as generator?


# Generator expressions versus map
# using (''.join
#  Makes a pointless list
#  Generates results
# Generates results
# impler as generator?

line = 'aaa,bbb,ccc'

print(''.join([x.upper() for x in line.split(',')]))  # Makes a pointless list

print(''.join(x.upper() for x in line.split(',')))  # Generates results

print(''.join(map(str.upper, line.split(','))))  # Generates results

print(''.join(x * 2 for x in line.split(',')))  # Simpler as generator?

print(''.join(map(lambda x: x * 2, line.split(','))))

# Generator expressions versus map
# [x * 2 for x in [abs(x)
#  Nested comprehensions
# Nested maps
# Nested generators
# Nested combinations

print([x * 2 for x in [abs(x) for x in (-1, -2, 3, 4)]])  # Nested comprehensions

print(list(map(lambda x: x * 2, map(abs, (-1, -2, 3, 4)))))  # Nested maps

print(list(x * 2 for x in (abs(x) for x in (-1, -2, 3, 4))))  # Nested generators

import math

print(list(map(math.sqrt, (x ** 2 for x in range(4)))))  # Nested combinations

# Generator expressions versus filter
# (''.join(x for x in line.split()
#  Generator with 'if'
#  Similar to filter using lambda


line = 'aa bbb c'

print(''.join(x for x in line.split() if len(x) > 1))  # Generator with 'if'

print(''.join(filter(lambda x: len(x) > 1, line.split())))  # Similar to filter

print(''.join(x.upper() for x in line.split() if len(x) > 1))

print(''.join(map(str.upper, filter(lambda x: len(x) > 1, line.split()))))

print(''.join(x.upper() for x in line.split() if len(x) > 1))

print()

res = ''
for x in line.split():
    if len(x) > 1:
        res += x.upper()
print(res)
