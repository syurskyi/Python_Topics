"""
Definition for a binary tree node.
class TreeNode:
    ___ __init__(self, x
        self.val = x
        self.left = None
        self.right = None
"""


class Solution:
    ___ kthSmallest(self, root, k
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        __ not root:
            r_

        stack = []
        node = root

        w___ node or stack:
            w___ node:
                stack.append(node)
                node = node.left

            node = stack.p..

            k -= 1
            __ k __ 0:
                r_ node.val

            node = node.right
