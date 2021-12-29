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
    ___ hasPathSum(self, root, s..):
        __ root __ N..
            r.. False
        ____ root.left __ N.. a.. root.right __ N..
            __ s.. __ root.val:
                r.. True
            ____:
                r.. False
        ____:
            s.. -= root.val
            r.. (self.hasPathSum(root.left, s..)
                    o. self.hasPathSum(root.right, s..))
