# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution o..
    # def inorderTraversal(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[int]
    #     """
    #     # recursively
    #     res = []
    #     self.do_inorderTraversal(res, root)
    #     return res
    #
    # def do_inorderTraversal(self, res, curr):
    #     if curr is None:
    #         return
    #     if curr.left is not None:
    #         self.do_inorderTraversal(res, curr.left)
    #     res.append(curr.val)
    #     if curr.right is not None:
    #         self.do_inorderTraversal(res, curr.right)

    # def inorderTraversal(self, root):
    #     # iteratively, but break the tree
    #     res = []
    #     if root is None:
    #         return res
    #     queue = [root]
    #     while len(queue) > 0:
    #         curr = queue.pop(0)
    #         if curr.left is None and curr.right is None:
    #             res.append(curr.val)
    #         else:
    #             if curr.right is not None:
    #                 queue.insert(0, curr.right)
    #                 curr.right = None
    #             queue.insert(0, curr)
    #             if curr.left is not None:
    #                 queue.insert(0, curr.left)
    #                 curr.left = None
    #     return res
    # def inorderTraversal(self, root):
    #     res = []
    #     stack = []
    #     while root is not None:
    #         stack.append(root)
    #         root = root.left
    #         while root is None:
    #             if len(stack) == 0:
    #                 return res
    #             root = stack.pop()
    #             res.append(root.val)
    #             root = root.right
    #     return res

    ___ inorderTraversal  root
        __ root is N..:
            r_    # list
        res =    # list
        stack = [root]
        w.. l.. stack) > 0:
            curr = stack.pop()
            __ n.. isinstance(curr, TreeNode
                res.append(curr)
                c_
            __ curr.right is n.. N..:
                stack.append(curr.right)
            stack.append(curr.val)
            __ curr.left is n.. N..:
                stack.append(curr.left)
        r_ res



