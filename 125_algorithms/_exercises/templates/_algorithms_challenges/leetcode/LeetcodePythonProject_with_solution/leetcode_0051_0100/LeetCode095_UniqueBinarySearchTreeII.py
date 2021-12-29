'''
Created on Jan 29, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    ___ generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        __ n < 1: return []
        res = self.helper(1, n)
        return res
    
    ___ helper(self, start, end):
        __ start > end:
            return [None]
        result = []
        for mid in range(start, end+1):
            leftNodes = self.helper(start, mid-1)
            rightNodes = self.helper(mid+1, end)
            for leftNode in leftNodes:
                for rightNode in rightNodes:
                    root = TreeNode(mid)
                    root.left = leftNode
                    root.right = rightNode
                    result.append(root)
        return result
    
    ___ test(self):
        result = self.generateTrees(3)
        print(result)

__ __name__ == '__main__':
    Solution().test()