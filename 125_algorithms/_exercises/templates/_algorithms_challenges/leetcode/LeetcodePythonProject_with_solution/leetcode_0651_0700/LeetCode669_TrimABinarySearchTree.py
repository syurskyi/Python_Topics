'''
Created on Oct 11, 2017

@author: MT
'''
# Definition for a binary tree node.
c_ TreeNode(object):
    ___ - , x, left=N.., right_ N..
        val = x
        left = left
        right = right

c_ Solution(object):
    ___ trimBST  root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        l, r = L, R
        __ n.. root o. l > r:
            r.. N..
        val = root.val
        __ l <= val <= r:
            newRoot = TreeNode(val)
            newRoot.left = trimBST(root, l, val-1)
            newRoot.right = trimBST(root, val+1, r)
            r.. newRoot
        ____ val < l:
            r.. trimBST(root.right, l, r)
        ____:
            r.. trimBST(root.left, l, r)
    
    ___ test
        testCases = [
        ]
        ___ root, l, r __ testCases:
            newRoot = trimBST(root, l, r)
            print(newRoot)

__ _____ __ _____
    Solution().test()
