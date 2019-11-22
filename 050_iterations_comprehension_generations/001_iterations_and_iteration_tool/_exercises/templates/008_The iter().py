# # The iter() Function
# # As we have seen before, the iter() function is used to request an iterator object from an iterable
# # And we can use that iterator to iterate the collection by calling next() until a StopIteration exception is raised.
#
# l _ 1 2 3 4  # list
# l_iter _ it__l
# ty__ l_iter
# n___ l_iter
# n___ l_iter
#
# # The iter() Function
# # class Squares with __getitem__
#
# c_ Squares
#     ___ __init__ ____ n
#         ____._n _ n
#
#     ___ __len__ ____
#         r_ ____._n
#
#     ___ __getitem______ i
#         i_ i >_ ____._n:
#             r... IndexError
#         e___
#             r_ i ** 2
#
#
# ___ i i_ sq
#     print i
#
# sq_iter _ it__(sq)
# ty__(sq_iter)
# '__next__' i_ di. s_i..
#
#
# # How to test if an object is iterable
# # Basically an object is iterable if it:
# #     implements the iterable protocol (__iter__ that returns an iterator)
# #     implements the sequence protocol (__getitem__, and __len__) - although __len__ is not required for iteration
# #  the best way, if you have some need to detect if something is iterable or not, is the following:
#
# ___ is_iterable obj
#     t__
#         it__ obj
#         r_ T...
#     e___ T..E..
#         r_ F...
#
# i._i..(S..I..
# i._i...S.. 5
#
# # In this example we are going to create a counter function (using a closure) - it's a pretty simplistic function -
# # counter() will return a closure that we can then call to increment an internal counter by 1 every time it is called:
#
# ___ counter
#     i _ 0
#
#     ___ inc
#         non___ i
#         i +_ 1
#         r_ i
#
#     r_ in.
#
#
# cnt _ co...
# cn.
# cn.
#
# # you may want to iterater through random numbers until a specific random number is generated:
#
# _______ random
# ran___.se___ 0
# ___ i i_ ra__ 10
#     print i ran___.r...i.. 0 10
#
# random_iterator _ it__(l____  ran___.r..i.. 0 10|; 8
#
# ran___.s... 0
#
# ___ num i_ r.._i..
#     print num
#
# #  try a countdown example like the one we discussed in the lecture.
# ___ countdown start_10
#     ___ run
#         non___ start
#         start -_ 1
#         r_ start
#     r_ r..
#
# takeoff _ countdown 10
# ___ _ i_ ra__ 15
#     print t...
#
# takeoff  _ countdown 10
# takeoff_iter _ it__ t.... -1
# ___ val i_ ta.._it..
#     print v..
