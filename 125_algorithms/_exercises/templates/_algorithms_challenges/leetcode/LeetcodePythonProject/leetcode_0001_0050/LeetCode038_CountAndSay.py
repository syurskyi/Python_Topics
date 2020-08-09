'''
Created on Jun 6, 2018

@author: tongq
'''
class Solution(object
    ___ countAndSay(self, n
        """
        :type n: int
        :rtype: str
        """
        res = '1'
        for _ in range(n-1
            tmp = ''
            i = 0
            w___ i < le.(res
                count = 1
                w___ i+1 < le.(res) and res[i+1] __ res[i]:
                    count += 1
                    i += 1
                tmp += '%s%s' % (count, res[i])
                i += 1
            res = tmp
        r_ res
