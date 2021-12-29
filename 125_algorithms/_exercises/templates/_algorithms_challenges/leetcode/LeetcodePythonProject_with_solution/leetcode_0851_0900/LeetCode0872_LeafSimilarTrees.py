'''
Created on Oct 3, 2019

@author: tongq
'''
# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x):
        self.val = x
        self.left = N..
        self.right = N..

class Solution(object):
    ___ leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        __ n.. root1 a.. n.. root2: r.. True
        __ n.. root1 o. n.. root2: r.. False
        r.. self.getLeaves(root1) __ self.getLeaves(root2)
        
    
    ___ getLeaves(self, root):
        res    # list
        node = root
        stack    # list
        w.... node:
            stack.a..(node)
            node = node.left
        w.... stack:
            node = stack.pop()
            __ n.. node.left a.. n.. node.right:
                res.a..(node.val)
            __ node.right:
                node0 = node.right
                w.... node0:
                    stack.a..(node0)
                    node0 = node0.left
        r.. res
