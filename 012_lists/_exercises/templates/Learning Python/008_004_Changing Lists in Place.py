__author__ = 'sergejyurskyj'

L = ['spam', 'Spam', 'SPAM!']
L[1] = 'eggs'                         # Index assignment
print(L)

L[0:2] = ['eat', 'more']              # Slice assignment: delete+insert
print(L)                                     # Replaces items 0,1

L.append('please')                    # Append method call: add item at end
print(L)

print('#' * 52 + ' Sort list items')

L.sort()                              # Sort list items ('S' < 'e')
print(L)

L = ['abc', 'ABD', 'aBe']
L.sort()                              # Sort with mixed case
print(L)

L = ['abc', 'ABD', 'aBe']
L.sort(key=str.lower)                 # Normalize to lowercase
print(L)

L = ['abc', 'ABD', 'aBe']
L.sort(key=str.lower, reverse=True)   # Change sort order
print(L)

print('#' * 52 + ' Sorting built-in')
L = ['abc', 'ABD', 'aBe']
print(sorted(L, key=str.lower, reverse=True))         # Sorting built-in

L = ['abc', 'ABD', 'aBe']
print(sorted([x.lower() for x in L], reverse=True))   # Pretransform items: differs!

print('#' * 52 + ' Add many items at end')
L = [1, 2]
L.extend([3,4,5])           # Add many items at end
print(L)

print('#' * 52 + ' Delete and return last item')
L.pop()                     # Delete and return last item
print(L)

print('#' * 52 + ' In-place reversal method')
L.reverse()                 # In-place reversal method
print(L)

print(list(reversed(L)))           # Reversal built-in with a result

print('#' * 52 + ' Push onto stack')
L = []
L.append(1)    # Push onto stack
L.append(2)
print(L)
L.pop()        # Pop off stack
print(L)

print('#' * 52 + ' Index of an object')
L = ['spam', 'eggs', 'ham']
print(L.index('eggs'))               # Index of an object

print('#' * 52 + ' Insert at position')
L.insert(1, 'toast')          # Insert at position
print(L)

print('#' * 52 + ' Delete by value')
L.remove('eggs')              # Delete by value
print(L)

print('#' * 52 + ' Delete by position')
L.pop(1)                      # Delete by position
'toast'
print(L)

print('#' * 52 + ' Delete one item')
del L[0]                           # Delete one item
print(L)

print('#' * 52 + ' Delete an entire section, Same as L[1:] = []')
del L[1:]                          # Delete an entire section
print(L)                                  # Same as L[1:] = []

print('#' * 52)
L = ['Already', 'got', 'one']
L[1:] = []
print(L)
L[0] = []
print(L)
