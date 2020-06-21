from collections import defaultdict, Counter

# Using Repeated Iteration

c1 = Counter('abba')
c1
# Counter({'a': 2, 'b': 2})

for c in c1:
    print(c)

# a
# b

# However, we can have an iteration that repeats the counter keys as many times as the indicated frequency:

for c in c1.elements():
    print(c)

# a
# a
# b
# b

# What's interesting about this functionality is that we can turn this around and use it as a way
# to create an iterable that has repeating elements.
# Suppose we want to to iterate through a list of (integer) numbers that are each repeated as many times as the number
# itself.
# For example 1 should repeat once, 2 should repeat twice, and so on.
# This is actually not that easy to do!
# Here's one possible way to do it:

l = []
for i in range(1, 11):
    for _ in range(i):
        l.append(i)
print(l)

# [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9,
# 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

# But we could use a Counter object as well:

c1 = Counter()
for i in range(1, 11):
    c1[i] = i
c1
# Counter({1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10})

print(c1.elements())

# So you'll notice that we have a chain object here. That's one big advantage to using the Counter object -
# the repeated iterable does not actually exist as list like our previous implementation - this is a lazy iterable,
# so this is far more memory efficient.
# And we can iterate through that chain quite easily:

for i in c1.elements():
    print(i, end=', ')

# 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9,
# 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,

# Just for fun, how could we reproduce this functionality using a plain dictionary?


class RepeatIterable:
    def __init__(self, **kwargs):
        self.d = kwargs
    def __setitem__(self, key, value):
        self.d[key] = value
    def __getitem__(self, key):
        self.d[key] = self.d.get(key, 0)
        return self.d[key]

r = RepeatIterable(x=10, y=20)
print(r.d)
# {'x': 10, 'y': 20}

r['a'] = 100
print(r['a'])
# 100

r['b']
# 0

print(r.d)
# {'x': 10, 'y': 20, 'a': 100, 'b': 0}

print(r.d)
# {'x': 10, 'y': 20, 'a': 100, 'b': 0}

# Now we have to implement that elements iterator:

class RepeatIterable:
    def __init__(self, **kwargs):
        self.d = kwargs

    def __setitem__(self, key, value):
        self.d[key] = value

    def __getitem__(self, key):
        self.d[key] = self.d.get(key, 0)
        return self.d[key]

    def elements(self):
        for k, frequency in self.d.items():
            for i in range(frequency):
                yield k

r = RepeatIterable(a=2, b=3, c=1)

for e in r.elements():
    print(e, end=', ')
# a, a, b, b, b, c, 

