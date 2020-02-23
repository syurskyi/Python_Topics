# # -*- coding: utf-8 -*-
# 
# """
# We’ve looked at how we can define classes and methods, including some special methods like `__init__` and `__len__`.
# All these methods had something in common: the `self` parameter at the start. As a reminder, here’s some code:
# """
# 
# 
# c_ Student
#     ___ - ____ name school
#         ____.?  ?
#         ____.?  ?
#         ____.marks     # list
# 
#     ___ average ____
#         r_ su. ____.m.. / le. ____.m..
# 
# 
# """
# When we create a new object from the `Student` class and we call a method, 
# we are automagically passing in the `self` parameter:
# """
# 
# rolf = ? 'Rolf', 'MIT'
# 
# ?.m__.ap.. 78
# ?.m__.ap.. 99
# 
# print ?.a..
# 
# """
# This is identical to that last line:
# """
# 
# print S__.av.. ?
# 
# """
# When we do `object.method()`, Python is in the background calling `Class.method(object)`, 
# so that `self` is always the object that called the method.
# 
# Indeed, if we were to have two objects:
# """
# 
# rolf = S..  'Rolf', 'MIT'
# anne = S.. 'Anne', 'Cambridge'
# 
# r__.m__.ap.. 78
# r__.m__.ap.. 99
# 
# a__.m__.ap.. 34
# a__.m__.ap.. 56
# 
# print(r__.av..
# print(a__.av..
# 
# """
# In the first case, `self` would be the `rolf` object, and in the second case `self` would be the `anne` object.
# 
# Notice that this knowledge now lets us do some very weird stuff (not recommended, as it’ll likely break things):
# """
# 
# # Student.average('hello')  # self is now 'hello', comment this out to run the rest of the file.
# 
# """
# Just remember `self` is a parameter like any other; and you can give it any value you want. 
# However, because the method is then accessing `’hello’.marks`, you’ll get an error for the string doesn’t have that
# property.
# 
# Anyway, so why is this important?
# 
# The first type of method we’ve looked at is called “instance method”: 
# one that takes the caller object as the first argument (that’s `self`).
# 
# There are two more types of method:
# 
# * One that takes the caller’s class as the first argument; and
# * One that takes nothing as the first argument.
# """
# 
# # # @classmethod
# """
# Let’s look at the one that takes the caller’s class as the first argument.
# """
# 
# 
# c_ Foo
#     ??
#     ___ hi ___
#         print ___. -n
# 
# 
# my_object = ?
# ?.hi  # prints Foo
# 
# # # @staticmethod
# """
# Now one that takes nothing as the first argument.
# """
# 
# 
# c_ Foo
#     ??
#     ___ hi
#         print("I don't take arguments!")
# 
# 
# my_object = ?
# ?.hi
# 
# """
# Those are some terrible examples! Let’s look at some more in the next section.
# """
