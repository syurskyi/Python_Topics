# -*- coding: utf-8 -*-

__author__ = 'sergejyurskyj'


type([1]) == type([])             # Type of another list
type([1]) == list                 # List type name
isinstance([1], list)             # List or customization thereof

import types                      # types has names for other types
def f(): pass
type(f) == types.FunctionType

L = [1, 2, 3]
M = ['X', L, 'Y']      # Embed a reference to L
print('#' * 52 + ' Embed a reference to L')
print(M)

print('#' * 52 + '  Changes M too')
L[1] = 0               # Changes M too
print(M)

print('#' * 52 + '  Embed a copy of L and Changes only L, not M')
L = [1, 2, 3]
M = ['X', L[:], 'Y']   # Embed a copy of L
L[1] = 0               # Changes only L, not M

print(L)

print(M)

L = [4, 5, 6]
X = L * 4              # Like [4, 5, 6] + [4, 5, 6] + ...
Y = [L] * 4            # [L] + [L] + ... = [L, L,...]

print('#' * 52 + '  Like [4, 5, 6] + [4, 5, 6] + ...')
print(X)

print('#' * 52 + '  [L] + [L] + ... = [L, L,...]')
print(Y)

L[1] = 0               # Impacts Y but not X
print('#' * 52 + '  Impacts Y but not X')
print(X)

print(Y)

L = ['grail']         # Append reference to same object
L.append(L)           # Generates cycle in object: [...]
print('#' * 52 + '  Append reference to same object. Generates cycle in object: [...] ')
print(L)

T = (1, 2, 3)
# T[2] = 4                 # Error!

print('#' * 52 + '  OK: (1, 2, 4)')
T = T[:2] + (4,)         # OK: (1, 2, 4)
print(T)