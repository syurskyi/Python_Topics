'''
Created on Feb 11, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode(object
    ___ __init__(self, x
        self.val = x
        self.left = None
        self.right = None

class Solution(object
    ___ upsideDownBinaryTree(self, root
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        __ not root: r_ root
        stack = []
        node = root
        w___ node:
            stack.append(node)
            node = node.left
        root = stack.pop()
        node = root
        w___ stack:
            newNode = stack.pop()
            right = newNode.right
            node.left = right
            node.right = newNode
            newNode.left = None
            newNode.right = None
            node = newNode
        r_ root
    
    ___ test(self
        pass

__ __name__ __ '__main__':
    Solution().test()