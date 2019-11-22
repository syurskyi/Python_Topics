# Aggregators
# Suppose we want to test if an iterable contains only numeric values.
# First, we need to figure out how we determine if something is a number.

l = [10, 20, 30, 40]

is_all_numbers = True
for item in l:
    if not isinstance(item, Number):
        is_all_numbers = False
        break
print(is_all_numbers)

l = [10, 20, 30, 40, 'hello']

is_all_numbers = True
for item in l:
    if not isinstance(item, Number):
        is_all_numbers = False
        break
print(is_all_numbers)

# Aggregator
# Suppose we have a file and we want to make sure that all the rows in the file have length > some number.
# We can easily test to make sure that every brand in our file is at least 3 characters long:
# And we can test to see if any line is more than 10 characters:
# More than 13?
# Of course, we can also do this using generator expressions instead of map:

with open('car-brands.txt') as f:
    for row in f:
        print(len(row), row, end='')

with open('car-brands.txt') as f:
    result = all(map(lambda row: len(row) >= 3, f))
print(result)

with open('car-brands.txt') as f:
    result = any(map(lambda row: len(row) > 10, f))
print(result)

with open('car-brands.txt') as f:
    result = any(map(lambda row: len(row) > 13, f))
print(result)

with open('car-brands.txt') as f:
    result = any(len(row) > 13 for row in f)
print(result)
