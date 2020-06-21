list(zip(range(5), range(100)))
# [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]

# If trailing or unmatched values are important to you, then you can use itertools.zip_longest() instead of zip().
# With this function, the missing values will be replaced with whatever you pass to the fillvalue argument
# (defaults to None). The iteration will continue until the longest iterable is exhausted:

from itertools import zip_longest
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
longest = range(5)
zipped = zip_longest(numbers, letters, longest, fillvalue='?')
list(zipped)
# [(1, 'a', 0), (2, 'b', 1), (3, 'c', 2), ('?', '?', 3), ('?', '?', 4)]