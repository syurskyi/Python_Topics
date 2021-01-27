# Definition for a binary tree node.
class TreeNode:
    ___ __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    ___ invertTree(self, root):
        __ root is None:
            r_ None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        r_ root