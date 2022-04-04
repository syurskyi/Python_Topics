#!/usr/bin/python3
"""
A full binary tree is a binary tree where each node has exactly 0 or 2 children.

Return a list of all possible full binary trees with N nodes.  Each element of
the answer is the root node of one possible tree.

Each node of each tree in the answer must have node.val = 0.

You may return the final list of trees in any order.



Example 1:

Input: 7
Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],
[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
"""

# Definition for a binary tree node.
c_ TreeNode:
    ___ - , x
        val = x
        left = N..
        right = N..


c_ Solution:
    ___ -
        cache    # dict

    ___ allPossibleFBT  N: i..) __ L..[TreeNode]:
        """
        recursive + memoization
        """
        __ N n.. __ cache:
            __ N __ 0:
                ret    # list
            ____ N __ 1:
                ret = [TreeNode(0)]
            ____:
                ret    # list
                ___ i __ r..(N
                    lefts = allPossibleFBT(i)
                    rights = allPossibleFBT(N-1-i)
                    # 0 or 2 child, cannot have only 1
                    __ lefts a.. rights:
                        ___ left __ lefts:
                            ___ right __ rights:
                                node = TreeNode(0)
                                node.left = left
                                node.right = right
                                ret.a..(node)
            cache[N] = ret

        r.. cache[N]
