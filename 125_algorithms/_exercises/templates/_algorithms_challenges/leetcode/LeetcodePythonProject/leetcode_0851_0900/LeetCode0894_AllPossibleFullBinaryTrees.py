'''
Created on Nov 5, 2019

@author: tongq
'''
# Definition for a binary tree node.
class TreeNode(object
    ___ __init__(self, x
        self.val = x
        self.left = None
        self.right = None

class Solution(object
    ___ __init__(self
        self.cache = {}
    
    ___ allPossibleFBT(self, N
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        res =   # list
        __ N%2 __ 0:
            r_ res
        __ N __ self.cache:
            r_ self.cache[N]
        __ N __ 1:
            res.append(TreeNode(0))
            r_ res
        ___ i __ range(N
            left = self.allPossibleFBT(i)
            right = self.allPossibleFBT(N-i-1)
            ___ leftNode __ left:
                ___ rightNode __ right:
                    root = TreeNode(0)
                    root.left = leftNode
                    root.right = rightNode
                    res.append(root)
        r_ res
    
    ___ allPossibleFBT_own_TLE(self, N
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        __ N <= 0:
            r_   # list
        __ N __ 1:
            r_ [TreeNode(0)]
        res =   # list
        ___ i __ range(N
            left = self.allPossibleFBT(i)
            right = self.allPossibleFBT(N-i-1)
            ___ leftNode __ left:
                ___ rightNode __ right:
                    root = TreeNode(0)
                    root.left = leftNode
                    root.right = rightNode
                    res.append(root)
        r_ res
