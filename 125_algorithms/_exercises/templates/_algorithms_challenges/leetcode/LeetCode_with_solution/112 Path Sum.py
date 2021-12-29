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
class TreeNode:
    ___ __init__(self, x):
        self.val = x
        self.left = N..
        self.right = N..

class Solution:
    ___ hasPathSum(self, root, s..):
        """
        dfs

        :param root: TreeNode
        :param sum: int
        :return: boolean
        """
        # trivial
        __ n.. root:
            r.. False

        # don't prune, possible negative
        # if sum<0:
        #    return False

        s.. = s..-root.val

        # terminal condition
        __ s..__0 and root.left __ N.. and root.right __ N..
            r.. True

        # dfs without pre-checking
        r.. self.hasPathSum(root.left, s..) o. self.hasPathSum(root.right, s..)




