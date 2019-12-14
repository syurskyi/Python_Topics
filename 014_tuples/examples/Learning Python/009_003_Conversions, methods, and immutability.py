T = ('cc', 'aa', 'dd', 'bb')
tmp = list(T)  # Make a list from a tuple's items
tmp.sort()  # Sort the list
print(tmp)
# ['aa', 'bb', 'cc', 'dd']
T = tuple(tmp)  # Make a tuple from the list's items
print(T)
# ('aa', 'bb', 'cc', 'dd')
print(sorted(T))  # Or use the sorted built-in, and save two steps
# ['aa', 'bb', 'cc', 'dd']

T = (1, 2, 3, 4, 5)
L = [x + 20 for x in T]
print(L)
# [21, 22, 23, 24, 25]

T = (1, 2, 3, 2, 4, 2)  # Tuple methods in 2.6, 3.0, and later
print(T.index(2))  # Offset of first appearance of 2
# 1
print(T.index(2, 2))  # Offset of appearance after offset 2
# 3
print(T.count(2))  # How many 2s are there?
# 3

T = (1, [2, 3], 4)
# T[1] = 'spam' # This fails: can't change tuple itself
# TypeError: object doesn't support item assignment
T[1][0] = 'spam'  # This works: can change mutables inside
print(T)
# (1, ['spam', 3], 4)
