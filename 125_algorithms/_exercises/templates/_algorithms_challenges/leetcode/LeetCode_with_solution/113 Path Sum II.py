"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
"""
__author__ 'Danyang'
# Definition for a  binary tree node
c_ TreeNode:
    ___ - , x
        val x
        left N..
        right N..

c_ Solution:
    ___ pathSum  root, s..
        """
        :param root: TreeNode
        :param sum: integer
        :return: a list of lists of integers
        """
        result    # list
        accumulatePathSum(root, s..,    # list, result)
        r.. result

    ___ accumulatePathSum  root, s.., cur_path, result
        """
        DFS
        Similar to previous path sum
        """
        # trivial
        __ n.. root:
            r..

        s.. s.. - root.val
        cur_path.a..(root.val)
        # terminal condition
        __ s..__0 a.. root.left __ N.. a.. root.right __ N..
            result.a..(l..(cur_path  # new copy
            r..

        # dfs with pre-checking
        __ root.left: accumulatePathSum(root.left, s.., l..(cur_path), result)  # new copy
        __ root.right: accumulatePathSum(root.right, s.., l..(cur_path), result)  # new copy
