'''
Created on Jan 30, 2017

@author: MT
'''

# Definition for a binary tree node.
c_ TreeNode(o..):
    ___ - , x):
        val = x
        left = N..
        right = N..

c_ Solution(o..):
    ___ isValidBST  root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        __ n.. root: r.. T..
        stack    # list
        prev = f__('-inf')
        node = root
        w.... node:
            stack.a..(node)
            node = node.left
        w.... stack:
            node = stack.pop()
            __ prev >= node.val:
                r.. F..
            prev = node.val
            node0 = node.right
            w.... node0:
                stack.a..(node0)
                node0 = node0.left
        r.. T..
