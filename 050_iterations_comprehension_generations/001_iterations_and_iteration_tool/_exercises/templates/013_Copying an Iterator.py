# # "Copying" an Iterator
# # Sometimes we may have an iterator that we want to use multiple times for some reason.
# # As we saw, iterators get exhausted, so
# # simply making multiple references to the same iterator will not work -
# # they will just point to the same iterator object.
# #
# # What we would really like is a way to "copy" an iterator and use these copies independently of each other.
# #
# # As you can see iters is a tuple contains 3 iterators - let's put them into some variables and see what each one is:
#
# f__ it.... _____ te.
#
# ___ squares n
#     ___ i i_ ra__ n
#         y___ i**2
#
# gen _ squares 10
# gen
#
# iters _ te. s.. 10; 3
# it.
#
# iter1, iter2, iter3 _ iters
# n___iter1 n___ iter1 n___ iter1
# n___ iter2 n___ iter2
# n___ iter3
#
# # "Copying" an Iterator
# # As you can see, iter1, iter2, and iter3 are essentially three independent "copies" of our original
# # iterator (squares(10))
# # Note that this works for any iterable, so even sequence types such as lists:
# # But you'll notice that the elements of lists are not lists themselves!
# #
# # As you can see, the elements returned by tee are actually iterators -
# # even if we used an iterable such as a list to start off with!
#
# l _ 1 2 3 4
# lists _ te. l 2
# l.... 0
# l.... 1
#
# li__ l.... 0
# li__ l.... 0
#
# l.... 1 i_ l.... 1 .__it__
# '__next__' i_ di. l.... 1
