'''
Created on Feb 11, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    ___ upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        __ not root: return root
        stack = []
        node = root
        while node:
            stack.append(node)
            node = node.left
        root = stack.pop()
        node = root
        while stack:
            newNode = stack.pop()
            right = newNode.right
            node.left = right
            node.right = newNode
            newNode.left = None
            newNode.right = None
            node = newNode
        return root
    
    ___ test(self):
        pass

__ __name__ == '__main__':
    Solution().test()