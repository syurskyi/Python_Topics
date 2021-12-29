'''
Created on Feb 22, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    ___ invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        __ not root: return None
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left = right
        root.right = left
        return root
    
    ___ invertTreeNonRec(self, root):
        __ not root: return None
        stack = [root]
        while stack:
            node = stack.pop()
            __ node:
                left = node.left
                right = node.right
                node.right = left
                node.left = right
                stack.append(left)
                stack.append(right)
        return root