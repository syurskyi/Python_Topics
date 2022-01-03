'''
Created on Jan 30, 2017

@author: MT
'''

# Definition for a binary tree node.
c_ TreeNode(object):
    ___ - , x):
        val = x
        left = N..
        right = N..

c_ Solution(object):
    ___ isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        __ n.. root: r.. T..
        stack    # list
        prev = float('-inf')
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
