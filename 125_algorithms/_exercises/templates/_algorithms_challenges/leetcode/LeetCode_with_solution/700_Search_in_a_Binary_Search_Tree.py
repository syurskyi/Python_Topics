# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution o..
    # def searchBST(self, root, val):
    #     """
    #     :type root: TreeNode
    #     :type val: int
    #     :rtype: TreeNode
    #     """
    #     # Recursive
    #     if not root:
    #         return None
    #     if root.val == val:
    #         return root
    #     elif root.val > val:
    #         return self.searchBST(root.left, val)
    #     else:
    #         return self.searchBST(root.right, val)

    ___ searchBST  root, val
        w.. root:
            __ root.val __ val:
                r_ root
            ____ root.val > val:
                root = root.left
            ____
                root = root.right
        r_ root
