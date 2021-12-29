'''
Created on Aug 21, 2017

@author: MT
'''
# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x, left=None, right_ N..
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    ___ longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxLen = 0
        self.helper(root)
        return self.maxLen
    
    ___ helper(self, root):
        __ not root: return 0, 0
        increase, decrease = 1, 1
        inLeft, deLeft = self.helper(root.left)
        inRight, deRight = self.helper(root.right)
        __ root.left:
            __ root.left.val+1 == root.val:
                increase = inLeft+1
            elif root.left.val-1 == root.val:
                decrease = deLeft+1
        __ root.right:
            __ root.right.val+1 == root.val:
                increase = max(increase, inRight+1)
            elif root.right.val-1 == root.val:
                decrease = max(decrease, deRight+1)
        self.maxLen = max(self.maxLen, increase+decrease-1)
        return increase, decrease
    
    ___ test(self):
        testCases = [
            TreeNode(1, TreeNode(2), TreeNode(3)),
            TreeNode(2, TreeNode(1), TreeNode(3)),
        ]
        for root in testCases:
            result = self.longestConsecutive(root)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
