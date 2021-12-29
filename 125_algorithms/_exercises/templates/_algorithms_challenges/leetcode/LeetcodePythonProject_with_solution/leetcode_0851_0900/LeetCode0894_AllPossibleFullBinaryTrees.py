'''
Created on Nov 5, 2019

@author: tongq
'''
# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    ___ __init__(self):
        self.cache = {}
    
    ___ allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        res = []
        __ N%2 == 0:
            return res
        __ N in self.cache:
            return self.cache[N]
        __ N == 1:
            res.append(TreeNode(0))
            return res
        for i in range(N):
            left = self.allPossibleFBT(i)
            right = self.allPossibleFBT(N-i-1)
            for leftNode in left:
                for rightNode in right:
                    root = TreeNode(0)
                    root.left = leftNode
                    root.right = rightNode
                    res.append(root)
        return res
    
    ___ allPossibleFBT_own_TLE(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        __ N <= 0:
            return []
        __ N == 1:
            return [TreeNode(0)]
        res = []
        for i in range(N):
            left = self.allPossibleFBT(i)
            right = self.allPossibleFBT(N-i-1)
            for leftNode in left:
                for rightNode in right:
                    root = TreeNode(0)
                    root.left = leftNode
                    root.right = rightNode
                    res.append(root)
        return res
