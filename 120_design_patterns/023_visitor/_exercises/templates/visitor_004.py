# """Visitor pattern
#
# Visitor gives us the ability to add new operations to existing objects without
# modifying these objects. It's one way to follow the open/closed principle.
# """
#
#
# # classes that we cannot change (e.g. a fairly stable class hierarchy)
#
#
# c_ Element o..
#     p..
#
#
# c_ ElementOne E..
#     p..
#
#
# c_ ElementTwo E..
#     p..
#
#
# c_ ElementThree(EO.. ET..
#     p..
#
#
# c_ ElementFour(ET..
#     p..
#
#
# # Extrinsic Visitor
#
#
# c_ Visitor o..
#
#     operations _ |
#         "ElementTwo": "custom_operation", "ElementFour": "another_custom_operation"
#     |
#
#     ___ visit element $  $$
#         """Perform an operation specific for the passed element.
#
#         Steps:
#         1. traverse the class hierarchy of an Element object
#         2. discover what operation to perform on the Element object
#         3. perform the specific operation on the Element object
#
#         Parameters
#         ----------
#         element : Element
#             object whose behavior must be implemented here
#
#         Returns
#         -------
#         return value/s of the method chosen at runtime
#         """
#         method_name _ "default_operation"
#         ___ cls __ element. -c. -m
#             ___
#                 method_name _ o___ ?. -n
#                 b...  # we found out a custom operation to perform, so we exit
#
#             _____ K..
#                 p..  # keep default_operation if there isn't a custom one
#         method _ ge.. ?  ?
#         r_ ? e.. $ $$
#
#     # implement the behaviors for the Element objects
#
#     ??
#     ___ default_operation(elem $ $$
#         print|
#             "No custom operation defined for @ or its class hierarchy".f..
#                 ?. -c . -n
#             |
#         |
#         print|
#             "default_operation on @ with args @ and kwargs @".f..
#                 ?. -c . -n, args, kwargs
#             |
#         |
#
#     ??
#     ___ custom_operation elem $ $$
#         print|
#             "custom_operation on @ with args @ and kwargs @".f..
#                 ?. -c . -n a.. kw..
#             |
#         |
#
#     ??
#     ___ another_custom_operation elem $ $$
#         print(
#             "another_custom_operation on @ with args @ and kwargs @".f..
#                 ?. -c . -n, a.. kw..
#             )
#         )
#
#
# ___ main
#     elements _ ?  ?  ?  ?
#     visitor _ ?
#     ___ elem __ e..
#         v____.v... ?
#
# __ ________ __ _________
#     ?
