__author__ = 'sergejyurskyj'


L1 = [1, ('a', 3)]         # Same value, unique objects
L2 = [1, ('a', 3)]
print(L1 == L2, L1 is L2)         # Equivalent? Same object?

S1 = 'spam'
S2 = 'spam'

print(S1 == S2, S1 is S2)


S1 = 'a longer string'
S2 = 'a longer string'
print(S1 == S2, S1 is S2)

L1 = [1, ('a', 3)]
L2 = [1, ('a', 2)]

print('#' * 52 + ' Less, equal, greater: tuple of results')
print(L1 < L2, L1 == L2, L1 > L2)     # Less, equal, greater: tuple of results

D1 = {'a':1, 'b':2}
D2 = {'a':1, 'b':3}
print(D1 == D2)
# print(D1 < D2)

D1 = {'a':1, 'b':2}
D2 = {'a':1, 'b':3}
print(D1 == D2)

# D1 < D2 # TypeError: unorderable types: dict() < dict()

list(D1.items())
sorted(D1.items())

print(sorted(D1.items()) < sorted(D2.items()))

print(sorted(D1.items()) > sorted(D2.items()))

L = [None] * 100

print(L)

