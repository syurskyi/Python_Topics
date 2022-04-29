import logging
from pprint import pprint
from sys import stdout as STDOUT


# Example 1
def normalize(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


# Example 2
visits = [15, 35, 80]
percentages = normalize(visits)
print(percentages)


# Example 3
path = 'my_numbers.txt'
with open(path, 'w') as f:
    for i in (15, 35, 80):
        f.write('%d\n' % i)

def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)


# Example 4
it = read_visits('my_numbers.txt')
percentages = normalize(it)
print(percentages)


# Example 5
it = read_visits('my_numbers.txt')
print(list(it))
print(list(it))  # Already exhausted


# Example 6
def normalize_copy(numbers):
    numbers = list(numbers)  # Copy the iterator
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


# Example 7
it = read_visits('my_numbers.txt')
percentages = normalize_copy(it)
print(percentages)


# Example 8
def normalize_func(get_iter):
    total = sum(get_iter())   # New iterator
    result = []
    for value in get_iter():  # New iterator
        percent = 100 * value / total
        result.append(percent)
    return result


# Example 9
percentages = normalize_func(lambda: read_visits(path))
print(percentages)


# Example 10
class ReadVisits(object):
    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)


# Example 11
visits = ReadVisits(path)
percentages = normalize(visits)
print(percentages)


# Example 12
def normalize_defensive(numbers):
    if iter(numbers) is iter(numbers):  # An iterator -- bad!
        raise TypeError('Must supply a container')
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


# Example 13
visits = [15, 35, 80]
normalize_defensive(visits)  # No error
visits = ReadVisits(path)
normalize_defensive(visits)  # No error


# Example 14
try:
    it = iter(visits)
    normalize_defensive(it)
except:
    logging.exception('Expected')
else:
    assert False
