'''
Created on Apr 8, 2017

@author: MT
'''

c_ Solution(o..
    ___ readBinaryWatch  num
        result    # list
        ___ i __ r..(12
            ___ j __ r..(60
                total = countDigits(i) + countDigits(j)
                __ total __ num:
                    s = '%s:%02d' % (i, j)
                    result.a..(s)
        r.. result
    
    ___ countDigits  num
        result = 0
        w.... num > 0:
            __ num & 1 __ 1:
                result += 1
            num >>= 1
        r.. result
    