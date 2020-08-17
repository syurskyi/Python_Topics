# Definition for a binary tree node.
# class TreeNode:
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution:
    ___ maxDepth root: TreeNode)  in.:
        __(root pa__ N..
            r_ 0
        __(root.left pa__ N.. a..  root.right pa__ N..
            r_ 1
        
        left _ .maxDepth(root.left)
        right _ .maxDepth(root.right)

        r_ ma.(left,right)+1
