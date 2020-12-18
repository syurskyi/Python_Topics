# c_ Indexer:
#     ___ -g ____ index
#         r_ ? ** 2
#
# X = I.
# print('#' * 23 + '  X[i] calls X.__getitem__(i)')
# print(X[2])                                # X[i] calls X.__getitem__(i)
#
#
# # for i in range(5):
# #    print(X[i], end=' ')            # Runs __getitem__(X, i) each time
#
#
# L = [5, 6, 7, 8, 9]
# print('#' * 23 + ' Slice with slice syntax')
# print(L[2:4])                              # Slice with slice syntax
#
# print(L[1:])
#
# print(L[:-1])
#
# print(L[::2])
#
# print('#' * 23 + ' Slice with slice objects')
# print(L[slice(2, 4)])                      # Slice with slice objects
#
# print(L[slice(1, None)])
#
# print(L[slice(None, -1)])
#
# print(L[slice(None, None, 2)])
#
#
# c_ Indexer
#     data = [5, 6, 7, 8, 9]
#     ___ -g ____  index   # Called for index or slice
#         print('getitem:' ?
#         r_ ____.d. i..     # Perform index or slice
#
# X = I...
# print('#' * 23 + ' Indexing sends __getitem__ an integer')
# (X[0])                                # Indexing sends __getitem__ an integer
#
# X[1]
#
# X[-1]
#
# print('#' * 23 + ' Slicing sends __getitem__ a slice object')
# X[2:4]                              # Slicing sends __getitem__ a slice object
#
# X[1:]
#
# # X[:-1]
#
# X[::2]
#
#
# ___ -s_i_ ____ index value    # Intercept index or slice assignment
#
#     ____.data i..  = v..           # Assign index or slice
#
#
# # method __index is only in Python 3.0
# c_ C
#     ___ -i ____
#         r_ 255
#
# X = C()
# # print(hex(X))               # Integer value
#
# print(bin(X))
#
# # print(oct(X))
#
#
# print(('C' * 256)[255])
#
# print(('C' * 256)[X])       # As index (not X[i])
#
# print(('C' * 256)[X:])      # As index (not X[i:])
#
