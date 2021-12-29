'''
Created on Feb 6, 2017

@author: MT
'''
# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x):
        self.val = x
        self.left = N..
        self.right = N..

class Solution(object):
    ___ maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        __ n.. root: r.. 0
        r.. self.helper(root)[1]
    
    ___ helper(self, root):
        __ n.. root:
            r.. 0, float('-inf')
        left  = self.helper(root.left)
        right = self.helper(root.right)
        single = max([left[0]+root.val, right[0]+root.val, 0])
        gbl = max([left[1], right[1], left[0]+right[0]+root.val])
        r.. single, gbl
    
    ___ test(self):
        pass
    
__ __name__ __ '__main__':
    Solution().test()
