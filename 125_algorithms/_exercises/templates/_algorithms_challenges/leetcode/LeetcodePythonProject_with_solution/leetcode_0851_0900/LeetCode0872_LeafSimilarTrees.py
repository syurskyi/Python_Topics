'''
Created on Oct 3, 2019

@author: tongq
'''
# Definition for a binary tree node.
c_ TreeNode(o..
    ___ - , x
        val = x
        left = N..
        right = N..

c_ Solution(o..
    ___ leafSimilar  root1, root2
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        __ n.. root1 a.. n.. root2: r.. T..
        __ n.. root1 o. n.. root2: r.. F..
        r.. getLeaves(root1) __ getLeaves(root2)
        
    
    ___ getLeaves  root
        res    # list
        node = root
        stack    # list
        w.... node:
            stack.a..(node)
            node = node.left
        w.... stack:
            node = stack.p.. )
            __ n.. node.left a.. n.. node.right:
                res.a..(node.val)
            __ node.right:
                node0 = node.right
                w.... node0:
                    stack.a..(node0)
                    node0 = node0.left
        r.. res
