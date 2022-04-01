"""
Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


c_ Solution:
    """
    time: O(n)
    space: O(1)
    """
    ans = f__('inf')
    pre = N..

    ___ getMinimumDifference  root):
        """
        :type root: TreeNode
        :rtype: int
        """
        __ n.. root:
            r.. ans

        getMinimumDifference(root.left)

        __ pre a.. root.val - pre.val < ans:
            ans = root.val - pre.val

        pre = root

        getMinimumDifference(root.right)
        r.. ans
