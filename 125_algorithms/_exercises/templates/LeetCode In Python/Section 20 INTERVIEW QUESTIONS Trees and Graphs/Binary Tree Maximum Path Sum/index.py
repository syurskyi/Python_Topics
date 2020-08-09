# Definition for a binary tree node.
# class TreeNode:
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    ans = -float("inf")
    ___ solution(self,node
        __(node is None
            r_ 0
        left = self.solution(node.left)
        right = self.solution(node.right)

        mxSide = max(node.val,max(left,right)+node.val)
        mxTop = max(mxSide,left+right+node.val)
        self.ans = max(self.ans,mxTop)
        r_ mxSide

    ___ maxPathSum(self, root: TreeNode) -> int:
        self.solution(root)
        r_ self.ans
