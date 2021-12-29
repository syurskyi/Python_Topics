"""
Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


class Solution:
    ___ kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        __ not root:
            return

        stack = []
        node = root

        while node or stack:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()

            k -= 1
            __ k == 0:
                return node.val

            node = node.right
