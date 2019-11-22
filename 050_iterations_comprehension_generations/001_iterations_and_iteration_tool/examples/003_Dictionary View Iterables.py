# Dictionary View Iterables

D = dict(a=1, b=2, c=3)
print(D)
K = D.keys()  # Views are not iterators themselves. TypeError: 'dict_keys' object is not an iterator
print(K)

# Dictionary View Iterables
# Views have an iterator
# which can be used manually
#  but does not support len(), index
# All iteration contexts use auto

from __future__ import print_function
D = dict(a=1, b=2, c=3)
K = D.keys()

I = iter(K)
print(next(I))
print(next(I))

for k in D.keys(): print(k, end=' ')

# Dictionary View Iterables
# Ditto for values() and items() views
#
#  Dictionaries still have own iterator, # Returns next key on each iteration
#
# Still no need to call keys() to iterate. But keys is an iterator in 3.0 too!

from __future__ import print_function
D = dict(a=1, b=2, c=3)
K = D.keys()
V = D.values()
print(V)
print(list(V))
print(list(D.items())
for (k, v) in D.items(): print(k, v, end=' ')
print()
print(D)

I = iter(D)
print(next(I))
print(next(I))

for key in D: print(key, end=' ')

# Dictionary View Iterables
# sorted


from __future__ import print_function

D = dict(a=1, b=2, c=3)
K = D.keys()
V = D.values()

for k in sorted(D.keys()): print(k, D[k], end=' ')
print()

print(D)

for k in sorted(D): print(k, D[k], end=' ')
