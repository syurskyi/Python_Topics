"""
Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


c_ Solution:
    ___ kthSmallest  root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        __ n.. root:
            r..

        stack    # list
        node = root

        w.... node o. stack:
            w.... node:
                stack.a..(node)
                node = node.left

            node = stack.pop()

            k -= 1
            __ k __ 0:
                r.. node.val

            node = node.right
