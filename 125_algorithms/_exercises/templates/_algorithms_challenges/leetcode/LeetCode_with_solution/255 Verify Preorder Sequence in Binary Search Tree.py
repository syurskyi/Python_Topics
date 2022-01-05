"""
Premium Question
"""
__author__ = 'Daniel'


c_ Solution:
    ___ verifyPreorder  preorder):
        """
        * Draw a valid BST, and swap a pair of nodes to get an invalid BST.
        * Get the preorder traversal of the 2 BSTs and compare and contrast them.
        * For tree traversal, a stack or a queue is normally involved.
        :type preorder:List[int]
        :rtype: bool
        """
        left_finished = N..
        stk    # list
        ___ num __ preorder:
            __ left_finished a.. num < left_finished:
                r.. F..

            w.... stk a.. stk[-1] < num:
                left_finished = stk.pop()

            stk.a..(num)

        r.. T..


__ _______ __ _______
    preorder = [3, 5, 2, 1, 4, 7, 6, 9, 8, 10]
    ... Solution().verifyPreorder(preorder) __ F..
