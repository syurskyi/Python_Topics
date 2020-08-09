# Definition for a binary tree node.
# class TreeNode:
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution:
    ___ isMirror(,t1,t2
        __(t1 is None and t2 is None
            r_ True
        __(t1 is None or t2 is None
            r_ False
        r_ (t1.val__t2.val) and .isMirror(t1.right,t2.left) and .isMirror(t1.left,t2.right)
    ___ isSymmetric(, root: TreeNode) -> bool:
        r_ .isMirror(root,root)