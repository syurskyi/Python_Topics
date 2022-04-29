import logging
from pprint import pprint
from sys import stdout as STDOUT


# Example 9
def sort_priority(numbers, group):
    found = [False]
    def helper(x):
        if x in group:
            found[0] = True
            return (0, x)
        return (1, x)
    numbers.sort(key=helper)
    return found[0]

numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = set([2, 3, 5, 7])
found = sort_priority(numbers, group)
print('Found:', found)
print(numbers)
