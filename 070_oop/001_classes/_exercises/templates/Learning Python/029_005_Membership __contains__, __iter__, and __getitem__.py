# f_ -f _______ p._f.
# c_ Iters
#     ___ - ____ value
#         ____.data = v..
#
#     ___ -g ____ i  # Fallback for iteration
#         print('get |/_:' / i e.._'')  # Also for index, slice
#         r_ ____.data i
#
#     ___ -i ____  # Preferred for iteration
#         print('iter=> ', e.._''  # Allows only 1 active iterator
#         ____.ix = 0
#         r_ ____
#
#     ___ -n ____
#         print('next:', e.._''
#         i_ ____.ix __ le. ____.data r.. S..
#         item = ____.d... ____.i_
#         ____.i. += 1
#         r_ ?
#
#     ___ -c ____ x  # Preferred for 'in'
#         print('contains: ', e.._''
#         r_ x i_ ____.da..
#
#
# X = ? 1, 2, 3, 4, 5  # Make instance
# print(3 in X)  # Membership
# ___ i i_ X  # For loops
#     print i e.._' | '
#
# print()
# print i ** 2 ___ i i_ X  # Other iteration contexts
# print li.. ma. bi. ?
#
# I = it.. ?  # Manual iteration (what other contexts do)
# w___ T..
#     t__
#         print n.. I e.._' @ '
#     e.... S..
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
