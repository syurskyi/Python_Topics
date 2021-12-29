# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @return a list of tree node
    ___ generateTrees(self, n):
        a = r..(1, n + 1)
        r.. self.generate_bst(a)

    ___ generate_bst(self, a):
        __ n.. a:
            r.. [N..]
        ____:
            res    # list
            ___ i, c __ enumerate(a):
                left = self.generate_bst(a[:i])
                right = self.generate_bst(a[i + 1:])
                ___ l __ left:
                    ___ r __ right:
                        root = TreeNode(c)
                        root.left = l
                        root.right = r
                        res.a..(root)
            r.. res
