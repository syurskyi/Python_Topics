'''
Created on Feb 26, 2017

@author: MT
'''

# Definition for a binary tree node.
c_ TreeNode(o..):
    ___ - , x, left=N.., right_ N..
        val = x
        left = left
        right = right

c_ Solution(o..):
    ___ lowestCommonAncestor  root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        __ n.. root:
            r.. N..
        ____ root __ p o. root __ q:
            r.. root
        l = lowestCommonAncestor(root.left, p, q)
        r = lowestCommonAncestor(root.right, p, q)
        __ l a.. r:
            r.. root
        ____ n.. l a.. n.. r:
            r.. N..
        ____:
            r.. r __ n.. l ____ l
    
    ___ test
        node1 = TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4)))
        node2 = TreeNode(1, TreeNode(0), TreeNode(8))
        root = TreeNode(3)
        root.left = node1
        root.right = node2
        result = lowestCommonAncestor(root, node2, node1)
        print(result)
        __ result:
            print(result.val)

__ _____ __ _____
    Solution().test()
