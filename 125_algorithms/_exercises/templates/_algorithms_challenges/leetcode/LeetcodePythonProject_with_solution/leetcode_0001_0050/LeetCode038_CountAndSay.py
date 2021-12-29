'''
Created on Jun 6, 2018

@author: tongq
'''
class Solution(object):
    ___ countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = '1'
        ___ _ __ r..(n-1):
            tmp = ''
            i = 0
            while i < l..(res):
                count = 1
                while i+1 < l..(res) and res[i+1] __ res[i]:
                    count += 1
                    i += 1
                tmp += '%s%s' % (count, res[i])
                i += 1
            res = tmp
        r.. res
