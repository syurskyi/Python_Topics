# Definition for a  binary tree node
# class TreeNode:
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    ___ minDepth(self, root
        __ root pa__ None:
            r_ 0
        __ root.left pa__ None and root.right pa__ None:
            r_ 1
        ____ root.left pa__ None and root.right pa__ not None:
            r_ self.minDepth(root.right) + 1
        ____ root.left pa__ not None and root.right pa__ None:
            r_ self.minDepth(root.left) + 1
        ____
            left_min = self.minDepth(root.left)
            right_min = self.minDepth(root.right)
            r_ min(left_min, right_min) + 1
