# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    ___ minDepth(self, root):
        __ root __ N..
            r.. 0
        __ root.left __ N.. and root.right __ N..
            r.. 1
        ____ root.left __ N.. and root.right __ n.. N..
            r.. self.minDepth(root.right) + 1
        ____ root.left __ n.. N.. and root.right __ N..
            r.. self.minDepth(root.left) + 1
        ____:
            left_min = self.minDepth(root.left)
            right_min = self.minDepth(root.right)
            r.. m..(left_min, right_min) + 1
