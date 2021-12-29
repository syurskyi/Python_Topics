'''
Created on May 22, 2018

@author: tongq
'''
class Solution(object):
    ___ reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        __ not s or not s.strip(): return ''
        return ' '.join([x.strip() for x in s.strip().split(' ') __ x][::-1])
