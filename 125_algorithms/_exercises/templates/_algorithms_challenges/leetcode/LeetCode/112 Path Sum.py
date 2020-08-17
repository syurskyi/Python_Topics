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
    ___ __init__(self, x
        self.val = x
        self.left = None
        self.right = None

class Solution:
    ___ hasPathSum(self, root, su.
        """
        dfs

        :param root: TreeNode
        :param sum: int
        :return: boolean
        """
        # trivial
        __ not root:
            r_ False

        # don't prune, possible negative
        # if sum<0:
        #    return False

        su. = su.-root.val

        # terminal condition
        __ sum__0 and root.left pa__ None and root.right pa__ None:
            r_ True

        # dfs without pre-checking
        r_ self.hasPathSum(root.left, su.) or self.hasPathSum(root.right, su.)




