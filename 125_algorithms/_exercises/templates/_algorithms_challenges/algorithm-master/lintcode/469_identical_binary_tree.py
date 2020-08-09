"""
Definition of TreeNode:
class TreeNode:
    ___ __init__(self, val
        this.val = val
        this.left, this.right = None, None
"""


class Solution:
    """
    @param: A: the root of binary tree A.
    @param: B: the root of binary tree B.
    @return: true if they are identical, or false.
    """
    ___ isIdentical(self, A, B
        __ not A and not B:
            r_ True

        __ not A or not B:
            r_ False

        __ A.val != B.val:
            r_ False

        r_ (
            self.isIdentical(A.left, B.left) and
            self.isIdentical(A.right, B.right)
        )
