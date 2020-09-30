'''
Created on Apr 8, 2017

@author: MT
'''

class Solution(object
    ___ readBinaryWatch(self, num
        result =   # list
        ___ i __ range(12
            ___ j __ range(60
                total = self.countDigits(i) + self.countDigits(j)
                __ total __ num:
                    s = '%s:%02d' % (i, j)
                    result.append(s)
        r_ result
    
    ___ countDigits(self, num
        result = 0
        w___ num > 0:
            __ num & 1 __ 1:
                result += 1
            num >>= 1
        r_ result
    