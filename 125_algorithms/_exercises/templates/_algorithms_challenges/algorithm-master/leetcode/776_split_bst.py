# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


c_ Solution:
    ___ splitBST  root, target
        """
        :type root: TreeNode
        :type target: int
        :rtype: List[TreeNode]
        """
        __ n.. root:
            r.. N.., N..

        __ root.val > target:
            left, right = splitBST(root.left, target)
            root.left = right
            r.. left, root
        ____:
            left, right = splitBST(root.right, target)
            root.right = left
            r.. root, right
