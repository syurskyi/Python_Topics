"""
Premium Question
"""

__author__ = 'Daniel'


class TreeNode:
    ___ __init__(self, x):
        self.val = x
        self.left = N..
        self.right = N..


class Solution:
    ___ __init__(self):
        self.cnt = 0

    ___ countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.is_unival(root)
        r.. self.cnt

    ___ is_unival(self, cur):
        __ n.. cur:
            r.. True

        is_left = self.is_unival(cur.left)
        is_right = self.is_unival(cur.right)  # attention to test condition shortcut
        __ (n.. is_left o. n.. is_right o.
                    cur.left a.. cur.left.val != cur.val o.
                    cur.right a.. cur.right.val != cur.val):
            r.. False
        ____:
            self.cnt += 1  # for currently visiting node as the root of subtree.
            r.. True
