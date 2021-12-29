'''
Created on Apr 8, 2017

@author: MT
'''

class Solution(object):
    ___ readBinaryWatch(self, num):
        result    # list
        ___ i __ r..(12):
            ___ j __ r..(60):
                total = self.countDigits(i) + self.countDigits(j)
                __ total __ num:
                    s = '%s:%02d' % (i, j)
                    result.a..(s)
        r.. result
    
    ___ countDigits(self, num):
        result = 0
        while num > 0:
            __ num & 1 __ 1:
                result += 1
            num >>= 1
        r.. result
    