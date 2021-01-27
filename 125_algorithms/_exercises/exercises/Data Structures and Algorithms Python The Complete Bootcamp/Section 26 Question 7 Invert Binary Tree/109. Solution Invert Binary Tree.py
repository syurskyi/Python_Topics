# Definition for a binary tree node.
class TreeNode:
    ___  -   val=0, left=N.., right=N..):
        val = val
        left = left
        right = right


class Solution:
    ___ invertTree  root):
        __ root __ N..:
            r_ N..

        root.left, root.right = root.right, root.left

        invertTree(root.left)
        invertTree(root.right)

        r_ root