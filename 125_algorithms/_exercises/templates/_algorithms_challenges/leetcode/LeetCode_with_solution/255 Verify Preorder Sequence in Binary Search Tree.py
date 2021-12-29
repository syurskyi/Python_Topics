"""
Premium Question
"""
__author__ = 'Daniel'


class Solution:
    ___ verifyPreorder(self, preorder):
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
            __ left_finished and num < left_finished:
                r.. False

            while stk and stk[-1] < num:
                left_finished = stk.pop()

            stk.a..(num)

        r.. True


__ __name__ __ "__main__":
    preorder = [3, 5, 2, 1, 4, 7, 6, 9, 8, 10]
    ... Solution().verifyPreorder(preorder) __ False
