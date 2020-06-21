# # abc_abc_base.py
#
# ______ a..
#
# # Forgetting to set the metaclass properly means the concrete implementations do not have their APIs enforced.
# # To make it easier to set up the abstract class properly, a base class is provided that sets the metaclass
# # automatically.
#
#
# c_ PluginBase a..
#
#     ??.?
#     ___ load  input
#         """Retrieve data from the input source
#         and return an object.
#         """
#
#     ??.?
#     ___ save  output data
#         """Save the data object to the output."""
#
#
# c_ SubclassImplementation P..
#
#     ___ load  input
#         r_ i___.r..
#
#     ___ save  output data
#         r_ o___.w.. d..
#
#
# __ ______ __ _____
#     print('Subclass:', iss.. (S...
#                                   P..)
#     print('Instance:', isi..(S..
#                                   P...
#
#
# # Subclass: True
# # Instance: True
#
# # To create a new abstract class, simply inherit from ABC.
