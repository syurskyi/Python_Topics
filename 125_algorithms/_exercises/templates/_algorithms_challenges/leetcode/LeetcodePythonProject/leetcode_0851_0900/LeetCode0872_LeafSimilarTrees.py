'''
Created on Oct 3, 2019

@author: tongq
'''
# Definition for a binary tree node.
class TreeNode(object
    ___ __init__(self, x
        self.val = x
        self.left = None
        self.right = None

class Solution(object
    ___ leafSimilar(self, root1, root2
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        __ not root1 and not root2: r_ True
        __ not root1 or not root2: r_ False
        r_ self.getLeaves(root1) __ self.getLeaves(root2)
        
    
    ___ getLeaves(self, root
        res = []
        node = root
        stack = []
        w___ node:
            stack.append(node)
            node = node.left
        w___ stack:
            node = stack.p..
            __ not node.left and not node.right:
                res.append(node.val)
            __ node.right:
                node0 = node.right
                w___ node0:
                    stack.append(node0)
                    node0 = node0.left
        r_ res
