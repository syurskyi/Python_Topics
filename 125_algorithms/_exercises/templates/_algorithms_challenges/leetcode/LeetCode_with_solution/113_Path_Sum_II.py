# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution o..
    ___ pathSum  root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res =    # list
        __ root is N..:
            r_ res
        __ sum __ root.val and root.left is N.. and root.right is N..:
            r_ [[root.val]]
        # left side
        left_res = pathSum(root.left, sum - root.val)
        # right side
        right_res = pathSum(root.right, sum - root.val)
        # add current prefix
        ___ t __ left_res + right_res:
            res.append([root.val] + t)
        r_ res
