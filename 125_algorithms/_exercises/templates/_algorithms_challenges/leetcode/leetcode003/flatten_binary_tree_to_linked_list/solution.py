# Definition for a  binary tree node
# class TreeNode:
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    ___ flatten(self, root
        __ root is None:
            r_
        self.flatten(root.left)
        self.flatten(root.right)
        left = root.left
        right = root.right
        __ left is not None:
            root.right = left
            root.left = None
            current = left
            w___ current.right is not None:
                current = current.right
            current.right = right
