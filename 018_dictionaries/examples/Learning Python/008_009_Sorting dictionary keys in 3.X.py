__author__ = 'sergejyurskyj'

D = {'a': 1, 'b': 2, 'c': 3}
print(D)

Ks = D.keys()                           # Sorting a view object doesn't work!
# Ks.sort()                               # AttributeError: 'dict_keys' object has no attribute 'sort'

print('#' * 52 + ' Force it to be a list and then sort')
Ks = list(Ks)                           # Force it to be a list and then sort
Ks.sort()
for k in Ks: print(k, D[k])

print('#' * 52 + ' Or you can use sorted() on the keys. orted() accepts any iterable , sorted() returns its result')
print(D)
Ks = D.keys()                           # Or you can use sorted() on the keys
for k in sorted(Ks): print(k, D[k])     # sorted() accepts any iterable , sorted() returns its result

print('#' * 52 + ' Better yet, sort the dict directly. dict iterators return keys')
print(D)                                # Better yet, sort the dict directly
for k in sorted(D): print(k, D[k])      # dict iterators return keys
