# """
# Open-Closed Principle
#
# Software entities(Classes, modules, functions) should be open for extension, not
# modification.
# """
# c_ Animal
#     ___ -  name ?
#         ?   ?
#
#     ___ get_name __ s..
#         p..
#
# animals _ |
#     A.. 'lion'
#     A.. 'mouse'
# |
#
# ___ animal_sound a... li..
#     ___ animal __ a..
#         __ ?.n.. __ 'l..'
#             print('roar')
#
#         ____ ?.n.. __ 'm..'
#             print('squeak')
#
# ? a..
#
# """
# The function animal_sound does not conform to the open-closed principle because
# it cannot be closed against new kinds of animals.  If we add a new animal,
# Snake, We have to modify the animal_sound function.  You see, for every new
# animal, a new logic is added to the animal_sound function.  This is quite a
# simple example. When your application grows and becomes complex, you will see
# that the if statement would be repeated over and over again in the animal_sound
# function each time a new animal is added, all over the application.
# """
#
# animals _ ?
#     A.. 'lion'
#     A.. 'mouse'
#     A.. 'snake
# ]
#
# ___ animal_sound a.. li..
#     ___ animal __ a..
#         __ ?.n.. __ 'l..'
#             print('roar')
#         ____ ?.n.. __ 'm..'
#             print('squeak')
#         ____ ?.n.. __ 's..'
#             print('hiss')
#
# a.. a..
#
#
# """
# How do we make it (the animal_sound) conform to OCP?
# """
#
# c_ Animal
#     ___ -  name ?
#         ?  ?
#
#     ___ get_name __ s..
#         p..
#
#     ___ make_sound
#         p..
#
#
# c_ Lion A..
#     ___ make_sound
#         r_ 'roar'
#
#
# c_ MouseA..
#     ___ make_sound:
#         r_ 'squeak'
#
#
# c_ Snake A..
#     ___ make_sound
#         r_ 'hiss'
#
#
# ___ animal_sound a.. li..
#     ___ animal __ a
#         print?.m..
#
# a.. a..
#
# """
# Animal now has a virtual method make_sound. We have each animal extend the
# Animal class and implement the virtual make_sound method.
#
# Every animal adds its own implementation on how it makes a sound in the
# make_sound.  The animal_sound iterates through the array of animal and just
# calls its make_sound method.
#
# Now, if we add a new animal, animal_sound doesn’t need to change.  All we need
# to do is add the new animal to the animal array.
#
# animal_sound now conforms to the OCP principle.
# """
#
# """
# Another example:
#
# Let’s imagine you have a store, and you give a discount of 20% to your favorite
# customers using this class: When you decide to offer double the 20% discount to
# VIP customers. You may modify the class like this:
# """
#
# c_ Discount
#     ___ -  customer price
#         ?   ?
#         ?  ?
#
#     ___ give_discount
#             __ ?c.. __ 'fav'
#                 r_ ?p.. * 0.2
#             __ ?c.. __ 'vip':
#                 r_ ?p.. * 0.4
#
#
# """
# No, this fails the OCP principle. OCP forbids it. If we want to give a new
# percent discount maybe, to a diff.  type of customers, you will see that a new
# logic will be added.
#
# To make it follow the OCP principle, we will add a new class that will extend
# the Discount.  In this new class, we would implement its new behavior:
# """
#
# c_ Discount
#     ___ -  customer price
#         ?  ?
#         ?  ?
#
#     ___ get_discount
#             r_ ?p.. * 0.2
#
#
# c_ VIPDiscount D..
#     ___ get_discount
#         r_ s___.g.. * 2
#
# """
# If you decide 80% discount to super VIP customers, it should be like this:
# You see, extension without modification.
# """
#
# c_ SuperVIPDiscount V..
#     ___ get_discount
#         r_ s___.g... * 2
