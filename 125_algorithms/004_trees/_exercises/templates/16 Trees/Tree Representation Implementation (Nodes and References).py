# # Nodes and References Implementation of a Tree
# #
# # In this notebook is the code corresponding to the lecture for implementing the representation of a Tree as a class with nodes and references!
#
# c_ BinaryTree o..
#     ___ - rootObj
#         key _ ?
#         leftChild _ N..
#         rightChild _ N..
#
#     ___ insertLeft newNode
#         __ l.. __ N..
#             l.. _ ? ?
#         ____
#             t _ ? ?
#             t.l.. _ l..
#             l.. _ t
#
#     ___ insertRight newNode
#         __ r.. __ N..
#             r.. _ ? ?
#         ____
#             t _ ? ?
#             t.r.. _ r..
#             r.. _ t
#
#
#     ___ getRightChild
#         r_ ?
#
#     ___ getLeftChild
#         r_ ?
#
#     ___ setRootVal obj
#         key _ ?
#
#     ___ getRootVal
#         r_ k..
#
# # We can see some examples of creating a tree and assigning children. Note that some outputs are Trees themselves!
# #
# # from __future__ import print_function
# #
# r _ ?('a')
# print(?.gRV..
# print(?.gLC..
# ?.iL.. ('b')
# print(?.gLC..
# print(?.gLC__.gRV..
# ?.iR.. 'c')
# print(?.gRC..
# print(?.gRC__.gRV..
# ?.gRC__.sRV.. 'hello')
# print(?.gRC__.gRV..
#
# # a
# # N..
# # <__main__.BinaryTree object at 0x104779c10>
# # b
# # <__main__.BinaryTree object at 0x103b42c50>
# # c
# # hello