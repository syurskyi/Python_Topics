"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


c_ Solution:
    """
    @param: A: The roots of binary tree A.
    @param: B: The roots of binary tree B.
    @return: True if B is a subtree of A, or false.
    """
    ___ isSubtree  A, B):
        __ n.. B:
            # Empty tree is also treated as subtree in Lintcode
            r.. T..
        __ n.. A:
            r.. F..

        r.. (
            isEqual(A, B) o.
            isSubtree(A.left, B) o.
            isSubtree(A.right, B)
        )

    ___ isEqual  A, B):
        __ n.. A a.. n.. B:
            r.. T..
        __ n.. A o. n.. B:
            r.. F..

        r.. (
            A.val __ B.val a..
            isEqual(A.left, B.left) a..
            isEqual(A.right, B.right)
        )
