'''
Created on Mar 1, 2017

@author: MT
'''

c_ Solution(object):
    ___ verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        low = float('-inf')
        i = -1
        ___ p __ preorder:
            __ p < low:
                r.. F..
            w.... i >= 0 a.. p > preorder[i]:
                low = preorder[i]
                i -= 1
            i += 1
            preorder[i] = p
        r.. T..
    
    ___ verifyPreorderStack(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        stack    # list
        low = float('-inf')
        ___ p __ preorder:
            __ p < low:
                r.. F..
            w.... stack a.. stack[-1] < p:
                low = stack.pop()
            stack.a..(p)
        r.. T..
