'''
Created on Apr 8, 2017

@author: MT
'''

class Solution(object):
    ___ readBinaryWatch(self, num):
        result = []
        for i in range(12):
            for j in range(60):
                total = self.countDigits(i) + self.countDigits(j)
                __ total == num:
                    s = '%s:%02d' % (i, j)
                    result.append(s)
        return result
    
    ___ countDigits(self, num):
        result = 0
        while num > 0:
            __ num & 1 == 1:
                result += 1
            num >>= 1
        return result
    