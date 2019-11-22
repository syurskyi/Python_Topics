# # Rolling our own Next method
# # implement a __len__ method to support the len() function
#
# c_ Squares
#     ___ __init__ ____ length
#         ____.le... _ length
#         ____.i _ 0
#
#     ___ next_ ____
#         i_ ____.i >_ ____.le...
#             ra... S..It..
#         e___
#             result _ ____.i ** 2
#             ____.i +_ 1
#             r_ r...
#
#     ___ __len__ ____
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
#     e___ S...I..
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
#     ___ __init__ ____ length * range_min_0 range_max_10
#         ____.l... _ length
#         ____.r._m. _ range_min
#         ____.r.._m.. _ range_max
#         ____.n.._r... _ 0
#
#     ___ __len__ ____
#         r... ____.le...
#
#     ___ __next__(____):
#         i_ ____.n.._r.. >_ ____.le..
#             r.. S...I..
#         e____
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
#     e____ S...I..
#         b.....
#
# # We still cannot use a for loop, and if we want to 'restart' the iteration, we have to create a new object every time.
# #
# numbers _ R.... 10
#
# ___ item i_ n....
#     print item #error
#
#
# # Iterators and Iterables
# # build class Cities
#
# c_ Cities:
#     ___ __init__ ____
#         ____._cities _ 'New York' 'Newark' 'New Delhi' 'Newcastle'
#     ___ __len__ ____
#         r_ len ____._cities
#     ___ __getitem__ ____ s
#         print 'getting item...'
#         r_ ____._cities |s
#     ___ __iter__ ____
#         print Calling Cities instance __iter__
#         r_ ____.C...I... ____
#     c_ CityIterator:
#         ___ __init__ ____ city_obj
#             # cities is an instance of Cities
#             print Calling CityIterator __init__
#             ____._c..._o.. _ city_obj
#             ____._index _ 0
#         ___ __iter__ ____
#             print Calling CitiyIterator instance __iter__
#             r_ ____
#         ___ __next__ ____
#             print Calling __next__
#             i_ ____._index >_ le. s____elf._c.._o..
#                 r.... S...I...
#             e____
#                 item _ ____._c___o__._cities ____._in___
#                 ____._in... +_ 1
#                 r_ it..
# # cities = Cities()
# # cities[0]
# # next(iter(cities))
# # cities = Cities()
# # for city in cities:
