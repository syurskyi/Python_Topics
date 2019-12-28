# __author__ = 'sergejyurskyj'
#
# L = ['spam', 'Spam', 'SPAM!']
# L 1 _ 'eggs'                         # Index assignment
# print L
#
# L 0 2 _ 'eat', 'more'              # Slice assignment: delete+insert
# print ?                                     # Replaces items 0,1
#
# ?.ap.. please                    # Append method call: add item at end
# print ?
#
# print('#' * 52 + ' Sort list items')
#
# ?.s..                              # Sort list items ('S' < 'e')
# print ?
#
# L = ['abc', 'ABD', 'aBe']
# ?.?                              # Sort with mixed case
# print L
#
# L = ['abc', 'ABD', 'aBe']
# ?.? k.._st_.l..                 # Normalize to lowercase
# print ?
#
# L = ['abc', 'ABD', 'aBe']
# ?.? k.._s__.l.. r.._T..   # Change sort order
# print ?
#
# print('#' * 52 + ' Sorting built-in')
# L = ['abc', 'ABD', 'aBe']
# print s.. ?, k.._s__.l.. r.._T..         # Sorting built-in
#
# L = 'abc', 'ABD', 'aBe'
# print s.. x.l.. ___ x i_ L r.._T..   # Pretransform items: differs!
#
# print('#' * 52 + ' Add many items at end')
# L = [1, 2]
# ?.e.. 3,4,5           # Add many items at end
# print ?
#
# print('#' * 52 + ' Delete and return last item')
# ?.p..                    # Delete and return last item
# print ?
#
# print('#' * 52 + ' In-place reversal method')
# ?.r..                 # In-place reversal method
# print ?
#
# print li.. r.. ?           # Reversal built-in with a result
#
# print('#' * 52 + ' Push onto stack')
# L =    # list
# ?.ap.. 1    # Push onto stack
# ?.ap.. 2
# print ?
# ?.p..       # Pop off stack
# print ?
#
# print('#' * 52 + ' Index of an object')
# L = ['spam', 'eggs', 'ham']
# print ?.i.. 'eggs               # Index of an object
#
# print('#' * 52 + ' Insert at position')
# ?.i.. 1 'toast')         # Insert at position
# print ?
#
# print('#' * 52 + ' Delete by value')
# ?.r.. eggs              # Delete by value
# print ?
#
# print('#' * 52 + ' Delete by position')
# ?.p.. 1                      # Delete by position
# 'toast'
# print ?
#
# print('#' * 52 + ' Delete one item')
# del ? 0                           # Delete one item
# print ?
#
# print('#' * 52 + ' Delete an entire section, Same as L[1:] = []')
# del ? 1;                          # Delete an entire section
# print ?                                 # Same as L[1:] = []
#
# print('#' * 52)
# L = ['Already', 'got', 'one']
# L 1; =  # list
# print ?
# L 0 =    # list
# print ?
