'''
Created on Jan 29, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x):
        self.val = x
        self.left = N..
        self.right = N..

class Solution(object):
    ___ generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        __ n < 1: r.. []
        res = self.helper(1, n)
        r.. res
    
    ___ helper(self, start, end):
        __ start > end:
            r.. [N..]
        result    # list
        ___ mid __ r..(start, end+1):
            leftNodes = self.helper(start, mid-1)
            rightNodes = self.helper(mid+1, end)
            ___ leftNode __ leftNodes:
                ___ rightNode __ rightNodes:
                    root = TreeNode(mid)
                    root.left = leftNode
                    root.right = rightNode
                    result.a..(root)
        r.. result
    
    ___ test(self):
        result = self.generateTrees(3)
        print(result)

__ __name__ __ '__main__':
    Solution().test()