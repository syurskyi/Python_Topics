# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution:
    # @return a list of tree node
    ___ generateTrees  n
        a r..(1, n + 1)
        r.. generate_bst(a)

    ___ generate_bst  a
        __ n.. a:
            r.. [N..]
        ____
            res    # list
            ___ i, c __ e..(a
                left generate_bst(a[:i])
                right generate_bst(a[i + 1:])
                ___ l __ left:
                    ___ r __ right:
                        root TreeNode(c)
                        root.left l
                        root.right r
                        res.a..(root)
            r.. res
