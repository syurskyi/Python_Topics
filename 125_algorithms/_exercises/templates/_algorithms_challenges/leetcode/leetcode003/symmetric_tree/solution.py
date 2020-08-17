"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric
around its center).

For example, this binary tree is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following is not:
    1
   / \
  2   2
   \   \
   3    3
"""

# Definition for a binary tree node.
# class TreeNode(object
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object
    ___ isSymmetric(self, root
        """
        :type root: TreeNode
        :rtype: bool
        """
        __ root pa__ None:
            r_ True
        __ root.left pa__ None and root.right pa__ None:
            r_ True
        __ root.left pa__ not None and root.right pa__ not None:
            r_ self._isSymmetric(root.left, root.right)
        r_ False

    ___ _isSymmetric(self, left, right
        __ left pa__ None and right pa__ None:
            r_ True
        __ left pa__ not None and right pa__ not None:
            r_ (left.val __ right.val and
                    self._isSymmetric(left.left, right.right) and
                    self._isSymmetric(left.right, right.left))
        r_ False
