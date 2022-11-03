# # Dictionary View Iterables
#
# D _ d.. a_1 b_2 c_3
# print D
# K _ D.k..  # Views are not iterators themselves. TypeError: 'dict_keys' object is not an iterator
# print K
#
# # Dictionary View Iterables
# # Views have an iterator
# # which can be used manually
# #  but does not support len(), index
# # All iteration contexts use auto
#
# f... __f.. _______ p.._f..
# D = d.. a_1 b_2 c_3
# K = D.k..
#
# I = i___ K
# print n___ I
# print n___ I
#
# ___ k __ D.k.. print k e.._' '
#
# # Dictionary View Iterables
# # Ditto for values() and items() views
# #
# #  Dictionaries still have own iterator, # Returns next key on each iteration
# #
# # Still no need to call keys() to iterate. But keys is an iterator in 3.0 too!
#
# f... __f.. _______ p.._f..
# D _ d.. a_1 b_2 c_3
# K _ D.k...
# V _ D.v...
# print(V)
# print l___ V
# print l___ D.items
# ___ k v __ D.i... print ? ? e.._' '
# print()
# print(D)
#
# I _ i___ D
# print n___ I
# print n___ I
#
# ___ key __ D print ? e.._' '
#
# # Dictionary View Iterables
# # sorted
#
#
# f... __f.. _______ p.._f..
#
# D _ d.. a_1 b_2 c_3
# K _ D.k..
# V _ D.v..
#
# ___ k __ so.. D.k.. print k D|k e.._' '
# print()
#
# print(D)
#
# ___ k __ so.. D print k D|k e.._' '
