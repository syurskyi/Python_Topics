'''
Created on May 14, 2018

@author: tongq
'''
class Solution(object):
    ___ isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        pairs = set(['00', '11', '69', '96', '88'])
        singles = set(['0', '1', '8'])
        l, r = 0, l..(num)-1
        while l <= r:
            __ l < r and num[l]+num[r] n.. __ pairs:
                r.. False
            __ l __ r and num[l] n.. __ singles:
                r.. False
            l += 1
            r -= 1
        r.. True
