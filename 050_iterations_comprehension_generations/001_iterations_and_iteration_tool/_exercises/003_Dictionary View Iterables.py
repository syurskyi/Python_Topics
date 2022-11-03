from __future__ import print_function

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


D = dict(a=1, b=2, c=3)
K = D.keys()
V = D.values()
print(V)
print(list(V))
print(list(D.items()))
for k, v in D.items(): print(k, v, end=' ')
print()
print(D)
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

from __future__ import print_function

D = dict(a=1, b=2, c=3)
K = D.keys()
V = D.values()

for k in sorted(D.keys()): print(k, D[k], end=' ')
print()

print(D)

for k in sorted(D): print(k, D[k], end=' ')
