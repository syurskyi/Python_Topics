# # Path Sum II
# # Question: Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
# # For example:
# # Given the below binary tree and sum = 22,
# # 5
# # / \
# # 4 8
# # / / \
# # 11 13 4
# # / \ / \
# # 7 2 5 1
# # return
# # [ [5,4,11,2], [5,8,4,5] ]
# # Solutions:
#
#
# c_ TreeNode
#     ___  -  x
#         val _ x
#         left _ N..
#         right _ N..
#
#
# c_ Solution
#     # @param root, a tree node
#     # @param sum, an integer
#     # @return a list of lists of integers
#     ___ ?  ? s..
#         solution _   # list
#         ? ? s.. 0   # list, solution)
#         r_ ?
#
#     ___ pathSumRec  root sum tempSum tempList solution
#         __ ? __ N..
#             r_
#         tempList.ap.. r__.v..
#         tempSum +_ r__.v..
#         __ r__.l.. __ N.. an. r__.r.. __ N..
#             __ ? __ su.
#                 s__.ap.. li.. t..
#             ____
#                 ? r__.l.. su. ? ? ?
#                 ? r__.r.. su. ? ? ?
#         t__.p..
#
#
# __  -n __ ______
#     BT ?.r.. ?.r...l.. ?.l.. _ ? 1 ? 2 ? 3 ? 10
#     print   ? .? ? 6