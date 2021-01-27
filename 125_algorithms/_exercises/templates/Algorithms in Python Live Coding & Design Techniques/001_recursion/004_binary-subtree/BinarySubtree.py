#
# c_ Node
#     ___  -   data
#         ? _ ?
#         left _ N..
#         right _ N..
#
#
# ___ is_subtree tree subtree
#
#     __ subtree __ N..
#         r_ T..
#     __ tree __ N..
#         r_ F..
#
#     tree1 _   # empty list
#     tree2 _  # empty list
#
#     in_order tree _1
#     in_order subtree _2
#
#     str1 _ _1. -s .re.. "[", "" .re.. "]" ""
#     str2 _ _2. -s .re.. "[", "" .re.. "]" ""
#
#     __ _1.f.. _2 __ -1
#         r_ F..
#
#     tree1 _ # empty list
#     tree2 _ # empty list
#
#     pre_order ? _1)
#     pre_order s.. _2
#
#     str3 _ _1. -s .re.. "[", "").re.. "]", ""
#     str4 _ _2. -s .re.. "[", "").re.. "]", ""
#
#     __ _3.f.. _4 __ -1
#         r_ F..
#     r_ T..
#
#
# ___ in_order tree tree1
#
#     __ ? __ N..
#         r_
#
#     ? t__.l.. _1
#     _1.ap.. t__.d..
#     ? t__.r.. _1
#
#
# ___ pre_order tree tree1
#
#     __ ? __ N..
#         r_
#
#     _1.ap.. ?.d..
#     ? ?.l.. _1
#     ? ?.r.. _1
#
#
# root1 _ ?(1)
# ?.left _ ?(2)
# ?.right _ ?(3)
# ?.left.left _ ?(4)
# ?.left.right _ ?(5)
# ?.right.left _ ?(6)
# ?.right.right _ ?(7)
#
# root2 _ ?(3)
# ?.left _ ?(6)
# ?.right _ ?(7)
#
#
# is_subtree _ is_subtree(root1, root2)
# print(is_subtree)
#
