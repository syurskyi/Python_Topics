'''
Created on Feb 11, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x):
        self.val = x
        self.left = N..
        self.right = N..

class Solution(object):
    ___ upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        __ n.. root: r.. root
        stack    # list
        node = root
        while node:
            stack.a..(node)
            node = node.left
        root = stack.pop()
        node = root
        while stack:
            newNode = stack.pop()
            right = newNode.right
            node.left = right
            node.right = newNode
            newNode.left = N..
            newNode.right = N..
            node = newNode
        r.. root
    
    ___ test(self):
        pass

__ __name__ __ '__main__':
    Solution().test()