'''
Created on Mar 1, 2017

@author: MT
'''

c_ Solution(o..
    ___ verifyPreorder  preorder
        """
        :type preorder: List[int]
        :rtype: bool
        """
        low f__('-inf')
        i -1
        ___ p __ preorder:
            __ p < low:
                r.. F..
            w.... i >_ 0 a.. p > preorder[i]:
                low preorder[i]
                i -_ 1
            i += 1
            preorder[i] p
        r.. T..
    
    ___ verifyPreorderStack  preorder
        """
        :type preorder: List[int]
        :rtype: bool
        """
        stack    # list
        low f__('-inf')
        ___ p __ preorder:
            __ p < low:
                r.. F..
            w.... stack a.. stack[-1] < p:
                low stack.p.. )
            stack.a..(p)
        r.. T..
