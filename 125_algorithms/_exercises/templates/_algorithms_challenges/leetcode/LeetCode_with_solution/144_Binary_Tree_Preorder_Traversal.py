# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution o..
    # def __init__(self):
    #     self.result = []
    #
    # def preorderTraversal(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[int]
    #     """
    #     if root is None:
    #         return []
    #     self.preorderTraversalHelper(root)
    #     return self.result
    #
    # def preorderTraversalHelper(self, node):
    #     if node is None:
    #         return
    #     self.result.append(node.val)
    #     self.preorderTraversalHelper(node.left)
    #     self.preorderTraversalHelper(node.right)

    ___ preorderTraversal  root):
        # stack
        __ root is N..:
            r_ []
        res = []
        stack = [root]
        w.. l.. stack) > 0:
            curr = stack.pop()
            res.append(curr.val)
            __ curr.right is not N..:
                stack.append(curr.right)
            __ curr.left is not N..:
                stack.append(curr.left)
        r_ res

