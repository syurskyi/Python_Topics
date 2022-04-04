'''
Created on Feb 11, 2017

@author: MT
'''

# Definition for a binary tree node.
c_ TreeNode(o..
    ___ - , x
        val = x
        left = N..
        right = N..

c_ Solution(o..
    ___ upsideDownBinaryTree  root
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        __ n.. root: r.. root
        stack    # list
        node = root
        w.... node:
            stack.a..(node)
            node = node.left
        root = stack.p.. )
        node = root
        w.... stack:
            newNode = stack.p.. )
            right = newNode.right
            node.left = right
            node.right = newNode
            newNode.left = N..
            newNode.right = N..
            node = newNode
        r.. root
    
    ___ test
        p..

__ _____ __ _____
    Solution().test()