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
    Recursion
    time: O(n)
    space: O(1)
    """
    ans = f__('inf')
    pre = N..

    ___ minDiffInBST  root):
        """
        :type root: TreeNode
        :rtype: int
        """
        __ n.. root:
            r.. ans

        minDiffInBST(root.left)

        __ pre a.. root.val - pre.val < ans:
            ans = root.val - pre.val

        pre = root

        minDiffInBST(root.right)
        r.. ans


c_ Solution:
    """
    Iteration
    time: O(n)
    space: O(n)
    """
    ___ minDiffInBST  root):
        """
        :type root: TreeNode
        :rtype: int
        """
        __ n.. root:
            r..

        ans = f__('inf')
        pre = N..

        stack    # list
        node = root

        w.... node o. stack:
            w.... node:
                stack.a..(node)
                node = node.left

            node = stack.pop()

            __ pre a.. node.val - pre.val < ans:
                ans = node.val - pre.val

            pre = node

            node = node.right

        r.. ans
