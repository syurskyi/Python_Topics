# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    ___ pathSum(self, root, s..):
        __ root __ N..
            r.. []
        one    # list
        res    # list
        self.ps(root, s.., one, res)
        r.. res

    ___ ps(self, root, s.., one, res):
        __ root __ N..
            r..
        ____ root.left __ N.. a.. root.right __ N..
            __ root.val __ s..:
                one.a..(root.val)
                res.a..(one[:])
                one.pop()
        ____:
            one.a..(root.val)
            self.ps(root.left, s.. - root.val, one, res)
            self.ps(root.right, s.. - root.val, one, res)
            one.pop()
