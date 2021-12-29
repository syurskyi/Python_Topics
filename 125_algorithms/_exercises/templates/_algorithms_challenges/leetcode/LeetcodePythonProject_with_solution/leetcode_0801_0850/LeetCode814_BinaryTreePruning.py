'''
Created on Apr 30, 2018

@author: tongq
'''
# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x, left=N.., right_ N..
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    ___ pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        __ n.. root: r.. root
        left  = self.pruneTree(root.left)
        right = self.pruneTree(root.right)
        __ left __ N.. and right __ N.. and root.val __ 0:
            r.. N..
        ____:
            root.left = left
            root.right = right
            r.. root
    
    ___ test(self):
        testCases = [
            
        ]
        ___ root __ testCases:
            result = self.pruneTree(root)

__ __name__ __ '__main__':
    Solution().test()
