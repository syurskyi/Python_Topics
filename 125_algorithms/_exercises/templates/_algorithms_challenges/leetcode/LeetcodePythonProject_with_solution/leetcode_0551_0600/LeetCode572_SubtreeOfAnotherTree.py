'''
Created on Sep 3, 2017

@author: MT
'''
# Definition for a binary tree node.
c_ TreeNode(o..
    ___ - , x
        val x
        left N..
        right N..

c_ Solution(o..
    ___ isSubtree  s, t
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        __ n.. s a.. n.. t:
            r.. T..
        __ n.. s:
            r.. F..
        r.. isSameTree(s, t) o.\
            isSubtree(s.left, t) o.\
            isSubtree(s.right, t)
    
    ___ isSameTree  s, t
        __ n.. s a.. n.. t:
            r.. T..
        __ n.. s o. n.. t:
            r.. F..
        __ s.val != t.val:
            r.. F..
        r.. isSameTree(s.left, t.left) a..\
            isSameTree(s.right, t.right)
