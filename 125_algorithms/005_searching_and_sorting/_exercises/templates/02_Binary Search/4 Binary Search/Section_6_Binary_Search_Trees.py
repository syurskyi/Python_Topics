# c_ Node o..
#
#     ___ - data
#         ? ?
#         leftChild _ N...
#         rightChild _ N...
#
#
# c_ BinarySearchTree o..
#
#     ___ -
#         root _ N...
#
#     ___ insert data
#         __ no. r..
#             r.. _ ? ?
#         ____
#             iN.. ? r..
#
#     # O(logN)   if the tree is balanced !!!!!!!!!!!!!  --> it can reduced to O(N) --> AVL RBT are needed !!!!!
#     ___ insertNode data node
#
#         __ ? < n__.d..
#             __ n__.l..
#                 i.. ? n__.l..
#             ____
#                 n__.l.. _ ? ?
#         ____
#             __ n__.r..
#                 i.. ? n__.r..
#             ____
#                 n__.r.. _ ? ?
#
#     # O(logN)
#     ___ removeNode data node
#
#         __ no. n__
#             r_ ?
#
#         __ ? < n__.d..
#             n__.l.. _ r.. ? n__.l..
#         ____ ? > n__.data:
#             n__.r.. _ r.. ? n__.r..
#         ____
#
#             __ no. n__.l.. an. no. n__.r..
#                 print("Removing a leaf node...")
#                 de. n__
#                 r_ N...
#
#             __ no. n__.leftChild  # node !!!
#                 print("Removing a node with single right child...")
#                 tempNode _ n__.r..
#                 del n__
#                 r_ ?
#             ____ no. n__.rightChild:  # node instead of self
#                 print("Removing a node with single left child...")
#                 tempNode _ n__.l..
#                 de. n__
#                 r_ ?
#
#             print("Removing node with two children....")
#             tempNode _ gP.. n__.l..  # self instead of elf  + get predecessor
#             n__.d.. _ tN__.d..
#             n__.l.. _ r.. t__.d.. n__.l..
#
#         r_ ? # !!!!!!!!!!!!
#
#     ___ getPredecessor node
#
#         __ ?.r..
#             r_ gP.. ?.r..
#
#         r_ ?
#
#     ___ remove data
#         __ r..
#             r.. _ r.. ? r..
#
#     # O(logN)
#     ___ getMinValue
#         __ r..
#             r_ gM.. r..
#
#     ___ getMin node
#
#         __ ?.l..
#             r_ ? ?.l..
#
#         r_ ?.d..
#
#     # O(logN)
#     ___ getMaxValue
#         __ r..
#             r_ gM.. r..
#
#     ___ getMax node
#
#         __ ?.r..
#             r_ ? ?.r..
#
#         r_ ?.d..
#
#     ___ traverse
#         __ r..
#             t.. r..
#
#         # O(N)
#
#     ___ traverseInOrder node
#
#         __ ?.l..
#             ? ?.l..
#
#         print("@ "  ?.d..    # string
#
#         __ ?.r..
#             ? ?.r..
#
#
# bst _ ?
# ?.i.. 10
# ?.i.. 13
# ?.i.. 5
# ?.i.. 14
# ?.r.. 10
#
# ?.t..
