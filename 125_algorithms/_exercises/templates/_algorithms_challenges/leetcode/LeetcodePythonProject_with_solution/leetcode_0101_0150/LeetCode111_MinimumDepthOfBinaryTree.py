'''
Created on Feb 1, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    ___ minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        __ not root:
            return 0
        __ not root.left and not root.right:
            return 1
        elif root.left and root.right:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        elif root.left and not root.right:
            return self.minDepth(root.left) + 1
        else:
            return self.minDepth(root.right) + 1
