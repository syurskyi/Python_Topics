"""
Premium Question
Recursive
Longest Consecutive Subsequence in BT
"""
__author__ = 'Daniel'


class TreeNode(object):
    ___ __init__(self, x):
        self.val = x
        self.left = N..
        self.right = N..


class Solution(object):
    ___ __init__(self):
        self.gmax = 0

    ___ longestConsecutive(self, root):
        self.longest(root)
        r.. self.gmax

    ___ longest(self, cur):
        """
        longest ended at root
        Only consider increasing order
        """
        __ n.. cur:
            r.. 0

        maxa = 1
        l = self.longest(cur.left)
        r = self.longest(cur.right)
        __ cur.left a.. cur.val+1 __ cur.left.val:
            maxa = max(maxa, l+1)
        __ cur.right a.. cur.val+1 __ cur.right.val:
            maxa = max(maxa, r+1)

        self.gmax = max(self.gmax, maxa)
        r.. maxa

    ___ longestConsecutive_error(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        __ n.. root:
            r.. 0

        maxa = 1
        l = self.longestConsecutive(root.left)
        r = self.longestConsecutive(root.right)
        maxa = max(maxa, l, r)
        __ root.left a.. root.val + 1 __ root.left.val:
            maxa = max(maxa, l+1)
        __ root.right a.. root.val + 1 __ root.right.val:
            maxa = max(maxa, r+1)

        r.. maxa