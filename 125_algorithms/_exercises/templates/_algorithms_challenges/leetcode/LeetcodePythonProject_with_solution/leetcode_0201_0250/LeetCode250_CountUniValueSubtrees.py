'''
Created on May 13, 2018

@author: tongq
'''
# Definition for a binary tree node.
c_ TreeNode(object):
    ___ - , x, left=N.., right_ N..
        val = x
        left = left
        right = right

c_ Solution(object):
    ___ countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = 0
        __ n.. root: r.. res
        __ isUniVal(root):
            res += 1
        res += countUnivalSubtrees(root.left)+\
            countUnivalSubtrees(root.right)
        r.. res
    
    ___ isUniVal(self, root):
        __ n.. root.left a.. n.. root.right:
            r.. T..
        __ n.. root.right:
            r.. root.val __ root.left.val a.. isUniVal(root.left)
        __ n.. root.left:
            r.. root.val __ root.right.val a.. isUniVal(root.right)
        r.. root.left.val __ root.val a.. root.right.val __ root.val a..\
            isUniVal(root.left) a.. isUniVal(root.right)
