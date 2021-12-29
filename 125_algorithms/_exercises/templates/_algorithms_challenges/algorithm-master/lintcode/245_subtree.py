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
        __ n.. B:
            # Empty tree is also treated as subtree in Lintcode
            r.. True
        __ n.. A:
            r.. False

        r.. (
            self.isEqual(A, B) o.
            self.isSubtree(A.left, B) o.
            self.isSubtree(A.right, B)
        )

    ___ isEqual(self, A, B):
        __ n.. A a.. n.. B:
            r.. True
        __ n.. A o. n.. B:
            r.. False

        r.. (
            A.val __ B.val a..
            self.isEqual(A.left, B.left) a..
            self.isEqual(A.right, B.right)
        )
