# # abc_incomplete.py
#
# ______ a..
# ____ a_001_abc_base ______ P...
#
# # Incomplete Implementations
# # Another benefit of subclassing directly from the abstract base class is that the subclass cannot be instantiated
# # unless it fully implements the abstract portion of the API.
#
# ??.?
# c_ IncompleteImplementation P..
#
#     ___ save output data
#         r_ o___.w.. d...
#
#
# __ ______ __ _____
#     print('Subclass:', iss.. I...
#                                   P..
#     print('Instance:', isi.. I...
#                                   P..
#
#
# # This keeps incomplete implementations from triggering unexpected errors at runtime.
#
# # $ python3 abc_incomplete.py
# #
# # Subclass: True
# # Traceback (most recent call last):
# #   File "abc_incomplete.py", line 24, in <module>
# #     print('Instance:', isinstance(IncompleteImplementation(),
# # TypeError: Can't instantiate abstract class
# # IncompleteImplementation with abstract methods load

# # python 2
#
# # import abc
# # from abc_base import PluginBase
# #
# # class IncompleteImplementation(PluginBase):
# #
# #     def save(self, output, data):
# #         return output.write(data)
# #
# # PluginBase.register(IncompleteImplementation)
# #
# # if __name__ == '__main__':
# #     print 'Subclass:', issubclass(IncompleteImplementation, PluginBase)
# #     print 'Instance:', isinstance(IncompleteImplementation(), PluginBase)
