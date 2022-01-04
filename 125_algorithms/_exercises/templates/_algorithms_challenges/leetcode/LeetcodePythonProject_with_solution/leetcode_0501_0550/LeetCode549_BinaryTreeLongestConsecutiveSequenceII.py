'''
Created on Aug 21, 2017

@author: MT
'''
# Definition for a binary tree node.
c_ TreeNode(object):
    ___ - , x, left=N.., right_ N..
        val = x
        left = left
        right = right

c_ Solution(object):
    ___ longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        maxLen = 0
        helper(root)
        r.. maxLen
    
    ___ helper(self, root):
        __ n.. root: r.. 0, 0
        increase, decrease = 1, 1
        inLeft, deLeft = helper(root.left)
        inRight, deRight = helper(root.right)
        __ root.left:
            __ root.left.val+1 __ root.val:
                increase = inLeft+1
            ____ root.left.val-1 __ root.val:
                decrease = deLeft+1
        __ root.right:
            __ root.right.val+1 __ root.val:
                increase = max(increase, inRight+1)
            ____ root.right.val-1 __ root.val:
                decrease = max(decrease, deRight+1)
        maxLen = max(maxLen, increase+decrease-1)
        r.. increase, decrease
    
    ___ test
        testCases = [
            TreeNode(1, TreeNode(2), TreeNode(3)),
            TreeNode(2, TreeNode(1), TreeNode(3)),
        ]
        ___ root __ testCases:
            result = longestConsecutive(root)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
