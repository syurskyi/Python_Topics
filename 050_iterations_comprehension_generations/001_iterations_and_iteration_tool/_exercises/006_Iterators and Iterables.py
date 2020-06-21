# # Rolling our own Next method
# # implement a __len__ method to support the len() function
#
# c_ Squares
#     ___ - ____ length
#         ____.? _ ?
#         ____.i _ 0
#
#     ___ next_ ____
#         __ ____.i >_ ____.le...
#             r... S..It..
#         ____
#             result _ ____.i ** 2
#             ____.i +_ 1
#             r_ r...
#
#     ___ -l ____
#         r_ ____.le..
#
# sq _ Sq.. 3
# len(sq)
# sq.next_
# sq.next_
# sq.next_
# #
# # So now, we can essentially loop over the collection in a very similar way to how we did it with sequences and the __getitem__ method:
# #
# sq _ S... 5
# w___ T..
#     t..
#         print s_.next_
#     ____ S...I..
#         # reached end of iteration
#         # stop looping
#         b....
#
# # Iterating Collections
# # class RandomNumbers:
#
# import random
#
# c_ RandomNumbers
#     ___ - ____ length * range_min_0 range_max_10
#         ____.l... _ length
#         ____.r._m. _ range_min
#         ____.r.._m.. _ range_max
#         ____.n.._r... _ 0
#
#     ___ -l ____
#         r... ____.le...
#
#     ___ -n (____):
#         __ ____.n.._r.. >_ ____.le..
#             r.. S...I..
#         _____
#             ____.n.._r.. +_ 1
#             r_ ra___.rand___ ____.r.._m..  ____.r.._ma.
#
#
# numbers _ R... 10
# len nu...
#
# w____ T...
#     t..
#         print n.... nu..
#     _____ S...I..
#         b.....
#
# # We still cannot use a for loop, and if we want to 'restart' the iteration, we have to create a new object every time.
# #
# numbers _ R.... 10
#
# ___ item __ n....
#     print item #error
#
#
# # Iterators and Iterables
# # build class Cities
#
# c_ Cities:
#     ___ - ____
#         ____._cities _ 'New York' 'Newark' 'New Delhi' 'Newcastle'
#     ___ -l ____
#         r_ le. ____._cities
#     ___ -g ____ s
#         print 'getting item...'
#         r_ ____._cities |s
#     ___ -it ____
#         print Calling Cities instance __iter__
#         r_ ____.C...I... ____
#     c_ CityIterator:
#         ___ - ____ city_obj
#             # cities is an instance of Cities
#             print Calling CityIterator __init__
#             ____._c..._o.. _ city_obj
#             ____._index _ 0
#         ___ -it ____
#             print Calling CitiyIterator instance __iter__
#             r_ ____
#         ___ -n ____
#             print Calling __next__
#             __ ____._index >_ le. _____._c.._o..
#                 r.... S...I...
#             _____
#                 item _ ____._c___o__._cities ____._in___
#                 ____._in... +_ 1
#                 r_ it..
# # cities = Cities()
# # cities[0]
# # next(iter(cities))
# # cities = Cities()
# # for city in cities:
