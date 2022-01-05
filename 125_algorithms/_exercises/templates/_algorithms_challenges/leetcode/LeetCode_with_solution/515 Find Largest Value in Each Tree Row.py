#!/usr/bin/python3
"""
You need to find the largest value in each row of a binary tree.

Example:
Input:

          1
         / \
        3   2
       / \   \
      5   3   9

Output: [1, 3, 9]
"""


# Definition for a binary tree node.
c_ TreeNode:
    ___ - , x):
        val = x
        left = N..
        right = N..


c_ Solution:
    ___ largestValues  root):
        """
        BFS
        :type root: TreeNode
        :rtype: List[int]
        """
        ret    # list
        __ n.. root:
            r.. ret

        q = [root]
        w.... q:
            ret.a..(m..(map(l.... e: e.val, q)))
            cur_q    # list
            ___ e __ q:
                __ e.left:
                    cur_q.a..(e.left)
                __ e.right:
                    cur_q.a..(e.right)

            q = cur_q

        r.. ret
