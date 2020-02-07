# # -*- coding: utf-8 -*-
#
# """
# In a class, not all methods are the same. Python sometimes makes a distinction depending on the method name.
# Here’s one of these special methods:
# """
#
#
# c_ Student
#   ___  - ____ name
#     ____.?  ?
#
#
# """
# This method is different from other methods because it gets called automatically for you when you create a new object.
# For example:
# """
#
# my_student = ? 'Jose'
#
# """
# What happens here is that a new object is created, and then the `__init__` method is called with the new object as `self` and the string you passed as `'name'`.
# """
#
# # # Other interesting special methods
# # ## `len()`
#
# """
# Given an *iterable* (generally a list, tuple, set, or dictionary; something you can iterate over), `len()` gives you the number of elements. For example:
# """
#
# movies = ['Matrix', 'Finding Nemo']
#
# print ?. -c # what's this?
#
# count = le. m..
# print ?  # 2
#
# """
# We can make `len()` work on our classes too, by adding the `__len__` method:
# """
#
#
# c_ Garage
#     ___  - ____
#         ____.cars _    # list
#
#     ___ -l ____
#         r_ le. ____.c..
#
#
# ford_garage = ?
# ?.c__.ap..  'Fiesta'
# ?.c__.ap.. 'Focus'
#
# print le. ?
#
# # ## Getting a specific item (square bracket notation)
#
# """
# We can also use square bracket notation in our `Garage`:
# """
#
#
# c_ Garage
#     ___  - ____
#         ____.cars _   # list
#
#     ___ -l ____
#         r_ le. ____.c..
#
#     ___ -g ____ i
#         r_ ____.c.. ?
#
#
# ford_garage = ?
# ?.c__.ap.. 'Fiesta'
# ?.c__.ap..( Focus'
#
# print(? 1  # Focus
#
# """
# A great thing about this is now you can iterate over the garage using a for loop.
# To do this you need both `__len__` and `__getitem__`:
# """
#
# ___ car __ ?
#   print ?
#
# # ## String representation
# """
# If you want to print your objects out (and sometimes during development it can be handy, as we’ll see), we can use `__repr__` and `__str__`:
#
# * `__repr__` should be used to print out a string representing the object such that with that string you can re-create the object fully.
# * `__str__` should be used when printing the object out to a user, for example—can be more descriptive or even miss out some details.
# """
#
#
# c_ Garage
#     ___  - ____
#         ____.cars _   # list
#
#     ___ -r ____
#         r_ _*Garage |____.c..
#
#     ___ -s ____
#         r_ _*Garage with |le. ____.c..| cars'
#
#
# """
# You should implement at least `__repr__`.
#
# In order to call these methods, you can:
# """
#
# garage = ?
# ?.c__.ap.. 'Fiesta'
# ?.c__.ap.. 'Focus'
#
# print ?
# print st. ?
# print re.. ?
#
#
# # # More
# """
# There are many magic “dunder” methods you can implement, including some to overload what mathematical operators do,
# what boolean operators do, make your objects callable, adding context managers, and more.
#
# We’ll be learning about all this throughout the course!
# """
