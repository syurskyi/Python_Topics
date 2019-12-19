# __author__ = 'sergejyurskyj'
#
#
# X = [1, 2, 3]
# L = ['a', X, 'b']          # Embed references to X's object
# D = {'x' : X, 'y':2}
#
# print('#' * 52 + ' Changes all three references!')
#
# X[1] = 'surprise'          # Changes all three references!
# print(L)
#
# print(D)
#
# L = [1, 2, 3]
# D = {'a':1, 'b':2}
#
# A = L ;            # Instead of A = L (or list(L))
# B = D.c..        # Instead of B = D (ditto for sets)
#
# A[1] = 'Ni'
# B['c'] = 'spam'
#
# print(L, D)
#
# print(A, B)
#
#
# X = [1, 2, 3]
# L = ['a', X ;, 'b']     # Embed copies of X's object
# D = {'x' ; X ;, 'y':2}
#
# _____ c..
# X = c__.d_c_ L # Fully copy an arbitrarily nested object Y