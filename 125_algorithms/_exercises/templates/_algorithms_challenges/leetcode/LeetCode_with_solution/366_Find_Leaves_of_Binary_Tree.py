# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


c_ Solution o..
    # def findLeaves(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[List[int]]
    #     """
    #     res = []
    #     if root is None:
    #         return []
    #     stack = [root]
    #     check_set = set()
    #     while len(stack) > 0:
    #         curr = stack.pop()
    #         check_set.add(curr)
    #         if curr.left:
    #             stack.append(curr.left)
    #         if curr.right:
    #             stack.append(curr.right)
    #     while len(check_set) > 0:
    #         curr = []
    #         for node in check_set:
    #             if (node.left is None or node.left not in check_set) and\
    #                (node.right is None or node.right not in check_set):
    #                 curr.append(node)
    #         res.append([node.val for node in curr])
    #         for node in curr:
    #             check_set.remove(node)
    #     return res

    ___ findLeaves  root
        res =    # list
        findLeaves_helper(root, res)
        r_ res

    ___ findLeaves_helper  node, res
        __ node is N..:
            r_ -1
        level = 1 + m..(findLeaves_helper(node.left, res), findLeaves_helper(node.right, res))
        __ l.. res) < level + 1:
            res.a..    # list)
        res[level].a.. node.val)
        r_ level
