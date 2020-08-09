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
    ___ hasPathSum(self, root, sum
        __ root is None:
            r_ False
        ____ root.left is None and root.right is None:
            __ sum __ root.val:
                r_ True
            ____
                r_ False
        ____
            sum -= root.val
            r_ (self.hasPathSum(root.left, sum)
                    or self.hasPathSum(root.right, sum))
