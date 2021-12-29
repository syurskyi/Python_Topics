"""
Premium Question
Recursive
Longest Consecutive Subsequence in BT
"""
__author__ = 'Daniel'


class TreeNode(object):
    ___ __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    ___ __init__(self):
        self.gmax = 0

    ___ longestConsecutive(self, root):
        self.longest(root)
        return self.gmax

    ___ longest(self, cur):
        """
        longest ended at root
        Only consider increasing order
        """
        __ not cur:
            return 0

        maxa = 1
        l = self.longest(cur.left)
        r = self.longest(cur.right)
        __ cur.left and cur.val+1 == cur.left.val:
            maxa = max(maxa, l+1)
        __ cur.right and cur.val+1 == cur.right.val:
            maxa = max(maxa, r+1)

        self.gmax = max(self.gmax, maxa)
        return maxa

    ___ longestConsecutive_error(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        __ not root:
            return 0

        maxa = 1
        l = self.longestConsecutive(root.left)
        r = self.longestConsecutive(root.right)
        maxa = max(maxa, l, r)
        __ root.left and root.val + 1 == root.left.val:
            maxa = max(maxa, l+1)
        __ root.right and root.val + 1 == root.right.val:
            maxa = max(maxa, r+1)

        return maxa