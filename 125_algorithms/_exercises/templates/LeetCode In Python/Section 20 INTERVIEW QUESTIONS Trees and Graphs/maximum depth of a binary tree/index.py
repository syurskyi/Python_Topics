# Definition for a binary tree node.
# class TreeNode:
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    ___ maxDepth(self, root: TreeNode) -> int:
        __(root is None
            r_ 0
        __(root.left is None and  root.right is None
            r_ 1
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        r_ ma.(left,right)+1
