# # abc_find_subclasses.py
#
# ____ a_001_abc_base _____ P..
# ______ a_003_abc_subclass
# ______ a_002_abc_register
#
# # A side effect of using direct subclassing is it is possible to find all of the implementations of a plug-in by asking
# # the base class for the list of known classes derived from it (this is not an abc feature, all classes can do this).
#
# ___ sc __ P__. -s
#     print ?. -n
#
# # $ python3 abc_find_subclasses.py
# #
# # SubclassImplementation
#
# # Even though abc_register() is imported, RegisteredImplementation is not among the list of subclasses because
# # it is not actually derived from the base.
#

# # python 2
# # import abc
# # from abc_base import PluginBase
# # import abc_subclass
# # import abc_register
# #
# # for sc in PluginBase.__subclasses__():
# #     print sc.__name__
