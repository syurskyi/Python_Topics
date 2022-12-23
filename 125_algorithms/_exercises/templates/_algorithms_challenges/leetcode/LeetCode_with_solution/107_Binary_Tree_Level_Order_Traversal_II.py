# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution o..
    # def levelOrderBottom(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[List[int]]
    #     """
    #     res = []
    #     if root is None:
    #         return []
    #     self.get_level(res, root, 0)
    #     # reverse result
    #     res.reverse()
    #     return res
    #
    # def get_level(self, res, root, depth):
    #     if root is None:
    #         return
    #     if depth == len(res):
    #         res.append([])
    #     res[depth].append(root.val)
    #     self.get_level(res, root.left, depth + 1)
    #     self.get_level(res, root.right, depth + 1)
    ___ levelOrderBottom  root
        __ root is N..:
            r_    # list
        # use stack
        stack = [[root]]
        res =    # list
        w.. l.. stack) > 0:
            top = stack.pop()
            res.insert(0, [t.val ___ t __ top])
            temp =    # list
            ___ node __ top:
                __ node.left is n.. N..:
                    temp.a.. node.left)
                __ node.right is n.. N..:
                    temp.a.. node.right)
            __ l.. temp) > 0:
                stack.a.. temp)
        r_ res