from collections import defaultdict, Counter

# Mathematical Operations
# These Counter objects also support several other mathematical operations when both operands are Counter objects.
# In all these cases the result is a new Counter object.
#     +: same as update, but returns a new Counter object instead of an in-place update.
#     -: subtracts one counter from another, but discards zero and negative values
#     &: keeps the minimum of the key values
#     |: keeps the maximum of the key values

c1 = Counter('aabbcc')
c2 = Counter('abc')
print(c1 + c2)
# Counter({'a': 3, 'b': 3, 'c': 3})

print(c1 - c2)
# Counter({'a': 1, 'b': 1, 'c': 1})

c1 = Counter(a=5, b=1)
c2 = Counter(a=1, b=10)
print(c1 & c2)
# Counter({'a': 1, 'b': 1})

print(c1 | c2)
# Counter({'a': 5, 'b': 10})

# The unary + can also be used to remove any non-positive count from the Counter:

c1 = Counter(a=10, b=-10)
print(+c1)
# Counter({'a': 10})

# The unary - changes the sign of each counter, and removes any non-positive result:

print(-c1)
# Counter({'b': 10})