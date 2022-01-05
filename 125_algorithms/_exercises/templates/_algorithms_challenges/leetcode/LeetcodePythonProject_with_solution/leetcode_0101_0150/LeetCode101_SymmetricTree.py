'''
Created on Jan 31, 2017

@author: MT
'''

# Definition for a binary tree node.
c_ TreeNode(object):
    ___ - , x, left=N.., right_ N..
        val = x
        left = left
        right = right

c_ Solution(object):
    ___ isSymmetricRecursive  root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        __ n.. root: r.. T..
        r.. helper(root.left, root.left)
    
    ___ helper  left, right):
        __ n.. left a.. n.. right:
            r.. T..
        ____ n.. left o. n.. right:
            r.. F..
        ____ left.val != right.val:
            r.. F..
        ____:
            r.. helper(left.left, right.right) a..\
                helper(left.right, right.left)
    
    ___ isSymmetric  root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        __ n.. root: r.. T..
        stack    # list
        __ root.left:
            __ n.. root.right: r.. F..
            stack.a..(root.left)
            stack.a..(root.right)
        ____ root.right:
            r.. F..
        w.... stack:
            __ l..(stack)%2 != 0:
                r.. F..
            right = stack.pop()
            left = stack.pop()
            __ right.val != left.val:
                r.. F..
            __ left.left:
                __ n.. right.right:
                    r.. F..
                stack.a..(left.left)
                stack.a..(right.right)
            ____ right.right:
                r.. F..
            __ left.right:
                __ n.. right.left:
                    r.. F..
                stack.a..(left.right)
                stack.a..(right.left)
            ____ right.left:
                r.. F..
        r.. T..
        