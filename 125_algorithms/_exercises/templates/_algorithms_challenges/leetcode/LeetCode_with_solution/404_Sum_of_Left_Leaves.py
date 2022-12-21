# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution o..
    # def sumOfLeftLeaves(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: int
    #     """
    #     if root is None:
    #         return 0
    #     if root.left is not None:
    #         if root.left.left is None and root.left.right is None:
    #             return root.left.val + self.sumOfLeftLeaves(root.right)
    #     return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)

    ___ sumOfLeftLeaves  root
        stack = [root]
        res = 0
        w.. l.. stack) > 0:
            curr = stack.pop(0)
            __ curr is n.. N..:
                __ curr.left is n.. N..:
                    __ curr.left.left is N.. a.. curr.left.right is N..:
                        res += curr.left.val
                stack.insert(0, curr.right)
                stack.insert(0, curr.left)
        r_ res
