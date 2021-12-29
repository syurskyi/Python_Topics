# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    ___ trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        __ n.. root:
            r.. N..
        __ L > root.val:
            r.. self.trimBST(root.right, L, R)
        ____ R < root.val:
            r.. self.trimBST(root.left, L, R)
        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)
        r.. root
