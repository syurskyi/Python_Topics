values = ["a", "b", "c"]

for value in values:
    print(value)

# a
# b
# c

index = 0

for value in values:
    print(index, value)
    index += 1

# 0 a
# 1 b
# 2 c

index = 0

for value in values:
    print(index, value)

# 0 a
# 0 b
# 0 c

for index in range(len(values)):
    value = values[index]
    print(index, value)

# 0 a
# 1 b
# 2 c

for count, value in enumerate(values):
    print(count, value)

# 0 a
# 1 b
# 2 c

print(values[0])
# a


for count, value in enumerate(values, start=1):
    print(count, value)

# 1 a
# 2 b
# 3 c

def check_whitespace(lines):
    """Check for whitespace and line length issues."""
    for lno, line in enumerate(lines):
        if "\r" in line:
            yield lno+1, "\\r in line"
        if "\t" in line:
            yield lno+1, "OMG TABS!!!1"
        if line[:-1].rstrip(" \t") != line[:-1]:
            yield lno+1, "trailing whitespace"

users = ["Test User", "Real User 1", "Real User 2"]
for index, user in enumerate(users):
    if index == 0:
        print("Extra verbose output for:", user)
    print(user)

# Extra verbose output for: Test User
# Real User 1
# Real User 2


def even_items(iterable):
    """Return items from ``iterable`` when their index is even."""
    values = []
    for index, value in enumerate(iterable, start=1):
        if not index % 2:
            values.append(value)
    return values


def even_items(iterable):
    return [v for i, v in enumerate(iterable, start=1) if not i % 2]

seq = list(range(1, 11))

print(seq)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_items(seq)
# [2, 4, 6, 8, 10]

alphabet = "abcdefghijklmnopqrstuvwxyz"

even_items(alphabet)
# ['b', 'd', 'f', 'h', 'j', 'l', 'n', 'p', 'r', 't', 'v', 'x', 'z']

list(alphabet[1::2])
# ['b', 'd', 'f', 'h', 'j', 'l', 'n', 'p', 'r', 't', 'v', 'x', 'z']

def alphabet():
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for a in alpha:
        yield a

# alphabet[1::2]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'function' object is not subscriptable

even_items(alphabet())
# ['b', 'd', 'f', 'h', 'j', 'l', 'n', 'p', 'r', 't', 'v', 'x', 'z']

def my_enumerate(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1


seasons = ["Spring", "Summer", "Fall", "Winter"]

my_enumerate(seasons)
# <generator object my_enumerate at 0x7f48d7a9ca50>

list(my_enumerate(seasons))
# [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]

list(my_enumerate(seasons, start=1))
# [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]

####################### Unpacking Arguments With enumerate()

tuple_2 = (10, "a")
first_elem, second_elem = tuple_2
first_elem
# 10
second_elem
# 'a'

values = ["a", "b"]
enum_instance = enumerate(values)
enum_instance
# <enumerate at 0x7fe75d728180>
next(enum_instance)
# (0, 'a')
next(enum_instance)
# (1, 'b')
# next(enum_instance)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration

first = ["a", "b", "c"]
second = ["d", "e", "f"]
third = ["g", "h", "i"]
for one, two, three in zip(first, second, third):
    print(one, two, three)

# a d g
# b e h
# c f i

for count, (one, two, three) in enumerate(zip(first, second, third)):
    print(count, one, two, three)

# 0 a d g
# 1 b e h
# 2 c f i

for count, (one, two, three) in enumerate(zip(first, second, third)):
    print(count, one, two, three)

# 0 a d g
# 1 b e h
# 2 c f i
