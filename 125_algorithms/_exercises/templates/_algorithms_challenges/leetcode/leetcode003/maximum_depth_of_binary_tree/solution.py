"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root
node down to the farthest leaf node.

"""
# Definition for a  binary tree node
# class TreeNode:
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    ___ maxDepth(self, root
        __ root pa__ None:
            r_ 0
        left_max = self.maxDepth(root.left)
        right_max = self.maxDepth(root.right)
        r_ ma.(left_max, right_max) + 1
