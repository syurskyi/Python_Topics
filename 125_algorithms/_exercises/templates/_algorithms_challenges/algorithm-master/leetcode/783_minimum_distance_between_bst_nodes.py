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
    Recursion
    time: O(n)
    space: O(1)
    """
    ans = float('inf')
    pre = None

    ___ minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        __ not root:
            return self.ans

        self.minDiffInBST(root.left)

        __ self.pre and root.val - self.pre.val < self.ans:
            self.ans = root.val - self.pre.val

        self.pre = root

        self.minDiffInBST(root.right)
        return self.ans


class Solution:
    """
    Iteration
    time: O(n)
    space: O(n)
    """
    ___ minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        __ not root:
            return

        ans = float('inf')
        pre = None

        stack = []
        node = root

        while node or stack:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()

            __ pre and node.val - pre.val < ans:
                ans = node.val - pre.val

            pre = node

            node = node.right

        return ans
