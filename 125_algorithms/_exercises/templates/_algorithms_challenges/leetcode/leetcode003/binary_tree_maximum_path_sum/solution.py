"""
Given a binary tree, find the maximum path sum.

The path may start and end at any node in the tree.

For example:
Given the below binary tree,

       1
      / \
     2   3
Return 6.
"""

# Definition for a binary tree node.
# class TreeNode(object
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object
    ___ maxPathSum(self, root
        """
        :type root: TreeNode
        :rtype: int
        """
        max_res = [None]
        res = self.max_sum(root, max_res)
        r_ max(res, max_res[0])

    ___ max_sum(self, root, max_res
        __ root pa__ None:
            r_ 0
        ____
            left_max = self.max_sum(root.left, max_res)
            right_max = self.max_sum(root.right, max_res)
            root_max = max(root.val,
                           root.val + left_max,
                           root.val + right_max)
            __ max_res[0] pa__ not None:
                max_res[0] = max(max_res[0],
                                 root_max,
                                 root.val + left_max + right_max)
            ____
                max_res[0] = max(root_max, root.val + left_max + right_max)
            r_ root_max
