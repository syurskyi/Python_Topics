'''
Created on Mar 6, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode(object
    ___ __init__(self, x, left=None, right=None
        self.val = x
        self.left = left
        self.right = right

class Solution(object
    ___ inorderSuccessor(self, root, p
        __ not root: r_ None
        __ root.val <= p.val:
            r_ self.inorderSuccessor(root.right, p)
        ____
            left = self.inorderSuccessor(root.left, p)
            __ left:
                r_ left
            ____
                r_ root
    
    ___ inorderSuccessorNonRec(self, root, p
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        __ p.right:
            node = p.right
            w___ node.left:
                node = node.left
            r_ node.val
        stack = []
        node = root
        w___ node != p:
            stack.append(node)
            __ node.val > p.val:
                node = node.left
            ____ node.val < p.val:
                node = node.right
            ____
                break
        w___ stack and stack[-1].val < p.val:
            stack.p..
        __ not stack:
            r_ None
        node = stack[-1]
        r_ node
