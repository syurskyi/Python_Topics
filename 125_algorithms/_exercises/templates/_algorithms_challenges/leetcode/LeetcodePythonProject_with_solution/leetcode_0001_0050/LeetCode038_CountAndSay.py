'''
Created on Jun 6, 2018

@author: tongq
'''
c_ Solution(object):
    ___ countAndSay  n):
        """
        :type n: int
        :rtype: str
        """
        res = '1'
        ___ _ __ r..(n-1):
            tmp = ''
            i = 0
            w.... i < l..(res):
                count = 1
                w.... i+1 < l..(res) a.. res[i+1] __ res[i]:
                    count += 1
                    i += 1
                tmp += '%s%s' % (count, res[i])
                i += 1
            res = tmp
        r.. res
