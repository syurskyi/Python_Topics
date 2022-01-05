'''
Created on Nov 5, 2019

@author: tongq
'''
# Definition for a binary tree node.
c_ TreeNode(o..):
    ___ - , x):
        val = x
        left = N..
        right = N..

c_ Solution(o..):
    ___ - ):
        cache    # dict
    
    ___ allPossibleFBT  N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        res    # list
        __ N%2 __ 0:
            r.. res
        __ N __ cache:
            r.. cache[N]
        __ N __ 1:
            res.a..(TreeNode(0))
            r.. res
        ___ i __ r..(N):
            left = allPossibleFBT(i)
            right = allPossibleFBT(N-i-1)
            ___ leftNode __ left:
                ___ rightNode __ right:
                    root = TreeNode(0)
                    root.left = leftNode
                    root.right = rightNode
                    res.a..(root)
        r.. res
    
    ___ allPossibleFBT_own_TLE  N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        __ N <= 0:
            r.. []
        __ N __ 1:
            r.. [TreeNode(0)]
        res    # list
        ___ i __ r..(N):
            left = allPossibleFBT(i)
            right = allPossibleFBT(N-i-1)
            ___ leftNode __ left:
                ___ rightNode __ right:
                    root = TreeNode(0)
                    root.left = leftNode
                    root.right = rightNode
                    res.a..(root)
        r.. res
