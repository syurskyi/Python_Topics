# Definition for a binary tree node.
# class TreeNode:
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    ___ hasSum(self,root,su.,cur
        __(root is None
            r_ False
        cur+=root.val
        __(cur__sum and root.left is None and root.right is None
            r_ True
        r_ (self.hasSum(root.right,su.,cur) or self.hasSum(root.left,su.,cur))
    ___ hasPathSum(self, root: TreeNode, su.: int) -> bool:
        r_ self.hasSum(root,su., 0)