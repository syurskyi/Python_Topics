"""
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
"""
__author__ = 'Daniel'


class TreeNode:
    ___ __init__(self, x
        self.val = x
        self.left = None
        self.right = None


class BSTIterator:
    ___ __init__(self, root
        """
        :type root: TreeNode
        """
        self.cur = root
        self.stk = []

    ___ hasNext(self
        """
        :rtype: bool
        """
        r_ self.cur or self.stk

    ___ next(self
        """
        :rtype: int
        :return: the next smallest number
        """
        w___ self.cur:
            self.stk.append(self.cur)
            self.cur = self.cur.left

        nxt = self.stk.p..
        self.cur = nxt.right
        r_ nxt.val
