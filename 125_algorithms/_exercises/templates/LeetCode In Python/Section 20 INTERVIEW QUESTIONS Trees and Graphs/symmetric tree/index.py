# Definition for a binary tree node.
# class TreeNode:
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution:
    ___ isMirror(,t1,t2
        __(t1 pa__ N.. a.. t2 pa__ N..
            r_ T..
        __(t1 pa__ N.. o.. t2 pa__ N..
            r_ F..
        r_ (t1.val__t2.val) a.. .isMirror(t1.right,t2.left) a.. .isMirror(t1.left,t2.right)
    ___ isSymmetric root: TreeNode)  bool:
        r_ .isMirror(root,root)