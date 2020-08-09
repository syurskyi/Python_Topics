# Definition for a binary tree node.
# class TreeNode:
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution:
    ___ hasSum(,root,su.,cur
        __(root is N..
            r_ F..
        cur+_root.val
        __(cur__sum a.. root.left is N.. a.. root.right is N..
            r_ T..
        r_ (.hasSum(root.right,su.,cur) o.. .hasSum(root.left,su.,cur))
    ___ hasPathSum(, root: TreeNode, su.: in.)  bool:
        r_ .hasSum(root,su., 0)