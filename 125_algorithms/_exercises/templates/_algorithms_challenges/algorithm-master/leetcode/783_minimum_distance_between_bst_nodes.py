"""
Definition for a binary tree node.
class TreeNode:
    ___ __init__(self, x
        self.val = x
        self.left = None
        self.right = None
"""


class Solution:
    """
    Recursion
    time: O(n)
    space: O(1)
    """
    ans = float('inf')
    pre = None

    ___ minDiffInBST(self, root
        """
        :type root: TreeNode
        :rtype: int
        """
        __ not root:
            r_ self.ans

        self.minDiffInBST(root.left)

        __ self.pre and root.val - self.pre.val < self.ans:
            self.ans = root.val - self.pre.val

        self.pre = root

        self.minDiffInBST(root.right)
        r_ self.ans


class Solution:
    """
    Iteration
    time: O(n)
    space: O(n)
    """
    ___ minDiffInBST(self, root
        """
        :type root: TreeNode
        :rtype: int
        """
        __ not root:
            r_

        ans = float('inf')
        pre = None

        stack = []
        node = root

        w___ node or stack:
            w___ node:
                stack.append(node)
                node = node.left

            node = stack.p..

            __ pre and node.val - pre.val < ans:
                ans = node.val - pre.val

            pre = node

            node = node.right

        r_ ans
