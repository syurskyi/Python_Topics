'''
Created on Feb 16, 2017

@author: MT
'''
c_ Solution(object):
    ___ hammingWeight  n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        ___ i __ r..(32):
            __ (n >> i)&1 __ 1:
                count+=1
        r.. count
    
    ___ test
        testCases = [
            i..('00000000000000000000000000001011', 2),
        ]
        ___ n __ testCases:
            print('n:      {0:032b}'.f..(n))
            result = hammingWeight(n)
            print('result: {0:d}'.f..(result))
            print('-='*20+'-')

__ _____ __ _____
    Solution().test()