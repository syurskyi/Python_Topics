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
__author__ = 'Danyang'
# Definition for a  binary tree node
class TreeNode:
    ___ __init__(self, x):
        self.val = x
        self.left = N..
        self.right = N..

class Solution:
    ___ pathSum(self, root, s..):
        """
        :param root: TreeNode
        :param sum: integer
        :return: a list of lists of integers
        """
        result    # list
        self.accumulatePathSum(root, s.., [], result)
        r.. result

    ___ accumulatePathSum(self, root, s.., cur_path, result):
        """
        DFS
        Similar to previous path sum
        """
        # trivial
        __ n.. root:
            r..

        s.. = s.. - root.val
        cur_path.a..(root.val)
        # terminal condition
        __ s..__0 and root.left __ N.. and root.right __ N..
            result.a..(l..(cur_path))  # new copy
            r..

        # dfs with pre-checking
        __ root.left: self.accumulatePathSum(root.left, s.., l..(cur_path), result)  # new copy
        __ root.right: self.accumulatePathSum(root.right, s.., l..(cur_path), result)  # new copy
