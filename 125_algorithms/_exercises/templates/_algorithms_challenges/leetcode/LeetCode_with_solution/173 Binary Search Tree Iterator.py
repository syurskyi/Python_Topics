"""
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
"""
__author__ 'Daniel'


c_ TreeNode:
    ___ - , x
        val x
        left N..
        right N..


c_ BSTIterator:
    ___ - , root
        """
        :type root: TreeNode
        """
        cur root
        stk    # list

    ___ hasNext
        """
        :rtype: bool
        """
        r.. cur o. stk

    ___ next
        """
        :rtype: int
        :return: the next smallest number
        """
        w.... cur:
            stk.a..(cur)
            cur cur.left

        nxt stk.p.. )
        cur nxt.right
        r.. nxt.val
