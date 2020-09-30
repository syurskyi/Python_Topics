#!/usr/bin/python3
"""
Given a non-empty binary tree, return the average value of the nodes on each
level in the form of an array.
Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2
is 11. Hence return [3, 14.5, 11].
Note:
The range of node's value is in the range of 32-bit signed integer.
"""
from typing ______ List


# Definition for a binary tree node.
class TreeNode:
    ___ __init__(self, x
        self.val = x
        self.left = None
        self.right = None


class Solution:
    ___ averageOfLevels(self, root: TreeNode) -> List[float]:
        """
        BFS
        """
        ret =   # list
        __ not root:
            r_ ret

        q = [root]
        w___ q:
            n = le.(q)
            avg = su.(map(lambda node: node.val, q)) / n
            ret.append(avg)
            cur_q =   # list
            ___ node __ q:
                __ node.left:
                    cur_q.append(node.left)
                __ node.right:
                    cur_q.append(node.right)

            q = cur_q

        r_ ret
