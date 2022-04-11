'''
Created on Sep 6, 2017

@author: MT
'''
# Definition for a binary tree node.
c_ TreeNode(o..
    ___ - , x, left=N.., right_ N..
        val x
        left left
        right right

c_ Solution(o..
    ___ tree2str  t
        """
        :type t: TreeNode
        :rtype: str
        """
        res ''
        __ t:
            res += s..(t.val)
            __ t.right:
                res += '(%s)' % tree2str(t.left)
                res += '(%s)' % tree2str(t.right)
            ____ t.left:
                res += '(%s)' % tree2str(t.left)
        r.. res
