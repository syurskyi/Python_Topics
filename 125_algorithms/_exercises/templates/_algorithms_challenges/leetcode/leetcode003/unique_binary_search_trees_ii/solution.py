# Definition for a  binary tree node
# class TreeNode:
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @return a list of tree node
    ___ generateTrees(self, n
        a = range(1, n + 1)
        r_ self.generate_bst(a)

    ___ generate_bst(self, a
        __ not a:
            r_ [None]
        ____
            res = []
            ___ i, c in enumerate(a
                left = self.generate_bst(a[:i])
                right = self.generate_bst(a[i + 1:])
                ___ l in left:
                    ___ r in right:
                        root = TreeNode(c)
                        root.left = l
                        root.right = r
                        res.append(root)
            r_ res
