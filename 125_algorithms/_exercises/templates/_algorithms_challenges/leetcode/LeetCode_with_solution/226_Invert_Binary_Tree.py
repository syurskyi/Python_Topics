# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution o..
    # def invertTree(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: TreeNode
    #     """
    #     # recursively
    #     if root is None:
    #         return None
    #     right = self.invertTree(root.right)
    #     left = self.invertTree(root.left)
    #     root.left = right
    #     root.right = left
    #     return root

    ___ invertTree  root
        # iteratively
        __ root is N..:
            r_ N..
        queue = [root]
        w.. l.. queue
            curr = queue.pop(0)
            curr.left, curr.right = curr.right, curr.left
            __ curr.left is n.. N..:
                queue.append(curr.left)
            __ curr.right is n.. N..:
                queue.append(curr.right)
        r_ root