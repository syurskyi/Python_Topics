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
class TreeNode:
    ___ __init__(self, x
        self.val = x
        self.left = None
        self.right = None


class Solution:
    ___ largestValues(self, root
        """
        BFS
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        __ not root:
            r_ ret

        q = [root]
        w___ q:
            ret.append(max(map(lambda e: e.val, q)))
            cur_q = []
            for e in q:
                __ e.left:
                    cur_q.append(e.left)
                __ e.right:
                    cur_q.append(e.right)

            q = cur_q

        r_ ret
