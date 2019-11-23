from collections import defaultdict, Counter

# It is so common to create a frequency distribution of elements in an iterable, that this is supported automatically:

c1 = Counter('able was I ere I saw elba')
print(c1)

# Counter({'a': 4,
#          'b': 2,
#          'l': 2,
#          'e': 4,
#          ' ': 6,
#          'w': 2,
#          's': 2,
#          'I': 2,
#          'r': 1})

# Of course this works for iterables in general, not just strings:

import random

random.seed(0)

my_list = [random.randint(0, 10) for _ in range(1_000)]
c2 = Counter(my_list)
c2

# Counter({6: 95,
#          0: 97,
#          4: 91,
#          8: 76,
#          7: 94,
#          5: 89,
#          9: 85,
#          3: 80,
#          2: 88,
#          1: 107,
#          10: 98})

# We can also initialize a Counter object by passing in keyword arguments, or even a dictionary:

c2 = Counter(a=1, b=10)
print(c2)

Counter({'a': 1, 'b': 10})
c3 = Counter({'a': 1, 'b': 10})
print(c3)

# Counter({'a': 1, 'b': 10})

# Technically we can store values other than integers in a Counter object - it's possible but of limited use since
# the default is still 0 irrespective of what other values are contained in the object.
