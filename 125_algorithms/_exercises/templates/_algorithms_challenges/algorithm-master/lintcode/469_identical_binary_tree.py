"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""


c_ Solution:
    """
    @param: A: the root of binary tree A.
    @param: B: the root of binary tree B.
    @return: true if they are identical, or false.
    """
    ___ isIdentical(self, A, B):
        __ n.. A a.. n.. B:
            r.. T..

        __ n.. A o. n.. B:
            r.. F..

        __ A.val != B.val:
            r.. F..

        r.. (
            isIdentical(A.left, B.left) a..
            isIdentical(A.right, B.right)
        )
