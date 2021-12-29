'''
Created on Mar 1, 2017

@author: MT
'''

class Solution(object):
    ___ verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        low = float('-inf')
        i = -1
        ___ p __ preorder:
            __ p < low:
                r.. False
            while i >= 0 and p > preorder[i]:
                low = preorder[i]
                i -= 1
            i += 1
            preorder[i] = p
        r.. True
    
    ___ verifyPreorderStack(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        stack    # list
        low = float('-inf')
        ___ p __ preorder:
            __ p < low:
                r.. False
            while stack and stack[-1] < p:
                low = stack.pop()
            stack.a..(p)
        r.. True
