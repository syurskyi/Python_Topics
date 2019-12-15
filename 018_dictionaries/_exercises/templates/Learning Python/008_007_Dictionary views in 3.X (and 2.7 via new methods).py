__author__ = 'sergejyurskyj'

D = dict(a=1, b=2, c=3)
print(D)

print('#' * 52 + ' Makes a view object in 3.0, not a list')
K = D.keys()                       # Makes a view object in 3.0, not a list
print(K)

print('#' * 52 + ' Force a real list in 3.0 if needed')
print(list(K))                            # Force a real list in 3.0 if needed

print('#' * 52 + ' Ditto for values and items views')
V = D.values()                     # Ditto for values and items views
print(V)
print(list(V))
print(list(D.items()))

print('#' * 52 + ' List operations fail unless converted')
#K[0]                               # List operations fail unless converted
                                    # TypeError: 'dict_keys' object does not support indexing
print(list(K)[0])

print('#' * 52 + ' Iterators used automatically in loops')
for k in D.keys(): print(k)        # Iterators used automatically in loops

print('#' * 52 + ' Still no need to call keys() to iterate')
for key in D: print(key)           # Still no need to call keys() to iterate


D = {'a':1, 'b':2, 'c':3}
print(D)

K = D.keys()
V = D.values()

print('#' * 52 + ' Views maintain same order as dictionary')
print(list(K))                # Views maintain same order as dictionary
print(list(V))

print('#' * 52 + ' Change the dictionary in-place')
del D['b']             # Change the dictionary in-place
print(D)

print('#' * 52 + ' Reflected in any current view objects')
print(list(K))                # Reflected in any current view objects

print('#' * 52 + ' Not true in 2.X!')
print(list(V))                # Not true in 2.X!
