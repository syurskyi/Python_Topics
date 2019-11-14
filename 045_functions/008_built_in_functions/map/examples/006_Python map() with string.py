def to_upper_case(s):
    return str(s).upper()

def print_iterator(it):
    for x in it:
        print(x, end=' ')
    print('')  # for new line

# map() with string
map_iterator = map(to_upper_case, 'abc')
print(type(map_iterator))
print_iterator(map_iterator)

# Output:
# <class 'map'>
# A B C

# Python map() with tuple

# map() with tuple
map_iterator = map(to_upper_case, (1, 'a', 'abc'))
print_iterator(map_iterator)

# Output:
# 1 A ABC

# Python map() with list


map_iterator = map(to_upper_case, ['x', 'a', 'abc'])
print_iterator(map_iterator)

# X A ABC

# Converting map to list, tuple, set

map_iterator = map(to_upper_case, ['a', 'b', 'c'])
my_list = list(map_iterator)
print(my_list)

map_iterator = map(to_upper_case, ['a', 'b', 'c'])
my_set = set(map_iterator)
print(my_set)

map_iterator = map(to_upper_case, ['a', 'b', 'c'])
my_tuple = tuple(map_iterator)
print(my_tuple)

# Output:
# ['A', 'B', 'C']
# {'C', 'B', 'A'}
# ('A', 'B', 'C')

# Python map() with lambda

list_numbers = [1, 2, 3, 4]

map_iterator = map(lambda x: x * 2, list_numbers)
print_iterator(map_iterator)

# Output:
# 2 4 6 8

# map() with multiple iterable arguments
list_numbers = [1, 2, 3, 4]
tuple_numbers = (5, 6, 7, 8)
map_iterator = map(lambda x, y: x * y, list_numbers, tuple_numbers)
print_iterator(map_iterator)

# Output: 5 12 21 32

# map() with multiple iterable arguments of different sizes
list_numbers = [1, 2, 3, 4]
tuple_numbers = (5, 6, 7, 8, 9, 10)
map_iterator = map(lambda x, y: x * y, list_numbers, tuple_numbers)
print_iterator(map_iterator)

map_iterator = map(lambda x, y: x * y, tuple_numbers, list_numbers)
print_iterator(map_iterator)

# Output:
# 5 12 21 32
# 5 12 21 32

# Python map() with function None

map_iterator = map(None, 'abc')
print(map_iterator)
for x in map_iterator:
    print(x)

# Output:
#
#
# Traceback (most recent call last):
#   File "/Users/pankaj/Documents/github/journaldev/Python-3/basic_examples/python_map_example.py", line 3, in <module>
#     for x in map_iterator:
# TypeError: 'NoneType' object is not callable

