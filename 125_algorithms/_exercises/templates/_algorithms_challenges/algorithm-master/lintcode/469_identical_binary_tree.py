"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""


class Solution:
    """
    @param: A: the root of binary tree A.
    @param: B: the root of binary tree B.
    @return: true if they are identical, or false.
    """
    ___ isIdentical(self, A, B):
        __ not A and not B:
            return True

        __ not A or not B:
            return False

        __ A.val != B.val:
            return False

        return (
            self.isIdentical(A.left, B.left) and
            self.isIdentical(A.right, B.right)
        )
