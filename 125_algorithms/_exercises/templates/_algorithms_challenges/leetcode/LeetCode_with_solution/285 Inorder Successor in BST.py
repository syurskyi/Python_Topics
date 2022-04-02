"""
Premium Question
"""
__author__ = 'Daniel'


c_ TreeNode(o..
    ___ - , x
        val = x
        left = N..
        right = N..


c_ Solution(o..
    ___ inorderSuccessor  root, p
        """
        search

        If it is a general binary tree
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        find = [N..]
        s..(root, p, find)
        r.. find[0]

    ___ s..  cur, p, find
        __ n.. cur:
            r..

        __ cur.val > p.val:
            find[0] = cur
            s..(cur.left, p, find)
        ____:
            s..(cur.right, p, find)