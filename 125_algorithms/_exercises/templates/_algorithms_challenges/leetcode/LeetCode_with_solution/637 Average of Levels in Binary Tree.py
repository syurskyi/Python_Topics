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
____ t___ _______ L..


# Definition for a binary tree node.
c_ TreeNode:
    ___ - , x
        val x
        left N..
        right N..


c_ Solution:
    ___ averageOfLevels  root: TreeNode) __ L..[f__]:
        """
        BFS
        """
        ret    # list
        __ n.. root:
            r.. ret

        q [root]
        w.... q:
            n l..(q)
            avg s.. m..(l.... node: node.val, q / n
            ret.a..(avg)
            cur_q    # list
            ___ node __ q:
                __ node.left:
                    cur_q.a..(node.left)
                __ node.right:
                    cur_q.a..(node.right)

            q cur_q

        r.. ret
