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

# c_ Foo o..
#
#     ___ -g ____ name
#         print "getting attribute @"  ?
#         r_ o__.-g____ ?
#
#     ___ -s ____ name, val
#         print "setting attribute @ to @"  ?  ?
#         r_ o__.-s ____ ?  ?
#
#
#
# foo = ?
# ?.var = 100
# # setting attribute var to 100
# ?.name = 'stuart'
# # setting attribute name to 'stuart'
# bar = foo.var
# # getting attribute var
# foo.var = foo.name
# # getting attribute name
# # setting attribute var to 'stuart'
