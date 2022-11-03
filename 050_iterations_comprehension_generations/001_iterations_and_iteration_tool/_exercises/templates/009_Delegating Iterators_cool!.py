# # Delegating Iterators
# # Technically we can see the underlying data by accessing the (pseudo) private variable _persons.
# # But we really would prefer making our PersonNames instances iterable.
# # To do so we need to implement the __iter__ method that returns an iterator that can be used for iterating over the _persons list.
# # And of course we can sort, use list comprehensions, and so on - our PersonNames is an iterable.
#
# f_ col__ _______ n..t..
# Person _ n_t_ 'Person', 'first last'
# c_ PersonNames
#     ___ __init__ ____  persons
#         ___:
#             ____._persons _ |p___.first.cap...
#                              + ' ' + p____.last.cap...
#                             ___ person i_ persons]
#         e___  T..E.. A..E..
#             ____._persons _    # List
#
# persons _ P... 'michaeL' 'paLin' P... 'eric', 'idLe'
#            P... 'john', 'cLeese'
#
# person_names _ P...N.. p....
# p._n_._pe..
# c_ PersonNames
#     ___ __init__ ____ persons
#         ___:
#             ____._p... _ p___.first.cap...
#                              + ' ' + p___.last.cap...
#                             ___ p___ i_ persons
#         e___ T..E..
#             ____._persons _   # list
#     ___ __iter__ ____
#         r_ it__ ____._persons
# persons _ P.. 'michaeL', 'paLin' P.. 'eric', 'idLe'
#            P.. 'john', 'cLeese'
# person_names _ P...N.. p...
# ___ p i_ p.._n.
#     print(p)
