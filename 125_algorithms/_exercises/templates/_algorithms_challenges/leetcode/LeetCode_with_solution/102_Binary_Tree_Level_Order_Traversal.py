# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution o..
    # def levelOrder(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[List[int]]
    #     """
    #     res = []
    #     if root is None:
    #         return []
    #     self.get_level(res, root, 0)
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

    ___ levelOrder  root
        # https://leetcode.com/discuss/90680/9-lines-python-code
        __ root is N..:
            r_    # list
        q = [[root]]
        ___ level __ q:
            record =    # list
            ___ node __ level:
                __ node.left:
                    record.append(node.left)
                __ node.right:
                    record.append(node.right)
            __ record:
                q.append(record)
        r_ [[x.val ___ x __ level] ___ level __ q]

