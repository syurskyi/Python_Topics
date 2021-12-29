'''
Created on Apr 30, 2018

@author: tongq
'''
# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x, left=None, right_ N..
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    ___ pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        __ not root: return root
        left  = self.pruneTree(root.left)
        right = self.pruneTree(root.right)
        __ left is None and right is None and root.val == 0:
            return None
        else:
            root.left = left
            root.right = right
            return root
    
    ___ test(self):
        testCases = [
            
        ]
        for root in testCases:
            result = self.pruneTree(root)

__ __name__ == '__main__':
    Solution().test()
