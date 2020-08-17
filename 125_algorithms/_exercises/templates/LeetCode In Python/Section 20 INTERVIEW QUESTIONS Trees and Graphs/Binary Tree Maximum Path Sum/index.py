# Definition for a binary tree node.
# class TreeNode:
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None


c_ Solution:
    ans _ -fl..("inf")
    ___ solution(,node
        __(node pa__ N..
            r_ 0
        left _ .solution(node.left)
        right _ .solution(node.right)

        mxSide _ ma.(node.val,ma.(left,right)+node.val)
        mxTop _ ma.(mxSide,left+right+node.val)
        .ans _ ma.(.ans,mxTop)
        r_ mxSide

    ___ maxPathSum root: TreeNode)  in.:
        .solution(root)
        r_ .ans
