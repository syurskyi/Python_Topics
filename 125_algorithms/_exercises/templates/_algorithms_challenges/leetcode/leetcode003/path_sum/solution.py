# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    ___ hasPathSum(self, root, s..):
        __ root __ N..
            r.. F..
        ____ root.left __ N.. a.. root.right __ N..
            __ s.. __ root.val:
                r.. T..
            ____:
                r.. F..
        ____:
            s.. -= root.val
            r.. (hasPathSum(root.left, s..)
                    o. hasPathSum(root.right, s..))
