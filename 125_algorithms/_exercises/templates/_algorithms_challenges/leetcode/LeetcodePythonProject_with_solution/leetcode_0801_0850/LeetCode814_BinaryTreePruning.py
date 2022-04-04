'''
Created on Apr 30, 2018

@author: tongq
'''
# Definition for a binary tree node.
c_ TreeNode(o..
    ___ - , x, left=N.., right_ N..
        val = x
        left = left
        right = right

c_ Solution(o..
    ___ pruneTree  root
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        __ n.. root: r.. root
        left  = pruneTree(root.left)
        right = pruneTree(root.right)
        __ left __ N.. a.. right __ N.. a.. root.val __ 0:
            r.. N..
        ____
            root.left = left
            root.right = right
            r.. root
    
    ___ test
        testCases = [
            
        ]
        ___ root __ testCases:
            result = pruneTree(root)

__ _____ __ _____
    Solution().test()
