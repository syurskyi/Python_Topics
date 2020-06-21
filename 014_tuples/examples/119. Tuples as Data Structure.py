print(('a', 10, True))

# But the parentheses are not what indicate a tuple - it is the commas:

a = ('a', 10, True)
b = 'b', 20, False

print('#' * 52 + '  But the parentheses are not what indicate a tuple - it is the commas:')
print(type(a))
print(type(b))

def iterate(t):
    for element in t:
        print(element)

# iterate(1, 2, 3)  # error


print('#' * 52 + '  Iteration')
iterate((1, 2, 3))

a = 'a', 10, True

print('#' * 52 + '  Index')
print(a[2])


print('#' * 52 + '  Slice')
a = 1, 2, 3, 4, 5
print(a[2:4])

print('#' * 52 + '  Iterate')
a = 1, 2, 3, 4, 5
for element in a:
    print(element)

print('#' * 52 + '  unpacking')
point = 10, 20, 30
x, y, z = point
print(x)
print(y)
print(z)

# Tuples are immutable, in the sense that we cannot change the reference of an object in the
# container and we cannot add  or remove objects from the container. This is the same as strings.

a = 10, 'python', True
# a[0] = 20 # TypeError: 'tuple' object does not support item assignment

# We can however 'extend' tuples, but just as with strings, we are actually just creating a new tuple:

print('#' * 52 + '  extend tuples creating a new tuple')

a = 1, 2, 3

print(id(a))

a = a + (4, 5, 6)
print(a)
print(id(a))

print('#' * 52 + '  define a simple point class to store the x and y coordinates of a point in 2D space')


class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'{self.__class__.__name__}(x={self.x}, y={self.y})'

a = Point2D(0, 0), Point2D(10, 10), Point2D(20, 20)

print(a)

print('#' * 52 + '  Although the tuple `a` is immutable, its contained elements are mutable:')
print('#' * 52 + '  But we can modify the contents of the first element:')

a[0].x = -10
print(a)

print('#' * 52 + '  Tuples as Data Records')

pt1 = (0, 0)
pt2 = (10, 10)

london = 'London', 'UK', 8_780_000
new_york = 'New York', 'USA', 8_500_000
beijing = 'Beijing', 'China', 21_000_000

cities = london, new_york, beijing

city_names = [t[0] for t in cities]
print(city_names)

total = 0
for city in cities:
    total += city[2]
print (f'total={total}')

print([city[2] for city in cities])

print('#' * 52 + '  Next we simply sum up the population values: ')
print(sum([city[2] for city in cities]))

print('#' * 52 + '  since tuples are sequence types, and hence iterable, we can also use unpacking to extract values '
                 'from the tuple:')


city, country, population = new_york

print(city)
print(country)
print(population)

print('#' * 52 + '  We can also use extended unpacking: ')

record = 'DJIA', 2018, 1, 19, 25_987, 26_072, 25_942, 26_072

symbol, year, month, day, open_, high, low, close = record

print(symbol)
print(close)

symbol, year, month, day, *others, close = record
print(symbol, year, month, day, close)
print(others)

print('#' * 52 + '  A convetion often used in Python when we are not particularly interested in something, is to use'
                 ' an underscore as a variable name: ')

symbol, year, month, day, *_, close = record

print(_)

print('#' * 52 + '  By the way do not write code like this to do the unpacking we just did: ')

symbol, year, close = record[0], record[1], record[7]
symbol, year, *_, close = record

for element in cities:
    print(element)

print('#' * 52 + '  As you can see, each element is a tuple, and we can actually unpack it at the same time as the loop'
                 ' this way: ')

for city, country, population in cities:
    print(f'city={city}, population={population}')

for index, value in enumerate(beijing):
    print(f'{index}: {value}')

for city, _, population in cities:
    print(f'city={city}, population={population}')

print('#' * 52 + '  Another frequent application of usign tuples as data structures is for returning multiple values'
                 ' from a function. ')

from random import uniform
from math import sqrt


def random_shot(radius):
    '''Generates a random 2D coordinate within
    the bounds [-radius, radius] * [-radius, radius]
    (a square of area 4)
    and also determines if it falls within
    a circle centered at the origin
    with specified radius'''

    random_x = uniform(-radius, radius)
    random_y = uniform(-radius, radius)

    if sqrt(random_x ** 2 + random_y ** 2) <= radius:
        is_in_circle = True
    else:
        is_in_circle = False

    return random_x, random_y, is_in_circle

num_attempts = 1_000_000
count_inside = 0
for i in range(num_attempts):
    *_, is_in_circle = random_shot(1)
    if is_in_circle:
        count_inside += 1

print(f'Pi is approximately: {4 * count_inside / num_attempts}')

