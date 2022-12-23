# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution o..
    # def postorderTraversal(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[int]
    #     """
    #     # Recursion
    #     if root is None:
    #         return []
    #     res = []
    #     self.postorderHelp(root, res)
    #     return res
    #
    # def postorderHelp(self, node, stack):
    #     if node is None:
    #         return
    #     self.postorderHelp(node.left, stack)
    #     self.postorderHelp(node.right, stack)
    #     stack.append(node.val)

    # def postorderTraversal(self, root):
    #     # Stack
    #     if root is None:
    #         return []
    #     res = []
    #     stack = [root]
    #     while len(stack) > 0:
    #         curr = stack.pop()
    #         res.insert(0, curr.val)
    #         if curr.left is not None:
    #             stack.append(curr.left)
    #         if curr.right is not None:
    #             stack.append(curr.right)
    #     return res

    ___ postorderTraversal  root
        __ root is N..:
            r_    # list
        res =    # list; stack = [root]
        w.. l.. stack) > 0:
            curr = stack.pop()
            __ n.. isinstance(curr, TreeNode
                res.a.. curr)
                c_
            stack.a.. curr.val)
            __ curr.right is n.. N..:
                stack.a.. curr.right)
            __ curr.left is n.. N..:
                stack.a.. curr.left)
        r_ res
