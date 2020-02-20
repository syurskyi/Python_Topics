# # abc_register.py
#
# # Registering a Concrete Class
# # There are two ways to indicate that a concrete class implements an abstract API: either explicitly register the class
# # or create a new subclass directly from the abstract base. Use the register() class method as a decorator on a concrete
# # class to add it explicitly when the class provides the required API, but is not part of the inheritance tree of the
# # abstract base class.
#
# ______ a..
# ____ a_001_abc_base ______ P..
#
#
# c_ LocalBaseClass
#     p..
#
#
# ??.?                                # registration
# c_ RegisteredImplementation L..
#
#     ___ load input
#         r_ i__.r..
#
#     ___ save  output data
#         r_ o__.w..  d..
#
#
# __ ______ __ _____
#     print('Subclass:', iss..(R..
#                                   P..
#     print('Instance:', isi..(R..
#                                   P..
#
#
# # $ python3 abc_register.py
# #
# # Subclass: True
# # Instance: True
#
# # In this example the RegisteredImplementation is derived from LocalBaseClass, but is registered as implementing
# # the PluginBase API so issubclass() and isinstance() treat it as though it is derived from PluginBase.
#

# python2
#
# # import abc
# # from abc_base import PluginBase
# #
# #
# # class RegisteredImplementation(object):
# #
# #     def load(self, input):
# #         return input.read()
# #
# #     def save(self, output, data):
# #         return output.write(data)
# #
# #
# # PluginBase.register(RegisteredImplementation)
# #
# # if __name__ == '__main__':
# #     print 'Subclass:', issubclass(RegisteredImplementation, PluginBase)
# #     print 'Instance:', isinstance(RegisteredImplementation(), PluginBase)
