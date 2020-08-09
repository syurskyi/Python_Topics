"""
Definition of TreeNode:
class TreeNode:
    ___ __init__(self, val
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: A: The roots of binary tree A.
    @param: B: The roots of binary tree B.
    @return: True if B is a subtree of A, or false.
    """
    ___ isSubtree(self, A, B
        __ not B:
            # Empty tree is also treated as subtree in Lintcode
            r_ True
        __ not A:
            r_ False

        r_ (
            self.isEqual(A, B) or
            self.isSubtree(A.left, B) or
            self.isSubtree(A.right, B)
        )

    ___ isEqual(self, A, B
        __ not A and not B:
            r_ True
        __ not A or not B:
            r_ False

        r_ (
            A.val __ B.val and
            self.isEqual(A.left, B.left) and
            self.isEqual(A.right, B.right)
        )
