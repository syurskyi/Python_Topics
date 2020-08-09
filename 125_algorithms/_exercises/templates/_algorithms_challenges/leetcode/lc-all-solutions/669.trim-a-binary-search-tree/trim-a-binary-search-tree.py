# Definition for a binary tree node.
# class TreeNode:
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    ___ trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        __ not root:
            r_ None
        __ L > root.val:
            r_ self.trimBST(root.right, L, R)
        ____ R < root.val:
            r_ self.trimBST(root.left, L, R)
        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)
        r_ root
