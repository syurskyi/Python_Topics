# The range Iterable
R = range(10)
# range returns an iterator, not a list
print(R)
I = iter(R)
# Make an iterator from the range
print(next(I))  # Advance to next result
print(next(I))
print(next(I))
print(list(range(10)))  # To force a list if required

print(len(R))  # range also does len and indexing, but no others
print(R[0])
print(R[-1])

print(next(I))  # Continue taking from iterator, where left off
print(I.__next__())  # .next() becomes .__next__(), but use new next()

# The map  Iterable
M = map(abs, (-1, 0, 1))  # map returns an iterator, not a list
print(M)

print(next(M))  # Use iterator manually: exhausts results. hese do not support len() or indexing

print(next(M))

print(next(M))

# print(next(M))

for x in M: print(x)  # map iterator is now empty: one pass only

M = map(abs, (-1, 0, 1))  # Make a new iterator to scan again

for x in M: print(x)  # Iteration contexts auto call next()

print(list(map(abs, (-1, 0, 1))))  # Can force a real list if needed

# The zip Iterables
Z = zip((1, 2, 3), (10, 20, 30))  # zip is the same: a one-pass iterator

print(Z)

print(list(Z))

for pair in Z: print(pair)  # Exhausted after one pass

Z = zip((1, 2, 3), (10, 20, 30))

for pair in Z: print(pair)  # Iterator used automatically or manually

Z = zip((1, 2, 3), (10, 20, 30))
print(next(Z))
print(next(Z))

# The filter Iterables
print(filter(bool, ['spam', '', 'ni']))
print(list(filter(bool, ['spam', '', 'ni'])))

# Multiple Versus Single Pass Iterators
# Range

R = range(3)  # range allows multiple iterators

# print(next(R))                       # TypeError: range object is not an iterator

I1 = iter(R)
print(next(I1))
print(next(I1))

I2 = iter(R)  # Two iterators on one range
print(next(I2))

print(next(I1))  # I1 is at a different spot than I2

R = range(3)  # But range allows many iterators
I1, I2 = iter(R), iter(R)
print([next(I1), next(I1), next(I1)])

print(next(I2))  # Multiple active scans, like 2.X lists

# Multiple Versus Single Pass Iterators
# Zip

Z = zip((1, 2, 3), (10, 11, 12))

I1 = iter(Z)
I2 = iter(Z)  # Two iterators on one zip

print(next(I1))
print(next(I1))

print(next(I2))  # I2 is at same spot as I1!

# Multiple Versus Single Pass Iterators
# Map

M = map(abs, (-1, 0, 1))  # Ditto for map (and filter)
I1 = iter(M);
I2 = iter(M)
print(next(I1), next(I1), next(I1))

# next(I2)                              # (3.X) Single scan is exhausted! StopIteration
