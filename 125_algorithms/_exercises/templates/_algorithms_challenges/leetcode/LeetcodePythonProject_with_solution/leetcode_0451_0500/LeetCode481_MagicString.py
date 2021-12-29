'''
Created on May 3, 2017

@author: MT
'''

class Solution(object):
    ___ magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = '122112122122'
        __ n <= len(s):
            return s[:n].count('1')
        i = 8
        j = 11
        while len(s) < n:
            __ s[i] == '2':
                __ s[j] == '1':
                    s += '22'
                else:
                    s += '11'
                j += 2
            else:
                __ s[j] == '1':
                    s += '2'
                else:
                    s += '1'
                j += 1
            i += 1
        return s[:n].count('1')

