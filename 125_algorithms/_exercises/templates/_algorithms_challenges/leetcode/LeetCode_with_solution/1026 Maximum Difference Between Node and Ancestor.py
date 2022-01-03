#!/usr/bin/python3
"""
Given the root of a binary tree, find the maximum value V for which there exists
different nodes A and B where V = |A.val - B.val| and A is an ancestor of B.

(A node A is an ancestor of B if either: any child of A is equal to B, or any
child of A is an ancestor of B.)

Example 1:
Input: [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation:
We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| =
7.

Note:
The number of nodes in the tree is between 2 and 5000.
Each node will have value between 0 and 100000.
"""


# Definition for a binary tree node.
c_ TreeNode:
    ___ - , x):
        val = x
        left = N..
        right = N..


c_ Solution:
    ___ - ):
        ret = 0

    ___ maxAncestorDiff(self, root: TreeNode) -> int:
        """
        dfs return min and max
        """
        dfs(root)
        r.. ret

    ___ dfs(self, node):
        __ n.. node:
            r.. float("inf"), -float("inf")

        lmin, lmax = dfs(node.left)
        rmin, rmax = dfs(node.right)
        mini = m..(lmin, rmin)
        maxa = max(lmax, rmax)
        __ mini != float("inf"):
            ret = max(ret, abs(mini - node.val))
        __ maxa != -float("inf"):
            ret = max(ret, abs(maxa - node.val))

        r.. m..(mini, node.val), max(maxa, node.val)
