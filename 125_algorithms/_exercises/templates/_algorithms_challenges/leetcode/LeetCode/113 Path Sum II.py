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
    ___ __init__(self, x
        self.val = x
        self.left = None
        self.right = None

class Solution:
    ___ pathSum(self, root, su.
        """
        :param root: TreeNode
        :param sum: integer
        :return: a list of lists of integers
        """
        result = []
        self.accumulatePathSum(root, su., [], result)
        r_ result

    ___ accumulatePathSum(self, root, su., cur_path, result
        """
        DFS
        Similar to previous path sum
        """
        # trivial
        __ not root:
            r_

        su. = su. - root.val
        cur_path.append(root.val)
        # terminal condition
        __ sum__0 and root.left is None and root.right is None:
            result.append(list(cur_path))  # new copy
            r_

        # dfs with pre-checking
        __ root.left: self.accumulatePathSum(root.left, su., list(cur_path), result)  # new copy
        __ root.right: self.accumulatePathSum(root.right, su., list(cur_path), result)  # new copy
