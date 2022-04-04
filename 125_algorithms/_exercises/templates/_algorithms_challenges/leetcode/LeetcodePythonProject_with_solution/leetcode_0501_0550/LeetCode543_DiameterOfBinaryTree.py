'''
Created on Aug 20, 2017

@author: MT
'''

# Definition for a binary tree node.
c_ TreeNode(o..
    ___ - , x, left=N.., right_ N..
        val = x
        left = left
        right = right

c_ Solution(o..
    ___ diameterOfBinaryTree  root
        """
        :type root: TreeNode
        :rtype: int
        """
        __ n.. root: r.. 0
        r.. helper(root)[-1]-1
    
    # returns include, exclude
    ___ helper  root
        __ n.. root:
            r.. 0, 0
        left = helper(root.left)
        right = helper(root.right)
        include = m..(1+left[0], 1+right[0])
        exclude = m..([left[1], right[1], left[0]+right[0]+1])
        r.. include, exclude
    
    ___ test
        testCases = [
            TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(3,
        ]
        ___ root __ testCases:
            result = diameterOfBinaryTree(root)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
