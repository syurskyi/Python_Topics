# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution o..
    # p.left = parent.right
    # parent.right = p.right
    # p.right = parent
    # parent = p.left
    # p = left
    ___ upsideDownBinaryTree  root
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # top-down
        node, parent, parentRight = root, N.., N..
        w.. node is n.. N..:
            left = node.left
            node.left = parentRight
            parentRight = node.right
            node.right = parent
            parent = node
            node = left
        r_ parent