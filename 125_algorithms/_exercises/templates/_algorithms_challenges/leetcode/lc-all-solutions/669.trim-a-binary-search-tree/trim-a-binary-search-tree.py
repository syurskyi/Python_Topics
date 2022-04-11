# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution:
    ___ trimBST  root: TreeNode, L: i.., R: i..) __ TreeNode:
        __ n.. root:
            r.. N..
        __ L > root.val:
            r.. trimBST(root.right, L, R)
        ____ R < root.val:
            r.. trimBST(root.left, L, R)
        root.left trimBST(root.left, L, R)
        root.right trimBST(root.right, L, R)
        r.. root
