'''
Created on Jan 29, 2017

@author: MT
'''

# Definition for a binary tree node.
c_ TreeNode(object):
    ___ - , x):
        val = x
        left = N..
        right = N..

c_ Solution(object):
    ___ generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        __ n < 1: r.. []
        res = helper(1, n)
        r.. res
    
    ___ helper(self, start, end):
        __ start > end:
            r.. [N..]
        result    # list
        ___ mid __ r..(start, end+1):
            leftNodes = helper(start, mid-1)
            rightNodes = helper(mid+1, end)
            ___ leftNode __ leftNodes:
                ___ rightNode __ rightNodes:
                    root = TreeNode(mid)
                    root.left = leftNode
                    root.right = rightNode
                    result.a..(root)
        r.. result
    
    ___ test
        result = generateTrees(3)
        print(result)

__ __name__ __ '__main__':
    Solution().test()