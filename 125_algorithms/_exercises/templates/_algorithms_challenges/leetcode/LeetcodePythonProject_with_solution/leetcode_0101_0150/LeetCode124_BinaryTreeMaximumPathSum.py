'''
Created on Feb 6, 2017

@author: MT
'''
# Definition for a binary tree node.
c_ TreeNode(object):
    ___ - , x):
        val = x
        left = N..
        right = N..

c_ Solution(object):
    ___ maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        __ n.. root: r.. 0
        r.. helper(root)[1]
    
    ___ helper(self, root):
        __ n.. root:
            r.. 0, float('-inf')
        left  = helper(root.left)
        right = helper(root.right)
        single = max([left[0]+root.val, right[0]+root.val, 0])
        gbl = max([left[1], right[1], left[0]+right[0]+root.val])
        r.. single, gbl
    
    ___ test
        p..
    
__ _____ __ _____
    Solution().test()
