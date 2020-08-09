'''
Created on May 22, 2018

@author: tongq
'''
class Solution(object
    ___ reverseWords(self, s
        """
        :type s: str
        :rtype: str
        """
        __ not s or not s.strip( r_ ''
        r_ ' '.join([x.strip() ___ x in s.strip().split(' ') __ x][::-1])
