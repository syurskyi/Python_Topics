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
    ___ recoverTree  root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        __ n.. root: r..
        first = N..
        second = N..
        prev = N..
        inOrder(root)
        __ second a.. first:
            val = second.val
            second.val = first.val
            first.val = val
    
    ___ inOrder  root):
        __ n.. root:
            r..
        inOrder(root.left)
        __ prev:
            __ root.val < prev.val:
                __ n.. first:
                    first = prev
                second = root
        prev = root
        inOrder(root.right)
    
    ___ test
        p..

__ _____ __ _____
    Solution().test()