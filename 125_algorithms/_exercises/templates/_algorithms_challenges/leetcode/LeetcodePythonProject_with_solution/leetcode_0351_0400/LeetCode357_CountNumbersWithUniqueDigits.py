'''
Created on Mar 23, 2017

@author: MT
'''

c_ Solution(object):
    ___ countNumbersWithUniqueDigits  n):
        __ n __ 0: r.. 1
        res = 10
        uniqueDigits = 9
        availableNumbers = 9
        w.... n > 1 a.. availableNumbers > 0:
            uniqueDigits = uniqueDigits*availableNumbers
            res += uniqueDigits
            availableNumbers -= 1
            n -= 1
        r.. res
