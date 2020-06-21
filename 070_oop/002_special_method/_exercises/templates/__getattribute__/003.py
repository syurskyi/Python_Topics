# __getattribute__(self, name)
# After all this, __getattribute__ fits in pretty well with its companions __setattr__ and __delattr__.
# However, I don't recommend you use it. __getattribute__ can only be used with new-style classes (all classes
# are new-style in the newest versions of Python, and in older versions you can make a class new-style
# by subclassing object. It allows you to define rules for whenever an attribute's value is accessed.
# It suffers from some similar infinite recursion problems as its partners-in-crime (this time you call the base class's
# __getattribute__ method to prevent this). It also mainly obviates the need for __getattr__, which,
# when __getattribute__ is implemented, only gets called if it is called explicitly or an AttributeError is raised.
# This method can be used (after all, it's your choice), but I don't recommend it because it has a small use case
# (it's far more rare that we need special behavior to retrieve a value than to assign to it) and because
# it can be really difficult to implement bug-free.

# # Override access to one variable in a class, but return all others normally
# # http://stackoverflow.com/a/371833/18852
#
# c_ D o..
#     ___  -
#         ____.test _ 20
#         ____.test2 _ 40
#     ___ -g ____ name
#         __ ? __ 'test'
#             r_ 0
#         ____
#             r_ o__.-g ____ ?
#
# obj1 = ?
# print ?.test
# print ?.test2
