'''
Created on Oct 8, 2017

@author: MT
'''
# Definition for a binary tree node.
c_ TreeNode(o..):
    ___ - , x, left=N..,right_ N..
        val = x
        left = left
        right = right

c_ Solution(o..):
    ___ checkEqualTree  root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        __ n.. root: r.. F..
        r.. helper(root, 0, T..)
    
    ___ helper  root, sumVal, firstLevel):
        __ n.. root:
            r.. F..
        __ sumVal __ s..(root) a.. n.. firstLevel:
            r.. T..
        __ (root.left a.. helper(root.left, sumVal+root.val+s..(root.right), F..)) o.\
            (root.right a.. helper(root.right, sumVal+root.val+s..(root.left), F..)):
            r.. T..
        r.. F..
    
    ___ s..  root):
        __ n.. root: r.. 0
        res = root.val
        res += s..(root.left)
        res += s..(root.right)
        r.. res
    
    ___ sumVal  root):
        __ n.. root: r.. 0
        r.. root.val +\
            sumVal(root.left)+\
            sumVal(root.right)
    
    ___ test
        testCases = [
            TreeNode(5, TreeNode(10), TreeNode(10, TreeNode(2), TreeNode(3))),
            TreeNode(1, TreeNode(2), TreeNode(10, TreeNode(2), TreeNode(20))),
            TreeNode(1, TreeNode(-1)),
            TreeNode(1, N.., TreeNode(2)),
            TreeNode(2, TreeNode(1, TreeNode(0), TreeNode(2, TreeNode(3))), TreeNode(3)),
        ]
        ___ root __ testCases:
            result = checkEqualTree(root)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
