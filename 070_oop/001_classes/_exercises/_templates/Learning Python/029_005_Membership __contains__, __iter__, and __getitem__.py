# f_ -f _______ p._f.
# c_ Iters
#     ___ - ____ value
#         ____.data = ?
#
#     ___ -g ____ i  # Fallback for iteration
#         print('get|@:'  i e.._'')  # Also for index, slice # string
#         r_ ____.d.. ?
#
#     ___ -i ____  # Preferred for iteration
#         print('iter=> ', e.._''  # Allows only 1 active iterator
#         ____.ix = 0
#         r_ ____
#
#     ___ -n ____
#         print('next:', e.._''
#         __ ____.ix __ le. ____.d..
#             r.. S..
#         item = ____.d... ____.i_
#         ____.i. += 1
#         r_ ?
#
#     ___ -c ____ x  # Preferred for 'in'
#         print('contains: ', e.._''
#         r_ x i_ ____.d..
#
#
# X = ? 1, 2, 3, 4, 5  # Make instance
# print(3 in X)  # Membership
# ___ i __ ?  # For loops
#     print ? e.._' | '
#
# print()
# print i ** 2 ___ ? __ ?  # Other iteration contexts
# print li.. ma. bi. ?
#
# I = it.. ?  # Manual iteration (what other contexts do)
# w___ T..
#     ___
#         print n.. I e.._' @ '
#     _.... S..
#         b..
#
# X = ? 'spam'  # Indexing
# X[0]  # __getitem__(0)
# # get[0]:'s'
#
# 'spam'[1:]  # Slice syntax
#
# 'spam'[slice(1, None)]  # Slice object
#
#
# X[1:]  # __getitem__(slice(..))
# # get[slice(1, None, None)]:'pam'
# X[:-1]
# # get[slice(None, -1, None)]:'spa'
