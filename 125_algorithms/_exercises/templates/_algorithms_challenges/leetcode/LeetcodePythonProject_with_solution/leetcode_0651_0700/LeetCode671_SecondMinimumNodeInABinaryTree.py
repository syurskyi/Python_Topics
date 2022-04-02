'''
Created on Oct 12, 2017

@author: MT
'''
# Definition for a binary tree node.
c_ TreeNode(o..
    ___ - , x, left=N.., right_ N..
        val = x
        left = left
        right = right

c_ Solution(o..
    ___ findSecondMinimumValue  root
        """
        :type root: TreeNode
        :rtype: int
        """
        __ n.. root: r.. -1
        first = f__('inf')
        second = f__('inf')
        queue = [root]
        w.... queue:
            node = queue.pop(0)
            __ node.val < first:
                second = first
                first = node.val
            ____ first < node.val < second:
                second = node.val
            __ node.left:
                queue.a..(node.left)
            __ node.right:
                queue.a..(node.right)
        r.. second __ second != f__('inf') ____ -1
    
    ___ test
        testCases = [
            TreeNode(2, TreeNode(2), TreeNode(5, TreeNode(5), TreeNode(7))),
        ]
        ___ root __ testCases:
            result = findSecondMinimumValue(root)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
