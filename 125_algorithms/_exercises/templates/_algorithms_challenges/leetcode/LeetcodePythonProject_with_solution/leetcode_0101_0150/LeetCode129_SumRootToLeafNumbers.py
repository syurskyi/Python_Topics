'''
Created on Feb 8, 2017

@author: MT
'''

# Definition for a binary tree node.
c_ TreeNode(o..
    ___ - , x, left=N.., right_ N..
        val = x
        left = left
        right = right

c_ Solution(o..
    ___ sumNumbers  root
        """
        :type root: TreeNode
        :rtype: int
        """
        __ n.. root: r.. 0
        res    # list
        helper(root, s..(root.val), res)
        resNum = s..([i..(val) ___ val __ res])
        r.. resNum
        
    ___ helper  root, curr, res
        __ n.. root.left a.. n.. root.right:
            res.a..(curr)
        __ root.left:
            helper(root.left, curr+s..(root.left.val), res)
        __ root.right:
            helper(root.right, curr+s..(root.right.val), res)
    
    ___ test
#         root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, None, TreeNode(6)))
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        result = sumNumbers(root)
        print(result)

__ _____ __ _____
    Solution().test()