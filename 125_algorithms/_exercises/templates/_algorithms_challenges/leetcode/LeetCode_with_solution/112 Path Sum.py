"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along
the path equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""
__author__ = 'Danyang'
# Definition for a  binary tree node
c_ TreeNode:
    ___ - , x):
        val = x
        left = N..
        right = N..

c_ Solution:
    ___ hasPathSum(self, root, s..):
        """
        dfs

        :param root: TreeNode
        :param sum: int
        :return: boolean
        """
        # trivial
        __ n.. root:
            r.. F..

        # don't prune, possible negative
        # if sum<0:
        #    return False

        s.. = s..-root.val

        # terminal condition
        __ s..__0 a.. root.left __ N.. a.. root.right __ N..
            r.. T..

        # dfs without pre-checking
        r.. hasPathSum(root.left, s..) o. hasPathSum(root.right, s..)




