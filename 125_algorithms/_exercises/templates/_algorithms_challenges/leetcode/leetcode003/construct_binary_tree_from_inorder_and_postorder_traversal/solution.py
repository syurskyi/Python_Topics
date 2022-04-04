# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    ___ buildTree  inorder, postorder
        __ n.. inorder o. n.. postorder:
            r.. N..
        ____
            d = postorder[-1]
            root = TreeNode(d)
            i = inorder.i.. d)
            left = buildTree(inorder[:i], postorder[:i])
            right = buildTree(inorder[i + 1:], postorder[i:-1])
            root.left = left
            root.right = right
            r.. root
