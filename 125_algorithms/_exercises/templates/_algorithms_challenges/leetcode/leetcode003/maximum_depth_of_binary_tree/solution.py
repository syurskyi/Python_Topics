"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root
node down to the farthest leaf node.

"""
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution:
    # @param root, a tree node
    # @return an integer
    ___ maxDepth  root
        __ root __ N..
            r.. 0
        left_max maxDepth(root.left)
        right_max maxDepth(root.right)
        r.. m..(left_max, right_max) + 1
