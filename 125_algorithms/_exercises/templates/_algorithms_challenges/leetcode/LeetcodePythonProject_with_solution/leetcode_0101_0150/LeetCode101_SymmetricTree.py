'''
Created on Jan 31, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x, left=N.., right_ N..
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    ___ isSymmetricRecursive(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        __ n.. root: r.. True
        r.. self.helper(root.left, root.left)
    
    ___ helper(self, left, right):
        __ n.. left and n.. right:
            r.. True
        ____ n.. left o. n.. right:
            r.. False
        ____ left.val != right.val:
            r.. False
        ____:
            r.. self.helper(left.left, right.right) and\
                self.helper(left.right, right.left)
    
    ___ isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        __ n.. root: r.. True
        stack    # list
        __ root.left:
            __ n.. root.right: r.. False
            stack.a..(root.left)
            stack.a..(root.right)
        ____ root.right:
            r.. False
        while stack:
            __ l..(stack)%2 != 0:
                r.. False
            right = stack.pop()
            left = stack.pop()
            __ right.val != left.val:
                r.. False
            __ left.left:
                __ n.. right.right:
                    r.. False
                stack.a..(left.left)
                stack.a..(right.right)
            ____ right.right:
                r.. False
            __ left.right:
                __ n.. right.left:
                    r.. False
                stack.a..(left.right)
                stack.a..(right.left)
            ____ right.left:
                r.. False
        r.. True
        