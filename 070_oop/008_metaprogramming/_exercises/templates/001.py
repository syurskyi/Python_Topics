# c_ AbstractClass
#
#     def do_something
#         p..
#
#
# c_ B A..
#     p..
#
# a = A..
# b = B()
# #
# # If we start this program, we see that this is not an abstract class, because:
# #
# #     we can instantiate an instance from
# #     we are not required to implement do_something in the class defintition of B
# #
# # Our example implemented a case of simple inheritance which has nothing to do with an abstract class. In fact,
# # Python on its own doesn't provide abstract classes. Yet, Python comes with a module which provides
# # the infrastructure for defining Abstract Base Classes (ABCs). This module is called - for obvious reasons - abc.
# # The following Python code uses the abc module and defines an abstract base class:
#
# _____ a.. i.... A.. a..
#
#
# c_ AbstractClassExample A..
#
#     ___ -  value
#         self.?  ?
#         s___ . -
#
#     ??
#     ___ do_something
#         p..
#
# # We will define now a subclass using the previously defined abstract class. You will notice that we haven't
# # implemented the do_something method, even though we are required to implement it, because this method is decorated
# # as an abstract method with the decorator "abstractmethod". We get an exception that DoAdd42 can't be instantiated:
#
# c_ DoAdd42 ?
#     p..
#
# # x = DoAdd42(4)
# #
# # ---------------------------------------------------------------------------
# # TypeError                                 Traceback (most recent call last)
# # <ipython-input-9-83fb8cead43d> in <module>()
# #       2     pass
# #       3
# # ----> 4 x = DoAdd42(4)
# #
# # TypeError: Can't instantiate abstract class DoAdd42 with abstract methods do_something
# #
# # We will do it the correct way in the following example, in which we define two classes inheriting from
# # our abstract class:
#
#
# c_ DoAdd42 ?
#
#     ___ do_something
#         r_ ?v.. + 42
#
# c_ DoMul42 ?
#
#     ___ do_something
#         r_ ?v.. * 42
#
# x = DoAdd42(10)
# y = DoMul42(10)
#
# print(x.do_something())
# print(y.do_something())
#
# # 52
# # 420
# #
# # A class that is derived from an abstract class cannot be instantiated unless all of its abstract methods are
# # overridden.
# #
# # You may think that abstract methods can't be implemented in the abstract base class. This impression is wrong:
# # An abstract method can have an implementation in the abstract class! Even if they are implemented, designers
# # of subclasses will be forced to override the implementation. Like in other cases of "normal" inheritance,
# # the abstract  method can be invoked with super() call mechanism. This makes it possible to provide some basic
# # functionality in  the abstract method, which can be enriched by the subclass implementation.
#
# ____ a.. _______ A.. a...
#
# c_ AbstractClassExample A..
#
#     ??
#     ___ do_something
#         print("Some implementation!")
#
# c_ AnotherSubclass Ab..
#
#     ___ do_something
#         s__ .d..
#         print("The enrichment from AnotherSubclass")
#
# x = AnotherSubclass()
# x.do_something()
#
#
# # Some implementation!
# # The enrichment from AnotherSubclass
