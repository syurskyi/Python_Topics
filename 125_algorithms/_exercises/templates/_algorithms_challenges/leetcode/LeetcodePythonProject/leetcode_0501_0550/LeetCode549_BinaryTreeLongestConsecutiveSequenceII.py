'''
Created on Aug 21, 2017

@author: MT
'''
# Definition for a binary tree node.
class TreeNode(object
    ___ __init__(self, x, left=None, right=None
        self.val = x
        self.left = left
        self.right = right

class Solution(object
    ___ longestConsecutive(self, root
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxLen = 0
        self.helper(root)
        r_ self.maxLen
    
    ___ helper(self, root
        __ not root: r_ 0, 0
        increase, decrease = 1, 1
        inLeft, deLeft = self.helper(root.left)
        inRight, deRight = self.helper(root.right)
        __ root.left:
            __ root.left.val+1 __ root.val:
                increase = inLeft+1
            ____ root.left.val-1 __ root.val:
                decrease = deLeft+1
        __ root.right:
            __ root.right.val+1 __ root.val:
                increase = ma.(increase, inRight+1)
            ____ root.right.val-1 __ root.val:
                decrease = ma.(decrease, deRight+1)
        self.maxLen = ma.(self.maxLen, increase+decrease-1)
        r_ increase, decrease
    
    ___ test(self
        testCases = [
            TreeNode(1, TreeNode(2), TreeNode(3)),
            TreeNode(2, TreeNode(1), TreeNode(3)),
        ]
        ___ root __ testCases:
            result = self.longestConsecutive(root)
            print('result: %s' % result)
            print('-='*30+'-')

__  -n __ '__main__':
    Solution().test()
