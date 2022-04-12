#!/usr/bin/python3
"""
Given a binary tree, write a function to get the maximum width of the given
tree. The width of a tree is the maximum width among all levels. The binary tree
has the same structure as a full binary tree, but some nodes are null.

The width of one level is defined as the length between the end-nodes (the
leftmost and right most non-null nodes in the level, where the null nodes
between the end-nodes are also counted into the length calculation.

Example 1:

Input:

           1
         /   \
        3     2
       / \     \
      5   3     9

Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
Example 2:

Input:

          1
         /
        3
       / \
      5   3

Output: 2
Explanation: The maximum width existing in the third level with the length 2 (5,3).
Example 3:

Input:

          1
         / \
        3   2
       /
      5

Output: 2
Explanation: The maximum width existing in the second level with the length 2 (3,2).
Example 4:

Input:

          1
         / \
        3   2
       /     \
      5       9
     /         \
    6           7
Output: 8
Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).
"""


# Definition for a binary tree node.
c_ TreeNode:
    ___ - , x
        val x
        left N..
        right N..


c_ Solution:
    ___ widthOfBinaryTree  root: TreeNode) __ i..:
        """
           0
          0 1
        0 1 2 3

        BFS, level index
        """
        __ n.. root:
            r.. 0

        ret 0
        q [(0, root)]  # (index, node)
        w.... q:
            cur_q    # list
            left, right q 0 0 , q[-1][0]
            ret m..(ret, right - left + 1)
            ___ idx, node __ q:
                __ node.left:
                    cur_q.a..((idx * 2, node.left
                __ node.right:
                    cur_q.a..((idx * 2 + 1, node.right

            q cur_q

        r.. ret
