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

# # Custom Attribute Access
# # Descriptor objects allow you to create attributes that have custom behavior, but Python goes one step further
# # by exposing the mechanism by which attributes are located. It is this mechanism that is responsible
# # for implementing descriptors, and it is at the heart of how attributes are accessed.
# #
# # __getattribute__
# # There are two magic methods that are involved in getting attributes  __getattr__ and __getattribute__
# # Of the two it is __getattribute__ that is fundamental as it is called for every attribute access and if you override
# # it then you override every attribute access.
# #
# # Note that many magic methods are accessed directly and __getattribute__ is not involved in the access so you cannot
# # customize it. There is a limit to even Pythons magic.
# #
# # For example:
# #
# c_ MyClass
#     ___ -g ____ item
#         print ?
#         r_ N..
# # In this case __getattribute__ simply prints the name of the attribute and returns None. This may be trivial
# # but already you can see the potential as now any instance that you create seems to have any attribute you care
# # to access:
#
# myObj = ?
# ?.myAttribute1
# ?.myAttribute2
# ?.myAttribute3
#
# # prints the name of each attribute and doesnt throw an exception that myObj doesnt have these attributes.
# # If you try the same thing with the class:
# #
# M__._1
#
# # then you will see an exception telling you that MyClass doesnt have myAttribute1.
# # The class supplies the __getattribute__ method to its instances and the metaclass supplies the __getattribute__ method
# # to the class.
# #
# # For example:
# #
#
#
# c_ MyMeta ty..
#     ___ -g ____ item
#         print ?
#         r_ N..
#
#
# c_ MyClass me.._M..
#     ___ -g ____ item
#         print ?
#         r_ N..
# # After this you can access any attribute on MyClass just as you did in the instance.
# # The idea behind __getattribute__ is fairly simply but there is one trap that you have to be aware of.
# #
# # When you define a custom __getattribute__ it is called for every attribute access  even for the attributes you dont
# # want to modify the access to.
# #
# # In addition, if you try to access an attribute from within __getattribute__ then __getattribute__ is called and
# # the result is an infinite recursion.
# #
# # If you want to access attributes within __getattribute__ you have to call the __getattribute__ method of
# # the superclass.
# #
# # For example, if you write:
# #
# c_ MyClass
#     myAttribute1=42
#     ___ -g ____ item
#         print ?
#         r_ ____.m...
#
# # Then the final return self.myAttribute1 will result in __getattribute__ being called again to supply the result,
# # and this in turn will call __getattribute__ again and so on until the system runs out of memory.
# #
# # The correct approach is:
#
# c_ MyClass
#     myAttribute1=42
#     ___ -g ____ item
#         print ?
#         r_ s__.-g ?
#
# # Now the base class's __getattribute__ will return the attribute without involving out custom __getattribute__.
# # It is worth knowing that the built-in function:
# #
# g.. o.. i.. value
#
# # also calls __getattribute__
# # Included in chapter but not in this extract:
# # __getattr__
# # Customizing Assignment __setattr__
# # Default Methods
# # Custom Deleting Attributes
# # Custom Dir
# # Slots
# # Summary
# # The descriptor object can customize access to any attribute via the __get__, __set__ and __delete__ functions
# # which are automatically called on attribute access or deletion.
# # If a descriptor defines __get__ and __set__ then it is a data descriptor; if only __get__ is defined it is a non-data
# # descriptor.
# # Data descriptors cannot be overridden by a definition in the instance, whereas non-data descriptors can be.
# # __getattribute__ is called for every attribute access and if you override it then you override every attribute access.
# # If __getattribute__ fails to find an attribute then it automatically calls __getattr__ if it is defined.
# # __setattr__ is called every time you attempt an assignment to an attribute.
# # You can use __getattr__ to implement default attributes and methods.
# # You can use del or delattr to delete an attribute but in either case __delattr__ is called if it is defined.
# # The __dir__ magic method can be used to define a custom dir command.
# # Slots are just a more efficient way of implementing attributes using a descriptor.
# # Another way of accessing attributes is via the index or key operator []. This can be customized using __getitem__
# # and __setitem__. There are also a range of additional magic methods that can make attribute access look more like
# # a collection.
