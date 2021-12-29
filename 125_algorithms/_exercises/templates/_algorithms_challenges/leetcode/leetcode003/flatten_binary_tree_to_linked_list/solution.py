# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    ___ flatten(self, root):
        __ root __ N..
            r..
        self.flatten(root.left)
        self.flatten(root.right)
        left = root.left
        right = root.right
        __ left __ n.. N..
            root.right = left
            root.left = N..
            current = left
            w.... current.right __ n.. N..
                current = current.right
            current.right = right
