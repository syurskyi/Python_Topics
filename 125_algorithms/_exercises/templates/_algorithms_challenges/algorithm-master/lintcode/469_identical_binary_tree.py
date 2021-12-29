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
        __ n.. A a.. n.. B:
            r.. True

        __ n.. A o. n.. B:
            r.. False

        __ A.val != B.val:
            r.. False

        r.. (
            self.isIdentical(A.left, B.left) a..
            self.isIdentical(A.right, B.right)
        )
