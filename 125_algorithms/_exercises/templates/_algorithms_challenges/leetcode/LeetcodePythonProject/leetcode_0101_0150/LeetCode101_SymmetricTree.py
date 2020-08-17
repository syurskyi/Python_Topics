'''
Created on Jan 31, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode(object
    ___ __init__(self, x, left=None, right=None
        self.val = x
        self.left = left
        self.right = right

class Solution(object
    ___ isSymmetricRecursive(self, root
        """
        :type root: TreeNode
        :rtype: bool
        """
        __ not root: r_ True
        r_ self.helper(root.left, root.left)
    
    ___ helper(self, left, right
        __ not left and not right:
            r_ True
        ____ not left or not right:
            r_ False
        ____ left.val != right.val:
            r_ False
        ____
            r_ self.helper(left.left, right.right) and\
                self.helper(left.right, right.left)
    
    ___ isSymmetric(self, root
        """
        :type root: TreeNode
        :rtype: bool
        """
        __ not root: r_ True
        stack = []
        __ root.left:
            __ not root.right: r_ False
            stack.append(root.left)
            stack.append(root.right)
        ____ root.right:
            r_ False
        w___ stack:
            __ le.(stack)%2 != 0:
                r_ False
            right = stack.p..
            left = stack.p..
            __ right.val != left.val:
                r_ False
            __ left.left:
                __ not right.right:
                    r_ False
                stack.append(left.left)
                stack.append(right.right)
            ____ right.right:
                r_ False
            __ left.right:
                __ not right.left:
                    r_ False
                stack.append(left.right)
                stack.append(right.left)
            ____ right.left:
                r_ False
        r_ True
        