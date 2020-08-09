'''
Created on Apr 30, 2018

@author: tongq
'''
# Definition for a binary tree node.
class TreeNode(object
    ___ __init__(self, x, left=None, right=None
        self.val = x
        self.left = left
        self.right = right

class Solution(object
    ___ pruneTree(self, root
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        __ not root: r_ root
        left  = self.pruneTree(root.left)
        right = self.pruneTree(root.right)
        __ left is None and right is None and root.val __ 0:
            r_ None
        ____
            root.left = left
            root.right = right
            r_ root
    
    ___ test(self
        testCases = [
            
        ]
        ___ root in testCases:
            result = self.pruneTree(root)

__ __name__ __ '__main__':
    Solution().test()
