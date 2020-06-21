# # Implementation of Graph Overview
# # In this lecture we will implement a simple graph by focusing on the Node class. Refer to this lecture for the solution
# # to the Interview Problem
# # The graph will be directed and the edges can hold weights.
# # We will have three classes, a State class, a Node class, and finally the Graph class.
# # We're going to be taking advantage of two built-in tools here, OrderDict and Enum
#
# ____ enum ______ E..
#
# c_ State E..
#     unvisited _ 1 #White
#     visited _ 2 #Black
#     visiting _ 3 #Gray
# #
# # Now for the Node class we will take advantage of the OrderedDict object in case we want to keep trak of the order keys
# # are added to the dictionary.
#
# ___ col.. ______ OD..
#
# c_ Node
#
#     ___ -  num
#         ? ?
#         visit_state _ ?.u..
#         adjacent _ ?  # key = node, val = weight
#
#     ___ -s
#         r_ st. ?
#
# # Then finally the Graph:
#
# c_ Graph
#
#     ___ -
#         nodes _ ?  # key = node id, val = node
#
#     ___ add_node num
#         node _ ? ?
#         nodes|? _ ?
#         r_ ?
#
#     ___ add_edge source dest weight_0
#         __ source no. __ nodes
#             a.. ?
#         __ d.. no. __ ?
#             ? d..
#         n..|s__ .a..|n..|d.. _ w..
#
# g = ?
# g.add_edge(0, 1, 5)
# #
# g.nodes
# #
# # OrderedDict([(0, <__main__.Node instance at 0x103a761b8>),
# #              (1, <__main__.Node instance at 0x104dfef80>)])
# #
# # Great Job!