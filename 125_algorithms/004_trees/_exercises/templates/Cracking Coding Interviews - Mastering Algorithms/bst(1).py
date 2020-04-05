# c_ Node
# 	___ - val left_N.. right_N..
# 		? ?
# 		? ?
# 		? ?
#
#
# ___ search root target
# 	__ ? __ N..
# 		r_ N..
# 	____ ?.v.. __ t..
# 		r_ ?
# 	____ ?.v.. < t..
# 		r_ s.. ?.r.. t..
# 	____
# 		r_ s.. ?.l.. t..
#
# # runtime: O(logn)
#
# #               15
# #            /      \
# #        10          32
# #       /  \         /  \
# #     1      12     17   39
# #      \    /  \         /
# #       5  11  14      37
# #      / \
# #     4   7
#
#
# leaf1 = ?(4)
# leaf2 = ?(7)
#
# leaf3 = ?(11)
# leaf4 = ?(14)
#
# leaf5 = ?(37)
#
# leaf6 = ?(17)
#
# node1 = ?(5, leaf1, leaf2)
# node2 = ?(12, leaf3, leaf4)
# node3 = ?(39, leaf5, None)
#
# node4 = ?(32, leaf6, node3)
#
# node5 = ?(1, None, node1)
#
# node6 = ?(10, node5, node2)
#
#
# root = ?(15, node6, node4)
#
# print(search(root, 37).val)
# print(search(root, 40))
