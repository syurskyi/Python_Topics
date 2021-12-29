# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    ___ hasPathSum(self, root, sum):
        __ root is None:
            return False
        elif root.left is None and root.right is None:
            __ sum == root.val:
                return True
            else:
                return False
        else:
            sum -= root.val
            return (self.hasPathSum(root.left, sum)
                    or self.hasPathSum(root.right, sum))
