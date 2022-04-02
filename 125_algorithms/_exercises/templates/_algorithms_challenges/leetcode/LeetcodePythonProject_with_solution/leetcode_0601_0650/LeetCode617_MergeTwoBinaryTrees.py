'''
Created on Sep 7, 2017

@author: MT
'''
# Definition for a binary tree node.
c_ TreeNode(o..
    ___ - , x, left=N.., right_ N..
        val = x
        left = left
        right = right

c_ Solution(o..
    ___ mergeTrees  t1, t2
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        root = TreeNode(-1)
        __ t1 a.. n.. t2:
            root.val = t1.val
            root.left = mergeTrees(t1.left, t2)
            root.right = mergeTrees(t1.right, t2)
        ____ n.. t1 a.. t2:
            root.val = t2.val
            root.left = mergeTrees(t1, t2.left)
            root.right = mergeTrees(t1, t2.right)
        ____ t1 a.. t2:
            root.val = t1.val + t2.val
            root.left = mergeTrees(t1.left, t2.left)
            root.right = mergeTrees(t1.right, t2.right)
        ____:
            root = N..
        r.. root
    
    ___ test
        testCases = [
            [
                TreeNode(1, TreeNode(3, TreeNode(5)), TreeNode(2)),
                TreeNode(2, TreeNode(1, N.., TreeNode(4)), TreeNode(3, N.., TreeNode(7))),
            ],
        ]
        ___ t1, t2 __ testCases:
            root = mergeTrees(t1, t2)
            print(root.val)

__ _____ __ _____
    Solution().test()
