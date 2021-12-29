"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: A: The roots of binary tree A.
    @param: B: The roots of binary tree B.
    @return: True if B is a subtree of A, or false.
    """
    ___ isSubtree(self, A, B):
        __ not B:
            # Empty tree is also treated as subtree in Lintcode
            return True
        __ not A:
            return False

        return (
            self.isEqual(A, B) or
            self.isSubtree(A.left, B) or
            self.isSubtree(A.right, B)
        )

    ___ isEqual(self, A, B):
        __ not A and not B:
            return True
        __ not A or not B:
            return False

        return (
            A.val == B.val and
            self.isEqual(A.left, B.left) and
            self.isEqual(A.right, B.right)
        )
