"""
Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


class Solution:
    """
    time: O(n)
    space: O(1)
    """
    ans = float('inf')
    pre = N..

    ___ getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        __ n.. root:
            r.. self.ans

        self.getMinimumDifference(root.left)

        __ self.pre and root.val - self.pre.val < self.ans:
            self.ans = root.val - self.pre.val

        self.pre = root

        self.getMinimumDifference(root.right)
        r.. self.ans
