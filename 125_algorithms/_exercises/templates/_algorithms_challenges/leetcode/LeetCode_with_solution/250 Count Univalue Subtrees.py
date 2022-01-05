"""
Premium Question
"""

__author__ = 'Daniel'


c_ TreeNode:
    ___ - , x):
        val = x
        left = N..
        right = N..


c_ Solution:
    ___ - ):
        cnt = 0

    ___ countUnivalSubtrees  root):
        """
        :type root: TreeNode
        :rtype: int
        """
        is_unival(root)
        r.. cnt

    ___ is_unival  cur):
        __ n.. cur:
            r.. T..

        is_left = is_unival(cur.left)
        is_right = is_unival(cur.right)  # attention to test condition shortcut
        __ (n.. is_left o. n.. is_right o.
                    cur.left a.. cur.left.val != cur.val o.
                    cur.right a.. cur.right.val != cur.val):
            r.. F..
        ____:
            cnt += 1  # for currently visiting node as the root of subtree.
            r.. T..
