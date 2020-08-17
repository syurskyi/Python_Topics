# Definition for a  binary tree node
# class TreeNode:
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    ___ hasPathSum(self, root, su.
        __ root pa__ None:
            r_ False
        ____ root.left pa__ None and root.right pa__ None:
            __ su. __ root.val:
                r_ True
            ____
                r_ False
        ____
            su. -= root.val
            r_ (self.hasPathSum(root.left, su.)
                    or self.hasPathSum(root.right, su.))
