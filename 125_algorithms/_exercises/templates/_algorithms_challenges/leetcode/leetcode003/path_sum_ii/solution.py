# Definition for a  binary tree node
# class TreeNode:
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    ___ pathSum(self, root, sum
        __ root is None:
            r_ []
        one = []
        res = []
        self.ps(root, sum, one, res)
        r_ res

    ___ ps(self, root, sum, one, res
        __ root is None:
            r_
        ____ root.left is None and root.right is None:
            __ root.val __ sum:
                one.append(root.val)
                res.append(one[:])
                one.pop()
        ____
            one.append(root.val)
            self.ps(root.left, sum - root.val, one, res)
            self.ps(root.right, sum - root.val, one, res)
            one.pop()
