# # abc_subclass.py
#
# # Implementation Through Subclassing
# # Subclassing directly from the base avoids the need to register the class explicitly.
#
# ______ a..
# ____ a_001_abc_base ______ P..
#
#
# c_ SubclassImplementation P..
#
#     ___ load  input
#         r_ i__.r..
#
#     ___ save  output data
#         r_ o___.w.. d..
#
#
# __ ______ __ _____
#     print('Subclass:', iss.. S..
#                                   P...
#     print('Instance:', isi...(S...
#                                   P...
#
#
# # $ python3 abc_subclass.py
# #
# # Subclass: True
# # Instance: True
#
#
# # In this case, normal Python class management features are used to recognize SubclassImplementation as implementing
# # the abstract PluginBase.
#

# python 2

# # import abc
# # from abc_base import PluginBase
# #
# #
# # class SubclassImplementation(PluginBase):
# #
# #     def load(self, input):
# #         return input.read()
# #
# #     def save(self, output, data):
# #         return output.write(data)
# #
# #
# # if __name__ == '__main__':
# #     print 'Subclass:', issubclass(SubclassImplementation, PluginBase)
# #     print 'Instance:', isinstance(SubclassImplementation(), PluginBase)
