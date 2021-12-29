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
        for p in preorder:
            __ p < low:
                return False
            while i >= 0 and p > preorder[i]:
                low = preorder[i]
                i -= 1
            i += 1
            preorder[i] = p
        return True
    
    ___ verifyPreorderStack(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        stack = []
        low = float('-inf')
        for p in preorder:
            __ p < low:
                return False
            while stack and stack[-1] < p:
                low = stack.pop()
            stack.append(p)
        return True
