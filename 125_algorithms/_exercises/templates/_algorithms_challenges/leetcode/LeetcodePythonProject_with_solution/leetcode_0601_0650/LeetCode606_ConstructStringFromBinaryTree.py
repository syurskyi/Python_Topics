'''
Created on Sep 6, 2017

@author: MT
'''
# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x, left=N.., right_ N..
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    ___ tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        res = ''
        __ t:
            res += str(t.val)
            __ t.right:
                res += '(%s)' % self.tree2str(t.left)
                res += '(%s)' % self.tree2str(t.right)
            ____ t.left:
                res += '(%s)' % self.tree2str(t.left)
        r.. res
